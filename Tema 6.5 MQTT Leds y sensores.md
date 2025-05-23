## MQTT y python


Vamos a publicar ahora los valores de nuestros sensores usando el protocolo MQTT.

Usaremos el módulo  **paho-mqtt** que permite tanto publicar como suscribirse a topics. Lo instalamos dentro del entorno virtual correspondiente

```sh
pip3 install paho-mqtt
```

En este ejemplo en python la Raspberry Pi hace parpadear un led conectado al GPIO4 cuando recibe un mensaje con topic "client/led"

```python
#! /usr/bin/python3
import paho.mqtt.client as mqtt
from gpiozero import LED
from time import sleep
MQTT_SERVER = "192.168.1.93"
MQTT_PATH = "client/led"
led = LED(4)
def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe(MQTT_PATH)
def on_message(client, userdata, msg):
  print(msg.topic+" "+str(msg.payload.decode("utf-8")))
  led.on()
  sleep(3)
  led.off()
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, 1883, 60)
client.loop_forever()   

```

![Montaje Led](./images/5cede883c672e070280861c4,816,544.jpeg)

Podemos probarlo publicando mensajes con el topic adecuado


```sh
mosquitto_pub -h 192.168.1.93 -t "client/led" -m "Blink"
```

Con todo lo visto sería sencillo enviar y recibir datos de sensores usando MQTT

