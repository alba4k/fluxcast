import http.server
import os
import socketserver
import threading
from typing import Optional
from urllib.parse import unquote, urlsplit


HLS_DIR = "/tmp/fluxcast"

DLNA_FLAGS = "01700000000000000000000000000000"
HLS_CONTENT_FEATURES = (
    "DLNA.ORG_OP=01;"
    "DLNA.ORG_CI=0;"
    f"DLNA.ORG_FLAGS={DLNA_FLAGS}"
)
TS_CONTENT_FEATURES = (
    "DLNA.ORG_PN=AVC_TS_MP_HD_AAC;"
    "DLNA.ORG_OP=01;"
    "DLNA.ORG_CI=0;"
    f"DLNA.ORG_FLAGS={DLNA_FLAGS}"
)


def _content_type(path: str) -> str:
    if path.endswith(".m3u8"):
        return "application/x-mpegurl"
    if path.endswith(".ts"):
        return "video/mp2t"
    return "application/octet-stream"


def _content_features(path: str) -> str:
    if path.endswith(".ts"):
        return TS_CONTENT_FEATURES
    return HLS_CONTENT_FEATURES


class HLSRequestHandler(http.server.BaseHTTPRequestHandler):
    """Serves low-latency HLS files with Range support for Samsung DLNA."""

    protocol_version = "HTTP/1.1"

    def log_message(self, format, *args):
        return

    def _local_path(self) -> Optional[str]:
        path = unquote(urlsplit(self.path).path).lstrip("/")
        if not path:
            path = "stream.m3u8"
        normalized = os.path.normpath(path)
        if normalized.startswith("..") or os.path.isabs(normalized):
            return None
        return os.path.join(HLS_DIR, normalized)

    def _send_common_headers(self, local_path: str) -> None:
        self.send_header("Content-Type", _content_type(local_path))
        self.send_header("Accept-Ranges", "bytes")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        self.send_header("Connection", "close")
        self.send_header("transferMode.dlna.org", "Streaming")
        self.send_header("contentFeatures.dlna.org", _content_features(local_path))

    def _send_empty(self, status: int) -> None:
        self.close_connection = True
        self.send_response(status)
        self.send_header("Content-Length", "0")
        self.send_header("Connection", "close")
        self.end_headers()

    def _parse_range(self, size: int) -> Optional[tuple[int, int]]:
        raw = self.headers.get("Range")
        if not raw:
            return None
        if not raw.startswith("bytes=") or "," in raw:
            return None

        start_text, _, end_text = raw[6:].partition("-")
        try:
            if start_text == "":
                suffix_len = int(end_text)
                if suffix_len <= 0:
                    return None
                return max(0, size - suffix_len), size - 1

            start = int(start_text)
            end = int(end_text) if end_text else size - 1
        except ValueError:
            return None

        if start >= size:
            return None
        return start, min(end, size - 1)

    def _serve_file(self, send_body: bool) -> None:
        local_path = self._local_path()
        if local_path is None or not os.path.isfile(local_path):
            self._send_empty(404)
            return

        size = os.path.getsize(local_path)
        byte_range = self._parse_range(size)
        self.close_connection = True

        if byte_range is None:
            start, end = 0, size - 1
            status = 200
        else:
            start, end = byte_range
            status = 206

        length = max(0, end - start + 1)
        self.send_response(status)
        self._send_common_headers(local_path)
        self.send_header("Content-Length", str(length))
        if status == 206:
            self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
        self.end_headers()

        if not send_body:
            return

        request_range = self.headers.get("Range")
        if local_path.endswith(".m3u8") or request_range:
            range_suffix = f", Range: {request_range}" if request_range else ""
            print(
                f"[FluxCast Server] {self.client_address[0]} -> {self.path} "
                f"({status}, {length} bytes{range_suffix})"
            )

        with open(local_path, "rb") as file:
            file.seek(start)
            remaining = length
            while remaining > 0:
                chunk = file.read(min(64 * 1024, remaining))
                if not chunk:
                    break
                self.wfile.write(chunk)
                remaining -= len(chunk)

    def do_HEAD(self):
        self._serve_file(send_body=False)

    def do_GET(self):
        self._serve_file(send_body=True)


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
