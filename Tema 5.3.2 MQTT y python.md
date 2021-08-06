## MQTT y python

Vamos a ver cómo integrar MQTT en nuestros proyectos

Usaremos el módulo  **paho-mqtt** que permite tanto publicar como suscribirse a topics. Lo instalamos

```sh
sudo pip3 install paho-mqtt
```

Y lo podemos probar con [ejemplo sencillo como este](https://github.com/javacasm/RaspberryOnline2ed/raw/master/codigo/testMQTT.py):

Tendremos que poner la ip de nuestra Raspberry sustituyendo la que aparece en el codigo, donde usamos "192.168.1.200"

```python
import paho.mqtt.client as mqtt # Importamos  MQTT library
import time # The time library is useful for delays
import datetime

v = '1.0'

IP_RASPBERRY = "192.168.1.200"

# Se llamará a esta función cada vez que nos llegue un mensaje
def messageFunction (client, userdata, message):
    topic = str(message.topic)
    message = str(message.payload.decode("utf-8"))
    print(str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S.%f "))+ topic + message)

ourClient = mqtt.Client("NuestroClienteDeEjemplo") # Creamos un cliente y le damos un id
ourClient.connect(IP_RASPBERRY, 1883) # IP del servidor MQTT
ourClient.subscribe("MeteoSalon/#") # Nos suscribimos a todos los topic que empiecen por MeteoSalon
ourClient.on_message = messageFunction # Funciń a la que se llamará cuando llegue un mensaje
ourClient.loop_start() # Arrancamos el cliente

# Main program loop
last_pub = int(round(time.time() * 1000))
while(1):
    now = int(round(time.time() * 1000))
    if (now - last_pub) > 30000: # Revisamos cada 30 segundos 
        ourClient.publish("MeteoSalon/Test", "Just Testing") # Publicamos un mensaje de teste
        last_pub = now
    time.sleep(0.1) # Esperamos 1 segundo
```

Podemos usar nuestra instancia de mosquitto y las herramientas cliente para probar su funcionamiento.
