#!/usr/bin/python3
"""
Ejemplo de lectura del adc MCP3008
 
Se requieren los módulos adafruit-blinka y adafruit-circuitpython-mcp3xxx

Instalación:

pip3 install adafruit-blinka
pip3 install adafruit-circuitpython-mcp3xxx
"""

import os
import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
 
# creamos el spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
 
# el pin CS selecciona la placa a usar 
cs = digitalio.DigitalInOut(board.D22)
 
# creamos el objeto mcp
mcp = MCP.MCP3008(spi, cs)
 
# leemos el canal 0
chan0 = AnalogIn(mcp, MCP.P0)
 
print('Valor ADC raw: ', chan0.value)
print('Voltaje ADC : ' + str(chan0.voltage) + 'V')
