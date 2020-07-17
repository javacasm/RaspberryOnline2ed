# Ejemplo basico de aplicación de efectos a la camara
# T5_camara_efectos.py
# Mas detalles en https://picamera.readthedocs.io/en/release-1.13/api_camera.html#picamera.PiCamera.image_effect

"""
Ejemplos

/home/pi/Desktop/imageblur.jpg          /home/pi/Desktop/imagehatch.jpg
/home/pi/Desktop/imagecartoon.jpg       /home/pi/Desktop/imagenegative.jpg
/home/pi/Desktop/imagecolorbalance.jpg  /home/pi/Desktop/imagenone.jpg
/home/pi/Desktop/imagecolorpoint.jpg    /home/pi/Desktop/imageoilpaint.jpg
/home/pi/Desktop/imagecolorswap.jpg     /home/pi/Desktop/imagepastel.jpg
/home/pi/Desktop/imagedeinterlace1.jpg  /home/pi/Desktop/imageposterise.jpg
/home/pi/Desktop/imagedeinterlace2.jpg  /home/pi/Desktop/imagesaturation.jpg
/home/pi/Desktop/imagedenoise.jpg       /home/pi/Desktop/imagesketch.jpg
/home/pi/Desktop/imageemboss.jpg        /home/pi/Desktop/imagesolarize.jpg
/home/pi/Desktop/imagefilm.jpg          /home/pi/Desktop/imagewashedout.jpg
/home/pi/Desktop/imagegpen.jpg          /home/pi/Desktop/imagewatercolor.jpg

"""


from picamera import PiCamera
from time import sleep
import random

camera = PiCamera()
efectos = ['none' , 'negative', 'solarize','sketch','denoise','emboss','oilpaint','hatch','gpen','pastel','watercolor','film','blur','saturation','colorswap','washedout','posterise','colorpoint','colorbalance','cartoon','deinterlace1','deinterlace2']
camera.start_preview() # muestra la previsualizacion
while True:
    efectoUsado = efectos[ random.randint(0, len(efectos)-1) ]
    print('Efecto ' + efectoUsado)
    camera.image_effect = efectoUsado
    sleep(5) # espera 5 segundos
    camera.capture('/home/pi/Desktop/image' + efectoUsado + '.jpg') # guarda la imagen
camera.stop_preview() # cierra la previsualizacion
