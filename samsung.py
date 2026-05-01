"""
samsung.py — Samsung Tizen Smart TV control via WebSocket API (port 8001/8002)

Protocol: Samsung SmartThings / Tizen TV WebSocket API v2
No extra pip deps beyond websocket-client (already in venv).

References:
  https://github.com/Ape/samsungctl
  https://github.com/xchwarze/samsung-tv-ws-api
"""

import base64
import json
import socket
import sys
import time
from typing import Optional

try:
    import websocket
except ImportError:
    print("[FluxCast] ERROR: websocket-client is not installed. "
          "Run: pip install websocket-client")
    sys.exit(1)

APP_NAME = "FluxCast"
# Samsung browser app IDs (try in order)
BROWSER_APP_IDS = [
    "org.tizen.browser",
    "org.tizen.crnt.applicationDock",
]


def _make_app_name_b64(name: str) -> str:
    return base64.b64encode(name.encode()).decode()


def _try_port(host: str, port: int, timeout: float = 2.0) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def _choose_port(host: str) -> int:
    if _try_port(host, 8002):
        return 8002
    if _try_port(host, 8001):
        return 8001
    print(f"[FluxCast] ERROR: Samsung TV at {host} is not reachable on port 8001 or 8002.")
    sys.exit(1)


def _build_ws_url(host: str, port: int, app_name: str) -> str:
    name_b64 = _make_app_name_b64(app_name)
    scheme = "wss" if port == 8002 else "ws"
    return f"{scheme}://{host}:{port}/api/v2/channels/samsung.remote.control?name={name_b64}"


class SamsungTV:

    def __init__(self, host: str, timeout: int = 10):
        self.host = host
        self.timeout = timeout
        self._ws: Optional[websocket.WebSocket] = None
        self._port: int = 0

    def connect(self) -> None:
        self._port = _choose_port(self.host)
        url = _build_ws_url(self.host, self._port, APP_NAME)

        print(f"[FluxCast] Connecting to Samsung TV at {self.host}:{self._port}…")

        ws_opts: dict = {"timeout": self.timeout}
        if self._port == 8002:
            import ssl
            ws_opts["sslopt"] = {"cert_reqs": ssl.CERT_NONE}

        try:
            self._ws = websocket.create_connection(url, **ws_opts)
        except Exception as exc:
            print(f"[FluxCast] ERROR: WebSocket connection failed — {exc}")
            print("[FluxCast] Check: TV is ON, same network, and")
            print("[FluxCast]   Settings → General → External Device Manager → "
                  "Device Connection Manager → ON")
            sys.exit(1)

        try:
            raw = self._ws.recv()
            msg = json.loads(raw)
            event = msg.get("event", "")
            if "unauthorized" in event.lower():
                print("[FluxCast] TV denied connection. "
                      "Please accept the access request on your TV screen and retry.")
                self._ws.close()
                sys.exit(1)
            if "ms.channel.connect" in event:
                print(f"[FluxCast] TV connected: {msg.get('data', {}).get('id', 'OK')}")
        except Exception:
            pass

    def _send(self, payload: dict) -> None:
        if self._ws is None:
            raise RuntimeError("Not connected")
        self._ws.send(json.dumps(payload))

    def open_url(self, url: str) -> None:
        for app_id in BROWSER_APP_IDS:
            try:
                self._launch_app(app_id, url)
                time.sleep(1.5)
                return
            except Exception:
                continue
        print("[FluxCast] WARNING: Could not launch browser app. "
              "Try opening the URL manually on the TV.")

    def _launch_app(self, app_id: str, url: str) -> None:
        payload = {
            "method": "ms.channel.emit",
            "params": {
                "event": "ed.apps.launch",
                "to": "host",
                "data": {
                    "appId": app_id,
                    "action_type": "NATIVE_LAUNCH",
                    "metaTag": url,
                },
            },
        }
        self._send(payload)

    def key(self, keycode: str) -> None:
        """Send a remote-control key (e.g. 'KEY_ENTER', 'KEY_UP')."""
        payload = {
            "method": "ms.remote.control",
            "params": {
                "Cmd": "Click",
                "DataOfCmd": keycode,
                "Option": "false",
                "TypeOfRemote": "SendRemoteKey",
            },
        }
        self._send(payload)

    def disconnect(self) -> None:
        if self._ws:
            try:
                self._ws.close()
            except Exception:
                pass
            self._ws = None
