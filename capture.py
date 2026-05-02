import glob
import os
import re
import subprocess
import shutil
import sys
import time
from typing import Optional, NamedTuple, List

FFMPEG_PATH = shutil.which("ffmpeg") or "/usr/sbin/ffmpeg"
VIDEO_FIFO = "/tmp/fluxcast_vid.pipe"


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
        out = subprocess.check_output(["pactl", "list", "short", "sinks"], text=True)
        for line in out.splitlines():
            if "RUNNING" in line:
                return line.split('\t')[1] + ".monitor"
    except Exception:
        pass
    return "default"


def start_capture(
    monitor: Monitor,
    fps: int = 30,
    bitrate: str = "4M",
    output_resolution: Optional[str] = None,
) -> List["subprocess.Popen[bytes]"]:
    """
    Returns [wf_proc, ffmpeg_proc].  Both must be passed to stop_capture().
    
    Architecture:
      wf-recorder (Wayland-native video) → NUT over named FIFO → ffmpeg (adds PulseAudio audio) → HLS
    """
    src_res = f"{monitor.width}x{monitor.height}"
    out_res = output_resolution or src_res

    audio_monitor = _detect_audio_monitor()

    # Prepare HLS output dir
    hls_dir = "/tmp/fluxcast"
    if os.path.exists(hls_dir):
        shutil.rmtree(hls_dir)
    os.makedirs(hls_dir, exist_ok=True)

    # Named FIFO for video: wf-recorder → ffmpeg
    if os.path.exists(VIDEO_FIFO):
        os.remove(VIDEO_FIFO)
    os.mkfifo(VIDEO_FIFO)

    vf_filters = []
    if out_res != src_res:
        vf_filters.append(f"scale={out_res.replace('x', ':')}")

    # ── Process 1: wf-recorder (video only, NUT muxer, pipe-friendly) ─────────
    wf_cmd = [
        "wf-recorder",
        "-y",
        "-D",               # no-damage: constant FPS even on static screens
        "-r", str(fps),
        "-o", monitor.name, # Wayland output name (e.g. HDMI-A-1)
        "-c", "libx264",    # encode in H.264 so the FIFO carries small data
        "-m", "nut",        # NUT muxer — designed for pipes, no seekable index needed
        "-p", "preset=ultrafast",
        "-p", "tune=zerolatency",
        "-p", "pix_fmt=yuv420p",
        "-p", "profile=main",
        "-f", VIDEO_FIFO,   # write to named FIFO
    ]

    # ── Process 2: ffmpeg (reads video from FIFO + audio from PulseAudio → HLS) ─
    ffmpeg_cmd = [
        FFMPEG_PATH, "-y",
        "-loglevel", "warning",

        # Video from wf-recorder via FIFO
        "-f", "nut",
        "-i", VIDEO_FIFO,

        # Audio from PulseAudio (ffmpeg wakes up suspended sinks)
        "-f", "pulse",
        "-i", audio_monitor,
    ]

    if vf_filters:
        ffmpeg_cmd += ["-vf", ",".join(vf_filters)]

    ffmpeg_cmd += [
        "-c:v", "copy",         # video already encoded by wf-recorder, just copy
        "-c:a", "aac",
        "-b:a", "128k",

        # HLS output — Samsung Tizen proven format
        "-f", "hls",
        "-hls_time", "2",
        "-hls_list_size", "6",
        "-hls_flags", "append_list",
        f"{hls_dir}/stream.m3u8",
    ]

    print(f"[FluxCast] Capturing screen : {monitor.name} via Wayland ({src_res})")
    print(f"[FluxCast] Capturing audio  : {audio_monitor}")
    if out_res != src_res:
        print(f"[FluxCast] Scaling output to: {out_res}")

    try:
        # Start ffmpeg FIRST (it opens the FIFO for reading, blocking until wf-recorder opens for writing)
        ffmpeg_proc = subprocess.Popen(ffmpeg_cmd, stderr=subprocess.DEVNULL)
        # Then start wf-recorder (opens FIFO for writing, unblocking ffmpeg)
        wf_proc = subprocess.Popen(wf_cmd, stderr=subprocess.DEVNULL)
    except FileNotFoundError as e:
        print(f"[FluxCast] ERROR: Required executable not found: {e}")
        sys.exit(1)

    time.sleep(2.0)
    if wf_proc.poll() is not None:
        print(f"[FluxCast] ERROR: wf-recorder exited immediately. Check monitor name.")
        sys.exit(1)
    if ffmpeg_proc.poll() is not None:
        print(f"[FluxCast] ERROR: ffmpeg exited immediately. Check audio device.")
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
    # Clean up FIFO
    if os.path.exists(VIDEO_FIFO):
        os.remove(VIDEO_FIFO)
