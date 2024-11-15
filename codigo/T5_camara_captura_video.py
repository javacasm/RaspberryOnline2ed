# Ejemplo básico de previsualización y captura de video con la camara
# T5_camara_captura_video.py
# Mas detalles en https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf

from picamera2 import Picamera2
picam2 = Picamera2()
picam2.start_and_record_video("test.mp4", duration=5)

