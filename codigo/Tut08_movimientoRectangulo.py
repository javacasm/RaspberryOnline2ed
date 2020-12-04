import pygame

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
Junio 2020
"""

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

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Movimiento rectángulo')

# coordenadas del cuadrado
x = 200
y = 200

# tamaño del rectángulo
rect_width = 20
rect_height = 20

# velocidad de movimiento
vel = 10

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

    pygame.draw.rect(screen, (255, 0, 0), (x, y, rect_width, rect_height)) # después dibujamos el rectángulo

    pygame.display.flip()  # actualizamos la pantalla

pygame.quit()     