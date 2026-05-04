# FluxCast

FluxCast streams a Linux desktop to a TV.

Current working fallback:

```text
screen/audio capture -> HLS/progressive MPEG-TS -> DLNA/UPnP TV player
```

Target low-latency path:

```text
screen/audio capture -> realtime H.264/AAC -> Wi-Fi Direct -> RTSP/RTP -> Miracast/WFD TV receiver
```

The DLNA path is already usable, but Samsung TVs still keep several seconds of
player buffer. The WFD/Miracast path is the Windows-like route and is being
built as a separate backend instead of replacing the stable fallback.

## Commands

Run the current DLNA fallback:

```bash
python3 main.py
```

Run passive capability diagnostics:

```bash
python3 main.py --doctor
```

Print the same diagnostics as JSON:

```bash
python3 main.py --doctor-json
```

Run an active Wi-Fi Direct peer scan:

```bash
python3 main.py --wfd-scan
```

Print the NetworkManager D-Bus connection call without activating Wi-Fi Direct:

```bash
python3 main.py --protocol wfd --wfd-peer 0 --wfd-dry-run
```

Try the experimental Miracast/WFD connection probe. Put the TV into
Screen Share/Wireless Display mode first:

```bash
python3 main.py --protocol wfd --wfd-peer 0
```

First WFD smoke test with generated video/audio:

```bash
python3 main.py --protocol wfd --wfd-peer 0 --wfd-test-pattern --output-res 1280x720 --bitrate 3M
```

If the TV opens but stays black, isolate the video path:

```bash
python3 main.py --protocol wfd --wfd-peer 0 --wfd-test-pattern --wfd-no-audio --output-res 1280x720 --bitrate 3M
```

If the test pattern reaches the TV, try the real desktop:

```bash
python3 main.py --protocol wfd --wfd-peer 0 --output-res 1920x1080 --bitrate 4M
```

## Backend Plan

- `dlna`: stable fallback, currently best with `progressive-ts`.
- `cast`: Chromecast-compatible media path.
- `wfd`: experimental Miracast/Wi-Fi Display path; goal is Windows-like latency.

WFD requires Linux support below Python: Wi-Fi Direct/P2P, WFD information
elements in `wpa_supplicant`, a realtime H.264 encoder, audio capture, and an
RTSP/RTP session. Python remains the coordinator, but the low-level wireless
display pieces are necessarily system-facing.

The current WFD backend can discover peers through NetworkManager D-Bus, start
an RTSP server on port `7236`, negotiate the WFD M1/M3/M4/M5/SETUP/PLAY flow,
and start a realtime RTP/MPEG-TS media stream when the TV sends `PLAY`.
