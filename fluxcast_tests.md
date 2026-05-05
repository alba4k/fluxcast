## Тест1
❯ python3 main.py --wfd-latency-log
[FluxCast Doctor] System capability report
[FluxCast Doctor] Miracast/WFD looks possible via NetworkManager; raw supplicant access is optional for this backend.

  Status Check                  Details
  ------ ---------------------- ------------------------------------------
  ok     python                 runtime (3.14.4 on Linux 7.0.3-arch1-1)
  ok     ffmpeg                 video/audio transcoding (/usr/sbin/ffmpeg)
  ok     wf-recorder            Wayland/wlroots screen capture (/usr/sbin/wf-recorder)
  ok     pactl                  PulseAudio/PipeWire-Pulse audio monitor detection (/usr/sbin/pactl)
  ok     xrandr                 X11 monitor detection fallback (/usr/sbin/xrandr)
  ok     nmcli                  NetworkManager Wi-Fi Direct control (/usr/sbin/nmcli)
  ok     iw                     kernel Wi-Fi interface inspection (/usr/sbin/iw)
  ok     wpa_cli                active Wi-Fi Direct scan/control (/usr/sbin/wpa_cli)
  ok     gdbus                  passive wpa_supplicant D-Bus capability checks (/usr/sbin/gdbus)
  ok     gst-launch-1.0         optional future WFD GStreamer pipeline (/usr/sbin/gst-launch-1.0)
  ok     gst-inspect-1.0        optional future WFD codec inspection (/usr/sbin/gst-inspect-1.0)
  ok     ffmpeg encoders        H.264 and AAC encoders are available (h264=libx264, h264_vaapi, h264_nvenc, h264_qsv, h264_v4l2m2m; aac=yes)
  ok     screen capture         Wayland capture path is available (WAYLAND_DISPLAY=wayland-1; wf-recorder=/usr/sbin/wf-recorder)
  ok     audio capture          default audio monitor can be derived (alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__Headphones__sink.monitor)
  ok     NetworkManager         Wi-Fi and P2P devices are visible (nmcli tool, version 1.56.0-1; wlan0:wifi:connected | lo:loopback:connected (externally) | virbr0:bridge:connected (externally) | p2p-dev-wlan0:wifi-p2p:disconnected | enp0s31f6:ethernet:unavailable)
  ok     iw P2P                 kernel exposes a P2P-device interface (phy#0 | 	Unnamed/non-netdev interface | 		wdev 0x2 | 		addr 2c:33:58:88:dc:45 | 		type P2P-device | 	Interface wlan0 | 		ifindex 3 | 		wdev 0x1 | 		addr 2c:33:58:88:dc:45 | 		ssid PODA_80295G | 		type managed | 		channel 36 (5180 MHz), width: 80 MHz, center1: 5210 MHz | 		txpower 22.00 dBm | 		multicast TXQ: | 			qsz-byt	qsz-pkt	flows	drops	marks	overlmt	hashcol	tx-bytes	tx-packets | 			0	0	0	0	0	0	0	0		0)
  warn   wpa_supplicant P2P     supplicant capability query failed (Error: GDBus.Error:org.freedesktop.DBus.Error.AccessDenied: Sender is not authorized to send message)
  warn   wpa_supplicant WFD     WFDIE query failed; supplicant may lack CONFIG_WIFI_DISPLAY (Error: GDBus.Error:org.freedesktop.DBus.Error.AccessDenied: Sender is not authorized to send message)


[FluxCast] Available monitors to capture:
  #    Monitor      Display  Resolution     Position       Refresh
  ---- ------------ -------- -------------- -------------- --------
  [0]  eDP-1        :0       2240x1400     0,0            60.0 Hz ← active
  [1]  HDMI-A-1     :0       1920x1080     2240,0         143.9 Hz

Select monitor [1]: 1
[FluxCast WFD] Starting NetworkManager Wi-Fi Direct scan on p2p-dev-wlan0 for 8s...
[FluxCast WFD] Wi-Fi Direct peer(s):
  [0] 82:47:86:69:2C:87  [TV] Samsung 7 Series (55) via NetworkManager
      WFD capability data detected
Select WFD peer [0]: 0
[FluxCast WFD] Latency log file: /tmp/fluxcast-wfd-latency.jsonl
[FluxCast WFD RTSP] Server listening on 0.0.0.0:7236
[FluxCast WFD] Connecting to [TV] Samsung 7 Series (55) via NetworkManager...
[FluxCast WFD] NetworkManager activation started: (objectpath '/org/freedesktop/NetworkManager/Settings/13', objectpath '/org/freedesktop/NetworkManager/ActiveConnection/9', @a{sv} {})
[FluxCast WFD] Waiting for NetworkManager P2P activation...
[FluxCast WFD] NM active connection: activating; p2p-dev-wlan0:config:0
[FluxCast WFD] NM active connection: activating; p2p-dev-wlan0/p2p-wlan0-4:activated:0
[FluxCast WFD] NM active connection: activated; p2p-dev-wlan0/p2p-wlan0-4:activated:0
[FluxCast WFD] P2P link is activated; waiting for Samsung RTSP...
[FluxCast WFD] Waiting for Samsung RTSP/WFD session. Press Ctrl+C to stop.
[FluxCast WFD RTSP] TV connected from 10.42.0.17:60100; local=10.42.0.1
[FluxCast WFD RTSP] -> M1_OPTIONS: OPTIONS (CSeq 1)
[FluxCast WFD RTSP] <- response: RTSP/1.0 200 OK
[FluxCast WFD RTSP]   CSeq: 1
[FluxCast WFD RTSP] <- response for M1_OPTIONS: 200 OK
[FluxCast WFD RTSP] -> M3_GET_PARAMETER: GET_PARAMETER (CSeq 2)
[FluxCast WFD RTSP]   wfd_video_formats
[FluxCast WFD RTSP]   wfd_audio_codecs
[FluxCast WFD RTSP]   wfd_client_rtp_ports
[FluxCast WFD RTSP] <- request: OPTIONS * RTSP/1.0
[FluxCast WFD RTSP]   CSeq: 1
[FluxCast WFD RTSP] -> response 200 OK for OPTIONS
[FluxCast WFD RTSP] <- response: RTSP/1.0 200 OK
[FluxCast WFD RTSP]   CSeq: 2
[FluxCast WFD RTSP]   Content-Type: text/parameters
[FluxCast WFD RTSP]   Content-Length: 199
[FluxCast WFD RTSP]   wfd_audio_codecs: LPCM 00000003 00, AAC 00000001 00
[FluxCast WFD RTSP]   wfd_video_formats: 40 00 01 10 000001e3 0f3fffff 00000fff 00 0000 00c8 01 none none
[FluxCast WFD RTSP]   wfd_client_rtp_ports: RTP/AVP/UDP;unicast 19002 0 mode=play
[FluxCast WFD RTSP] <- response for M3_GET_PARAMETER: 200 OK
[FluxCast WFD RTSP] Samsung RTP port: 19002; source port: 19004; audio=LPCM 00000003 00, AAC 00000001 00
[FluxCast WFD RTSP] Negotiated media mode: 1920x1080p30
[FluxCast WFD RTSP] Selected video format: 38 00 01 04 00000080 00000000 00000000 00 0000 0000 00 none none
[FluxCast WFD RTSP] -> M4_SET_PARAMETER: SET_PARAMETER (CSeq 3)
[FluxCast WFD RTSP]   wfd_video_formats: 38 00 01 04 00000080 00000000 00000000 00 0000 0000 00 none none
[FluxCast WFD RTSP]   wfd_audio_codecs: AAC 00000001 00
[FluxCast WFD RTSP]   wfd_presentation_URL: rtsp://10.42.0.1:7236/wfd1.0/streamid=0 none
[FluxCast WFD RTSP]   wfd_client_rtp_ports: RTP/AVP/UDP;unicast 19002 0 mode=play
[FluxCast WFD RTSP] <- response: RTSP/1.0 200 OK
[FluxCast WFD RTSP]   CSeq: 3
[FluxCast WFD RTSP] <- response for M4_SET_PARAMETER: 200 OK
[FluxCast WFD RTSP] -> M5_TRIGGER_SETUP: SET_PARAMETER (CSeq 4)
[FluxCast WFD RTSP]   wfd_trigger_method: SETUP
[FluxCast WFD RTSP] <- response: RTSP/1.0 200 OK
[FluxCast WFD RTSP]   CSeq: 4
[FluxCast WFD RTSP] <- response for M5_TRIGGER_SETUP: 200 OK
[FluxCast WFD RTSP] <- request: SETUP rtsp://10.42.0.1:7236/wfd1.0/streamid=0 RTSP/1.0
[FluxCast WFD RTSP]   CSeq: 2
[FluxCast WFD RTSP]   Transport: RTP/AVP/UDP;unicast;client_port=19002-19003
[FluxCast WFD RTSP] -> response 200 OK for SETUP
[FluxCast WFD RTSP] SETUP complete; RTP sink port=19002
[FluxCast WFD RTSP] <- request: PLAY rtsp://10.42.0.1:7236/wfd1.0/streamid=0 RTSP/1.0
[FluxCast WFD RTSP]   CSeq: 3
[FluxCast WFD RTSP]   Session: 4141160
[FluxCast WFD RTSP] -> response 200 OK for PLAY
[FluxCast WFD RTSP] Starting media as 1920x1080p30; RTP source port 19004
[FluxCast WFD Media] Raising bitrate for desktop clarity: 4M -> 8M
[FluxCast WFD Media] Capturing screen : HDMI-A-1 (1920x1080)
[FluxCast WFD Media] Capturing audio  : alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__Headphones__sink.monitor
[FluxCast WFD Media] RTP target      : 10.42.0.17:19002 from local port 19004
selected region 2240,0 1920x1080
Setting codec option: pix_fmt=yuv420p
Framerate: 30
Using video filter: fps=30
Output #0, nut, to '/dev/stdout':
  Stream #0:0: Video: rawvideo (BGR[0] / 0x524742), bgr0(pc), 1920x1080 [SAR 1:1 DAR 16:9], q=2-31, 1492992 kb/s
[Source @ 0x7f12f8005e40] Changing video frame properties on the fly is not supported by all filters.
[Source @ 0x7f12f8005e40] filter context - w: 1920 h: 1080 fmt: 121 csp: gbr range: unknown alpha: unspecified, incoming frame - w: 1920 h: 1080 fmt: 121 csp: unknown range: unknown alpha: unspecified pts_time: 0
[in#0/nut @ 0x55eaed5db140] Stream #0: not enough frames to estimate rate; consider increasing probesize
[aist#1:0/pcm_s16le @ 0x55eaed5f65c0] Guessed Channel Layout: stereo
[FluxCast WFD RTSP] PLAY accepted; media stream started.
[FluxCast WFD Media] Latency probe: first RTP bytes after PLAY in 701.3 ms
[FluxCast WFD Media] Latency probe: sender-path latency (RTSP connect -> first RTP) 3884.0 ms
[FluxCast WFD Media] Sender health: pid=158637:running, pid=158638:running; tx+1678 KiB on p2p-wlan0-4
[FluxCast WFD Media] Sender health: pid=158637:running, pid=158638:running; tx+6906 KiB on p2p-wlan0-4
[FluxCast WFD Media] Sender health: pid=158637:running, pid=158638:running; tx+12345 KiB on p2p-wlan0-4
[FluxCast WFD Media] Sender health: pid=158637:running, pid=158638:running; tx+18930 KiB on p2p-wlan0-4
[FluxCast WFD Media] Sender health: pid=158637:running, pid=158638:running; tx+24252 KiB on p2p-wlan0-4
[FluxCast WFD Media] Sender health: pid=158637:running, pid=158638:running; tx+29658 KiB on p2p-wlan0-4
[FluxCast WFD Media] Sender health: pid=158637:running, pid=158638:running; tx+34712 KiB on p2p-wlan0-4
[FluxCast WFD Media] Sender health: pid=158637:running, pid=158638:running; tx+40635 KiB on p2p-wlan0-4
[FluxCast WFD Media] Sender health: pid=158637:running, pid=158638:running; tx+46040 KiB on p2p-wlan0-4
[FluxCast WFD Media] Sender health: pid=158637:running, pid=158638:running; tx+51591 KiB on p2p-wlan0-4
[FluxCast WFD Media] Sender health: pid=158637:running, pid=158638:running; tx+56630 KiB on p2p-wlan0-4
[FluxCast WFD Media] Sender health: pid=158637:running, pid=158638:running; tx+62172 KiB on p2p-wlan0-4
^C
[FluxCast WFD] Stopping WFD session...
[FluxCast WFD] NetworkManager P2P connection deactivated.
[FluxCast WFD] NetworkManager P2P device disconnected.
[aost#0:1/aac @ 0x55eaed5febc0] Error submitting a packet to the muxer: Network is unreachable                             
    Last message repeated 1 times
[out#0/rtp_mpegts @ 0x55eaed5f9b00] Error muxing a packet
[out#0/rtp_mpegts @ 0x55eaed5f9b00] Task finished with error code: -101 (Network is unreachable)
[out#0/rtp_mpegts @ 0x55eaed5f9b00] Terminating thread with return code -101 (Network is unreachable)
 ~/test_scripts/fluxcast  main !8 ?2  [out#0/rtp_mpegts @ 0x55eaed5f9b00] Error writing trailer: Network is unreachable
[out#0/rtp_mpegts @ 0x55eaed5f9b00] Error closing file: Network is unreachable
❯ 
 ~/test_scripts/fluxcast  main !8 ?2  

❯ tail -f /tmp/fluxcast-wfd-latency.jsonl
{"ts": "2026-05-05T14:38:55.744+00:00", "mono": 7766.881472, "event": "sender_health", "processes": ["pid=158637:running", "pid=158638:running"], "tx_summary": "tx+12345 KiB on p2p-wlan0-4"}
{"ts": "2026-05-05T14:39:00.746+00:00", "mono": 7771.882821, "event": "sender_health", "processes": ["pid=158637:running", "pid=158638:running"], "tx_summary": "tx+18930 KiB on p2p-wlan0-4"}
{"ts": "2026-05-05T14:39:05.747+00:00", "mono": 7776.883841, "event": "sender_health", "processes": ["pid=158637:running", "pid=158638:running"], "tx_summary": "tx+24252 KiB on p2p-wlan0-4"}
{"ts": "2026-05-05T14:39:10.748+00:00", "mono": 7781.88519, "event": "sender_health", "processes": ["pid=158637:running", "pid=158638:running"], "tx_summary": "tx+29658 KiB on p2p-wlan0-4"}
{"ts": "2026-05-05T14:39:15.749+00:00", "mono": 7786.886133, "event": "sender_health", "processes": ["pid=158637:running", "pid=158638:running"], "tx_summary": "tx+34712 KiB on p2p-wlan0-4"}
{"ts": "2026-05-05T14:39:20.750+00:00", "mono": 7791.887094, "event": "sender_health", "processes": ["pid=158637:running", "pid=158638:running"], "tx_summary": "tx+40635 KiB on p2p-wlan0-4"}
{"ts": "2026-05-05T14:39:25.751+00:00", "mono": 7796.888124, "event": "sender_health", "processes": ["pid=158637:running", "pid=158638:running"], "tx_summary": "tx+46040 KiB on p2p-wlan0-4"}
{"ts": "2026-05-05T14:39:30.753+00:00", "mono": 7801.889874, "event": "sender_health", "processes": ["pid=158637:running", "pid=158638:running"], "tx_summary": "tx+51591 KiB on p2p-wlan0-4"}
{"ts": "2026-05-05T14:39:35.754+00:00", "mono": 7806.890952, "event": "sender_health", "processes": ["pid=158637:running", "pid=158638:running"], "tx_summary": "tx+56630 KiB on p2p-wlan0-4"}
{"ts": "2026-05-05T14:39:40.757+00:00", "mono": 7811.893781, "event": "sender_health", "processes": ["pid=158637:running", "pid=158638:running"], "tx_summary": "tx+62172 KiB on p2p-wlan0-4"}

## Тест 2
❯ python3 main.py --protocol wfd --output-res 1280x720 --fps 30 --bitrate 3M --wfd-media-pipeline ffmpeg --wfd-latency-log
[FluxCast Doctor] System capability report
[FluxCast Doctor] Miracast/WFD looks possible via NetworkManager; raw supplicant access is optional for this backend.

  Status Check                  Details
  ------ ---------------------- ------------------------------------------
  ok     python                 runtime (3.14.4 on Linux 7.0.3-arch1-1)
  ok     ffmpeg                 video/audio transcoding (/usr/sbin/ffmpeg)
  ok     wf-recorder            Wayland/wlroots screen capture (/usr/sbin/wf-recorder)
  ok     pactl                  PulseAudio/PipeWire-Pulse audio monitor detection (/usr/sbin/pactl)
  ok     xrandr                 X11 monitor detection fallback (/usr/sbin/xrandr)
  ok     nmcli                  NetworkManager Wi-Fi Direct control (/usr/sbin/nmcli)
  ok     iw                     kernel Wi-Fi interface inspection (/usr/sbin/iw)
  ok     wpa_cli                active Wi-Fi Direct scan/control (/usr/sbin/wpa_cli)
  ok     gdbus                  passive wpa_supplicant D-Bus capability checks (/usr/sbin/gdbus)
  ok     gst-launch-1.0         optional future WFD GStreamer pipeline (/usr/sbin/gst-launch-1.0)
  ok     gst-inspect-1.0        optional future WFD codec inspection (/usr/sbin/gst-inspect-1.0)
  ok     ffmpeg encoders        H.264 and AAC encoders are available (h264=libx264, h264_vaapi, h264_nvenc, h264_qsv, h264_v4l2m2m; aac=yes)
  ok     screen capture         Wayland capture path is available (WAYLAND_DISPLAY=wayland-1; wf-recorder=/usr/sbin/wf-recorder)
  ok     audio capture          default audio monitor can be derived (alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__Headphones__sink.monitor)
  ok     NetworkManager         Wi-Fi and P2P devices are visible (nmcli tool, version 1.56.0-1; wlan0:wifi:connected | lo:loopback:connected (externally) | virbr0:bridge:connected (externally) | p2p-dev-wlan0:wifi-p2p:disconnected | enp0s31f6:ethernet:unavailable)
  ok     iw P2P                 kernel exposes a P2P-device interface (phy#0 | 	Unnamed/non-netdev interface | 		wdev 0x2 | 		addr 2c:33:58:88:dc:45 | 		type P2P-device | 	Interface wlan0 | 		ifindex 3 | 		wdev 0x1 | 		addr 2c:33:58:88:dc:45 | 		ssid PODA_80295G | 		type managed | 		channel 36 (5180 MHz), width: 80 MHz, center1: 5210 MHz | 		txpower 22.00 dBm | 		multicast TXQ: | 			qsz-byt	qsz-pkt	flows	drops	marks	overlmt	hashcol	tx-bytes	tx-packets | 			0	0	0	0	0	0	0	0		0)
  warn   wpa_supplicant P2P     supplicant capability query failed (Error: GDBus.Error:org.freedesktop.DBus.Error.AccessDenied: Sender is not authorized to send message)
  warn   wpa_supplicant WFD     WFDIE query failed; supplicant may lack CONFIG_WIFI_DISPLAY (Error: GDBus.Error:org.freedesktop.DBus.Error.AccessDenied: Sender is not authorized to send message)


[FluxCast] Available monitors to capture:
  #    Monitor      Display  Resolution     Position       Refresh
  ---- ------------ -------- -------------- -------------- --------
  [0]  eDP-1        :0       2240x1400     0,0            60.0 Hz ← active
  [1]  HDMI-A-1     :0       1920x1080     2240,0         143.9 Hz

Select monitor [1]: 1
[FluxCast WFD] Starting NetworkManager Wi-Fi Direct scan on p2p-dev-wlan0 for 8s...
[FluxCast WFD] Wi-Fi Direct peer(s):
  [0] 82:47:86:69:2C:87  [TV] Samsung 7 Series (55) via NetworkManager
      WFD capability data detected
Select WFD peer [0]: 0
[FluxCast WFD] Latency log file: /tmp/fluxcast-wfd-latency.jsonl
[FluxCast WFD RTSP] Server listening on 0.0.0.0:7236
[FluxCast WFD] Connecting to [TV] Samsung 7 Series (55) via NetworkManager...
[FluxCast WFD] NetworkManager activation started: (objectpath '/org/freedesktop/NetworkManager/Settings/14', objectpath '/org/freedesktop/NetworkManager/ActiveConnection/10', @a{sv} {})
[FluxCast WFD] Waiting for NetworkManager P2P activation...
[FluxCast WFD] NM active connection: activating; p2p-dev-wlan0:config:0
[FluxCast WFD] NM active connection: activated; p2p-dev-wlan0/p2p-wlan0-5:activated:0
[FluxCast WFD] P2P link is activated; waiting for Samsung RTSP...
[FluxCast WFD] Waiting for Samsung RTSP/WFD session. Press Ctrl+C to stop.
[FluxCast WFD RTSP] TV connected from 10.42.0.17:60133; local=10.42.0.1
[FluxCast WFD RTSP] -> M1_OPTIONS: OPTIONS (CSeq 1)
[FluxCast WFD RTSP] <- response: RTSP/1.0 200 OK
[FluxCast WFD RTSP]   CSeq: 1
[FluxCast WFD RTSP] <- response for M1_OPTIONS: 200 OK
[FluxCast WFD RTSP] -> M3_GET_PARAMETER: GET_PARAMETER (CSeq 2)
[FluxCast WFD RTSP]   wfd_video_formats
[FluxCast WFD RTSP]   wfd_audio_codecs
[FluxCast WFD RTSP]   wfd_client_rtp_ports
[FluxCast WFD RTSP] <- request: OPTIONS * RTSP/1.0
[FluxCast WFD RTSP]   CSeq: 1
[FluxCast WFD RTSP] -> response 200 OK for OPTIONS
[FluxCast WFD RTSP] <- response: RTSP/1.0 200 OK
[FluxCast WFD RTSP]   CSeq: 2
[FluxCast WFD RTSP]   Content-Type: text/parameters
[FluxCast WFD RTSP]   Content-Length: 199
[FluxCast WFD RTSP]   wfd_audio_codecs: LPCM 00000003 00, AAC 00000001 00
[FluxCast WFD RTSP]   wfd_video_formats: 40 00 01 10 000001e3 0f3fffff 00000fff 00 0000 00c8 01 none none
[FluxCast WFD RTSP]   wfd_client_rtp_ports: RTP/AVP/UDP;unicast 19000 0 mode=play
[FluxCast WFD RTSP] <- response for M3_GET_PARAMETER: 200 OK
[FluxCast WFD RTSP] Samsung RTP port: 19000; source port: 19002; audio=LPCM 00000003 00, AAC 00000001 00
[FluxCast WFD RTSP] Negotiated media mode: 1280x720p30
[FluxCast WFD RTSP] Selected video format: 28 00 01 01 00000020 00000000 00000000 00 0000 0000 00 none none
[FluxCast WFD RTSP] -> M4_SET_PARAMETER: SET_PARAMETER (CSeq 3)
[FluxCast WFD RTSP]   wfd_video_formats: 28 00 01 01 00000020 00000000 00000000 00 0000 0000 00 none none
[FluxCast WFD RTSP]   wfd_audio_codecs: AAC 00000001 00
[FluxCast WFD RTSP]   wfd_presentation_URL: rtsp://10.42.0.1:7236/wfd1.0/streamid=0 none
[FluxCast WFD RTSP]   wfd_client_rtp_ports: RTP/AVP/UDP;unicast 19000 0 mode=play
[FluxCast WFD RTSP] <- response: RTSP/1.0 200 OK
[FluxCast WFD RTSP]   CSeq: 3
[FluxCast WFD RTSP] <- response for M4_SET_PARAMETER: 200 OK
[FluxCast WFD RTSP] -> M5_TRIGGER_SETUP: SET_PARAMETER (CSeq 4)
[FluxCast WFD RTSP]   wfd_trigger_method: SETUP
[FluxCast WFD RTSP] <- response: RTSP/1.0 200 OK
[FluxCast WFD RTSP]   CSeq: 4
[FluxCast WFD RTSP] <- response for M5_TRIGGER_SETUP: 200 OK
[FluxCast WFD RTSP] <- request: SETUP rtsp://10.42.0.1:7236/wfd1.0/streamid=0 RTSP/1.0
[FluxCast WFD RTSP]   CSeq: 2
[FluxCast WFD RTSP]   Transport: RTP/AVP/UDP;unicast;client_port=19000-19001
[FluxCast WFD RTSP] -> response 200 OK for SETUP
[FluxCast WFD RTSP] SETUP complete; RTP sink port=19000
[FluxCast WFD RTSP] <- request: PLAY rtsp://10.42.0.1:7236/wfd1.0/streamid=0 RTSP/1.0
[FluxCast WFD RTSP]   CSeq: 3
[FluxCast WFD RTSP]   Session: 4692465
[FluxCast WFD RTSP] -> response 200 OK for PLAY
[FluxCast WFD RTSP] Starting media as 1280x720p30; RTP source port 19002
[FluxCast WFD Media] Raising bitrate for desktop clarity: 3M -> 5M
[FluxCast WFD Media] Capturing screen : HDMI-A-1 (1920x1080)
[FluxCast WFD Media] Capturing audio  : alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__Headphones__sink.monitor
[FluxCast WFD Media] Scaling output  : 1280x720
[FluxCast WFD Media] RTP target      : 10.42.0.17:19000 from local port 19002
selected region 2240,0 1920x1080
Setting codec option: pix_fmt=yuv420p
Framerate: 30
Using video filter: fps=30
Output #0, nut, to '/dev/stdout':
  Stream #0:0: Video: rawvideo (BGR[0] / 0x524742), bgr0(pc), 1920x1080 [SAR 1:1 DAR 16:9], q=2-31, 1492992 kb/s
[Source @ 0x7f6014005e40] Changing video frame properties on the fly is not supported by all filters.
[Source @ 0x7f6014005e40] filter context - w: 1920 h: 1080 fmt: 121 csp: gbr range: unknown alpha: unspecified, incoming frame - w: 1920 h: 1080 fmt: 121 csp: unknown range: unknown alpha: unspecified pts_time: 0
[in#0/nut @ 0x563d65cf4140] Stream #0: not enough frames to estimate rate; consider increasing probesize
[aist#1:0/pcm_s16le @ 0x563d65d0f5c0] Guessed Channel Layout: stereo
[FluxCast WFD RTSP] PLAY accepted; media stream started.
[FluxCast WFD Media] Latency probe: first RTP bytes after PLAY in 702.3 ms
[FluxCast WFD Media] Latency probe: sender-path latency (RTSP connect -> first RTP) 2933.8 ms
[FluxCast WFD Media] Sender health: pid=160031:running, pid=160032:running; tx+944 KiB on p2p-wlan0-5
[FluxCast WFD Media] Sender health: pid=160031:running, pid=160032:running; tx+4893 KiB on p2p-wlan0-5
[FluxCast WFD Media] Sender health: pid=160031:running, pid=160032:running; tx+8567 KiB on p2p-wlan0-5
[FluxCast WFD Media] Sender health: pid=160031:running, pid=160032:running; tx+12068 KiB on p2p-wlan0-5
[FluxCast WFD Media] Sender health: pid=160031:running, pid=160032:running; tx+15444 KiB on p2p-wlan0-5
[FluxCast WFD Media] Sender health: pid=160031:running, pid=160032:running; tx+18790 KiB on p2p-wlan0-5
[FluxCast WFD Media] Sender health: pid=160031:running, pid=160032:running; tx+22238 KiB on p2p-wlan0-5
[FluxCast WFD Media] Sender health: pid=160031:running, pid=160032:running; tx+25857 KiB on p2p-wlan0-5
[FluxCast WFD Media] Sender health: pid=160031:running, pid=160032:running; tx+29257 KiB on p2p-wlan0-5
[FluxCast WFD Media] Sender health: pid=160031:running, pid=160032:running; tx+32465 KiB on p2p-wlan0-5
[FluxCast WFD Media] Sender health: pid=160031:running, pid=160032:running; tx+36093 KiB on p2p-wlan0-5
^C
[FluxCast WFD] Stopping WFD session...
[FluxCast WFD] NetworkManager P2P connection deactivated.
[FluxCast WFD] NetworkManager P2P device disconnected.

❯ tail -f /tmp/fluxcast-wfd-latency.jsonl
{"ts": "2026-05-05T14:42:17.192+00:00", "mono": 7968.32927, "event": "latency_probe", "sender_startup_ms": 702.3, "setup_ms": 2231.5, "sender_path_latency_ms": 2933.8}
{"ts": "2026-05-05T14:42:17.193+00:00", "mono": 7968.3299, "event": "sender_health", "processes": ["pid=160031:running", "pid=160032:running"], "tx_summary": "tx+944 KiB on p2p-wlan0-5"}
{"ts": "2026-05-05T14:42:22.195+00:00", "mono": 7973.331719, "event": "sender_health", "processes": ["pid=160031:running", "pid=160032:running"], "tx_summary": "tx+4893 KiB on p2p-wlan0-5"}
{"ts": "2026-05-05T14:42:27.196+00:00", "mono": 7978.332713, "event": "sender_health", "processes": ["pid=160031:running", "pid=160032:running"], "tx_summary": "tx+8567 KiB on p2p-wlan0-5"}
{"ts": "2026-05-05T14:42:32.197+00:00", "mono": 7983.334212, "event": "sender_health", "processes": ["pid=160031:running", "pid=160032:running"], "tx_summary": "tx+12068 KiB on p2p-wlan0-5"}
{"ts": "2026-05-05T14:42:37.199+00:00", "mono": 7988.3363, "event": "sender_health", "processes": ["pid=160031:running", "pid=160032:running"], "tx_summary": "tx+15444 KiB on p2p-wlan0-5"}
{"ts": "2026-05-05T14:42:42.200+00:00", "mono": 7993.337328, "event": "sender_health", "processes": ["pid=160031:running", "pid=160032:running"], "tx_summary": "tx+18790 KiB on p2p-wlan0-5"}
{"ts": "2026-05-05T14:42:47.201+00:00", "mono": 7998.338166, "event": "sender_health", "processes": ["pid=160031:running", "pid=160032:running"], "tx_summary": "tx+22238 KiB on p2p-wlan0-5"}
{"ts": "2026-05-05T14:42:52.202+00:00", "mono": 8003.339126, "event": "sender_health", "processes": ["pid=160031:running", "pid=160032:running"], "tx_summary": "tx+25857 KiB on p2p-wlan0-5"}
{"ts": "2026-05-05T14:42:57.203+00:00", "mono": 8008.340174, "event": "sender_health", "processes": ["pid=160031:running", "pid=160032:running"], "tx_summary": "tx+29257 KiB on p2p-wlan0-5"}
{"ts": "2026-05-05T14:43:02.204+00:00", "mono": 8013.341079, "event": "sender_health", "processes": ["pid=160031:running", "pid=160032:running"], "tx_summary": "tx+32465 KiB on p2p-wlan0-5"}
{"ts": "2026-05-05T14:43:07.205+00:00", "mono": 8018.342148, "event": "sender_health", "processes": ["pid=160031:running", "pid=160032:running"], "tx_summary": "tx+36093 KiB on p2p-wlan0-5"}

## Тест 3
❯ python3 main.py --protocol wfd --output-res 1280x720 --fps 30 --bitrate 4M --wfd-media-pipeline ffmpeg --wfd-latency-log
[FluxCast Doctor] System capability report
[FluxCast Doctor] Miracast/WFD looks possible via NetworkManager; raw supplicant access is optional for this backend.

  Status Check                  Details
  ------ ---------------------- ------------------------------------------
  ok     python                 runtime (3.14.4 on Linux 7.0.3-arch1-1)
  ok     ffmpeg                 video/audio transcoding (/usr/sbin/ffmpeg)
  ok     wf-recorder            Wayland/wlroots screen capture (/usr/sbin/wf-recorder)
  ok     pactl                  PulseAudio/PipeWire-Pulse audio monitor detection (/usr/sbin/pactl)
  ok     xrandr                 X11 monitor detection fallback (/usr/sbin/xrandr)
  ok     nmcli                  NetworkManager Wi-Fi Direct control (/usr/sbin/nmcli)
  ok     iw                     kernel Wi-Fi interface inspection (/usr/sbin/iw)
  ok     wpa_cli                active Wi-Fi Direct scan/control (/usr/sbin/wpa_cli)
  ok     gdbus                  passive wpa_supplicant D-Bus capability checks (/usr/sbin/gdbus)
  ok     gst-launch-1.0         optional future WFD GStreamer pipeline (/usr/sbin/gst-launch-1.0)
  ok     gst-inspect-1.0        optional future WFD codec inspection (/usr/sbin/gst-inspect-1.0)
  ok     ffmpeg encoders        H.264 and AAC encoders are available (h264=libx264, h264_vaapi, h264_nvenc, h264_qsv, h264_v4l2m2m; aac=yes)
  ok     screen capture         Wayland capture path is available (WAYLAND_DISPLAY=wayland-1; wf-recorder=/usr/sbin/wf-recorder)
  ok     audio capture          default audio monitor can be derived (alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__Headphones__sink.monitor)
  ok     NetworkManager         Wi-Fi and P2P devices are visible (nmcli tool, version 1.56.0-1; wlan0:wifi:connected | lo:loopback:connected (externally) | virbr0:bridge:connected (externally) | p2p-dev-wlan0:wifi-p2p:disconnected | enp0s31f6:ethernet:unavailable)
  ok     iw P2P                 kernel exposes a P2P-device interface (phy#1 | 	Unnamed/non-netdev interface | 		wdev 0x100000002 | 		addr 2c:33:58:88:dc:45 | 		type P2P-device | 	Interface wlan0 | 		ifindex 12 | 		wdev 0x100000001 | 		addr 2c:33:58:88:dc:45 | 		ssid PODA_80295G | 		type managed | 		channel 36 (5180 MHz), width: 80 MHz, center1: 5210 MHz | 		txpower 22.00 dBm | 		multicast TXQ: | 			qsz-byt	qsz-pkt	flows	drops	marks	overlmt	hashcol	tx-bytes	tx-packets | 			0	0	0	0	0	0	0	0		0)
  warn   wpa_supplicant P2P     supplicant capability query failed (Error: GDBus.Error:org.freedesktop.DBus.Error.AccessDenied: Sender is not authorized to send message)
  warn   wpa_supplicant WFD     WFDIE query failed; supplicant may lack CONFIG_WIFI_DISPLAY (Error: GDBus.Error:org.freedesktop.DBus.Error.AccessDenied: Sender is not authorized to send message)


[FluxCast] Available monitors to capture:
  #    Monitor      Display  Resolution     Position       Refresh
  ---- ------------ -------- -------------- -------------- --------
  [0]  eDP-1        :0       2240x1400     0,0            60.0 Hz ← active
  [1]  HDMI-A-1     :0       1920x1080     2240,0         143.9 Hz

Select monitor [1]: 1
[FluxCast WFD] Starting NetworkManager Wi-Fi Direct scan on p2p-dev-wlan0 for 8s...
[FluxCast WFD] Wi-Fi Direct peer(s):
  [0] 82:47:86:69:2C:87  [TV] Samsung 7 Series (55) via NetworkManager
      WFD capability data detected
Select WFD peer [0]: 0
[FluxCast WFD] Latency log file: /tmp/fluxcast-wfd-latency.jsonl
[FluxCast WFD RTSP] Server listening on 0.0.0.0:7236
[FluxCast WFD] Connecting to [TV] Samsung 7 Series (55) via NetworkManager...
[FluxCast WFD] NetworkManager activation started: (objectpath '/org/freedesktop/NetworkManager/Settings/15', objectpath '/org/freedesktop/NetworkManager/ActiveConnection/12', @a{sv} {})
[FluxCast WFD] Waiting for NetworkManager P2P activation...
[FluxCast WFD] NM active connection: activating; p2p-dev-wlan0:config:0
[FluxCast WFD] NM active connection: activating; p2p-dev-wlan0:ip-config:0
[FluxCast WFD] NM active connection: activated; p2p-dev-wlan0/p2p-wlan0-0:activated:0
[FluxCast WFD] P2P link is activated; waiting for Samsung RTSP...
[FluxCast WFD] Waiting for Samsung RTSP/WFD session. Press Ctrl+C to stop.
[FluxCast WFD RTSP] TV connected from 10.42.0.17:60166; local=10.42.0.1
[FluxCast WFD RTSP] -> M1_OPTIONS: OPTIONS (CSeq 1)
[FluxCast WFD RTSP] <- response: RTSP/1.0 200 OK
[FluxCast WFD RTSP]   CSeq: 1
[FluxCast WFD RTSP] <- response for M1_OPTIONS: 200 OK
[FluxCast WFD RTSP] -> M3_GET_PARAMETER: GET_PARAMETER (CSeq 2)
[FluxCast WFD RTSP]   wfd_video_formats
[FluxCast WFD RTSP]   wfd_audio_codecs
[FluxCast WFD RTSP]   wfd_client_rtp_ports
[FluxCast WFD RTSP] <- request: OPTIONS * RTSP/1.0
[FluxCast WFD RTSP]   CSeq: 1
[FluxCast WFD RTSP] -> response 200 OK for OPTIONS
[FluxCast WFD RTSP] <- response: RTSP/1.0 200 OK
[FluxCast WFD RTSP]   CSeq: 2
[FluxCast WFD RTSP]   Content-Type: text/parameters
[FluxCast WFD RTSP]   Content-Length: 199
[FluxCast WFD RTSP]   wfd_audio_codecs: LPCM 00000003 00, AAC 00000001 00
[FluxCast WFD RTSP]   wfd_video_formats: 40 00 01 10 000001e3 0f3fffff 00000fff 00 0000 00c8 01 none none
[FluxCast WFD RTSP]   wfd_client_rtp_ports: RTP/AVP/UDP;unicast 19002 0 mode=play
[FluxCast WFD RTSP] <- response for M3_GET_PARAMETER: 200 OK
[FluxCast WFD RTSP] Samsung RTP port: 19002; source port: 19004; audio=LPCM 00000003 00, AAC 00000001 00
[FluxCast WFD RTSP] Negotiated media mode: 1280x720p30
[FluxCast WFD RTSP] Selected video format: 28 00 01 01 00000020 00000000 00000000 00 0000 0000 00 none none
[FluxCast WFD RTSP] -> M4_SET_PARAMETER: SET_PARAMETER (CSeq 3)
[FluxCast WFD RTSP]   wfd_video_formats: 28 00 01 01 00000020 00000000 00000000 00 0000 0000 00 none none
[FluxCast WFD RTSP]   wfd_audio_codecs: AAC 00000001 00
[FluxCast WFD RTSP]   wfd_presentation_URL: rtsp://10.42.0.1:7236/wfd1.0/streamid=0 none
[FluxCast WFD RTSP]   wfd_client_rtp_ports: RTP/AVP/UDP;unicast 19002 0 mode=play
[FluxCast WFD RTSP] <- response: RTSP/1.0 200 OK
[FluxCast WFD RTSP]   CSeq: 3
[FluxCast WFD RTSP] <- response for M4_SET_PARAMETER: 200 OK
[FluxCast WFD RTSP] -> M5_TRIGGER_SETUP: SET_PARAMETER (CSeq 4)
[FluxCast WFD RTSP]   wfd_trigger_method: SETUP
[FluxCast WFD RTSP] <- response: RTSP/1.0 200 OK
[FluxCast WFD RTSP]   CSeq: 4
[FluxCast WFD RTSP] <- response for M5_TRIGGER_SETUP: 200 OK
[FluxCast WFD RTSP] <- request: SETUP rtsp://10.42.0.1:7236/wfd1.0/streamid=0 RTSP/1.0
[FluxCast WFD RTSP]   CSeq: 2
[FluxCast WFD RTSP]   Transport: RTP/AVP/UDP;unicast;client_port=19002-19003
[FluxCast WFD RTSP] -> response 200 OK for SETUP
[FluxCast WFD RTSP] SETUP complete; RTP sink port=19002
[FluxCast WFD RTSP] <- request: PLAY rtsp://10.42.0.1:7236/wfd1.0/streamid=0 RTSP/1.0
[FluxCast WFD RTSP]   CSeq: 3
[FluxCast WFD RTSP]   Session: 6818110
[FluxCast WFD RTSP] -> response 200 OK for PLAY
[FluxCast WFD RTSP] Starting media as 1280x720p30; RTP source port 19004
[FluxCast WFD Media] Raising bitrate for desktop clarity: 4M -> 5M
[FluxCast WFD Media] Capturing screen : HDMI-A-1 (1920x1080)
[FluxCast WFD Media] Capturing audio  : alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__Headphones__sink.monitor
[FluxCast WFD Media] Scaling output  : 1280x720
[FluxCast WFD Media] RTP target      : 10.42.0.17:19002 from local port 19004
selected region 2240,0 1920x1080
Setting codec option: pix_fmt=yuv420p
Framerate: 30
Using video filter: fps=30
Output #0, nut, to '/dev/stdout':
  Stream #0:0: Video: rawvideo (BGR[0] / 0x524742), bgr0(pc), 1920x1080 [SAR 1:1 DAR 16:9], q=2-31, 1492992 kb/s
[Source @ 0x7efc18005e40] Changing video frame properties on the fly is not supported by all filters.
[Source @ 0x7efc18005e40] filter context - w: 1920 h: 1080 fmt: 121 csp: gbr range: unknown alpha: unspecified, incoming frame - w: 1920 h: 1080 fmt: 121 csp: unknown range: unknown alpha: unspecified pts_time: 0
[in#0/nut @ 0x5559ac611140] Stream #0: not enough frames to estimate rate; consider increasing probesize
[aist#1:0/pcm_s16le @ 0x5559ac62c5c0] Guessed Channel Layout: stereo
[FluxCast WFD RTSP] PLAY accepted; media stream started.
[FluxCast WFD Media] Latency probe: first RTP bytes after PLAY in 701.0 ms
[FluxCast WFD Media] Latency probe: sender-path latency (RTSP connect -> first RTP) 3550.1 ms
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1129 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+4522 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+8125 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+11695 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+15373 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+18890 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+22224 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+25763 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+29207 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+31948 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+35827 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+39425 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+42853 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+46295 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+49754 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+53300 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+56719 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+60082 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+63174 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+66653 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+70628 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+73485 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+77286 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+80632 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+84366 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+87591 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+91008 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+94327 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+97909 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+101152 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+104876 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+108289 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+111724 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+115063 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+118599 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+122060 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+125337 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+128789 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+132364 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+135127 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+138783 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+142652 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+145945 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+149538 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+152967 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+156332 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+159653 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+163315 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+166759 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+169966 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+173558 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+176862 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+180270 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+183664 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+187280 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+190743 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+194115 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+197595 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+201045 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+204508 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+207954 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+211411 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+214883 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+218278 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+221851 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+225096 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+228499 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+231716 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+235464 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+238939 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+242425 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+245842 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+249298 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+252760 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+256183 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+259352 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+262762 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+266514 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+269978 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+273438 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+276805 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+280401 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+283473 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+286694 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+290593 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+294169 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+297621 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+300940 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+304321 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+307811 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+311271 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+314605 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+318152 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+321512 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+324961 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+328397 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+331930 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+335247 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+338796 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+342246 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+345481 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+349181 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+352418 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+355943 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+359424 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+362980 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+366334 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+369699 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+373102 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+376666 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+380052 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+383536 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+386936 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+390052 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+393839 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+397295 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+400790 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+404206 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+407613 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+410832 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+414565 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+418008 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+421464 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+424939 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+428171 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+431679 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+435210 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+438660 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+442082 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+445540 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+448769 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+452428 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+455879 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+459110 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+462039 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+465358 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+468915 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+472725 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+476246 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+479903 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+483233 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+486693 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+490152 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+493517 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+496881 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+500610 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+503920 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+507330 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+510825 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+514230 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+517622 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+520975 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+524597 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+527946 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+531446 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+534906 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+538223 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+541751 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+545171 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+548613 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+551434 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+555566 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+558994 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+562097 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+565844 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+569328 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+572756 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+576163 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+579518 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+583046 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+586484 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+589961 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+593360 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+596714 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+600461 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+603795 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+607312 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+610639 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+613614 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+616836 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+620113 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+623606 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+627039 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+630268 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+634144 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+637679 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+640954 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+644757 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+648324 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+650925 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+655065 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+658466 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+661662 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+664982 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+668448 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+671984 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+675572 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+679025 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+682708 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+685826 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+689383 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+692847 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+696405 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+699819 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+703260 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+706469 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+710188 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+713595 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+717062 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+720445 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+724020 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+727364 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+730532 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+734397 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+737649 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+740714 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+744323 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+747858 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+750767 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+754091 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+757419 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+760896 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+764448 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+768291 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+771994 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+775324 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+778730 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+782018 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+785475 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+788937 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+792519 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+795987 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+799441 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+803071 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+806345 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+809536 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+812938 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+816732 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+820125 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+823434 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+827011 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+829931 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+833360 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+837332 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+840746 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+844243 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+847755 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+851286 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+854534 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+857964 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+861308 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+864627 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+868197 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+871797 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+875183 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+878320 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+882201 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+885626 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+889048 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+892253 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+895495 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+899142 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+902814 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+906110 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+909753 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+913216 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+916593 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+920151 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+923497 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+926859 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+930421 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+933842 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+937273 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+940486 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+944162 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+947535 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+950990 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+954475 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+957982 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+961379 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+964509 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+967888 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+971644 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+975159 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+978571 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+982049 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+985531 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+988916 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+992383 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+995863 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+999274 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1002716 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1005395 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1009382 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1012308 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1015751 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1019788 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1023266 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1026733 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1030062 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1033512 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1037201 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1040594 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1043957 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1047482 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1050765 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1054245 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1057872 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1061270 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1064631 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1068122 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1071098 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1074126 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1077556 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1081022 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1084608 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1088668 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1092097 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1095317 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1098913 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1102360 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1105662 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1109266 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1112666 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1116143 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1119555 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1123101 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1126508 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1129816 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1133335 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1136832 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1140285 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1143668 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1147067 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1150579 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1154084 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1156717 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1160140 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1163994 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1167659 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1171160 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1174603 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1178011 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1181436 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1184910 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1188293 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1191536 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1195388 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1198809 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1202103 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1205556 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1209012 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1212478 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1215918 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1218911 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1222361 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1226397 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1229079 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1232650 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1236635 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1239183 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1243227 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1246646 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1250060 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1253238 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1257007 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1260555 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1263799 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1267353 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1270747 KiB on p2p-wlan0-0
[FluxCast WFD Media] Sender health: pid=161256:running, pid=161257:running; tx+1273594 KiB on p2p-wlan0-0
^C
[FluxCast WFD] Stopping WFD session...
[FluxCast WFD] NetworkManager P2P connection deactivated.
[FluxCast WFD] NetworkManager P2P device disconnected.

❯ tail -f /tmp/fluxcast-wfd-latency.jsonl
{"ts": "2026-05-05T14:49:43.436+00:00", "mono": 8414.572729, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+173558 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:49:48.437+00:00", "mono": 8419.574075, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+176862 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:49:53.438+00:00", "mono": 8424.575358, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+180270 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:49:58.440+00:00", "mono": 8429.576759, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+183664 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:50:03.440+00:00", "mono": 8434.577402, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+187280 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:50:08.441+00:00", "mono": 8439.578226, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+190743 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:50:13.442+00:00", "mono": 8444.579287, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+194115 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:50:18.443+00:00", "mono": 8449.579897, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+197595 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:50:23.446+00:00", "mono": 8454.582922, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+201045 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:50:28.447+00:00", "mono": 8459.584426, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+204508 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:50:33.448+00:00", "mono": 8464.585251, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+207954 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:50:38.449+00:00", "mono": 8469.586069, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+211411 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:50:43.450+00:00", "mono": 8474.587083, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+214883 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:50:48.451+00:00", "mono": 8479.588306, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+218278 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:50:53.452+00:00", "mono": 8484.589365, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+221851 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:50:58.453+00:00", "mono": 8489.590336, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+225096 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:51:03.455+00:00", "mono": 8494.592036, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+228499 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:51:08.456+00:00", "mono": 8499.592869, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+231716 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:51:13.457+00:00", "mono": 8504.593742, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+235464 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:51:18.457+00:00", "mono": 8509.594603, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+238939 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:51:23.458+00:00", "mono": 8514.595514, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+242425 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:51:28.459+00:00", "mono": 8519.596442, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+245842 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:51:33.460+00:00", "mono": 8524.597568, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+249298 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:51:38.461+00:00", "mono": 8529.598399, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+252760 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:51:43.462+00:00", "mono": 8534.599489, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+256183 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:51:48.463+00:00", "mono": 8539.600414, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+259352 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:51:53.465+00:00", "mono": 8544.601899, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+262762 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:51:58.466+00:00", "mono": 8549.602969, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+266514 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:52:03.467+00:00", "mono": 8554.604621, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+269978 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:52:08.469+00:00", "mono": 8559.605952, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+273438 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:52:13.470+00:00", "mono": 8564.607403, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+276805 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:52:18.471+00:00", "mono": 8569.608626, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+280401 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:52:23.472+00:00", "mono": 8574.609447, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+283473 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:52:28.473+00:00", "mono": 8579.610326, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+286694 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:52:33.474+00:00", "mono": 8584.611372, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+290593 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:52:38.476+00:00", "mono": 8589.613091, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+294169 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:52:43.477+00:00", "mono": 8594.614114, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+297621 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:52:48.478+00:00", "mono": 8599.614965, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+300940 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:52:53.479+00:00", "mono": 8604.616075, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+304321 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:52:58.480+00:00", "mono": 8609.617097, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+307811 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:53:03.481+00:00", "mono": 8614.61793, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+311271 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:53:08.482+00:00", "mono": 8619.618789, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+314605 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:53:13.483+00:00", "mono": 8624.620119, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+318152 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:53:18.484+00:00", "mono": 8629.621316, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+321512 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:53:23.485+00:00", "mono": 8634.622099, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+324961 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:53:28.487+00:00", "mono": 8639.624062, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+328397 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:53:33.488+00:00", "mono": 8644.625451, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+331930 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:53:38.490+00:00", "mono": 8649.627041, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+335247 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:53:43.491+00:00", "mono": 8654.628316, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+338796 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:53:48.492+00:00", "mono": 8659.629228, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+342246 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:53:53.494+00:00", "mono": 8664.630707, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+345481 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:53:58.495+00:00", "mono": 8669.631809, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+349181 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:54:03.496+00:00", "mono": 8674.632716, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+352418 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:54:08.496+00:00", "mono": 8679.633617, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+355943 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:54:13.497+00:00", "mono": 8684.634338, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+359424 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:54:18.498+00:00", "mono": 8689.635313, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+362980 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:54:23.499+00:00", "mono": 8694.636467, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+366334 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:54:28.500+00:00", "mono": 8699.637422, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+369699 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:54:33.502+00:00", "mono": 8704.639273, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+373102 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:54:38.503+00:00", "mono": 8709.640365, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+376666 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:54:43.504+00:00", "mono": 8714.641399, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+380052 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:54:48.505+00:00", "mono": 8719.642489, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+383536 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:54:53.506+00:00", "mono": 8724.643551, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+386936 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:54:58.507+00:00", "mono": 8729.644665, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+390052 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:55:03.508+00:00", "mono": 8734.645506, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+393839 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:55:08.509+00:00", "mono": 8739.646569, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+397295 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:55:13.510+00:00", "mono": 8744.647381, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+400790 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:55:18.511+00:00", "mono": 8749.648135, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+404206 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:55:23.512+00:00", "mono": 8754.649147, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+407613 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:55:28.514+00:00", "mono": 8759.650833, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+410832 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:55:33.515+00:00", "mono": 8764.652142, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+414565 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:55:38.516+00:00", "mono": 8769.653173, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+418008 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:55:43.518+00:00", "mono": 8774.654735, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+421464 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:55:48.519+00:00", "mono": 8779.656171, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+424939 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:55:53.520+00:00", "mono": 8784.657207, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+428171 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:55:58.522+00:00", "mono": 8789.658858, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+431679 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:56:03.523+00:00", "mono": 8794.660362, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+435210 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:56:08.525+00:00", "mono": 8799.662058, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+438660 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:56:13.526+00:00", "mono": 8804.663516, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+442082 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:56:18.528+00:00", "mono": 8809.665439, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+445540 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:56:23.529+00:00", "mono": 8814.666655, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+448769 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:56:28.532+00:00", "mono": 8819.669605, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+452428 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:56:33.533+00:00", "mono": 8824.670536, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+455879 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:56:38.534+00:00", "mono": 8829.671415, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+459110 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:56:43.536+00:00", "mono": 8834.672768, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+462039 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:56:48.537+00:00", "mono": 8839.673911, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+465358 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:56:53.538+00:00", "mono": 8844.675489, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+468915 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:56:58.539+00:00", "mono": 8849.676609, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+472725 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:57:03.540+00:00", "mono": 8854.677572, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+476246 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:57:08.541+00:00", "mono": 8859.678419, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+479903 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:57:13.542+00:00", "mono": 8864.679197, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+483233 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:57:18.543+00:00", "mono": 8869.680168, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+486693 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:57:23.545+00:00", "mono": 8874.681856, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+490152 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:57:28.546+00:00", "mono": 8879.68332, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+493517 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:57:33.547+00:00", "mono": 8884.684215, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+496881 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:57:38.548+00:00", "mono": 8889.684895, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+500610 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:57:43.549+00:00", "mono": 8894.685731, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+503920 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:57:48.549+00:00", "mono": 8899.686613, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+507330 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:57:53.550+00:00", "mono": 8904.687389, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+510825 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:57:58.551+00:00", "mono": 8909.688296, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+514230 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:58:03.552+00:00", "mono": 8914.689101, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+517622 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:58:08.553+00:00", "mono": 8919.689846, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+520975 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:58:13.553+00:00", "mono": 8924.690555, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+524597 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:58:18.554+00:00", "mono": 8929.691411, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+527946 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:58:23.555+00:00", "mono": 8934.692249, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+531446 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:58:28.556+00:00", "mono": 8939.693142, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+534906 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:58:33.557+00:00", "mono": 8944.693904, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+538223 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:58:38.558+00:00", "mono": 8949.694843, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+541751 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:58:43.559+00:00", "mono": 8954.695825, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+545171 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:58:48.560+00:00", "mono": 8959.697136, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+548613 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:58:53.561+00:00", "mono": 8964.698531, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+551434 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:58:58.563+00:00", "mono": 8969.699724, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+555566 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:59:03.564+00:00", "mono": 8974.700866, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+558994 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:59:08.565+00:00", "mono": 8979.701947, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+562097 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:59:13.567+00:00", "mono": 8984.703759, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+565844 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:59:18.568+00:00", "mono": 8989.704913, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+569328 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:59:23.569+00:00", "mono": 8994.706169, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+572756 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:59:28.570+00:00", "mono": 8999.706974, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+576163 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:59:33.571+00:00", "mono": 9004.707871, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+579518 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:59:38.572+00:00", "mono": 9009.708938, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+583046 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:59:43.573+00:00", "mono": 9014.710259, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+586484 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:59:48.575+00:00", "mono": 9019.711873, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+589961 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:59:53.575+00:00", "mono": 9024.712591, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+593360 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T14:59:58.576+00:00", "mono": 9029.713617, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+596714 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:00:03.577+00:00", "mono": 9034.714501, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+600461 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:00:08.578+00:00", "mono": 9039.715429, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+603795 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:00:13.580+00:00", "mono": 9044.71681, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+607312 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:00:18.581+00:00", "mono": 9049.718038, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+610639 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:00:23.582+00:00", "mono": 9054.719128, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+613614 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:00:28.583+00:00", "mono": 9059.720249, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+616836 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:00:33.584+00:00", "mono": 9064.721107, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+620113 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:00:38.585+00:00", "mono": 9069.721921, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+623606 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:00:43.586+00:00", "mono": 9074.722729, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+627039 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:00:48.586+00:00", "mono": 9079.723505, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+630268 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:00:53.587+00:00", "mono": 9084.724426, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+634144 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:00:58.588+00:00", "mono": 9089.725221, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+637679 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:01:03.590+00:00", "mono": 9094.726848, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+640954 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:01:08.591+00:00", "mono": 9099.727978, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+644757 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:01:13.592+00:00", "mono": 9104.728831, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+648324 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:01:18.592+00:00", "mono": 9109.729653, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+650925 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:01:23.593+00:00", "mono": 9114.730424, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+655065 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:01:28.594+00:00", "mono": 9119.731277, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+658466 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:01:33.595+00:00", "mono": 9124.732209, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+661662 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:01:38.596+00:00", "mono": 9129.733154, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+664982 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:01:43.597+00:00", "mono": 9134.734241, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+668448 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:01:48.598+00:00", "mono": 9139.73523, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+671984 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:01:53.599+00:00", "mono": 9144.736308, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+675572 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:01:58.600+00:00", "mono": 9149.737285, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+679025 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:02:03.601+00:00", "mono": 9154.738207, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+682708 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:02:08.602+00:00", "mono": 9159.739152, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+685826 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:02:13.603+00:00", "mono": 9164.74022, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+689383 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:02:18.604+00:00", "mono": 9169.741502, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+692847 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:02:23.605+00:00", "mono": 9174.742508, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+696405 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:02:28.607+00:00", "mono": 9179.743847, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+699819 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:02:33.608+00:00", "mono": 9184.744881, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+703260 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:02:38.609+00:00", "mono": 9189.745771, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+706469 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:02:43.610+00:00", "mono": 9194.746954, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+710188 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:02:48.611+00:00", "mono": 9199.747896, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+713595 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:02:53.612+00:00", "mono": 9204.748989, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+717062 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:02:58.613+00:00", "mono": 9209.750143, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+720445 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:03:03.614+00:00", "mono": 9214.751209, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+724020 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:03:08.615+00:00", "mono": 9219.752426, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+727364 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:03:13.616+00:00", "mono": 9224.753559, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+730532 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:03:18.618+00:00", "mono": 9229.754662, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+734397 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:03:23.619+00:00", "mono": 9234.756234, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+737649 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:03:28.620+00:00", "mono": 9239.757542, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+740714 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:03:33.622+00:00", "mono": 9244.759342, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+744323 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:03:38.624+00:00", "mono": 9249.760744, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+747858 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:03:43.625+00:00", "mono": 9254.762459, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+750767 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:03:48.627+00:00", "mono": 9259.763826, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+754091 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:03:53.628+00:00", "mono": 9264.765115, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+757419 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:03:58.630+00:00", "mono": 9269.766805, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+760896 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:04:03.631+00:00", "mono": 9274.767804, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+764448 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:04:08.632+00:00", "mono": 9279.768764, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+768291 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:04:13.633+00:00", "mono": 9284.769966, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+771994 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:04:18.634+00:00", "mono": 9289.771672, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+775324 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:04:23.636+00:00", "mono": 9294.772818, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+778730 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:04:28.637+00:00", "mono": 9299.773714, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+782018 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:04:33.639+00:00", "mono": 9304.775742, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+785475 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:04:38.640+00:00", "mono": 9309.777227, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+788937 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:04:43.641+00:00", "mono": 9314.778155, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+792519 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:04:48.642+00:00", "mono": 9319.77906, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+795987 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:04:53.643+00:00", "mono": 9324.780185, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+799441 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:04:58.645+00:00", "mono": 9329.781755, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+803071 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:05:03.646+00:00", "mono": 9334.782841, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+806345 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:05:08.647+00:00", "mono": 9339.78374, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+809536 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:05:13.648+00:00", "mono": 9344.785047, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+812938 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:05:18.649+00:00", "mono": 9349.785993, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+816732 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:05:23.650+00:00", "mono": 9354.786903, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+820125 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:05:28.651+00:00", "mono": 9359.787799, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+823434 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:05:33.652+00:00", "mono": 9364.788832, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+827011 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:05:38.653+00:00", "mono": 9369.789685, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+829931 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:05:43.653+00:00", "mono": 9374.790548, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+833360 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:05:48.654+00:00", "mono": 9379.791522, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+837332 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:05:53.655+00:00", "mono": 9384.792406, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+840746 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:05:58.656+00:00", "mono": 9389.793303, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+844243 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:06:03.657+00:00", "mono": 9394.79458, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+847755 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:06:08.659+00:00", "mono": 9399.795759, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+851286 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:06:13.660+00:00", "mono": 9404.796664, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+854534 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:06:18.660+00:00", "mono": 9409.797466, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+857964 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:06:23.662+00:00", "mono": 9414.798907, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+861308 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:06:28.663+00:00", "mono": 9419.800128, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+864627 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:06:33.664+00:00", "mono": 9424.80099, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+868197 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:06:38.665+00:00", "mono": 9429.802638, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+871797 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:06:43.667+00:00", "mono": 9434.803767, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+875183 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:06:48.668+00:00", "mono": 9439.805556, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+878320 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:06:53.670+00:00", "mono": 9444.807512, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+882201 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:06:58.671+00:00", "mono": 9449.808437, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+885626 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:07:03.672+00:00", "mono": 9454.809634, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+889048 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:07:08.673+00:00", "mono": 9459.810571, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+892253 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:07:13.674+00:00", "mono": 9464.811418, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+895495 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:07:18.675+00:00", "mono": 9469.812598, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+899142 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:07:23.677+00:00", "mono": 9474.813847, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+902814 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:07:28.678+00:00", "mono": 9479.814902, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+906110 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:07:33.679+00:00", "mono": 9484.815764, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+909753 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:07:38.679+00:00", "mono": 9489.816615, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+913216 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:07:43.680+00:00", "mono": 9494.817272, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+916593 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:07:48.681+00:00", "mono": 9499.818618, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+920151 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:07:53.683+00:00", "mono": 9504.820027, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+923497 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:07:58.684+00:00", "mono": 9509.82086, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+926859 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:08:03.685+00:00", "mono": 9514.822169, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+930421 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:08:08.686+00:00", "mono": 9519.823107, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+933842 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:08:13.687+00:00", "mono": 9524.823852, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+937273 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:08:18.687+00:00", "mono": 9529.824614, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+940486 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:08:23.688+00:00", "mono": 9534.825491, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+944162 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:08:28.690+00:00", "mono": 9539.827182, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+947535 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:08:33.691+00:00", "mono": 9544.828504, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+950990 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:08:38.692+00:00", "mono": 9549.829511, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+954475 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:08:43.693+00:00", "mono": 9554.830312, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+957982 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:08:48.694+00:00", "mono": 9559.831226, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+961379 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:08:53.695+00:00", "mono": 9564.832549, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+964509 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:08:58.696+00:00", "mono": 9569.833522, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+967888 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:09:03.697+00:00", "mono": 9574.834512, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+971644 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:09:08.698+00:00", "mono": 9579.835283, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+975159 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:09:13.699+00:00", "mono": 9584.836367, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+978571 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:09:18.700+00:00", "mono": 9589.837629, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+982049 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:09:23.701+00:00", "mono": 9594.838539, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+985531 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:09:28.702+00:00", "mono": 9599.839344, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+988916 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:09:33.703+00:00", "mono": 9604.840475, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+992383 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:09:38.704+00:00", "mono": 9609.841555, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+995863 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:09:43.705+00:00", "mono": 9614.842575, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+999274 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:09:48.707+00:00", "mono": 9619.843703, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1002716 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:09:53.709+00:00", "mono": 9624.845863, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1005395 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:09:58.710+00:00", "mono": 9629.846796, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1009382 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:10:03.710+00:00", "mono": 9634.847475, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1012308 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:10:08.711+00:00", "mono": 9639.848425, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1015751 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:10:13.712+00:00", "mono": 9644.84935, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1019788 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:10:18.713+00:00", "mono": 9649.850604, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1023266 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:10:23.715+00:00", "mono": 9654.851661, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1026733 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:10:28.716+00:00", "mono": 9659.852873, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1030062 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:10:33.717+00:00", "mono": 9664.85443, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1033512 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:10:38.718+00:00", "mono": 9669.855558, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1037201 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:10:43.719+00:00", "mono": 9674.856499, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1040594 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:10:48.720+00:00", "mono": 9679.857623, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1043957 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:10:53.722+00:00", "mono": 9684.858766, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1047482 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:10:58.723+00:00", "mono": 9689.8599, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1050765 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:11:03.724+00:00", "mono": 9694.861586, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1054245 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:11:08.726+00:00", "mono": 9699.862833, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1057872 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:11:13.726+00:00", "mono": 9704.86365, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1061270 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:11:18.727+00:00", "mono": 9709.864692, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1064631 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:11:23.731+00:00", "mono": 9714.868084, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1068122 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:11:28.732+00:00", "mono": 9719.8697, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1071098 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:11:33.734+00:00", "mono": 9724.871089, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1074126 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:11:38.735+00:00", "mono": 9729.872136, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1077556 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:11:43.736+00:00", "mono": 9734.873053, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1081022 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:11:48.737+00:00", "mono": 9739.873948, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1084608 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:11:53.738+00:00", "mono": 9744.874844, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1088668 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:11:58.739+00:00", "mono": 9749.875783, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1092097 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:12:03.740+00:00", "mono": 9754.876696, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1095317 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:12:08.741+00:00", "mono": 9759.8778, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1098913 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:12:13.742+00:00", "mono": 9764.878692, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1102360 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:12:18.742+00:00", "mono": 9769.879661, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1105662 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:12:23.743+00:00", "mono": 9774.880549, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1109266 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:12:28.744+00:00", "mono": 9779.881456, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1112666 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:12:33.745+00:00", "mono": 9784.882641, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1116143 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:12:38.746+00:00", "mono": 9789.883447, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1119555 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:12:43.747+00:00", "mono": 9794.884374, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1123101 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:12:48.748+00:00", "mono": 9799.885342, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1126508 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:12:53.749+00:00", "mono": 9804.886273, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1129816 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:12:58.750+00:00", "mono": 9809.887188, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1133335 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:13:03.751+00:00", "mono": 9814.887943, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1136832 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:13:08.752+00:00", "mono": 9819.88868, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1140285 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:13:13.752+00:00", "mono": 9824.889472, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1143668 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:13:18.754+00:00", "mono": 9829.890771, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1147067 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:13:23.755+00:00", "mono": 9834.892382, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1150579 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:13:28.756+00:00", "mono": 9839.892955, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1154084 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:13:33.757+00:00", "mono": 9844.893926, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1156717 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:13:38.758+00:00", "mono": 9849.895197, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1160140 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:13:43.759+00:00", "mono": 9854.89646, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1163994 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:13:48.760+00:00", "mono": 9859.897278, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1167659 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:13:53.761+00:00", "mono": 9864.898086, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1171160 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:13:58.763+00:00", "mono": 9869.900265, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1174603 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:14:03.764+00:00", "mono": 9874.901284, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1178011 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:14:08.765+00:00", "mono": 9879.902093, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1181436 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:14:13.767+00:00", "mono": 9884.903703, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1184910 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:14:18.768+00:00", "mono": 9889.905148, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1188293 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:14:23.769+00:00", "mono": 9894.90649, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1191536 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:14:28.770+00:00", "mono": 9899.907496, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1195388 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:14:33.774+00:00", "mono": 9904.910766, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1198809 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:14:38.775+00:00", "mono": 9909.912228, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1202103 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:14:43.776+00:00", "mono": 9914.913364, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1205556 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:14:48.778+00:00", "mono": 9919.914835, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1209012 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:14:53.779+00:00", "mono": 9924.916102, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1212478 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:14:58.780+00:00", "mono": 9929.917456, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1215918 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:15:03.781+00:00", "mono": 9934.918592, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1218911 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:15:08.782+00:00", "mono": 9939.919344, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1222361 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:15:13.783+00:00", "mono": 9944.92063, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1226397 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:15:18.784+00:00", "mono": 9949.921594, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1229079 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:15:23.785+00:00", "mono": 9954.922533, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1232650 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:15:28.786+00:00", "mono": 9959.923449, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1236635 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:15:33.787+00:00", "mono": 9964.924348, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1239183 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:15:38.788+00:00", "mono": 9969.925286, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1243227 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:15:43.789+00:00", "mono": 9974.926171, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1246646 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:15:48.790+00:00", "mono": 9979.927051, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1250060 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:15:53.791+00:00", "mono": 9984.928573, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1253238 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:15:58.793+00:00", "mono": 9989.929807, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1257007 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:16:03.794+00:00", "mono": 9994.930968, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1260555 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:16:08.795+00:00", "mono": 9999.932096, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1263799 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:16:13.796+00:00", "mono": 10004.932788, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1267353 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:16:18.796+00:00", "mono": 10009.933535, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1270747 KiB on p2p-wlan0-0"}
{"ts": "2026-05-05T15:16:23.797+00:00", "mono": 10014.934522, "event": "sender_health", "processes": ["pid=161256:running", "pid=161257:running"], "tx_summary": "tx+1273594 KiB on p2p-wlan0-0"}

## Тест 4
❯ python3 main.py --protocol wfd --wfd-test-pattern --output-res 1280x720 --bitrate 3M --wfd-media-pipeline gst --wfd-latency-log
[FluxCast Doctor] System capability report
[FluxCast Doctor] Miracast/WFD looks possible via NetworkManager; raw supplicant access is optional for this backend.

  Status Check                  Details
  ------ ---------------------- ------------------------------------------
  ok     python                 runtime (3.14.4 on Linux 7.0.3-arch1-1)
  ok     ffmpeg                 video/audio transcoding (/usr/sbin/ffmpeg)
  ok     wf-recorder            Wayland/wlroots screen capture (/usr/sbin/wf-recorder)
  ok     pactl                  PulseAudio/PipeWire-Pulse audio monitor detection (/usr/sbin/pactl)
  ok     xrandr                 X11 monitor detection fallback (/usr/sbin/xrandr)
  ok     nmcli                  NetworkManager Wi-Fi Direct control (/usr/sbin/nmcli)
  ok     iw                     kernel Wi-Fi interface inspection (/usr/sbin/iw)
  ok     wpa_cli                active Wi-Fi Direct scan/control (/usr/sbin/wpa_cli)
  ok     gdbus                  passive wpa_supplicant D-Bus capability checks (/usr/sbin/gdbus)
  ok     gst-launch-1.0         optional future WFD GStreamer pipeline (/usr/sbin/gst-launch-1.0)
  ok     gst-inspect-1.0        optional future WFD codec inspection (/usr/sbin/gst-inspect-1.0)
  ok     ffmpeg encoders        H.264 and AAC encoders are available (h264=libx264, h264_vaapi, h264_nvenc, h264_qsv, h264_v4l2m2m; aac=yes)
  ok     screen capture         Wayland capture path is available (WAYLAND_DISPLAY=wayland-1; wf-recorder=/usr/sbin/wf-recorder)
  ok     audio capture          default audio monitor can be derived (alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__Headphones__sink.monitor)
  ok     NetworkManager         Wi-Fi and P2P devices are visible (nmcli tool, version 1.56.0-1; wlan0:wifi:connected | lo:loopback:connected (externally) | virbr0:bridge:connected (externally) | p2p-dev-wlan0:wifi-p2p:disconnected | enp0s31f6:ethernet:unavailable)
  ok     iw P2P                 kernel exposes a P2P-device interface (phy#1 | 	Unnamed/non-netdev interface | 		wdev 0x100000002 | 		addr 2c:33:58:88:dc:45 | 		type P2P-device | 	Interface wlan0 | 		ifindex 12 | 		wdev 0x100000001 | 		addr 2c:33:58:88:dc:45 | 		ssid PODA_80295G | 		type managed | 		channel 36 (5180 MHz), width: 80 MHz, center1: 5210 MHz | 		txpower 22.00 dBm | 		multicast TXQ: | 			qsz-byt	qsz-pkt	flows	drops	marks	overlmt	hashcol	tx-bytes	tx-packets | 			0	0	0	0	0	0	0	0		0)
  warn   wpa_supplicant P2P     supplicant capability query failed (Error: GDBus.Error:org.freedesktop.DBus.Error.AccessDenied: Sender is not authorized to send message)
  warn   wpa_supplicant WFD     WFDIE query failed; supplicant may lack CONFIG_WIFI_DISPLAY (Error: GDBus.Error:org.freedesktop.DBus.Error.AccessDenied: Sender is not authorized to send message)

[FluxCast WFD] Starting NetworkManager Wi-Fi Direct scan on p2p-dev-wlan0 for 8s...
[FluxCast WFD] Wi-Fi Direct peer(s):
  [0] 82:47:86:69:2C:87  [TV] Samsung 7 Series (55) via NetworkManager
      WFD capability data detected
Select WFD peer [0]: 0
[FluxCast WFD] Test pattern smoke mode includes AAC audio.
[FluxCast WFD] Latency log file: /tmp/fluxcast-wfd-latency.jsonl
[FluxCast WFD RTSP] Server listening on 0.0.0.0:7236
[FluxCast WFD] Connecting to [TV] Samsung 7 Series (55) via NetworkManager...
[FluxCast WFD] NetworkManager activation started: (objectpath '/org/freedesktop/NetworkManager/Settings/16', objectpath '/org/freedesktop/NetworkManager/ActiveConnection/13', @a{sv} {})
[FluxCast WFD] Waiting for NetworkManager P2P activation...
[FluxCast WFD] NM active connection: activating; p2p-dev-wlan0:config:0
[FluxCast WFD] NM active connection: activating; p2p-dev-wlan0:ip-config:0
[FluxCast WFD] NM active connection: activated; p2p-dev-wlan0/p2p-wlan0-1:activated:0
[FluxCast WFD] P2P link is activated; waiting for Samsung RTSP...
[FluxCast WFD] Waiting for Samsung RTSP/WFD session. Press Ctrl+C to stop.
[FluxCast WFD RTSP] TV connected from 10.42.0.17:60297; local=10.42.0.1
[FluxCast WFD RTSP] -> M1_OPTIONS: OPTIONS (CSeq 1)
[FluxCast WFD RTSP] <- response: RTSP/1.0 200 OK
[FluxCast WFD RTSP]   CSeq: 1
[FluxCast WFD RTSP] <- response for M1_OPTIONS: 200 OK
[FluxCast WFD RTSP] -> M3_GET_PARAMETER: GET_PARAMETER (CSeq 2)
[FluxCast WFD RTSP]   wfd_video_formats
[FluxCast WFD RTSP]   wfd_audio_codecs
[FluxCast WFD RTSP]   wfd_client_rtp_ports
[FluxCast WFD RTSP] <- request: OPTIONS * RTSP/1.0
[FluxCast WFD RTSP]   CSeq: 1
[FluxCast WFD RTSP] -> response 200 OK for OPTIONS
[FluxCast WFD RTSP] <- response: RTSP/1.0 200 OK
[FluxCast WFD RTSP]   CSeq: 2
[FluxCast WFD RTSP]   Content-Type: text/parameters
[FluxCast WFD RTSP]   Content-Length: 199
[FluxCast WFD RTSP]   wfd_audio_codecs: LPCM 00000003 00, AAC 00000001 00
[FluxCast WFD RTSP]   wfd_video_formats: 40 00 01 10 000001e3 0f3fffff 00000fff 00 0000 00c8 01 none none
[FluxCast WFD RTSP]   wfd_client_rtp_ports: RTP/AVP/UDP;unicast 19000 0 mode=play
[FluxCast WFD RTSP] <- response for M3_GET_PARAMETER: 200 OK
[FluxCast WFD RTSP] Samsung RTP port: 19000; source port: 19002; audio=LPCM 00000003 00, AAC 00000001 00
[FluxCast WFD RTSP] Negotiated media mode: 1280x720p30
[FluxCast WFD RTSP] Selected video format: 28 00 01 01 00000020 00000000 00000000 00 0000 0000 00 none none
[FluxCast WFD RTSP] -> M4_SET_PARAMETER: SET_PARAMETER (CSeq 3)
[FluxCast WFD RTSP]   wfd_video_formats: 28 00 01 01 00000020 00000000 00000000 00 0000 0000 00 none none
[FluxCast WFD RTSP]   wfd_audio_codecs: AAC 00000001 00
[FluxCast WFD RTSP]   wfd_presentation_URL: rtsp://10.42.0.1:7236/wfd1.0/streamid=0 none
[FluxCast WFD RTSP]   wfd_client_rtp_ports: RTP/AVP/UDP;unicast 19000 0 mode=play
[FluxCast WFD RTSP] <- response: RTSP/1.0 200 OK
[FluxCast WFD RTSP]   CSeq: 3
[FluxCast WFD RTSP] <- response for M4_SET_PARAMETER: 200 OK
[FluxCast WFD RTSP] -> M5_TRIGGER_SETUP: SET_PARAMETER (CSeq 4)
[FluxCast WFD RTSP]   wfd_trigger_method: SETUP
[FluxCast WFD RTSP] <- response: RTSP/1.0 200 OK
[FluxCast WFD RTSP]   CSeq: 4
[FluxCast WFD RTSP] <- response for M5_TRIGGER_SETUP: 200 OK
[FluxCast WFD RTSP] <- request: SETUP rtsp://10.42.0.1:7236/wfd1.0/streamid=0 RTSP/1.0
[FluxCast WFD RTSP]   CSeq: 2
[FluxCast WFD RTSP]   Transport: RTP/AVP/UDP;unicast;client_port=19000-19001
[FluxCast WFD RTSP] -> response 200 OK for SETUP
[FluxCast WFD RTSP] SETUP complete; RTP sink port=19000
[FluxCast WFD RTSP] <- request: PLAY rtsp://10.42.0.1:7236/wfd1.0/streamid=0 RTSP/1.0
[FluxCast WFD RTSP]   CSeq: 3
[FluxCast WFD RTSP]   Session: 5883242
[FluxCast WFD RTSP] -> response 200 OK for PLAY
[FluxCast WFD RTSP] Starting media as 1280x720p30; RTP source port 19002
[FluxCast WFD Media] Starting GStreamer test RTP stream to 10.42.0.17:19000 from 10.42.0.1:19002
[FluxCast WFD Media] GST cmd: gst-launch-1.0 -e -q mpegtsmux name=mux alignment=7 prog-map=program_map,sink_4113=1,sink_4352=1 pat-interval=9000 pmt-interval=9000 pcr-interval=3600 ! rtpmp2tpay pt=33 mtu=1328 ! udpsink host=10.42.0.17 port=19000 bind-address=10.42.0.1 bind-port=19002 sync=false async=false videotestsrc is-live=true pattern=smpte ! video/x-raw,width=1280,height=720,framerate=30/1 ! videoconvert ! x264enc tune=zerolatency speed-preset=ultrafast bitrate=3000 key-int-max=30 bframes=0 byte-stream=true aud=true sliced-threads=true vbv-buf-capacity=200 ! video/x-h264,stream-format=byte-stream,alignment=au,profile=baseline ! queue ! mux.sink_4113 audiotestsrc is-live=true wave=sine freq=880 ! audioconvert ! audioresample ! audio/x-raw,format=S16LE,rate=48000,channels=2,layout=interleaved ! fdkaacenc bitrate=128000 ! aacparse ! queue ! mux.sink_4352
[FluxCast WFD RTSP] PLAY accepted; media stream started.
[FluxCast WFD Media] Latency probe: first RTP bytes after PLAY in 701.8 ms
[FluxCast WFD Media] Latency probe: sender-path latency (RTSP connect -> first RTP) 2915.0 ms
[FluxCast WFD Media] Sender health: pid=167178:running; tx+645 KiB on p2p-wlan0-1
[FluxCast WFD Media] Sender health: pid=167178:running; tx+2729 KiB on p2p-wlan0-1
[FluxCast WFD Media] Sender health: pid=167178:running; tx+4848 KiB on p2p-wlan0-1
[FluxCast WFD Media] Sender health: pid=167178:running; tx+6923 KiB on p2p-wlan0-1
[FluxCast WFD Media] Sender health: pid=167178:running; tx+9030 KiB on p2p-wlan0-1
[FluxCast WFD Media] Sender health: pid=167178:running; tx+11127 KiB on p2p-wlan0-1
[FluxCast WFD Media] Sender health: pid=167178:running; tx+13196 KiB on p2p-wlan0-1
^C00:32.6 / 99:99:99.
[FluxCast WFD] Stopping WFD session...
[FluxCast WFD] NetworkManager P2P connection deactivated.
[FluxCast WFD] NetworkManager disconnect warning: Error: GDBus.Error:org.freedesktop.NetworkManager.Device.NotActive: Device is not active
 ~/test_scripts/fluxcast  main !8 ?2  

❯ tail -f /tmp/fluxcast-wfd-latency.jsonl
{"ts": "2026-05-05T15:19:11.848+00:00", "mono": 10182.985474, "event": "media_starting", "mode": "1280x720p30", "tv_ip": "10.42.0.17", "sink_rtp_port": 19000, "source_rtp_port": 19002}
{"ts": "2026-05-05T15:19:12.797+00:00", "mono": 10183.934049, "event": "play_accepted", "setup_ms": 2213.2}
{"ts": "2026-05-05T15:19:13.499+00:00", "mono": 10184.635913, "event": "latency_probe", "sender_startup_ms": 701.8, "setup_ms": 2213.2, "sender_path_latency_ms": 2915.0}
{"ts": "2026-05-05T15:19:13.499+00:00", "mono": 10184.636516, "event": "sender_health", "processes": ["pid=167178:running"], "tx_summary": "tx+645 KiB on p2p-wlan0-1"}
{"ts": "2026-05-05T15:19:18.501+00:00", "mono": 10189.63823, "event": "sender_health", "processes": ["pid=167178:running"], "tx_summary": "tx+2729 KiB on p2p-wlan0-1"}
{"ts": "2026-05-05T15:19:23.503+00:00", "mono": 10194.639744, "event": "sender_health", "processes": ["pid=167178:running"], "tx_summary": "tx+4848 KiB on p2p-wlan0-1"}
{"ts": "2026-05-05T15:19:28.504+00:00", "mono": 10199.641344, "event": "sender_health", "processes": ["pid=167178:running"], "tx_summary": "tx+6923 KiB on p2p-wlan0-1"}
{"ts": "2026-05-05T15:19:33.506+00:00", "mono": 10204.643157, "event": "sender_health", "processes": ["pid=167178:running"], "tx_summary": "tx+9030 KiB on p2p-wlan0-1"}
{"ts": "2026-05-05T15:19:38.508+00:00", "mono": 10209.644995, "event": "sender_health", "processes": ["pid=167178:running"], "tx_summary": "tx+11127 KiB on p2p-wlan0-1"}
{"ts": "2026-05-05T15:19:43.510+00:00", "mono": 10214.64685, "event": "sender_health", "processes": ["pid=167178:running"], "tx_summary": "tx+13196 KiB on p2p-wlan0-1"}

## Тест 5
❯ python3 main.py --protocol wfd --output-res 1280x720 --fps 30 --bitrate 3M --wfd-no-audio --wfd-latency-log
[FluxCast Doctor] System capability report
[FluxCast Doctor] Miracast/WFD looks possible via NetworkManager; raw supplicant access is optional for this backend.

  Status Check                  Details
  ------ ---------------------- ------------------------------------------
  ok     python                 runtime (3.14.4 on Linux 7.0.3-arch1-1)
  ok     ffmpeg                 video/audio transcoding (/usr/sbin/ffmpeg)
  ok     wf-recorder            Wayland/wlroots screen capture (/usr/sbin/wf-recorder)
  ok     pactl                  PulseAudio/PipeWire-Pulse audio monitor detection (/usr/sbin/pactl)
  ok     xrandr                 X11 monitor detection fallback (/usr/sbin/xrandr)
  ok     nmcli                  NetworkManager Wi-Fi Direct control (/usr/sbin/nmcli)
  ok     iw                     kernel Wi-Fi interface inspection (/usr/sbin/iw)
  ok     wpa_cli                active Wi-Fi Direct scan/control (/usr/sbin/wpa_cli)
  ok     gdbus                  passive wpa_supplicant D-Bus capability checks (/usr/sbin/gdbus)
  ok     gst-launch-1.0         optional future WFD GStreamer pipeline (/usr/sbin/gst-launch-1.0)
  ok     gst-inspect-1.0        optional future WFD codec inspection (/usr/sbin/gst-inspect-1.0)
  ok     ffmpeg encoders        H.264 and AAC encoders are available (h264=libx264, h264_vaapi, h264_nvenc, h264_qsv, h264_v4l2m2m; aac=yes)
  ok     screen capture         Wayland capture path is available (WAYLAND_DISPLAY=wayland-1; wf-recorder=/usr/sbin/wf-recorder)
  ok     audio capture          default audio monitor can be derived (alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__Headphones__sink.monitor)
  ok     NetworkManager         Wi-Fi and P2P devices are visible (nmcli tool, version 1.56.0-1; wlan0:wifi:connected | lo:loopback:connected (externally) | virbr0:bridge:connected (externally) | p2p-dev-wlan0:wifi-p2p:disconnected | enp0s31f6:ethernet:unavailable)
  ok     iw P2P                 kernel exposes a P2P-device interface (phy#1 | 	Unnamed/non-netdev interface | 		wdev 0x100000002 | 		addr 2c:33:58:88:dc:45 | 		type P2P-device | 	Interface wlan0 | 		ifindex 12 | 		wdev 0x100000001 | 		addr 2c:33:58:88:dc:45 | 		ssid PODA_80295G | 		type managed | 		channel 36 (5180 MHz), width: 80 MHz, center1: 5210 MHz | 		txpower 22.00 dBm | 		multicast TXQ: | 			qsz-byt	qsz-pkt	flows	drops	marks	overlmt	hashcol	tx-bytes	tx-packets | 			0	0	0	0	0	0	0	0		0)
  warn   wpa_supplicant P2P     supplicant capability query failed (Error: GDBus.Error:org.freedesktop.DBus.Error.AccessDenied: Sender is not authorized to send message)
  warn   wpa_supplicant WFD     WFDIE query failed; supplicant may lack CONFIG_WIFI_DISPLAY (Error: GDBus.Error:org.freedesktop.DBus.Error.AccessDenied: Sender is not authorized to send message)


[FluxCast] Available monitors to capture:
  #    Monitor      Display  Resolution     Position       Refresh
  ---- ------------ -------- -------------- -------------- --------
  [0]  eDP-1        :0       2240x1400     0,0            60.0 Hz ← active
  [1]  HDMI-A-1     :0       1920x1080     2240,0         143.9 Hz

Select monitor [1]: 1
[FluxCast WFD] Starting NetworkManager Wi-Fi Direct scan on p2p-dev-wlan0 for 8s...
[FluxCast WFD] Wi-Fi Direct peer(s):
  [0] 82:47:86:69:2C:87  [TV] Samsung 7 Series (55) via NetworkManager
      WFD capability data detected
Select WFD peer [0]: 0
[FluxCast WFD] Latency log file: /tmp/fluxcast-wfd-latency.jsonl
[FluxCast WFD RTSP] Server listening on 0.0.0.0:7236
[FluxCast WFD] Connecting to [TV] Samsung 7 Series (55) via NetworkManager...
[FluxCast WFD] NetworkManager activation started: (objectpath '/org/freedesktop/NetworkManager/Settings/17', objectpath '/org/freedesktop/NetworkManager/ActiveConnection/14', @a{sv} {})
[FluxCast WFD] Waiting for NetworkManager P2P activation...
[FluxCast WFD] NM active connection: activating; p2p-dev-wlan0:config:0
[FluxCast WFD] NM active connection: activated; p2p-dev-wlan0/p2p-wlan0-2:activated:0
[FluxCast WFD] P2P link is activated; waiting for Samsung RTSP...
[FluxCast WFD] Waiting for Samsung RTSP/WFD session. Press Ctrl+C to stop.
[FluxCast WFD RTSP] TV connected from 10.42.0.17:60317; local=10.42.0.1
[FluxCast WFD RTSP] -> M1_OPTIONS: OPTIONS (CSeq 1)
[FluxCast WFD RTSP] <- response: RTSP/1.0 200 OK
[FluxCast WFD RTSP]   CSeq: 1
[FluxCast WFD RTSP] <- response for M1_OPTIONS: 200 OK
[FluxCast WFD RTSP] -> M3_GET_PARAMETER: GET_PARAMETER (CSeq 2)
[FluxCast WFD RTSP]   wfd_video_formats
[FluxCast WFD RTSP]   wfd_audio_codecs
[FluxCast WFD RTSP]   wfd_client_rtp_ports
[FluxCast WFD RTSP] <- request: OPTIONS * RTSP/1.0
[FluxCast WFD RTSP]   CSeq: 1
[FluxCast WFD RTSP] -> response 200 OK for OPTIONS
[FluxCast WFD RTSP] <- response: RTSP/1.0 200 OK
[FluxCast WFD RTSP]   CSeq: 2
[FluxCast WFD RTSP]   Content-Type: text/parameters
[FluxCast WFD RTSP]   Content-Length: 199
[FluxCast WFD RTSP]   wfd_audio_codecs: LPCM 00000003 00, AAC 00000001 00
[FluxCast WFD RTSP]   wfd_video_formats: 40 00 01 10 000001e3 0f3fffff 00000fff 00 0000 00c8 01 none none
[FluxCast WFD RTSP]   wfd_client_rtp_ports: RTP/AVP/UDP;unicast 19002 0 mode=play
[FluxCast WFD RTSP] <- response for M3_GET_PARAMETER: 200 OK
[FluxCast WFD RTSP] Samsung RTP port: 19002; source port: 19004; audio=LPCM 00000003 00, AAC 00000001 00
[FluxCast WFD RTSP] Negotiated media mode: 1280x720p30
[FluxCast WFD RTSP] Selected video format: 28 00 01 01 00000020 00000000 00000000 00 0000 0000 00 none none
[FluxCast WFD RTSP] -> M4_SET_PARAMETER: SET_PARAMETER (CSeq 3)
[FluxCast WFD RTSP]   wfd_video_formats: 28 00 01 01 00000020 00000000 00000000 00 0000 0000 00 none none
[FluxCast WFD RTSP]   wfd_audio_codecs: none
[FluxCast WFD RTSP]   wfd_presentation_URL: rtsp://10.42.0.1:7236/wfd1.0/streamid=0 none
[FluxCast WFD RTSP]   wfd_client_rtp_ports: RTP/AVP/UDP;unicast 19002 0 mode=play
[FluxCast WFD RTSP] TV disconnected from 10.42.0.17:60317
^C
[FluxCast WFD] Stopping WFD session...
[FluxCast WFD] NetworkManager P2P connection deactivated.
[FluxCast WFD] NetworkManager P2P device disconnected.
 ~/test_scripts/fluxcast  main !8 ?2 

❯ tail -f /tmp/fluxcast-wfd-latency.jsonl
{"ts": "2026-05-05T15:21:03.660+00:00", "mono": 10294.797036, "event": "rtsp_connected", "peer": "10.42.0.17:60317", "local_ip": "10.42.0.1"}

## Тест 6
❯ python3 main.py --wfd-scan
[FluxCast WFD] Starting NetworkManager Wi-Fi Direct scan on p2p-dev-wlan0 for 8s...
[FluxCast WFD] Wi-Fi Direct peer(s):
  [0] 82:47:86:69:2C:87  [TV] Samsung 7 Series (55) via NetworkManager
      WFD capability data detected
❯ python3 main.py --protocol wfd
[FluxCast Doctor] System capability report
[FluxCast Doctor] Miracast/WFD looks possible via NetworkManager; raw supplicant access is optional for this backend.

  Status Check                  Details
  ------ ---------------------- ------------------------------------------
  ok     python                 runtime (3.14.4 on Linux 7.0.3-arch1-1)
  ok     ffmpeg                 video/audio transcoding (/usr/sbin/ffmpeg)
  ok     wf-recorder            Wayland/wlroots screen capture (/usr/sbin/wf-recorder)
  ok     pactl                  PulseAudio/PipeWire-Pulse audio monitor detection (/usr/sbin/pactl)
  ok     xrandr                 X11 monitor detection fallback (/usr/sbin/xrandr)
  ok     nmcli                  NetworkManager Wi-Fi Direct control (/usr/sbin/nmcli)
  ok     iw                     kernel Wi-Fi interface inspection (/usr/sbin/iw)
  ok     wpa_cli                active Wi-Fi Direct scan/control (/usr/sbin/wpa_cli)
  ok     gdbus                  passive wpa_supplicant D-Bus capability checks (/usr/sbin/gdbus)
  ok     gst-launch-1.0         optional future WFD GStreamer pipeline (/usr/sbin/gst-launch-1.0)
  ok     gst-inspect-1.0        optional future WFD codec inspection (/usr/sbin/gst-inspect-1.0)
  ok     ffmpeg encoders        H.264 and AAC encoders are available (h264=libx264, h264_vaapi, h264_nvenc, h264_qsv, h264_v4l2m2m; aac=yes)
  ok     screen capture         Wayland capture path is available (WAYLAND_DISPLAY=wayland-1; wf-recorder=/usr/sbin/wf-recorder)
  ok     audio capture          default audio monitor can be derived (alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__Headphones__sink.monitor)
  ok     NetworkManager         Wi-Fi and P2P devices are visible (nmcli tool, version 1.56.0-1; wlan0:wifi:connected | lo:loopback:connected (externally) | virbr0:bridge:connected (externally) | p2p-dev-wlan0:wifi-p2p:disconnected | enp0s31f6:ethernet:unavailable)
  ok     iw P2P                 kernel exposes a P2P-device interface (phy#1 | 	Unnamed/non-netdev interface | 		wdev 0x100000002 | 		addr 2c:33:58:88:dc:45 | 		type P2P-device | 	Interface wlan0 | 		ifindex 12 | 		wdev 0x100000001 | 		addr 2c:33:58:88:dc:45 | 		ssid PODA_80295G | 		type managed | 		channel 36 (5180 MHz), width: 80 MHz, center1: 5210 MHz | 		txpower 22.00 dBm | 		multicast TXQ: | 			qsz-byt	qsz-pkt	flows	drops	marks	overlmt	hashcol	tx-bytes	tx-packets | 			0	0	0	0	0	0	0	0		0)
  warn   wpa_supplicant P2P     supplicant capability query failed (Error: GDBus.Error:org.freedesktop.DBus.Error.AccessDenied: Sender is not authorized to send message)
  warn   wpa_supplicant WFD     WFDIE query failed; supplicant may lack CONFIG_WIFI_DISPLAY (Error: GDBus.Error:org.freedesktop.DBus.Error.AccessDenied: Sender is not authorized to send message)


[FluxCast] Available monitors to capture:
  #    Monitor      Display  Resolution     Position       Refresh
  ---- ------------ -------- -------------- -------------- --------
  [0]  eDP-1        :0       2240x1400     0,0            60.0 Hz ← active
  [1]  HDMI-A-1     :0       1920x1080     2240,0         143.9 Hz

Select monitor [1]: 1
[FluxCast WFD] Starting NetworkManager Wi-Fi Direct scan on p2p-dev-wlan0 for 8s...
[FluxCast WFD] Wi-Fi Direct peer(s):
  [0] 82:47:86:69:2C:87  [TV] Samsung 7 Series (55) via NetworkManager
      WFD capability data detected
Select WFD peer [0]: 0
[FluxCast WFD RTSP] Server listening on 0.0.0.0:7236
[FluxCast WFD] Connecting to [TV] Samsung 7 Series (55) via NetworkManager...
[FluxCast WFD] NetworkManager activation started: (objectpath '/org/freedesktop/NetworkManager/Settings/18', objectpath '/org/freedesktop/NetworkManager/ActiveConnection/15', @a{sv} {})
[FluxCast WFD] Waiting for NetworkManager P2P activation...
[FluxCast WFD] NM active connection: activating; p2p-dev-wlan0:config:0
[FluxCast WFD] NM active connection: activating; p2p-dev-wlan0:ip-config:0
[FluxCast WFD] NM active connection: activated; p2p-dev-wlan0/p2p-wlan0-3:activated:0
[FluxCast WFD] P2P link is activated; waiting for Samsung RTSP...
[FluxCast WFD] Waiting for Samsung RTSP/WFD session. Press Ctrl+C to stop.
[FluxCast WFD RTSP] TV connected from 10.42.0.17:60340; local=10.42.0.1
[FluxCast WFD RTSP] -> M1_OPTIONS: OPTIONS (CSeq 1)
[FluxCast WFD RTSP] <- response: RTSP/1.0 200 OK
[FluxCast WFD RTSP]   CSeq: 1
[FluxCast WFD RTSP] <- response for M1_OPTIONS: 200 OK
[FluxCast WFD RTSP] -> M3_GET_PARAMETER: GET_PARAMETER (CSeq 2)
[FluxCast WFD RTSP]   wfd_video_formats
[FluxCast WFD RTSP]   wfd_audio_codecs
[FluxCast WFD RTSP]   wfd_client_rtp_ports
[FluxCast WFD RTSP] <- request: OPTIONS * RTSP/1.0
[FluxCast WFD RTSP]   CSeq: 1
[FluxCast WFD RTSP] -> response 200 OK for OPTIONS
[FluxCast WFD RTSP] <- response: RTSP/1.0 200 OK
[FluxCast WFD RTSP]   CSeq: 2
[FluxCast WFD RTSP]   Content-Type: text/parameters
[FluxCast WFD RTSP]   Content-Length: 199
[FluxCast WFD RTSP]   wfd_audio_codecs: LPCM 00000003 00, AAC 00000001 00
[FluxCast WFD RTSP]   wfd_video_formats: 40 00 01 10 000001e3 0f3fffff 00000fff 00 0000 00c8 01 none none
[FluxCast WFD RTSP]   wfd_client_rtp_ports: RTP/AVP/UDP;unicast 19000 0 mode=play
[FluxCast WFD RTSP] <- response for M3_GET_PARAMETER: 200 OK
[FluxCast WFD RTSP] Samsung RTP port: 19000; source port: 19002; audio=LPCM 00000003 00, AAC 00000001 00
[FluxCast WFD RTSP] Negotiated media mode: 1920x1080p30
[FluxCast WFD RTSP] Selected video format: 38 00 01 04 00000080 00000000 00000000 00 0000 0000 00 none none
[FluxCast WFD RTSP] -> M4_SET_PARAMETER: SET_PARAMETER (CSeq 3)
[FluxCast WFD RTSP]   wfd_video_formats: 38 00 01 04 00000080 00000000 00000000 00 0000 0000 00 none none
[FluxCast WFD RTSP]   wfd_audio_codecs: AAC 00000001 00
[FluxCast WFD RTSP]   wfd_presentation_URL: rtsp://10.42.0.1:7236/wfd1.0/streamid=0 none
[FluxCast WFD RTSP]   wfd_client_rtp_ports: RTP/AVP/UDP;unicast 19000 0 mode=play
[FluxCast WFD RTSP] <- response: RTSP/1.0 200 OK
[FluxCast WFD RTSP]   CSeq: 3
[FluxCast WFD RTSP] <- response for M4_SET_PARAMETER: 200 OK
[FluxCast WFD RTSP] -> M5_TRIGGER_SETUP: SET_PARAMETER (CSeq 4)
[FluxCast WFD RTSP]   wfd_trigger_method: SETUP
[FluxCast WFD RTSP] <- response: RTSP/1.0 200 OK
[FluxCast WFD RTSP]   CSeq: 4
[FluxCast WFD RTSP] <- response for M5_TRIGGER_SETUP: 200 OK
[FluxCast WFD RTSP] <- request: SETUP rtsp://10.42.0.1:7236/wfd1.0/streamid=0 RTSP/1.0
[FluxCast WFD RTSP]   CSeq: 2
[FluxCast WFD RTSP]   Transport: RTP/AVP/UDP;unicast;client_port=19000-19001
[FluxCast WFD RTSP] -> response 200 OK for SETUP
[FluxCast WFD RTSP] SETUP complete; RTP sink port=19000
[FluxCast WFD RTSP] <- request: PLAY rtsp://10.42.0.1:7236/wfd1.0/streamid=0 RTSP/1.0
[FluxCast WFD RTSP]   CSeq: 3
[FluxCast WFD RTSP]   Session: 1222373
[FluxCast WFD RTSP] -> response 200 OK for PLAY
[FluxCast WFD RTSP] Starting media as 1920x1080p30; RTP source port 19002
[FluxCast WFD Media] Raising bitrate for desktop clarity: 4M -> 8M
[FluxCast WFD Media] Capturing screen : HDMI-A-1 (1920x1080)
[FluxCast WFD Media] Capturing audio  : alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__Headphones__sink.monitor
[FluxCast WFD Media] RTP target      : 10.42.0.17:19000 from local port 19002
selected region 2240,0 1920x1080
Setting codec option: pix_fmt=yuv420p
Framerate: 30
Using video filter: fps=30
Output #0, nut, to '/dev/stdout':
  Stream #0:0: Video: rawvideo (BGR[0] / 0x524742), bgr0(pc), 1920x1080 [SAR 1:1 DAR 16:9], q=2-31, 1492992 kb/s
[Source @ 0x7fcd28005e40] Changing video frame properties on the fly is not supported by all filters.
[Source @ 0x7fcd28005e40] filter context - w: 1920 h: 1080 fmt: 121 csp: gbr range: unknown alpha: unspecified, incoming frame - w: 1920 h: 1080 fmt: 121 csp: unknown range: unknown alpha: unspecified pts_time: 0
[in#0/nut @ 0x55b4d4358140] Stream #0: not enough frames to estimate rate; consider increasing probesize
[aist#1:0/pcm_s16le @ 0x55b4d43735c0] Guessed Channel Layout: stereo
[FluxCast WFD RTSP] PLAY accepted; media stream started.
[FluxCast WFD Media] Latency probe: first RTP bytes after PLAY in 704.5 ms
[FluxCast WFD Media] Latency probe: sender-path latency (RTSP connect -> first RTP) 3324.6 ms
[FluxCast WFD Media] Sender health: pid=168823:running, pid=168824:running; tx+1522 KiB on p2p-wlan0-3
[FluxCast WFD Media] Sender health: pid=168823:running, pid=168824:running; tx+7755 KiB on p2p-wlan0-3
^C
[FluxCast WFD] Stopping WFD session...
[FluxCast WFD] NetworkManager P2P connection deactivated.
[FluxCast WFD] NetworkManager disconnect warning: Error: GDBus.Error:org.freedesktop.NetworkManager.Device.NotActive: Device is not active
 ~/test_scripts/fluxcast  main !8 ?2 

## Тест 7 (при первой комменде был зависший экран, при второй комманде видео шло но без звука)
❯ source venv/bin/activate
❯ python3 main.py --protocol dlna --transport progressive-ts
=======================================================
  FluxCast — Desktop → Smart TV via UPnP/DLNA
=======================================================

[FluxCast] Available monitors to capture:
  #    Monitor      Display  Resolution     Position       Refresh
  ---- ------------ -------- -------------- -------------- --------
  [0]  eDP-1        :0       2240x1400     0,0            60.0 Hz ← active
  [1]  HDMI-A-1     :0       1920x1080     2240,0         143.9 Hz

Select monitor [1]: 1
[FluxCast] Capturing Wayland monitor : HDMI-A-1 (1920x1080)
[FluxCast] Screen capture started.
[FluxCast] HTTP server: http://192.168.100.103:8080/session-1777994682/progressive.ts
[FluxCast] Session: session-1777994682
[FluxCast] Transport: progressive-ts
[FluxCast] Waiting for HLS source to start… ready! (3 segments, 7.8s)
[FluxCast] HLS source is producing segments ✓
[FluxCast] Searching for UPnP/DLNA Cast devices (timeout=5s)…

[FluxCast] Found DLNA device(s):
  [0] [TV] Samsung 7 Series (55)  (UE55TU7092UXXH)
[FluxCast] Auto-selected: [TV] Samsung 7 Series (55)
[FluxCast] Sending stream URL to [TV] Samsung 7 Series (55) via UPnP/DLNA…
[FluxCast Server] progressive-ts -> 192.168.100.13 (200, start=0, current=4956 KiB, live-edge restart)
[FluxCast Server] progressive-ts closed for 192.168.100.13 (sent=1664 KiB, 0.2s)
[FluxCast] Output signal sent! The TV should open its native video player.
[FluxCast] Casting started. Press Ctrl+C to stop.
[FluxCast Server] progressive-ts -> 192.168.100.13 (206, start=0, current=4739 KiB, live-edge restart, Range: bytes=0-)
[FluxCast Server] progressive-ts closed for 192.168.100.13 (sent=256 KiB, 0.1s)
[FluxCast Server] progressive-ts -> 192.168.100.13 (206, start=1000000576, current=0 KiB, live-edge restart, live-seek 1000000576->19931948, Range: bytes=1000000576-)
[FluxCast Server] progressive-ts closed for 192.168.100.13 (sent=640 KiB, 0.2s, live-seek 1000000576->19931948)
[FluxCast Server] progressive-ts -> 192.168.100.13 (206, start=688128, current=19464 KiB, Range: bytes=688128-)
[FluxCast Server] progressive-ts closed for 192.168.100.13 (sent=2176 KiB, 0.2s)
[FluxCast Server] progressive-ts -> 192.168.100.13 (206, start=9999750000, current=0 KiB, live-edge restart, live-seek 9999750000->19931948, Range: bytes=9999750000-)
[FluxCast Server] progressive-ts closed for 192.168.100.13 (sent=244 KiB, 0.0s, live-seek 9999750000->19931948)
[FluxCast Server] progressive-ts -> 192.168.100.13 (206, start=688128, current=19464 KiB, Range: bytes=688128-)
^C
[FluxCast] Stopping…
[FluxCast Server] progressive-ts closed for 192.168.100.13 (sent=8320 KiB, 38.2s)
[FluxCast] Stopped. Goodbye!

❯ python3 main.py --protocol dlna --transport hls
=======================================================
  FluxCast — Desktop → Smart TV via UPnP/DLNA
=======================================================

[FluxCast] Available monitors to capture:
  #    Monitor      Display  Resolution     Position       Refresh
  ---- ------------ -------- -------------- -------------- --------
  [0]  eDP-1        :0       2240x1400     0,0            60.0 Hz ← active
  [1]  HDMI-A-1     :0       1920x1080     2240,0         143.9 Hz

Select monitor [1]: 1
[FluxCast] Capturing Wayland monitor : HDMI-A-1 (1920x1080)
[FluxCast] Screen capture started.
[FluxCast] HTTP server: http://192.168.100.103:8080/session-1777994776/stream.m3u8
[FluxCast] Session: session-1777994776
[FluxCast] Transport: hls
[FluxCast] Waiting for HLS source to start… ready! (3 segments, 5.6s)
[FluxCast] HLS source is producing segments ✓
[FluxCast] Searching for UPnP/DLNA Cast devices (timeout=5s)…

[FluxCast] Found DLNA device(s):
  [0] [TV] Samsung 7 Series (55)  (UE55TU7092UXXH)
[FluxCast] Auto-selected: [TV] Samsung 7 Series (55)
[FluxCast] Sending stream URL to [TV] Samsung 7 Series (55) via UPnP/DLNA…
[FluxCast Server] HLS playlist #1 -> 192.168.100.13 (200, 173 bytes, last=stream1.ts)
[FluxCast] Output signal sent! The TV should open its native video player.
[FluxCast] Casting started. Press Ctrl+C to stop.
[FluxCast Server] HLS playlist #2 -> 192.168.100.13 (206, 173 bytes, last=stream1.ts, Range: bytes=0-)
[FluxCast Server] HLS playlist #3 -> 192.168.100.13 (206, 173 bytes, last=stream1.ts, Range: bytes=0-)
[FluxCast Server] HLS playlist #4 -> 192.168.100.13 (206, 173 bytes, last=stream1.ts, Range: bytes=0-)
[FluxCast Server] HLS playlist #5 -> 192.168.100.13 (200, 173 bytes, last=stream1.ts)
[FluxCast Server] HLS segment stream0.ts -> 192.168.100.13 (200, 4665 KiB, behind=1 seg/1.0s)
[FluxCast Server] HLS segment stream1.ts -> 192.168.100.13 (200, 5591 KiB, behind=15 seg/15.0s)
[FluxCast Server] HLS segment stream14.ts -> 192.168.100.13 (200, 5461 KiB, behind=unknown (mixed playlist cache))
[FluxCast Server] HLS segment stream15.ts -> 192.168.100.13 (200, 4188 KiB, behind=3 seg/3.0s)
[FluxCast Server] HLS segment stream16.ts -> 192.168.100.13 (200, 5900 KiB, behind=2 seg/2.0s)
^C
[FluxCast] Stopping…
[FluxCast] Stopped. Goodbye!

## Тест 8 (не работает)
❯ python3 main.py --protocol cast
=======================================================
  FluxCast — Desktop → Smart TV via UPnP/DLNA
=======================================================

[FluxCast] Available monitors to capture:
  #    Monitor      Display  Resolution     Position       Refresh
  ---- ------------ -------- -------------- -------------- --------
  [0]  eDP-1        :0       2240x1400     0,0            60.0 Hz ← active
  [1]  HDMI-A-1     :0       1920x1080     2240,0         143.9 Hz

Select monitor [1]: 1
[FluxCast] Capturing Wayland monitor : HDMI-A-1 (1920x1080)
[FluxCast] Screen capture started.
[FluxCast] HTTP server: http://192.168.100.103:8080/session-1777994902/progressive.ts
[FluxCast] Session: session-1777994902
[FluxCast] Transport: progressive-ts
[FluxCast] Waiting for HLS source to start… ready! (3 segments, 4.0s)
[FluxCast] HLS source is producing segments ✓
[FluxCast] Searching for Cast devices on the network…
[FluxCast] Searching for Cast devices (timeout=5s)…
[FluxCast] ERROR: No Cast devices found on the network.
[FluxCast] TIP: Use --tv-ip <IP> to connect directly, e.g.:
[FluxCast]      python main.py --tv-ip 192.168.100.XXX
❯ python3 main.py --protocol cast --tv-ip 192.168.100.13
=======================================================
  FluxCast — Desktop → Smart TV via UPnP/DLNA
=======================================================

[FluxCast] Available monitors to capture:
  #    Monitor      Display  Resolution     Position       Refresh
  ---- ------------ -------- -------------- -------------- --------
  [0]  eDP-1        :0       2240x1400     0,0            60.0 Hz ← active
  [1]  HDMI-A-1     :0       1920x1080     2240,0         143.9 Hz

Select monitor [1]: 1
[FluxCast] Capturing Wayland monitor : HDMI-A-1 (1920x1080)
[FluxCast] Screen capture started.
[FluxCast] HTTP server: http://192.168.100.103:8080/session-1777994953/progressive.ts
[FluxCast] Session: session-1777994953
[FluxCast] Transport: progressive-ts
[FluxCast] Waiting for HLS source to start… ready! (2 segments, 0.8s)
[FluxCast] HLS source is producing segments ✓
[FluxCast] Connecting directly to Cast device at 192.168.100.13:8009…
[FluxCast] ERROR: No Cast device responded at 192.168.100.13:8009.
[FluxCast] Make sure the TV is ON, on the same network, and Cast is enabled in Settings → General → External Device Manager.
 ~/te/fluxcast  main !10 ?2  
