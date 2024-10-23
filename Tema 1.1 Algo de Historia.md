## Orígenes de Raspberry Pi

La intención de los creadores de Raspberry era crear un sistema barato que nos permitiera enseñar a programar a niños y adultos.

* Un estudio de la Universidad de Cambridge en 2005 puso en evidencia cómo cada vez menos estudiantes querían estudiar informática.

* Pensaron que la solución podría ser un ordenador superbarato con el que pudieran jugar, aprendiendo en el camino.

* Los primeros prototipos de Raspberry Pi se empezaron a construir en 2006, pero era difícil con la electrónica disponible en la época.

  ![Prototipo Raspberry](./images/prototipo-Raspi-reducida-40.png)

* En 2009, ya existía la tecnología necesaria y se creó "Raspberry Pi Foundation" administrada por Eben Upton.

* En 2011, surgen los primeros prototipos disponibles para probar y se ve factible vender modelos de 25$ y 35$. Aparece el modelo B Beta.

  ![Placa beta Raspberry Pi](./images/betaPi-sin-fondo-reducida-75.jpg)
  
  
Utiliza un diseño avanzado como podemos observar en la imagen, donde se ha colocado un chip encima de otro.

![Ejemplo de diseño avanzado, usando 2 chips superpuestos](./images/EncapsuladoCPU-RAM-reducida-40.jpg)

Actualmente existen varios formatos, vamos a ver los más usados:

* La versión más actual a día de hoy (Octubre de 2024) es la [Versión 5](https://www.raspberrypi.com/products/raspberry-pi-5/) 2.4GHz Quad-Core de 64bits hasta 8GB, USB 3.0, 2 HDMI 4K Gigabit, Wifi y bluetooth.

![Raspberry Pi 5](./images/raspberry-pi-5-reducida-50.jpg)

* La versión [Raspberry Pi Zero W](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/) (1Ghz 512Mb) con un tamaño muy pequeño y un precio superreducido de 10€ - 15€, según la queramos con o sin wifi.

![Raspberry Pi Zero](./images/Raspberry-Pi-Zero-web_reducida_60.jpg)

* [Módulo Raspberry Pi Compute 3+](https://www.raspberrypi.com/products/compute-module-3-plus/): es equivalente a una Raspberry Pi 3 B+ pero en un formato pensado para construir ordenadores a partir de varias Raspberry. Se puede adquirir con un disco interno eMMC de 8GB/16GB/32GB que sustituye a la tarjeta SD.

![Módulo Raspberry Pi Compute 3+](./images/Raspberry_Pi_Compute_Module.png)

Se puede integrar en Module Kit 3:

![Raspberry Pi Kit 3](./images/Raspberry-Pi-Compute-Module-Kit-3_reducida_60.jpg)

* Raspberry Pi 400, es equivalente a una Raspberry Pi 4, pero en formato teclado, con carcasa incorporada. 

Seguramente hayas oído hablar también de la Raspberry Pi Pico pero aunque comparte nombre, porque está diseñada también por la Fundación Raspberry Pi, la Pico es un microcontrolador, no un miniordenador y es más parecido a un Arduino (Realmente más parecido a un ESP32)

Más adelante veremos muchos más detalles de esta versión y de las anteriores. 

Puedes encontrar más detalles en el [Artículo de la Wikipedia sobre Raspberry Pi](https://en.wikipedia.org/wiki/Raspberry_Pi)


## Raspberry Pi vs Arduino

![Comparativa de tamaño entre Arduino Mega, Raspberry Pi y Arduino UNO](./images/arduinovsRaspberry.jpg)

Una pregunta muy frecuente es si para determinado proyecto es mejor usar Arduino o Raspberry Pi: la respuesta es sencilla, son equipos muy distintos con capacidades diferentes y generalmente son complementarios.

Vamos a ver las diferencias en detalle, pero podríamos resumirlas diciendo que Raspberry es el cerebro donde Arduino hace más el papel de músculo (desde el punto de vista eléctrico).

Arduino es más robusto eléctricamente: si se produce un cortocircuito entre pines o se comente un error se apagará y reseteará, pero las probabilidades de romperlo son bajas. En cambio si hacemos esto mismo con una Raspberry lo más seguro es que la dejemos inservible.

Algunas ventajas de Arduino:

* Es capaz de dar una mayor corriente por cada patilla (hasta 40mA) mientras que Raspberry Pi no puede dar más de 5mA
* Dispone de entradas analógicas, es decir, es capaz de leer valores eléctricos intermedios entre 0 y 5v, no solo digitales como Raspberry Pi
* La sencillez de su funcionamiento (como microcontrolador) le aporta una gran robustez a la hora de soportar cortes de alimentación.
* Últimamente están apareciendo diversas versiones de Arduino con mayor capacidad, soportando una programación más compleja y potente, como Yún o Galileo.

Raspberry Pi tiene una mayor capacidad de procesamiento, lo que la hace más adecuada para determinadas tareas, como reconocimiento de imágenes o cálculos complejos, algo que sería impensable para Arduino.


* Raspberry Pi dispone de mayor capacidad de almacenamiento y de memoria permitiendo utilizar programación más avanzada.

* Raspberry Pi es un entorno completo, no necesita de ningún dispositivo externo para programarse.

¿Son incompatibles?: En absoluto, lo más frecuente es usarlas conjuntamente, conectándolos y haciendo que la Raspberry actúe como cerebro y Arduino como ejecutor.

Vistas las diferencias entre los dos dispositivos queda claro que son perfectamente complementarios:

* Donde uno adolece de poco cerebro, el otro aporta gran procesamiento
* Donde uno es eléctricamente débil, el otro es robusto

## Raspberry en los medios

Han sido muchas las películas y series donde han aparecido últimamente Raspberry Pi

* [Serie Mr. Robot](http://null-byte.wonderhowto.com/how-to/hacks-mr-robot-build-hacking-raspberry-pi-0163143/): lo utilizan como punto de acceso externo y para inyectar datos erróneos en el sistema de control de temperatura y así poder controlarlo.

  ![Imagen de la Serie Mr. Robot](./images/hacks-mr-robot-raspberry-reducida-45.jpg)

* CSI Cyber: lo usan como un router que les permite capturar datos de la red donde están (un parque de atracciones) y así descubren cómo poder controlar las atracciones.

  ![Imagen de la Serie CSI](./images/RaspberryPi_on_CSI-Cyber_reducida_75.jpg)

¿Conoces alguna aparición más en los medios? No dudes en contárnosla.

