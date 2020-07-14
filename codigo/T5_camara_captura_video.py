# Ejemplo basico de previsualizacion y captura de video con la camara
# captest_basico_video.py
# Mas detalles en https://projects.raspberrypi.org/en/projects/getting-started-with-picamera

from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview() # comenzamos la previsualizacion
camera.start_recording('/home/pi/Desktop/video.h264') # empezamos a grabar
sleep(5) # esperamos 5 segundos que durara la grabación
camera.stop_recording() # paramos la grabación
camera.stop_preview() # paramos la previsualizacion
