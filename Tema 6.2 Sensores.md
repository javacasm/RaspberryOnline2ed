## Sensores

Veamos cómo podemos conectar sensores de temperatura digitales como el DS18x20 o el DHT11

### DS18x20

Este sensor de aspecto idéntico a un transistor nos permite medir fácilmente la temperatura con un montaje mínimo:

![Montaje DS18x20](./images/oneWireDS18x20.png)

Necesitamos una resistencia de 4.7 ohmios que actuará como pull-up en el montaje.

Por defecto el driver de one-wire us el GPIO04, pero si necesitamos cambiarlo podemos hacerlo modificando en el fichero /boot/config.txt la línea 'dtoverlay=w1-gpio,gpiopin=x'

Para poder usarlo tenemos que activar en la configuración el acceso al protocolo OneWire que usa este sensor. Para ello entramos en configuración con 

```sh
sudo raspi-config
```
Y en la opción "Interfacing" activamos "one-wire interface"

![one-wire config](./images/one-wire_config.png)

y reiniciamos para que se activen los cambios.

Instalamos el módulo python **w1thermsensor** dentro del correspondiente entorno virtual con 

```sh
pip3 install w1thermsensor
```
Un sencillo programa nos permite ver el valor de temperatura cada segundo

```python
import time

from w1thermsensor import W1ThermSensor # importamos la librería
sensor = W1ThermSensor()

while True:
    temperature = sensor.get_temperature()
    print(' Temperatura {}º'.format(temperature))
    time.sleep(1) 
```

[Código](https://github.com/javacasm/RaspberryOnline2ed/blob/master/codigo/test_ds18x20.py)

### Sensores de temperatura y humedad DHT: DHT22

Vamos a hacer ahora un montaje con un conocido sensor de humedad y temperatura como es el DHT22. Lo mismo sería aplicable a su hermano pequeño el DHT11

![DHT11 y DHT22](./images/DHT11_DHT22.png)

Vamos a hacerlo usando un módulo específico que existe para [este sensor](https://github.com/adafruit/Adafruit_Python_DHT) 

El montaje es muy sencillo (tomado de la [página de "el atareao"](https://www.atareao.es/podcast/temperatura-con-la-raspberry/)), donde se incluye una resistencia de 10K en modo pull-up, que pondremos si usamos el sensor directamente. En el caso de que utilicemos un módulo con un pcb con el sensor DHT22 soldado en ella no será necesaria la resistencia si este la lleva incorporada.

![Montaje DHT22](./images/montajeDHT22.png)

Podrías usar las librerías de Adafruit para los sensores DHT, pero desde hace tiempo [desaconseja el uso de estos sensores](https://learn.adafruit.com/modern-replacements-for-dht11-dht22-sensors)

También podíamos haber aprovechado para hacer este montaje usando [CiruitPython](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/overview) que es una variante de Micropython (la versión de python para microcontroladores), creada por Adafruit, que ha añadido objetos de más alto nivel como motor, sensor, etc.. El problema es que es una instalación bastante pesada donde instalamos mucho más de lo que necesitamos. No obstante si quieres seguir por ahí, puedes seguir [este tutorial](https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup)

Nosotros vamos a usar una versión más sencilla con el módulo Python `gpiod`

Para ello necesitamos asegurarnos que tenemos instalado y funcionando el servicio `pigpiod`. Desde una consola hacemos los siguiente

```sh
sudo apt update sudo apt install pigpio python3-pigpio
```

Y habilitamos y activamos el servicio `pigpiod` con

```sh
sudo systemctl enable pigpiod 
sudo systemctl start pigpiod
```

Ahora, desde nuestro entorno virtual de python para gpio instalamos el módulo `pigpio-dht`con

```sh
pip3 install pigpio-dht
```

El [programa](https://github.com/javacasm/RaspberryOnline2ed/blob/master/codigo/test_dht22_pigpiod) no puede ser más sencillo

```python
import time
from pigpio_dht import DHT22

# Conecta el sensor en GPIO4
sensor = DHT22(4)

try:
    while True:
        result = sensor.read()
        if result['valid']:
            print(f"Temperatura: {result['temp_c']:.1f}°C")
            print(f"Humedad: {result['humidity']:.1f}%")
        else:
            print("Error al leer el sensor")
        time.sleep(2)
except KeyboardInterrupt:
    print("\nPrograma terminado")
```


