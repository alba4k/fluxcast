# FluxCast

FluxCast streams a Linux desktop to a TV.

## Project Status

FluxCast is currently in **early $\mathbf{\color{red}!!!ALPHA!!!}$ testing**. 

Current validated scope:

- `wfd` is the primary path and the only mode tested as "release-ready".
- `dlna` works as fallback, using `--transport hls`.
- `cast` is experimental and currently not working in the tested Samsung setup.

The project currently focuses on **WFD/Miracast on Linux (Hyprland/wlroots class setups)**.  
DLNA and Cast are available, but they are best treated as fallback or experimental paths.

## Quick Start

Default WFD run (interactive monitor/peer selection):

```bash
python3 main.py
```

WFD with latency/session JSONL log:

```bash
python3 main.py --wfd-latency-log
```

DLNA fallback:

```bash
python3 main.py --protocol dlna --transport hls
```

Cast mode (optional, if your TV supports it):

```bash
python3 main.py --protocol cast
```

## What Works Best

### WFD (Primary)

```text
screen + audio capture -> H.264/AAC RTP -> Wi-Fi Direct + RTSP -> TV WFD receiver
```

This is the lowest-latency and most predictable path in the current codebase.

### DLNA (Fallback)

```text
desktop capture -> HTTP stream -> DLNA/UPnP AVTransport -> native TV player
```

- Prefer `--transport hls` on Samsung TVs.
- `progressive-ts` can freeze or stutter on some models.

### Cast (Optional)

- Requires a TV/device with real Google Cast support.
- Requires `pychromecast`.
- Not reliable on many Samsung TV models.


## Installation

### Python packages

```bash
git clone https://github.com/IlyaP358/fluxcast.git
cd fluxcast
python3 -m venv venv # if you may use only miracast dont need it
pip install -r requirements.txt
python3 main.py # and flags as you need
```

DLNA/Cast features require additional packages listed in `requirements.txt`.

### System tools (important)

WFD mode also depends on system binaries, not only Python packages:

- `ffmpeg`
- `wf-recorder` (Wayland/wlroots capture path)
- `nmcli`, `gdbus`, `iw`, `wpa_cli` (Wi-Fi Direct and diagnostics)
- `pactl` (audio monitor autodetect)

Use:

```bash
python3 main.py --doctor
```

to check your machine before running WFD.


## Documentation

Detailed flags, modes, and usage examples:  
[documentation/documentation.md](documentation/documentation.md)



## Tested Environment

Hardware:

- PC: ThinkBook 14 G4+ IAP
- CPU: Intel i5-1240P (16 threads) up to 4.40 GHz
- GPU: Intel Iris Xe Graphics
- RAM: 16 GB

Software:

- OS: Arch Linux
- Kernel: 7.0.3-arch1-1
- WM: Hyprland 0.54.3
- Shell: zsh 5.9
- Terminal: kitty 0.46.2
