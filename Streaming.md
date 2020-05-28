

 raspivid -o - -t 99999 |cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://0.0.0.0:8554/}' :demux=h264

Cliente VLC rtsp://192.168.1.33:8554/


https://www.raspberrypi.org/forums/viewtopic.php?t=44169