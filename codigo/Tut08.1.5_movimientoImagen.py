"""
Tutorial básico de pyGame
08.2 - Movimiento de formas con teclas:

Eventos de teclado:
Propiedades:
* key 
    pygame.K_q ...
    pygame.K_LEFT ...

Docs: 
* Eventos https://www.pygame.org/docs/ref/event.html
* Keys https://www.pygame.org/docs/ref/key.html

CC by SA @javacasm
Diciembre 2020
"""

import pygame


# graficos

width = 640
height = 400


# 3 formas de definir los colores
red = pygame.Color('Red')
cyan = pygame.Color('cyan')
blue = pygame.Color(0,0,255) # ¿alpha?
green = (0,  255, 0)
white = (255,255,255)
black = (0,0,0)

pygame.init() # Inicializa el entorno de pygame


# Music
pygame.mixer.music.load('./music/Fortunate Note - Silent Partner.mp3') # cargamos el fichero
pygame.mixer.music.set_volume(0.5 ) # volumen entre 0 y 1.0
pygame.mixer.music.play()

# Screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Movimiento rectángulo')

miImagen = pygame.image.load('./images/python-logo.png') # cargamos la imagen

# coordenadas del cuadrado
x = 200
y = 200

# velocidad de movimiento
vel = 1

miImagen = pygame.image.load('./images/python-logo.png') # cargamos la imagen

miFondo = pygame.image.load('./images/fondo.png') # lo cargamos

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    if event.type == pygame.KEYDOWN:
            print('Teca pulsada: '+event.unicode)

            if event.key == pygame.K_q: # salimos con la tecla q
                running == False

            if event.key == pygame.K_LEFT:
                print('Movmiento izda')
                x -= vel

            if event.key == pygame.K_RIGHT:
                print('Movmiento drcha')                
                x += vel

            if event.key == pygame.K_UP:
                print('Movmiento arriba')
                y -= vel

            if  event.key == pygame.K_DOWN:
                print('Movmiento abajo')        
                y += vel

    screen.fill(black) # ponemos el fondo negro
    screen.blit(miFondo,(0,0))
    screen.blit(miImagen,(x, y)) # después copiamos la imagen

    pygame.display.flip()  # actualizamos la pantalla

pygame.quit()     