## Sense Hat

![](sensehat.png)

[Sense Hat](https://www.raspberrypi.org/products/sense-hat/) es un "sombrero" pensado para el aprendizaje de la programación y la electrónica y que contiene: 
* "Pantalla" de 64 leds RGB 
* Barómetro
* Termómetro
* Higrómetro
* Acelerómetro
* Giróscopo
* Magnetómetro
* Sensor de color
* Sensor de brillo
* Joystick de 5 pulsadores

Fue desarrollado por la fundación Raspberry Pi junto con la ESA (Agencia Espacial Europea) y desde su creación ha existido la competición [Astro Pi](https://astro-pi.org/)  

Puedes encontrar más detalles en su [documentación oficial](https://datasheets.raspberrypi.com/sense-hat/sense-hat-product-brief.pdf) cuyos participantes pueden ver sus programas ejecutarse en Rasperry que los astronautas usan en la ISS (Estación Espacial Internacional)

Si no tienes una placa SenseHat puedes usar el simulador
[Simulando el Sense Hat](https://www.raspberrypi.org/blog/sense-hat-emulator/)



### Programando Sense Hat con Scratch

Podemos programar la placa Sense Hat desde Scratch. Para ello necesitamos incluir en nuestro proyecto la extensión "Raspberry Pi Sense Hat"

![](sensehat_scratch_extension.png)

Una vez incluida la extensión, tendremos acceso a bloques para controlar los leds, pudiendo mostrar letras y texto y enciendo los leds con los colores que queramos.



![](sensehat-scratch.png)

También podemos mostrar los valores de los distintos sensores y detectar los eventos causados al pulsar el joystick en alguna de las direcciones o por los cambios de posición detectados por el acelerómetro:

![](scratch_sensehat_sensores.png)

### Programando Sense Hat con Python

Para programar Sense Hat con Python, tenemos que instalar el módulo "sense-hat". Lo haremos con:

```python
sudo apt update
sudo apt install sense-hat
sudo reboot
```

Una vez instalado podemos comenzar a programarlo siguiendo las indicaciones de su [documentación](https://pythonhosted.org/sense-hat/) y sus [ejemplos](https://github.com/astro-pi/python-sense-hat/tree/master/docs/examples). Por ejemplo nuestro "Hola Mundo" será:

```python
from sense_hat import SenseHat

sense = SenseHat()

sense.show_message("Hola mundo!")
```

Para poner todos los leds de un mismo color

```python

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

def set_color(color):

    for x in range(8):
        for y in range(8)
            sense.set_pixel(x,y,color)

BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (150,0,0)
VERDE = (0,150,0)
AZUL = (0,0,150)

colores = [BLANCO,ROJO, VERDE, AZUL, NEGRO]

for color in colores:
	set_color()
	sleep(1)
```
### Varios



Sensores

Ver lo que pone la Guia de la Raspi400

Libro SenseHat

[Usando un cable para conectar Sense Hat a Raspberry 400](https://www.dominicsayers.com/sense-hat/)
