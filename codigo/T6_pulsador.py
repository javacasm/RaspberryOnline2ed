# Encendemos un led cuando se activa el pulsador
import wiringpi

io=wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)

io.pinMode(7,io.OUTPUT)  # Pin 7 como salida
io.pinMode(0,io.INPUT)   # Pin 0 como entrada
io.pullUpDnControl(0,io.PUD_UP)  # Activo la resistencia pull-up del pulsador

while True:  # Hacemos un bucle sin fin
	x=io.digitalRead(0)  # Leemos el valor del pulsador 
	if x==io.LOW: 	# Si esta pulsado valor bajo (por la resistencia pull-up)
		io.digitalWrite(7,io.HIGH)   # Activamos el led
	else:
		io.digitalWrite(7,io.LOW) 	# Apagamos el led

