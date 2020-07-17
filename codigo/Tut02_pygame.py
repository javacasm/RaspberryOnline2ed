"""
Tutorial básico de pyGame
02 - Definimos colores de diferente formas:
* Usando la clase pygame.Color:
    * Usando nombres de colores : 'Red', 'Blue', 'Black', 'Aqua' ¿Listado?
* Usando una tupla de 3 valores para la intensidad ¿Alpha?
Usamos el método fill sobre surface para rellenar la ventana de un color dado
Docs: 
* Sobre la clase Color https://www.pygame.org/docs/ref/color.html
* Colores definidos https://github.com/pygame/pygame/blob/master/src_py/colordict.py

CC by SA @javacasm
Junio 2020
"""

import pygame

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
pygame.display.set_caption('Ejemplo colores')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    screen.fill(green) # rellenamos la pantalla de verde

    pygame.display.flip()  # actualizamos la pantalla

pygame.quit()     
