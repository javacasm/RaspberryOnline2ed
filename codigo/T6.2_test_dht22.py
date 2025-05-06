#!/usr/bin/python3

"""
Ejemplo de lectura de tmperatura y humdad con el sensor DHT22
Se requiere el módulo adafruit_DHT de circuitpython 

Instalación:

pip3 install adafruit-circuitpython-dht lgpio
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


