"""
FluxCast entry point

Usage:
    python main.py [OPTIONS]

    --protocol dlna|cast     dlna = UPnP native screening (default, like Windows Cast to Device)
                             cast = pychromecast (needs Chromecast built-in)
    --host HOST              LAN IP to advertise to the TV (default: auto-detect)
    --port PORT              HTTP server port (default: 8080)
    --output-res WxH         Scale output (e.g. 1920x1080); default: native
    --fps N                  Frames per second (default: 30)
    --bitrate Xm             Video bitrate (default: 4M)
    --discover-timeout N     mDNS/UPnP scan timeout (default: 5)
    --tv-ip IP               (For cast protocol only: direct IP connection)
"""

import argparse
import glob
import os
import signal
import socket
import time
import sys
import termios

from capture import prompt_monitor, start_capture, stop_capture
from server import HLS_DIR, StreamServer


def get_local_ip() -> str:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="FluxCast — stream your Arch Linux desktop to a Smart TV"
    )
    parser.add_argument("--protocol", default="dlna",
                        choices=["dlna", "cast"],
                        help="Connection protocol: dlna (UPnP, default) "
                             "or cast (pychromecast / Chromecast built-in)")
    parser.add_argument("--tv-ip", default=None, dest="tv_ip",
                        help="TV IP address (only applicable for --protocol cast)")
    parser.add_argument("--host", default=None,
                        help="LAN IP to advertise in the stream URL (default: auto)")
    parser.add_argument("--port", type=int, default=8080,
                        help="HTTP server port (default: 8080)")
    parser.add_argument("--output-res", default=None, dest="output_res",
                        help="Scale output to WxH, e.g. 1920x1080 (default: native)")
    parser.add_argument("--fps", type=int, default=30,
                        help="Frames per second (default: 30)")
    parser.add_argument("--bitrate", default="4M",
                        help="Video bitrate (default: 4M)")
    parser.add_argument("--discover-timeout", type=int, default=5,
                        dest="discover_timeout",
                        help="Discovery timeout in seconds (default: 5)")
    return parser.parse_args()


# ── terminal helpers ──────────────────────────────────────────────────────────

def _save_term():
    try:
        if sys.stdin.isatty():
            return termios.tcgetattr(sys.stdin.fileno())
    except termios.error:
        pass
    return None


def _restore_term(saved) -> None:
    if saved is None:
        return
    try:
        if sys.stdin.isatty():
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, saved)
    except termios.error:
        pass


def _wait_for_hls_segments(required_segments: int = 2, timeout: float = 15.0) -> bool:
    playlist = os.path.join(HLS_DIR, "stream.m3u8")
    start = time.monotonic()

    while time.monotonic() - start < timeout:
        segments = []
        for path in glob.glob(os.path.join(HLS_DIR, "stream*.ts")):
            try:
                if os.path.getsize(path) > 0:
                    segments.append(path)
            except OSError:
                pass
        if os.path.exists(playlist) and os.path.getsize(playlist) > 0:
            try:
                with open(playlist, "r", encoding="utf-8", errors="replace") as file:
                    playlist_text = file.read()
            except OSError:
                playlist_text = ""
            listed_segments = playlist_text.count(".ts")
            if listed_segments >= required_segments and len(segments) >= required_segments:
                waited = time.monotonic() - start
                print(f" ready! ({len(segments)} segments, {waited:.1f}s)")
                return True
        time.sleep(0.2)

    print(" [TIMEOUT]")
    return False


# ── main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    args = parse_args()

    host = args.host or get_local_ip()
    stream_url = f"http://{host}:{args.port}/stream.m3u8"

    _tty_state = _save_term() # save before ffmpeg corrupts it

    ffmpeg_procs = None
    stream_server = None
    tv = None

    def shutdown(signum=None, frame=None):
        print("\n[FluxCast] Stopping…")
        if tv is not None:
            try:
                if args.protocol == "dlna":
                    from dlna import stop_cast
                    stop_cast(tv)
                else:
                    from cast import cast
                    cast.stop_cast(tv)
            except Exception:
                pass
        if stream_server:
            stream_server.stop()
        stop_capture(ffmpeg_procs)
        _restore_term(_tty_state)
        print("[FluxCast] Stopped. Goodbye!")
        sys.exit(0)

    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    print("=" * 55)
    print("  FluxCast — Desktop → Smart TV via UPnP/DLNA")
    print("=" * 55)

    monitor = prompt_monitor()

    ffmpeg_procs = start_capture(
        monitor=monitor,
        fps=args.fps,
        bitrate=args.bitrate,
        output_resolution=args.output_res,
    )
    print("[FluxCast] Screen capture started.")

    # HTTP server — serves the HLS playlist and MPEG-TS segments from /tmp/fluxcast.
    stream_server = StreamServer(host="0.0.0.0", port=args.port)
    stream_server.start()
    print(f"[FluxCast] HTTP server: {stream_url}")

    print("[FluxCast] Waiting for HLS stream to start…", end="", flush=True)
    if not _wait_for_hls_segments(required_segments=2, timeout=15.0):
        print("[FluxCast] ERROR: ffmpeg produced no playable HLS segments.")
        shutdown()
    print("[FluxCast] HLS is producing segments ✓")

    if args.protocol == "dlna":
        from dlna import discover_devices, prompt_device, start_cast
        devices = discover_devices(timeout=args.discover_timeout)
        tv = prompt_device(devices)
        start_cast(tv, stream_url)

    else:  # cast protocol
        from cast import discover_devices, connect_by_ip, prompt_device, start_cast
        if args.tv_ip:
            tv = connect_by_ip(args.tv_ip)
        else:
            print("[FluxCast] Searching for Cast devices on the network…")
            devices = discover_devices(timeout=args.discover_timeout)
            tv = prompt_device(devices)
            print(f"[FluxCast] Found: {tv.cast_info.friendly_name}")
        start_cast(tv, stream_url)

    print("[FluxCast] Casting started. Press Ctrl+C to stop.")
    signal.pause()


if __name__ == "__main__":
    main()
