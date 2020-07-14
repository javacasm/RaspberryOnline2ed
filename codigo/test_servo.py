from gpiozero import Servo  # importamos los modulos necesarios
from time import sleep

servo = Servo(18)           # definimos el servo conectado al gpio 18

while True:                 # bucle infinito
    servo.min()             # posicion de un extremo
    sleep(2)                # esperamos 2 segundos
    servo.mid()             # posicion central
    sleep(2)                # esperamos 2 segundos
    servo.max()             # posicion del otro extremo
    sleep(2)                # esperamos 2 segundos
