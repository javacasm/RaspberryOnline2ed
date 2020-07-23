"""
Test de sensor de distancia con ultrasonidos

CC by SA @javacasm
Julio 2020
"""
v = '0.2'

from gpiozero import DistanceSensor
import time
ultrasonic1 = DistanceSensor(echo = 17, trigger = 4)
ultrasonic1.max_distance = 2

ultrasonic2 = DistanceSensor(echo = 6, trigger = 5)
ultrasonic2.max_distance = 2

def distance2cm(u):
    return int(u.distance * 100)

while True:
    print(distance2cm(ultrasonic1), ' ' , distance2cm(ultrasonic2))
    time.sleep(0.2)
