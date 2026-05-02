import http.server
import os
import socketserver
import threading
from typing import Optional

HLS_DIR = "/tmp/fluxcast"


class HLSRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Serves HLS segments from /tmp/fluxcast with CORS + no-cache headers."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=HLS_DIR, **kwargs)

    def log_message(self, format, *args):
        if self.path.endswith(".m3u8"):
            print(f"[FluxCast Server] {self.client_address[0]} → {self.path}")

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        self.send_header("transferMode.dlna.org", "Streaming")
        if self.path.endswith(".m3u8"):
            self.send_header("Content-Type", "application/x-mpegurl")
        elif self.path.endswith(".ts"):
            self.send_header("Content-Type", "video/mp2t")
        super().end_headers()


class StreamServer:
    def __init__(self, host: str = "0.0.0.0", port: int = 8080):
        self.host = host
        self.port = port
        self._server: Optional[socketserver.TCPServer] = None
        self._thread: Optional[threading.Thread] = None

    def start(self, capture_process=None) -> None:
        os.makedirs(HLS_DIR, exist_ok=True)
        self._server = http.server.ThreadingHTTPServer(
            (self.host, self.port), HLSRequestHandler
        )
        self._thread = threading.Thread(target=self._server.serve_forever, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        if self._server:
            self._server.shutdown()
