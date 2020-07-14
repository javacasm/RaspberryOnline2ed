from gpiozero import LED, Button # importamos modulos necesarios
from time import sleep

led = LED(17)  # declaramos un led conectado al GPIO 17
button = Button(2) # Declaramos un pulsador conectado al GPIO 2

button.wait_for_press()  	# Espera hasta que se pulse el boton
led.on()					# Encendemos el led
sleep(3) 					# Esperamos 3 segundos
led.off()					# Apagamos el led
