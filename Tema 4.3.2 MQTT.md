## MQTT

**MQTT** es un servicio de comunicaciones entre dispositivos sencillo y ligero. Está pensado para que pueda funcionar en equipos con poca capacidad de cálculo.

Los equipos envían y reciben mensajes que está formatos por un **Topic** que es como una etiqueta con estructura arbórea y un mensaje o contenido.

Todos los participantes pueden **publicar** mensajes y/o también se pueden **suscribir** a determinados topics, de manera que reciban los mensajes con ese topic.

Utiliza una arquitectura como la que se ve en la imagen, donde el sistema central actúa como **Broker**, recibiendo los mensajes de todos los equipos y notificando a aquellos que se han suscrito a topics.

![Arquitectura MQTT](./images/MQTT_arquitectura.png)

Al ser un servicio sencillo actúa como transporte en sistemas más complejos.

Existen brokers accesibles a través de internet como por ejemplo

## Instalación en Raspberry

Instalamos servidor **mosquitto** que actúa como broker en la Raspberry:

```sh
sudo apt install mosquitto
```

Ejecutamos mosquitto 


Si queremos que se arranque como servicio al iniciar la raspberry, hacemos

```sh
sudo systemctl enable mosquitto.service
```



Para depurar el funcionamiento de mosquitto y ver los logs cuando funciona como servicio podemos usar

https://community.home-assistant.io/t/how-to-debug-mosquitto-mqtt/107709/20
http://www.steves-internet-guide.com/mosquitto-logging/
https://github.com/thomasnordquist/MQTT-Explorer

Para publicar y recibir mensajes necesitaremos las herramientas cliente, que podemos instalar con

```sh
sudo apt install mosquitto-clients
```


Podemos suscribirnos a un tema/topic con el comando 

```sh
mosquitto_sub -h servidorMQTT -t Tema
``` 

Para publicar en un "Topic" un "Mensaje" (siempre son cadenas)

```sh
mosquitto_pub -h servidorMQTT -t "Topic" -m "Mensaje"
```




## Ejemplos

Vamos a suscribirnos al topic "MeteoSalon/#", es decir a todos los mensajes que "cuelgen" del topic "MeteoSalon".
La opción **-v** es para que muestre más detalles sobre los mensajes

```sh
mosquitto_sub -h 192.168.1.200 -t "MeteoSalon/#" -v

```

y la aplicación quedará esperando hasta que se reciban mensajes con un topic compatible

Desde el mismo servidor podemos probar que funciona con la utilidad **mosquitto_pub**

```sh
mosquitto_pub -h 192.168.1.200 -t "MeteoSalon/led" -m "On"
```

En el servidor vemos la siguiente traza

```sh
1574598811: New connection from 192.168.1.200 on port 1883.
1574598811: New client connected from 192.168.1.200 as mosqpub/7375-raspberryp (c1, k60).
1574598811: Client mosqpub/7375-raspberryp disconnected.
```

y en la aplicación cliente

```sh
MeteoSalon/led On
```

### Ejemplo de arquitectura de topics

A medida que vamos añadiendo dispositivos y enviado más mensajes se puede complicar el árbol de topics

Para ellos es mejor usar una arquitectura. Por ejemplo esta [tomada del blog de ricardo veal](https://ricveal.com/blog/sonoff-mqtt/)

```sh
    state_topic: "stat/sonoff/1/POWER"
    command_topic: "cmnd/sonoff/1/POWER"
    availability_topic: "tele/sonoff/1/LWT"
```


Telemetría para que cuenten sus cosas ¿Por ejemplo los sensores?
Command para peticiones ¿request?
Stat para confirmaciones de estados




## Recursos

[Instalación de mosquito en la Raspberry)[https://randomnerdtutorials.com/how-to-install-mosquitto-broker-on-raspberry-pi/]

https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266

https://geekytheory.com/tutorial-raspberry-pi-gpio-y-mqtt-parte-1
