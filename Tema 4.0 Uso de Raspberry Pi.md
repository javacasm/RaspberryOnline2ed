# Tema 4 - Uso de Raspberry Pi

En este tema vamos a ver los usos normales de Raspberry Pi.

Dado que el uso de los típicos programas de ofimática o similares es idéntico al que se hace en otros ordenadores nos vamos a hablar de ellos.

Nos centraremos en los usos más típicos donde se trabaja con la consola/terminal. Es el típico uso que se hace en los sistemas Linux. La mayoría de los que veremos se puede hacer en los sistemas con Linux de las distribuciones [Debian](https://www.debian.org/index.es.html) y [Ubuntu](https://www.ubuntu.com/) en los que está basado Raspbian.


## Problemas habituales

Siempre podemos encontrarnos con problemas. Veamos los más frecuentes

### Alimentación

Necesitamos un mínimo de 2A (3A para V4), si la alimentación está por debajo se pueden producir cuelgues inesperados e incluso que no arranque.

Cuando la Raspberry detecta que no tiene suficiente alimentación visualiza un rayo amarillo en la pantalla

![Problemas de alimentación. Fuente Raspberry Para Torpes](https://i0.wp.com/raspberryparatorpes.net/wp-content/uploads/2018/02/raspberry-pi-under_volt.jpg?resize=500%2C300&ssl=1)

### Velocidad de la tarjeta

Se recomienda velocidad 10, una velocidad menor da problemas como bloqueos

### Espacio en disco

Al menos 8GB por sistema operativo, mejor 16GB o más

### No se ve nada en el monitor

¿Lo arrancaste con el monitor conectado? Es necesario arrancar con el monitor conectado, si Raspberry no detecta ningún monitor en arranque desactiva la salida de vídeo.


