# Tema 6 - Electrónica con Raspberry Pi

En este tema vamos a ver como conectar dispositivos electrónicos a la Raspberry Pi.

## Cuidados eléctricos

Trabajar con electrónica es siempre algo delicado pero mucho más cuando trabajamos conectados a un ordenador.

* No existe protección en los terminales, con lo que es muy, muy sencillo quemar la placa.
* Cuidado con colocar la placa sobre un instrumento o superficie metálica. Mejor usar una caja
* Cuidado con los dispositivos que conectamos, pudieran demandar más potencia de la que le puede dar
* Antes de realizar cualquier tipo de conexión en los conectores o pines debemos de tener siempre la precaución de tener desconectada la alimentación de la Raspberry Pi.
* Evitaremos derivaciones eléctricas o cortos .
* Conviene recordar que los pines de la CPU de la placa están conectados directamente a los diferentes conectores y pines, con lo que cualquier cosa que hagamos sobre los pines la estamos haciendo directamente sobre la CPU.
* También hay que tener en cuenta que los pines GPIO no soportan 5 V, sólo 3.3V y un máximo de 16 mA, por lo que hay que tomar precauciones en este sentido.


## Adaptadores

Existen diferentes adaptadores que nos facilitan el uso de electrónica y ademas protegen a la Raspberry. En la sección de las placas hablaremos de ellas.

## Potencia

Los pines de la Raspberry no proporcionan potencia, más allá de encender unos leds. Si necesitas más potencia tendrás que añadir componentes electrónicos capaces de gestionarlo.

## GPIO

![GPIO](./images/GPIORasp.png)

* Son los pines que podemos usar como salidas o como entradas, es decir, para activar dispositivos (leds, motores, etc) o para leer el estado de sensores, interruptores etc. Siempre funcionan en modo digital.
* Podemos configurar cada uno como entrada o como salida
* Utilizan **3.3V** Por ello tenemos que tener cuidado con lo conectamos. Un dispositivo que use 5V podría dañarla.
* Algunos de ellos se pueden usar como comunicaciones especializadas: SPI, I2C, UART



## Pines

Hay que tener cuidado con no equivocarse. Para evitar errores podemos usar una etiqueta

![Etiquetas para los pines](./images/etiquetas.png)

O esta otra versión del gran @pighixxx con los diferentes etiquetados

![Etiquetas de @pighixxx](https://pbs.twimg.com/media/DACXWfzXkAE--mT.jpg)


[Vídeo sobre etiquetas en los GPIO de Raspberry](https://youtu.be/9UiZ7m6UacM)

Las distintas versiones de la Raspberry tienen algunos pines distintos

![GPIO para la versión 2](./images/GPIOV2.png)
	
Las versiones de 40 pines hasta la Raspberry pi 3+

![GPIO de 40 pines](./images/pi2GPIO.jpg)

Los GPIOs para la Raspberry pi 4

![GPIOs para la Raspberry pi 4](./images/GPIO4.webp)

## Manejo basico de los pines

### Encendiendo un led

Necesitaremos un Led y una resistencia de 220Ohmios (o 330) 
Vamos conectarlos de la siguiente manera

![Led](./images/led-gpio17.png)

El programa es muy sencillo

```python
	from gpiozero import LED  # importamos los modulos necesarios
	from time import sleep

	red = LED(17)  	# declaramos un led conectado al GPIO 17

	while True:  	# Repetimos en bucle para siempre
		red.on() 	# Encendemos el led
		sleep(1)	# Esperamos 1 segundo
		red.off()	# Apagamos el led
		sleep(1)	# Esperamos otro segundo
	```

[Código](https://github.com/javacasm/RaspberryOnline/blob/master/codigo/test_led.py)

Podemos utilizar el edito Thonny para ejecutar los siguientes ejemplos 

### Usando botones/pulsadores

Vamos ahora a conectar un botón y a detectar cuando está pulsado

![Botón](./images/button.png)

Y el programa es muy sencillo también

```p	ython
	from gpiozero import Button # importamos los modulos necesarios

	button = Button(2) # Declaramos pulsador conectado al GPIO 2

	button.wait_for_press() # Espera hasta que se pulse el boton
	print('Me has pulsado') # Nos informa de que se ha pulsado
```

[Código](https://github.com/javacasm/RaspberryOnline/blob/master/codigo/Test_boton.py)

Fácilmente podemos mezclar los dos ejemplos, haciendo que el led se encienda durante un tiempo cuando pulsemos

```python
	from gpiozero import LED, Button # importamos modulos necesarios
	from time import sleep

	led = LED(17)  # declaramos un led conectado al GPIO 17
	button = Button(2) # Declaramos un pulsador conectado al GPIO 2

	button.wait_for_press()  	# Espera hasta que se pulse el boton
	led.on()					# Encendemos el led
	sleep(3) 					# Esperamos 3 segundos
	led.off()					# Apagamos el led
	```

Ya tenemos todo lo necesario para montar un semáforo ¿te animas?

## Controlando motores

Para controlar motores vamos a necesitar una placa que se encargue de manejar la suficiente potencia.
Vamos a usar un módulo muy utilizado llamado L298

![Driver de motores L298](./images/l298-dual-h-bridge-motor-driver.jpg)

Usaremos un par de sencillos motores DC

![Motor DC de tipo TT](./images/motor_tt.jpg)

Y también necesitaremos una alimentación externa para los motores, que puede ser unas pilas o un batería con el 

Conectaremos los motores de la siguiente manera

![Conexión motores a L298](./images/wires-in-board.jpg)

Y la batería de la siguiente forma

![Conexión de la batería](./images/battery-holder.jpg)

Y ahora conectaremos los pines de control de la siguiente forma

![Conexión de los pines de control](./images/gpio-board.jpg)

 Conectaremos 7 -> In1,  8 -> In2,  9 -> In3, 10 -> In4 y  GND -> GND

Veamos ahora un sencillo ejemplo de control

```python
	from gpiozero import Motor  # Importamos los modulos
	from time import sleep

	# Motor izquierdo (L) conectando pines 7 y 8 a la placa L298
	motorL = Motor(forward = 7, backward = 8)
	# Motor derecho (R) conectando pines 9 y 9 a la placa L298
	motorR = Motor(forward = 9, backward = 10)

	while True:  # Bucle para siempre
		motorL.forward()  # Motor L hacia adelante
		motorR.forward()  # Motor R hacia adelante
		sleep(5)		  # Esperamos 5 segundos
		motorL.backward() # Motor L hacia atras
		motorR.backward() # Motor R hacia atras
		sleep(5)		  # Esperamos 5 segundos
```

[Código](https://github.com/javacasm/RaspberryOnline/blob/master/codigo/Test_motores.py)

Y nuestros motores deben de moverse hacia adelante y hacia atrás

Si lo que queremos es montar un robot con esos 2 motores podemos hacerlo de una manera más sencilla usando este ejemplo

```python
	from gpiozero import Robot  # importamos todo lo modulos necesarios
	from time import sleep
	robby = Robot(left=(7,8), right=(9,10))  # definimos las conexiones del robot
	robby.forward(0.4) # nos movemos hacia adelante con 40% de velocidad
	sleep(5)         # esperamos 5 segundos
	robby.right(0.4) # nos giramos a la derecha con 40% de velocidad
	sleep(5)         # esperamos 5 segundos
	robby.stop() # paramos

```

[Código](https://github.com/javacasm/RaspberryOnline/blob/master/codigo/test_robot.py)

Ahora ya podemos hacer robót como estos

[zerobot](https://www.thingiverse.com/thing:2352440)

![zerobot](https://cdn.thingiverse.com/renders/a4/48/26/89/b2/c200276c9a8a68e2538f83dc438e61f1_preview_featured.JPG)

[Smart Zero](https://www.thingiverse.com/thing:2727285)

![Smart zero](https://cdn.thingiverse.com/renders/b2/e2/fa/57/54/8580f06ab82a9cf5ed57c2194e3115c5_preview_featured.JPG)

[Formula Pi](https://www.formulapi.com/) Capaces de buscar su propio camino usando la cámara com podemos ver en [este vídeo](https://youtu.be/2PU-UDYm2Xw?t=40)

![Formula Pi](https://d2cdo4blch85n8.cloudfront.net/wp-content/uploads/2016/07/PiBorg-Formula-Pi-Raspberry-Pi-Self-driving-Toy-Race-Car-image-3-630x473.jpg)

## Controlando un servomotor

Un servomotor es un tipo de motor que sólo realiza movimientos angulares entre 0 y 180 grados (existen algunos modelos que se llaman trucados o de rotación continua pero no vamos a tratar aquí)
Una de las grandes ventajas de los servos es que incluyen su propio contolador con lo que sólo necesitamos alimentarlos y una señal de control

![Servomotor](./images/Micro-servo.jpg)

Podremos controlarlos de las patillas GPIO12, GPIO13, GPIO18, GPIO19

![Pines PWM](./images/Raspberry_pi_3_PWMpins.png)

Conectaremos 18 -> Naranja, 5V -> Rojo, GND -> Marrón

El código es muy sencillo. Este ejemplo va desde el mínimo, al punto medio y luego al máximo

```python
	from gpiozero import Servo  # importamos los modulos necesarios
	from time import sleep

	servo = Servo(18)			# definimos el servo conectado al gpio 18

	while True:					# bucle infinito
		servo.min()				# posicion de un extremo
		sleep(2)				# esperamos 2 segundos
		servo.mid()				# posicion central
		sleep(2)				# esperamos 2 segundos
		servo.max()				# posicion del otro extremo
		sleep(2)				# esperamos 2 segundos
```

[Código](https://github.com/javacasm/RaspberryOnline/blob/master/codigo/test_servo.py)

## Controlando una pantalla LCD de tipo I2C

Vamos a ver cómo conectar una pantalla LCD de tipo LCD de las que se suelen tener las máquinas de vending

![Pantalla LCD de tipo I2C](./images/lcd-i2c.jpg)

En primar lugar tenemos que activar el bus I2C en la pestaña de configuración de interfaces

![raspi-config](http://www.circuitbasics.com/wp-content/uploads/2016/02/Raspberry-Pi-LCD-I2C-Connections-sudo-raspi-config.png)

![Enable I2C](http://www.circuitbasics.com/wp-content/uploads/2016/02/Raspberry-Pi-LCD-I2C-Connections-sudo-raspi-config-enable-i2c.png)

Ahora instalaremos herramientas i2c

		sudo apt-get install i2c-tools

Y una librería python

		sudo apt-get install python-smbus

Conectamos el LCD

![Conexion LCD](./images/2.LCD_I2C_bb.png)

Conectaremos SDA(3) -> SDA, SCL(5) -> SCL, 3.3V -> Vcc y  GND -> GND

Y ejecutamos la herramienta para detectar dispositivos i2C y su correspondiente dirección (normalmente el fabricante nos proporciona este dato)

![Instalacion I2C](./images/Instalacion_I2C.png)

Vemos que se ha detectado el LCD en la dirección 0x27 (en nuestro caso podemos obtener otro valor como 0x30 o 0x3F)

Usaremos el codigo de [I2C_LCD_driver.py](https://github.com/javacasm/RaspberryOnline/blob/master/codigo/I2C_LCD_driver.py)

Para probar a ver si funciona todo

```python
    import I2C_LCD_driver
    from time import *

    mylcd = I2C_LCD_driver.lcd()

    mylcd.lcd_display_string("Hola LCD!", 1)

```

Un ejemplo sencillo para hacer que parpadee un texto

```python
    import time
    import I2C_LCD_driver
    mylcd = I2C_LCD_driver.lcd()

    while True:
        mylcd.lcd_display_string(u"TEXTO PARPADEANTE")
        time.sleep(1)
        mylcd.lcd_clear()
        time.sleep(1)
```

Mostrar la fecha y la hora

```python
      import I2C_LCD_driver
      import time
      mylcd = I2C_LCD_driver.lcd()


      while True:
          mylcd.lcd_display_string("Hora: %s" %time.strftime("%H:%M:%S"), 1)

          mylcd.lcd_display_string("Fecha: %s" %time.strftime("%d/%m/%Y"), 2)
```

Para mostrar la dirección IP, algo muy útil si no tenemos conectada otra pantalla

```python
    import I2C_LCD_driver
    import socket
    import fcntl
    import struct

    mylcd = I2C_LCD_driver.lcd()

    def get_ip_address(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,
            struct.pack('256s', ifname[:15])
        )[20:24])

    mylcd.lcd_display_string("IP Address:", 1)

    mylcd.lcd_display_string(get_ip_address('eth0'), 2)
```

Más ejemplos en [la fuente original](http://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/)		

Más [proyectos](http://projects.raspberrypi.org) e [información](https://gpiozero.readthedocs.io/en/stable/installing.html) sobre electrónica

## Otras Librerías

Existen otras librerías que nos facilitarán el acceso a los GPIO (todas usan lenguaje python como base). Nosotros veremos algunas de ellas por motivos históricos y porque muchos proyectos las usan y conviene saber utilizalas.

Para probarlas re-haremos algunos de los ejemplos ya vistos con estas librerías

* Shell (línea de comandos)
* Rpi. GPIO
* wiringPi (Gordon Henderson wiringpi.com)
* BCM 2835

Veamos como llaman a los distintos pines

![Nombre de los GPIOs](./images/NombresGPIO.png)

#### Wiring

Para instalarlo tenemos que tener instalado parte del entorno de desarrollo de python

		sudo apt-get install python-dev python-pip

Descargamos el código (también podíamos haber descargado el fichero zip)

		sudo pip install wiringpi

La compilamos

		./build

Y ya podemos usarla

		gpio readall


![Leer el estado de todos los pines](./images/readall.png)


### Conectando un led

Este es el esquema para conectar un led

![LED](./images/led.png)

El montaje sería

![Esquema de conexión de un led](./images/esquemaled.png)

Hagamos un programa que parpadea el led conectado

```python
		import time
		# Importamos la libreria wiringpi
		import wiringpi
		# Configuramos la numeracion de los pines con respecto al
		# estandar de la libreria wiringpi (pin de entrada salida
		#	GPIO0)

		io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)

		# Configuramos el pin 0 como salida
		io.pinMode(0,io.OUTPUT)

		# Ciclo for que ejecutamos 3 veces
		for x in range (0,3):
			io.digitalWrite(0,io.HIGH) #encendemos el led
			time.sleep(0.5) # esperamos medio segundo
			io.digitalWrite(0,io.LOW) # apagamos el led
			time.sleep(0.5) # esperamos medio segundo
```

Para ejecutar estos programas necesitamos permiso de administrador

		sudo python blink.py

### Conectado un pulsador

![Conectando un pulsador](./images/pulsador.png)

Usando el código

```python
		# Encendemos un led cuando se activa el pulsador
		import wiringpi

		io=wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)

		io.pinMode(7,io.OUTPUT)  # Pin 7 como salida
		io.pinMode(0,io.INPUT)   # Pin 0 como entrada
		io.pullUpDnControl(0,io.PUD_UP)  # Resistencia pull-up

		while True:  # Hacemos un bucle sin fin
			x=io.digitalRead(0)  # Leemos el valor del pulsador
			if x==io.LOW: 	# Si esta pulsado valor bajo (por la resistencia pull-up)
				io.digitalWrite(7,io.HIGH)   # Activamos el led
			else:
				io.digitalWrite(7,io.LOW) 	# Apagamos el led
```

Vemos que para leer el pulsador activamos las resistencias pull-up, es decir cuando se pulse se pone en estado bajo, esto es lo que se conoce como  lógica invertida (o negativa). Aunque puede parecer raro, es como se suele utilizar en la industria pues aporta ventajas de conexión y mantenimiento.

### Usando GPIO

Instalamos la librería

		sudo apt-get install python-dev python-rpi.gpio

El programa que los usa

```python
		import RPi.GPIO as GPIO
		# Usamos la numeración de los GPIO no el numero de los pines
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(7, GPIO.IN) # establecemos el GPIO 7 como entrada
		GPIO.setup(8, GPIO.OUT) # establecemos el GPIO 8 como salida
		input_value = GPIO.input(7) # recuperamos el valor de entreda
		GPIO.output(8, True) # establecemos la salida en alto
```

O este ejemplo más complejo

```python
		import RPi.GPIO as GPIO
		import time
		# Usamos la posición en el conector
		GPIO.setmode(GPIO.BOARD)
		# pin 11 (GPIO17) como output
		GPIO.setup(11, GPIO.OUT)
		var=1
		print "Empezamos el bucle infinito"
		while var==1 :
			print "Output False"
			GPIO.output(11, False)
			time.sleep(1) # esperamos un tiempo
			print "Output True"
			GPIO.output(11, True)
			time.sleep(1)
```

### Usando más potencia

En el caso bastante normal de que necesitemos más potencia de las que nos da un pin (16mA) Podemos utilizar un transistor. Veamos el montaje

![Conexión con transistor](./images/transistor.png)


A la salida de este transistor podemos conectar un relé para obtener aún más potencia

### Leyendo valores analógicos

Para leer valores analógicos usaremos electrónica externa, com pueden se [esta placa](https://www.abelectronics.co.uk/p/65/adc-differential-pi-raspberry-pi-analogue-to-digital-converter) o [esta otra](http://www.adafruit.com/products/1085), ambas de 16 bits. El [montaje es sencillo](http://learn.adafruit.com/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi)

![ADC](./images/adc.png)

### Usos de los GPIOs

* Encender apagar LEDs (no podemos aspirar a encender nada de mayor potencia directamente). Estas son las salidas digitales, capaces de estar en estado alto o bajo.
* Algunos de estos pines pueden generar PWM (modulación por ancho de pulso) protocolo que usan los servos.
* Detectar pulsaciones de botones/interruptores. Estas son las entradas digitales.
• Acceso al puerto serie por los terminales TX/TX
• Acceso al bus I2C, bus de comunicaciones usado por muchos dispositivos
• Acceso al bus SPI, bus de comunicaciones similar al I2C pero con diferentes especificaciones

El bus I2C y SPI nos permiten conectar con dispositivos externos que nos
expanden su funcionalidad. Es como si conectáramos periféricos a nuestra
Raspberry.

![GPIO de 40 pines](./images/pi2GPIO.jpg)

* También están disponibles las líneas de alimentación de 5v y 3.3v y por supuesto tierra.

* Todos los pines se pueden configurar tanto de entrada como de salida.

* Algunos de los pines tienen una segunda función como por ejemplo los etiquetados como SCL y SDA utilizados para I2C y los MOSI, MISO y SCKL utilizados para conectar con dispositivos SPI.
* Hay que tener muy claro que todos los pines usan niveles lógicos de 3.3V y no es seguro conectarlos directamente a 5V, porque las entradas han de ser menores de 3.3V. Igualmente no podemos esperar salidas superiores a 3.3V.
* En caso de querer conectar con lógica de 5v tendremos que usar una electrónica para adaptar niveles.
* Existen dispositivos convertidores de niveles (level shifters) con diferentes tecnologías. Los más antiguos están formados por unas resistencias y unos transistores.

![Conversores de niveles (shifter)](./images/shifter.png)

Para identificar más fácilmente los pines recordad que podemos usar el truco de las etiquetas del que ya hablamos


## Placas GPIO

Existen muchas placas que facilitan la conexión de electrónica.

[Vídeo: Cómo conectar shields a RaspBerry Pi](https://www.youtube.com/watch?v=J9ZolkLrbdg)

### Clobber

* Es bastante arriesgado y complicado trabajar directamente con los pines del conector GPIO de la RaspBerry.
* Existen en el mercado una gran variedad de placas que nos facilitan la vida.
* Algunas sólo nos facilitan la conexión.
* Otras nos proporcionan mayor funcionalidad.
* En cualquier caso ganamos en tranquilidad al usarlas.


![Clobber](./images/clobber.jpg)

Son simples adaptadores que nos facilitan la vida permitiendo conectar de manera sencilla con las placas de prototipo


[Vídeo: Conectando electrónica a Raspberry - Cobbler DIY](https://youtu.be/CyNVsgw-t3U?list=PLDxBiw1MlK6SqyPGhhox9WlsximiNrcgK)


### PiPlate

![PiPlate](./images/piplate.png)

Se trata de una placa de prototipo especialmente adaptada al tamaño de la Raspberry y que nos permite acceder de forma sencilla a los pines por nombre y funcionalidad.

[Video: Placa de prototipo para Raspberry Pi - Pi Plate](https://youtu.be/AB50mlF0ikU?list=PLDxBiw1MlK6SqyPGhhox9WlsximiNrcgK)


### PiFace

![PiFace](./images/piface.png)

* Tiene un fin claramente educativo,
* Incluye diferentes dispositivos
* Leds que se pueden activar independientemente,
* 2 relés para activar cargas de potencia y
* 4 pulsadores conectados a otras tantas entradas

![Esquema de PiFace](./images/esquemapiface.png)

### Slice of I/O

![Slice](./images/slice.png)

Se trata de una placa sencilla que nos permite acceder a 8 entradas y otras tantas salidas con la seguridad de que existe una electrónica que protege a nuestra RaspBerry

### Gertboard

![Gertboard](./images/gertboard.png)

Es una placa de desarrollo con una enorme cantidad de complementos, como son controladores de motores, ADC, DAC, 12 leds, 3 pulsadores y hasta un microcontrolador ATMega (similar a Arduino)

### RaspiRobot

![RaspiRobot](./images/raspirobot.png)

Esta placa nos permite controlar un típico robot de 2 motores de manera muy sencillo. 

* El manejo de motores es mucho más complejo que el manejo de leds.
* La programación es exactamente la misma,
* La electrónica necesaria para controlarlos es totalmente diferente.
* Si bien podemos conectar directamente un led a un pin de GPIO, conectar un motor es totalmente desaconsejable, por varias razones:
	* La primera porque los motores requieren de mayor potencia para funcionar,
	* Necesitaremos una electrónica capaz de gestionar estas potencias
	* Serán controladas desde los pines de la RaspBerry.
	* En caso de forzar la electrónica de alimentación de nuestra Raspberry a dar una mayor potencia podríamos quemarla.
	* El funcionamiento de los motores hace que estos generen al acelerar unas corrientes de inducción de sentido opuesto a las que les aplicamos para funcionar y que de no ser suprimidas podrían dañar la electrónica a la que están conectados.

En la [web de RaspiRobot](https://github.com/simonmonk/raspirobotboard/wiki) vemos instrucciones de montaje

[Vídeo: Raspirobot - Controlando robots con Raspberry](https://youtu.be/FjjP8007DXA?list=PLDxBiw1MlK6SqyPGhhox9WlsximiNrcgK)

¿Qué podemos hacer con RaspiRobot?

* Controla 2 motores,
* 2 leds,
* 2 entradas de pulsador,
* 2 salidas de colector abierto, para poder usar mayores potencias
* Conector I2C y
* otro serie

Descargamos la librería

	wget https://github.com/simonmonk/raspirobotboard/archive/master.zip

La descomprimimos conviene

	unzip master.zip
	
y la instalamos

	sudo python setup.py install

Un programa sencillo podría ser

		from raspirobotboard import *
		rr = RaspiRobot() # creamos el objeto
		rr.set_led1(1) # activamos el led 1
		rr.set_led2(0) # desactivamos el led 2
		rr.set_oc1(1) # activamos la salida 1
		rr.forward() # movemos los dos motores hacia adelante
		rr.reverse() # movemos los dos motores hacia atrás
		rr.left() # motor izquierdo hacia adelante, derecho hacia atrás
		rr.right() # motor izquierdo hacia atrás, derecho hacia adelante
		rr.stop() # los dos motores hacia atrás
		rr.sw1_closed() # devuelver True o False según cerrado o abierto


### Steppers: motores paso a paso

![Stepper](./images/stepper.png)

Los motores paso a paso son motores que nos permiten una gran precisión de giro, pudiendo determinar su moviendo en grados.

Vamos a ver cómo usar el motor de la imagen, que tiene 4 bobinas. La placa de control es muy sencilla y necesita de 4 pines para controlarla (en realidad la placa sólo transforma la salida de los pines de raspberry en una señal de la potencia que necesita el motor)

Veamos como conectarla usando 5V y GND y los pines 24,25,8 y 7


Vamos a ver ahora la programación.

		import timeimport RPi.GPIO as GPIO
		GPIO.setmode(GPIO.BCM)
		StepPins = [24,25,8,7] # Pines que conectamos a la placa de control
		for pin in StepPins: # configuramos todos los pines como salida
			GPIO.setup(pin,GPIO.OUT)
			GPIO.output(pin, False)
			StepCounter = 0
			WaitTime = 0.5
			StepCount1 = 4
			Seq1 = []
			Seq1 = range(0, StepCount1) # Definimos la secuencia de giro
			Seq1[0] = [1,0,0,0]
			Seq1[1] = [0,1,0,0]
			Seq1[2] = [0,0,1,0]
			Seq1[3] = [0,0,0,1]
			while 1==1: # realizamos un bucle infinito enviando la secuencia
				for pin in range(0, 4): #iteramos sobre los pasos de la secuencia
					xpin = StepPins[pin]
					if Seq[StepCounter][pin]!=0:
						GPIO.output(xpin, True)
					else:
						GPIO.output(xpin, False)
					StepCounter += 1
					time.sleep(WaitTime)

Veamos un ejemplo de su precisión

![Robot polarplot](./images/polarplot.png)		

### Servos

Los servos son motores pensados para mantener una posición concreta, disponen de electrónica de control propia y a la se le indica la posición que deben mantener mediante un pulso que hay que enviar 50 veces por segundo.

El ancho de este pulso determina la posición a mantener, como podemos ver en la imagen adjunta.

![Control de servos](./images/servocontrol.png)

La estabilidad de la posición depende de la precisión con la enviemos la señal de control.

Veamos un método para generar esta señal con python. Está pensada para controlar 2 servos:

		def mover_servo(grados,servo):
			if servo==1: GPIO_servo=22
			elif servo==2: GPIO_servo=21
			# creamos el pulso
			pos_servo=(0.0000122*grados)+0.0002
			GPIO.output(GPIO_servo, True) #activamos la salida
			time.sleep(pos_servo) # esperamos la duración del pulso
			GPIO.output(GPIO_servo, False) # desativamos la señal porque el pulso ha terminado
			#esperamos el tiempo necesario hasta enviar el siguiente pulso
			time.sleep(0.0025-pos_servo)


Si lo probamos veremos que el servo vibra debido a la mala calidad de la señal por su falta de estabilidad. Python es un lenguaje interpretado y temporización que hemos hecho dependerá de la carga que tenga nuestra Raspberry

Podemos mejorar la calidad de la señal utilizando un programa escrito en C que producirá una mejor temporización.


### Uniéndolo todo

Vamos a utilizar un par de servos para hacer que una cámara [siga una cara](http://www.instructables.com/id/Pan-Tilt-face-tracking-with-the-raspberry-pi/?ALLSTEPS)

![Opencv + Camara](./images/opencvCamara.png)

Estos son los pasos para instalar todo lo necesario

		sudo apt-get update
		sudo apt-get install git python-opencv python-all-dev libopencv-dev
		sudo modprobe servoblaster
		git clone https://github.com/mitchtech/py_servo_facetracker

Y para ejecutarlo

		cd py_servo_facetracker
		python ./facetracker_servo_gpio.py 0



### Motores y servos

A veces no interesa controlar varios motores y servos desde una misma placa. 

[Servo desde python](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-8-using-a-servo-motor?view=all)

![Servo desde python](https://learn.adafruit.com/system/assets/assets/000/003/489/medium800/learn_raspberry_pi_overview.jpg?1396797194)

[Varios motores](https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi?view=all)

![Controlando varios motores](https://learn.adafruit.com/system/assets/assets/000/022/670/medium800/raspberry_pi_2348_iso_demo_01_ORIG.jpg?1422298425)

## Sensores

Veamos como podemos conectar [sensores de temperatura digitales](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing?view=all)

![Sensores de temperatura](https://learn.adafruit.com/system/assets/assets/000/003/775/medium800/learn_raspberry_pi_summary.jpg?1396801585)

### Algunos enlaces

Por si te interesa profundicar veamos algunos enlaces interesantes sobre tutoriales de electrónica

*  http://www.sc.ehu.es/sbweb/electronica/elec_basica/default.htm
*  http://www.tutoelectro.com/
*  http://www.electronicafacil.net/circuitos/
*  http://www.areatecnologia.com/
*  http://www.simbologia-electronica.com/

## Conexión con Arduino

Anteriormente vimos que Arduino y Raspberry Pi son perfecgamente complementarios.

Por tanto el conectarlos de manera que ambos puedan trabajar juntos parece que es la mejor idea.

A lo largo de este capítulo veremos varias formas de conectarlos, algunas utilizando un simple cable y otras con placas y electrónica de por medio.

Vamos a comenzar con la manera de conectarlos más sencilla, las que los conectan con cables

### Conectando vía cable

Las más sencillas son aquellas que conectan los puertos serie de ambos Esta conexión la podemos hacer de varias formas.

* Utilizando un cable USB, puesto que Arduino sólo consume (si no tiene nada conectado) en torno a los 50mA podemos alimentarlo sin problema del USB de la Raspberry.

* Utilizando un cable serie entre ambos puertos serie. Hay que tener en cuenta los diferentes voltajes

En cualquiera de los dos casos es necesario que desactivemos la consola serie de la Raspberry e instalemos la librería py-serial.

En [este tutorial](https://geekytheory.com/arduino-raspberry-pi-lectura-de-datos/) podemos ver cómo hacerlo.

Otra opción interesante es conectarlos utilizando el protocolo I2C, de esta forma la comunicación puede alcanzar más velocidad y nos serviría para conectar otros dispositivos I2C. En [este otro tutorial](https://oscarliang.com/raspberry-pi-arduino-connected-i2c/) se explica en detalle.

![raspberry arduino i2c](https://raspberrypi4dummies.files.wordpress.com/2013/07/arduino-rpi-i2c-communication_bb.png)

### Utilizando placas intermedias

Existen dispositivos pensados para facilitar esta comunicación. Veamos algunos de ellos

#### Alamode

Se trata de una placa compatible con Arduino que se conecta directamente a los GPIO de la Raspberry Pi y que dispone de su propia tarjeta SD

Más información en [este](http://www.internetdelascosas.cl/2013/09/11/alamode-un-arduino-para-raspberry-pi/) y [este enlace]( http://makezine.com/2012/12/12/new-product-alamode-arduino-compatible-shield-for-raspberry-pi/)

![Alamode](./images/alamode-01-150x150.jpg)

#### Paperduino pi

[Paperduino](http://paperpcb.dernulleffekt.de/doku.php?id=raspberry_boards:paperduinopi) es diseño de Arduino que se puede hacer directamente sobre una placa de prototipo y que está pensado para conectarlo directamente a la Raspberry

![Paperduino](./images/Paperduino.png)


#### Raspberry Pi to arduino shield Bridge


![Cooking hakcs](./images/CookingHack_arduino_raspberry.jpg)

[Esta placa](http://www.cooking-hacks.com/documentation/tutorials/raspberry-pi-to-arduino-shields-connection-bridge) nos permite crear una especie de emulador de Arduino, es decir, ejecutar proyectos de arduino (ino o pde) en la raspberry. Además tiene  conectores estándar de Arduino lo que nos permite conectar shield de arduino.
Hay que tener cuidado con los shields que conectamos puesto que podríamos tener problemas si estos funcionan en 5v y


