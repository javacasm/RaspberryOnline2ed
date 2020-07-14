# Ejemplo basico de previsualizacion y captura con la camara
# captest_basico_imagen.py
# Mas detalles en https://projects.raspberrypi.org/en/projects/getting-started-with-picamera

from picamera import PiCamera
from time import sleep

camera = PiCamera() # creamos el objeto camara

camera.start_preview() # muestra la previsualizacion
sleep(5) # espera 5 segundos
camera.capture('/home/pi/Desktop/image.jpg') # guarda la imagen
camera.stop_preview() # cierra la previsualizacion
