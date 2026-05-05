import glob
import os
import re
import subprocess
import shutil
import sys
import time
from typing import Optional, NamedTuple

FFMPEG_PATH = shutil.which("ffmpeg") or "/usr/sbin/ffmpeg"


class Monitor(NamedTuple):
    display: str
    name: str # e.g. 'eDP-1'
    width: int
    height: int
    x: int # x offset within the combined framebuffer
    y: int
    refresh: float # Hz



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


def start_capture(
    monitor: Monitor,
    fps: int = 30,
    bitrate: str = "4M",
    output_resolution: Optional[str] = None,
) -> "subprocess.Popen[bytes]":
    src_res = f"{monitor.width}x{monitor.height}"
    out_res = output_resolution or src_res
    cmd = [
        "wf-recorder",
        "-y",
        "-D",
        "-r", str(fps),
        "-a",
        "-C", "aac",
        "-P", "b:a=128k",
        "-c", "libx264",
        "-m", "hls",
        "-p", "preset=ultrafast",
        "-p", "tune=zerolatency",
        "-p", "hls_time=2",
        "-p", "hls_list_size=6",
        "-p", "hls_flags=append_list",
        "-p", "pix_fmt=yuv420p",
        "-p", "profile=main",
        "-f", "/tmp/fluxcast/stream.m3u8",
        "-o", monitor.name,
    ]

    print(f"[FluxCast] Capturing Wayland monitor : {monitor.name} ({src_res})")
    if out_res != src_res:
        print(f"[FluxCast] Scaling output to : {out_res}")

    hls_dir = "/tmp/fluxcast"
    if os.path.exists(hls_dir):
        shutil.rmtree(hls_dir)
    os.makedirs(hls_dir, exist_ok=True)

    try:
        process = subprocess.Popen(
            cmd,
            stderr=subprocess.DEVNULL,
        )
    except FileNotFoundError as e:
        print(f"[FluxCast] ERROR: Required executable not found: {e}")
        sys.exit(1)

    time.sleep(1.5)
    if process.poll() is not None:
        print(f"[FluxCast] ERROR: wf-recorder exited immediately. Check monitor name.")
        sys.exit(1)

    return process


def stop_capture(process: "Optional[subprocess.Popen[bytes]]") -> None:
    if process is None:
        return
    if process.poll() is None:
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
