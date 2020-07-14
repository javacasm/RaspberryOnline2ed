import time
# Importamos la librería wiringpi
import wiringpi2
#Configuramos la numeración de los pines con respecto al
#estandar de la librería wiringpi (pin de entrada salida
# GPIO0)
io = wiringpi2.GPIO(wiringpi2.GPIO.WPI_MODE_PINS)
#Configuramos el pin 0 como salida
io.pinMode(0,io.OUTPUT)
# Ciclo for que ejecutamos 3 veces
for x in range (0,3):
io.digitalWrite(0,io.HIGH) #encendemos el led
time.sleep(0.5) # esperamos medio segundo
io.digitalWrite(0,io.LOW) # apagamos el led
time.sleep(0.5) # esperamos medio segundo
