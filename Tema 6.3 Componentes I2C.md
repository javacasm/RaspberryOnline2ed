## Controlando una pantalla LCD de tipo I2C

Vamos a ver cómo conectar una pantalla LCD de tipo LCD de las que se suelen tener las máquinas de vending

![Pantalla LCD de tipo I2C](./images/lcd-i2c.jpg)

En primar lugar tenemos que activar el bus I2C en la pestaña de configuración de interfaces

![raspi-config](http://www.circuitbasics.com/wp-content/uploads/2016/02/Raspberry-Pi-LCD-I2C-Connections-sudo-raspi-config.png)

![Enable I2C](http://www.circuitbasics.com/wp-content/uploads/2016/02/Raspberry-Pi-LCD-I2C-Connections-sudo-raspi-config-enable-i2c.png)

Ahora instalaremos herramientas i2c

```sh
sudo apt-get install i2c-tools
```

Y una librería python
```sh
sudo apt-get install python-smbus
```

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


AÑADIR ALGUN SENSOR COMO EL BME280 O EL UVA