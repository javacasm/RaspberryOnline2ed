# Ejemplo básico de previsualización y captura de imagen con la camara
# T5_camara_captura_imagen.py
# Mas detalles en https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf

from picamera2 import Picamera2, Preview # importamos todo lo necesario
import time
picam2 = Picamera2() # creamos el objeto para acceder a la cámara
# vamos a hacer una configuración por defecto para que se previsualice
# en el escritorio
camera_config = picam2.create_preview_configuration() 
picam2.configure(camera_config)
# arrancamos la previsualización
picam2.start_preview(Preview.QTGL)
picam2.start()
# mantenemos la previsualización durante 2 segundos
time.sleep(2)
# guardamos la captura en el fichero "test.jpg"
picam2.capture_file("test.jpg")
