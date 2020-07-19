#!/usr/bin/python3

"""
Ejemplo de lectura de tmperatura y humdad con el sensor DHT22
Se requiere el módulo Adafruit_DHT

Instalación:

pip3 install Adafruit_DHT
"""

import sys
import Adafruit_DHT as dht
import time



sensor = dht.DHT22 # Podría ser tambien un DH11
pin = 4
while True:
    humedad, temperatura = dht.read_retry(sensor, pin) # recuperamos los valores del sensor
    print('Temp={0:0.1f} ºC,  Hum={1:0.1f} %'.format(temperatura, humedad))
    time.sleep(5) # esperamos 5 segundos