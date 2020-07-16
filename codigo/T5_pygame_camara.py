# Ejemplo basico de visualizacion y captura con la camara y pyGame
# T5_pygame_captura.py
# Mas detalles en https://projects.raspberrypi.org/en/projects/getting-started-with-picamera

import picamera
import pygame
import io

# Init pygame 
pygame.init()
screen = pygame.display.set_mode((0,0))

# Init camera
camera = picamera.PiCamera()
camera.resolution = (1280, 720) # resolución de la camara
camera.crop = (0.0, 0.0, 1.0, 1.0) #¿recortamos?

x = (screen.get_width() - camera.resolution[0]) / 2 # centramos en el eje x
y = (screen.get_height() - camera.resolution[1]) / 2 # centramos en el eje y

# Init buffer
rgb = bytearray(camera.resolution[0] * camera.resolution[1] * 3) # necesitamos 3 bytes por cada pixel de la camara

# Bucle principal
exitFlag = True
while(exitFlag):
    for event in pygame.event.get():
        if(event.type is pygame.MOUSEBUTTONDOWN or 
           event.type is pygame.QUIT):
            exitFlag = False
# para evitar parpadeos, se lee en una imagen y luego se copia a la pantalla
    stream = io.BytesIO()
    camera.capture(stream, use_video_port=True, format='rgb')
    stream.seek(0)
    stream.readinto(rgb) # leemos la informacion de la camara
    stream.close()
    img = pygame.image.frombuffer(rgb[0:
          (camera.resolution[0] * camera.resolution[1] * 3)],
           camera.resolution, 'RGB') # pasamos los datos leidos a una imagen

    screen.fill(0) # ponemos el fondo de la pantalla en negro
    if img: # si la imagen es valida la pasamos a pantalla
        screen.blit(img, (x,y))

    pygame.display.update() # actualizamos la pantalla

camera.close()
pygame.display.quit()

