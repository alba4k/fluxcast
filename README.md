# FluxCast

FluxCast streams a Linux desktop to a TV.

Default path:

```text
screen/audio capture -> realtime H.264/AAC -> Wi-Fi Direct -> RTSP/RTP -> Miracast/WFD TV receiver
```

Fallback path:

```text
screen/audio capture -> HLS/progressive MPEG-TS -> DLNA/UPnP TV player
```

## Full Documentation

- Full CLI reference, all flags, combinations, and latency log format:
  - [documentation/documentation.md](documentation/documentation.md)

## Commands

Default run (WFD, interactive monitor and peer selection):

```bash
python3 main.py
```

WFD with latency JSONL logging:

```bash
python3 main.py --wfd-latency-log
```

DLNA fallback:

```bash
python3 main.py --protocol dlna
```

Capability diagnostics:

```bash
python3 main.py --doctor
```
