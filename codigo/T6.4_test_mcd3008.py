#!/usr/bin/python3
"""
Ejemplo de lectura del adc MCP3008
 
Se requieren los módulos gpiozero

Instalación:


"""

from gpiozero import MCP3008
pot = MCP3008(0)
print(pot.value)
while True:
    print(pot.value)
