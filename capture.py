import glob
import os
import re
import subprocess
import shutil
import sys
import time
from typing import Optional, NamedTuple, List

FFMPEG_PATH = shutil.which("ffmpeg") or "/usr/sbin/ffmpeg"
HLS_DIR = "/tmp/fluxcast"


class Monitor(NamedTuple):
    display: str
    name: str    # e.g. 'eDP-1'
    width: int
    height: int
    x: int       # x offset within the combined framebuffer
    y: int
    refresh: float  # Hz


def _detect_live_displays() -> list:
    locks = glob.glob("/tmp/.X*-lock")
    displays = []
    for lock in sorted(locks):
        m = re.search(r"/\.X(\d+)-lock$", lock)
        if m:
            displays.append(f":{m.group(1)}")
    return displays or [":0"]


def _parse_xrandr(display: str) -> list:
    xrandr = shutil.which("xrandr")
    if not xrandr:
        return []

    env = os.environ.copy()
    env["DISPLAY"] = display
    try:
        result = subprocess.run(
            [xrandr, "--query"],
            capture_output=True, text=True, timeout=4, env=env,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return []

    if result.returncode != 0:
        return []

    monitors: list = []
    lines = result.stdout.splitlines()
    for i, line in enumerate(lines):
        m = re.match(
            r"^(\S+)\s+connected\s+(?:primary\s+)?(\d+)x(\d+)\+(\d+)\+(\d+)",
            line,
        )
        if not m:
            continue
        name, w, h, x, y = m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))
        refresh = 0.0
        if i + 1 < len(lines):
            rm = re.search(r"([\d.]+)\*", lines[i + 1])
            if rm:
                refresh = float(rm.group(1))
        monitors.append(Monitor(
            display=display, name=name,
            width=w, height=h, x=x, y=y, refresh=refresh,
        ))
    return monitors


def gather_monitors() -> list:
    all_monitors: list = []
    for disp in _detect_live_displays():
        all_monitors.extend(_parse_xrandr(disp))
    return all_monitors


def prompt_monitor() -> Monitor:
    monitors = gather_monitors()

    if not monitors:
        print("[FluxCast] WARNING: xrandr returned no monitors. Falling back to :0 1920x1080.")
        return Monitor(display=":0", name="(unknown)", width=1920, height=1080,
                       x=0, y=0, refresh=60.0)

    current_display = os.environ.get("DISPLAY", "")

    print("\n[FluxCast] Available monitors to capture:")
    print(f"  {'#':<4} {'Monitor':<12} {'Display':<8} "
          f"{'Resolution':<14} {'Position':<14} {'Refresh'}")
    print(f"  {'-'*4} {'-'*12} {'-'*8} {'-'*14} {'-'*14} {'-'*8}")

    default_idx = 0
    for i, mon in enumerate(monitors):
        pos = f"{mon.x},{mon.y}"
        hz = f"{mon.refresh:.1f} Hz" if mon.refresh else "—"
        current = " ← active" if mon.display == current_display and i == 0 else ""
        print(f"  [{i}]  {mon.name:<12} {mon.display:<8} "
              f"{mon.width}x{mon.height:<8} {pos:<14} {hz}{current}")
        if mon.display == current_display:
            default_idx = i

    print()
    raw = input(f"Select monitor [{default_idx}]: ").strip()
    if raw == "":
        return monitors[default_idx]
    try:
        idx = int(raw)
        return monitors[idx]
    except (ValueError, IndexError):
        print(f"[FluxCast] Invalid choice, using monitor {default_idx}.")
        return monitors[default_idx]


def _detect_audio_monitor() -> str:
    """Return the .monitor PulseAudio source for the currently running sink."""
    try:
        sink = subprocess.check_output(
            ["pactl", "get-default-sink"], text=True, stderr=subprocess.DEVNULL
        ).strip()
        if sink:
            return sink + ".monitor"
    except Exception:
        pass

    try:
        out = subprocess.check_output(["pactl", "list", "short", "sinks"], text=True)
        for line in out.splitlines():
            if "RUNNING" in line:
                return line.split('\t')[1] + ".monitor"
    except Exception:
        pass
    return "default"


def _double_bitrate(value: str) -> str:
    match = re.fullmatch(r"\s*(\d+(?:\.\d+)?)([kKmMgG]?)\s*", value)
    if not match:
        return value

    amount = float(match.group(1)) * 2
    suffix = match.group(2)
    amount_text = str(int(amount)) if amount.is_integer() else f"{amount:g}"
    return amount_text + suffix


def start_capture(
    monitor: Monitor,
    fps: int = 30,
    bitrate: str = "4M",
    output_resolution: Optional[str] = None,
) -> List["subprocess.Popen[bytes]"]:
    """
    Returns [wf_proc, ffmpeg_proc].  Both must be passed to stop_capture().
    
    Architecture:
      wf-recorder (Wayland-native video) -> NUT pipe -> ffmpeg -> low-latency HLS
    """
    src_res = f"{monitor.width}x{monitor.height}"
    out_res = output_resolution or src_res
    gop = max(1, int(fps))
    hls_time = "1"

    audio_monitor = _detect_audio_monitor()

    if os.path.exists(HLS_DIR):
        shutil.rmtree(HLS_DIR)
    os.makedirs(HLS_DIR, exist_ok=True)

    vf_filters = [
        f"scale={out_res.replace('x', ':')}:out_range=tv"
        if out_res != src_res else
        "scale=iw:ih:out_range=tv",
        "format=yuv420p",
    ]

    # ── Process 1: wf-recorder (video only, writes encoded H.264/NUT to stdout) ──
    wf_cmd = [
        "wf-recorder",
        "-y",
        "-D",               # no-damage: constant FPS on static screens
        "-r", str(fps),
        "-o", monitor.name, # Wayland output name (e.g. HDMI-A-1)
        "-c", "libx264",
        "-m", "nut",        # NUT — pipe-friendly container, no seek index
        "-p", "preset=ultrafast",
        "-p", "tune=zerolatency",
        "-p", "pix_fmt=yuv420p",
        "-p", "profile=main",
        "-p", f"x264-params=keyint={gop}:min-keyint={gop}:scenecut=0:repeat-headers=1:aud=1",
        "-f", "/dev/stdout",  # write to stdout
    ]

    # ── Process 2: ffmpeg (reads wf-recorder stdout via stdin pipe + adds audio) ─
    ffmpeg_cmd = [
        FFMPEG_PATH, "-y",
        "-loglevel", "warning",    # show warnings/errors while we stabilize Samsung playback

        # Keep startup quick without starving ffmpeg of H.264 stream metadata.
        "-fflags", "+genpts",
        "-probesize", "65536",
        "-analyzeduration", "100000",

        # Video: read from wf-recorder via stdin pipe
        "-thread_queue_size", "1024",
        "-f", "nut",
        "-i", "pipe:0",

        # Audio from PulseAudio (ffmpeg wakes up suspended sinks)
        "-thread_queue_size", "1024",
        "-f", "pulse",
        "-i", audio_monitor,
    ]

    ffmpeg_cmd += [
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-vf", ",".join(vf_filters),

        # Re-encode into a conservative DLNA/Samsung-friendly H.264 stream.
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-tune", "zerolatency",
        "-profile:v", "main",
        "-level:v", "4.0",
        "-pix_fmt", "yuv420p",
        "-r", str(fps),
        "-g", str(gop),
        "-keyint_min", str(gop),
        "-sc_threshold", "0",
        "-bf", "0",
        "-b:v", bitrate,
        "-maxrate", bitrate,
        "-bufsize", _double_bitrate(bitrate),
        "-x264-params", "repeat-headers=1:aud=1",

        "-c:a", "aac",
        "-profile:a", "aac_low",
        "-b:a", "128k",
        "-ac", "2",
        "-ar", "48000",

        # Samsung DLNA is much happier with HLS files than a raw infinite pipe.
        "-force_key_frames", f"expr:gte(t,n_forced*{hls_time})",
        "-f", "hls",
        "-hls_time", hls_time,
        "-hls_init_time", hls_time,
        "-hls_list_size", "3",
        "-hls_delete_threshold", "6",
        "-hls_allow_cache", "0",
        "-hls_segment_type", "mpegts",
        "-hls_flags", "delete_segments+omit_endlist+independent_segments+temp_file",
        "-hls_segment_filename", f"{HLS_DIR}/stream%05d.ts",
        f"{HLS_DIR}/stream.m3u8",
    ]

    print(f"[FluxCast] Capturing screen : {monitor.name} via Wayland ({src_res})")
    print(f"[FluxCast] Capturing audio  : {audio_monitor}")
    if out_res != src_res:
        print(f"[FluxCast] Scaling output to: {out_res}")

    try:
        # wf-recorder writes NUT to its stdout
        wf_proc = subprocess.Popen(
            wf_cmd,
            stdout=subprocess.PIPE,
            stderr=None,   # temporarily print stderr directly for diagnostics
        )
        # ffmpeg reads wf-recorder's stdout via its own stdin
        ffmpeg_proc = subprocess.Popen(
            ffmpeg_cmd,
            stdin=wf_proc.stdout,  # direct kernel pipe — no FIFO needed
            stdout=subprocess.DEVNULL,
            stderr=None,
        )
        # Close parent's reference to wf_proc.stdout so ffmpeg gets EOF on wf exit
        wf_proc.stdout.close()
    except FileNotFoundError as e:
        print(f"[FluxCast] ERROR: Required executable not found: {e}")
        sys.exit(1)

    time.sleep(2.0)
    if wf_proc.poll() is not None:
        print("[FluxCast] ERROR: wf-recorder exited. See stderr above.")
        sys.exit(1)
    if ffmpeg_proc.poll() is not None:
        print("[FluxCast] ERROR: ffmpeg exited. See stderr above.")
        sys.exit(1)

    return [wf_proc, ffmpeg_proc]


def stop_capture(processes: "Optional[List[subprocess.Popen[bytes]]]") -> None:
    if not processes:
        return
    for proc in processes:
        if proc is not None and proc.poll() is None:
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
