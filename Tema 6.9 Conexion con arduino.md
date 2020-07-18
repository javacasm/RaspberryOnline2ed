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


