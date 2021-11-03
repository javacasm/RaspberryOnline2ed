from gpiozero import Servo  # importamos los módulos necesarios
from time import sleep

servo = Servo(18)           # definimos el servo conectado al gpio 18

while True:                 # bucle infinito
    servo.min()             # posición de un extremo
    sleep(2)                # esperamos 2 segundos
    servo.mid()             # posición central
    sleep(2)                # esperamos 2 segundos
    servo.max()             # posición del otro extremo
    sleep(2)                # esperamos 2 segundos
