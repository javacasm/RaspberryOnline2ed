from gpiozero import LED  # importamos los modulos necesarios
from time import sleep

red = LED(17)  	# declaramos nuestro led como conectado al GPIO 17

while True:  	# Repetimos en bucle para siempre
	red.on() 	# Encendemos el led
	sleep(1)	# Esperamos 1 segundo
	red.off()	# Apagamos el led
	sleep(1)	# esperamos otro segundo
