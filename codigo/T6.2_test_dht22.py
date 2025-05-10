#!/usr/bin/python3

"""
Ejemplo de lectura de temperatura y humdead con el sensor DHT22
Se requiere el módulo adafruit-circuitpython-dht de circuitpython y sus dependencias

Instalación:

pip3 install adafruit-circuitpython-dht lgpio RPi.GPIO
"""

import sys
import adafruit_dht	 as dht
import time
import board
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
sensor = dht.DHT22(board.D18)
while True:

    if sensor.humidity != None and sensor.temperature != None:
        print(f'Temp={sensor.temperature} ºC,  Hum={sensor.humidity} %')
        time.sleep(5) # esperamos 5 segundos
    else:
        print('Error de conexión. Verifique el montaje')


