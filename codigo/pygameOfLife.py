
# pyGame of Life
# Siguiendo tutorial de .dotcsv  https://www.youtube.com/watch?v=qPtKv9fSHZY

import pygame  
# Lo usamos para dibujar en pantalla
import numpy as np
# Lo utilizamos para manejar matrices fácilmente
import time


pygame.init()

width, height = 1000, 1000  # Tamaño de la pantalla
screen = pygame.display.set_mode((height,width))

bgColor = 25, 25, 25  # Color del fondo

deathCellcolor = 128, 128, 128
liveCellColor = 255, 255, 255

nxC, nyC = 50, 50 # Número de celdas en el eje X y el Y

dimCW = width / nxC # Ancho de la celda
dimCH = height / nyC # Alto de la celda


# Estado de las celdas: Viva = 1, Muerta = 0
gameState = np.zeros((nxC, nyC))


# Autómata palo
gameState[5, 3]  = 1
gameState[5, 4]  = 1
gameState[5, 5]  = 1


# Autómata móvil
gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1

pauseExect = False

bRunning = True
# Bucle de ejecución
while bRunning:

    newGameState = np.copy(gameState)

    screen.fill(bgColor)
    time.sleep(0.1) 

    ev = pygame.event.get()

    for event in ev:
        # Detectamos si se presiona una tecla
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                bRunning = False
            else:
                pauseExect = not pauseExect  # Invertimos el estado

        if event.type == pygame.QUIT:
            bRunning = False

        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) > 0 : # Algún botón está pulsado
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)) , int(np.floor(posY / dimCH))
            newGameState[celX, celY] = not newGameState[celX, celY] 

    # Vamos a dibujar el estado de la rejilla
    for y in range(0, nyC):
        for x in range(0, nxC):        
            
            if not pauseExect:
                # Contamos los vecinos vivos sin contarnos  a  nosotros (x,y) ) 
                # TODO: ¿Es necesario usar módulo el tamaño 
                # o podemos usar que python soporta indices negativos?
                n_neigh =   gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                            gameState[(x    ) % nxC, (y - 1) % nyC] + \
                            gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                            gameState[(x - 1) % nxC, (y    ) % nyC] + \
                            gameState[(x + 1) % nxC, (y    ) % nyC] + \
                            gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                            gameState[(x    ) % nxC, (y + 1) % nyC] + \
                            gameState[(x + 1) % nxC, (y + 1) % nyC]              

                # Regla #1: Una célula muerta con exactamente 3 vecinas vivas revive
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1

                # Regla #2: Una célula viva con 2 o más de 3 vecinas vivas muere

                elif gameState[x, y]== 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0


            # Creamos un array de 4 puntos (cada punto (x,y) )
            poly = [( (  x  ) * dimCW, (  y  ) * dimCH ),
                    ( (x + 1) * dimCW, (  y  ) * dimCH ),
                    ( (x + 1) * dimCW, (y + 1) * dimCH ),
                    ( (  x  ) * dimCW, (y + 1) * dimCH ) ]
            
            # Dibujamos la celda según su estado
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, deathCellcolor, poly, 1) # pintamos el borde con grosor 1
            else :
                pygame.draw.polygon(screen, liveCellColor, poly, 0)  # pintamos la celda rellena


        # Actualizamos el estado con lo calculado

    gameState = np.copy(newGameState)

    pygame.display.flip() # Mostramos el contenido dibujado
    