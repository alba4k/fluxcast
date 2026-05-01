import http.server
import socketserver
import os
import threading
from typing import Optional

HLS_DIR = "/tmp/fluxcast"


class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    """
    Serves files from /tmp/fluxcast with CORS and no-cache headers.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=HLS_DIR, **kwargs)

    def log_message(self, format, *args):
        # Mute logging unless you want it
        if "stream.m3u8" in self.path:
            print(f"[FluxCast Server] {self.client_address[0]} requested: {self.path}")

    def end_headers(self):
        # Enable CORS for web players, though DLNA doesn't care
        self.send_header("Access-Control-Allow-Origin", "*")
        # Ensure the playlist isn't cached
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        
        # Samsung specific DLNA streaming spoof headers, just in case
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
        """ Note: capture_process is ignored, as ffmpeg now writes directly to disk """
        os.makedirs(HLS_DIR, exist_ok=True)
        
        # ThreadingHTTPServer handles concurrent requests (crucial for Samsung DLNA probes)
        self._server = http.server.ThreadingHTTPServer((self.host, self.port), CORSRequestHandler)
        self._thread = threading.Thread(target=self._server.serve_forever, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        if self._server:
            self._server.shutdown()
