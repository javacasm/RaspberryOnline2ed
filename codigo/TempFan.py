"""
Control de la velociad de un ventilador en función de la temperatura de la CPU

Conectamos un transistor al pin 21
"""

from gpiozero import PWMLED
from time import sleep
import sys
import os
from time import sleep
import signal

maxTMP = 70
medTMP = 60

fan = PWMLED(21)

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    temp =(res.replace("temp=","").replace("'C\n",""))
    #print("temp is {0}".format(temp)) #Uncomment here for testing
    return temp

try:
    while True:
    	CPU_temp = float(getCPUtemperature())
	    if CPU_temp > maxTMP:
			fan.value = 1.0  # Máxima velocidad
		elif CPU_temp > medTMP:
			fan.value = 0.5  # Velocidad media
		else:
			fan.value = 0    # Parada
		sleep(5)