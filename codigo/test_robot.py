from gpiozero import Robot  # importamos todo lo modulos necesarios
from time import sleep
robby = Robot(left=(7,8), right=(9,10))  # definimos las conexiones del robot
robby.forward(0.4) # nos movemos hacia adelante con 40% de velocidad
sleep(5)         # esperamos 5 segundos
robby.right(0.4) # nos giramos a la derecha con 40% de velocidad
sleep(5)         # esperamos 5 segundos
robby.stop() # paramos