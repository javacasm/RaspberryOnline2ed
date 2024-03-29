# Ejemplo básico de aplicación de efectos a la camara
# T5_camara_efectos.py
# Mas detalles en https://picamera.readthedocs.io/en/release-1.13/api_camera.html#picamera.PiCamera.image_effect

from picamera import PiCamera
from time import sleep
import random

camera = PiCamera()
efectos = ['none' , 'negative', 'solarize','sketch','denoise','emboss','oilpaint','hatch','gpen','pastel','watercolor','film','blur','saturation','colorswap','washedout','posterise','colorpoint','colorbalance','cartoon','deinterlace1','deinterlace2']
camera.start_preview() # muestra la previsualización
while True:
    efectoUsado = efectos[ random.randint(0, len(efectos)-1) ]
    print('Efecto ' + efectoUsado)
    camera.image_effect = efectoUsado
    sleep(5) # espera 5 segundos
    camera.capture('/home/pi/Desktop/image' + efectoUsado + '.jpg') # guarda la imagen
camera.stop_preview() # cierra la previsualización
