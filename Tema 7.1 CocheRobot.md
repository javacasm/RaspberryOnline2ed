# Robotica

![Robot con Raspberry](./images/RobotTop.jpg)

### Motores y servos

A veces no interesa controlar varios motores y servos desde una misma placa. 


## Controlando motores

[Tutorial básico de motores](https://projects.raspberrypi.org/en/projects/physical-computing/14)

## Placa Adafruit

[Producto](https://www.adafruit.com/product/2348)

![Placa](https://cdn-shop.adafruit.com/970x728/2348-06.jpg)

![adafruit_products_raspi_motor_hat_dc_m1_bb.jpg](./images/adafruit_products_raspi_motor_hat_dc_m1_bb.jpg)

## Sensor de distancia (ultrasonidos)

![Montaje sensor ultrasonidos](https://projects-static.raspberrypi.org/projects/physical-computing/225a16929b40a969453040649df87044fc67e670/en/images/wiring-uds.png)



```python
# Test de sensor de distancia con ultrasonidos

from gpiozero import DistanceSensor
ultrasonic = DistanceSensor(echo=17, trigger=4)
ultrasonic.max_distance = 2
while True:
    print(ultrasonic.distance)

```

[Tutorial de sensor de distancia con ultrasonidos](https://projects.raspberrypi.org/en/projects/physical-computing/12)

## Referencias

[Tutorial placa adafruit](https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi?view=all)

### Robot con placa adafruit

[Robot sencillo con placa adafruit](https://learn.adafruit.com/simple-raspberry-pi-robot?view=all)


### Robot sencillo

![Robot sencillo con video](https://hackster.imgix.net/uploads/attachments/376456/img_20171108_192721_aAocqmt3yt.jpg?auto=compress%2Cformat&w=900&h=675&fit=min)


[Raspberry Pi Web-controlled Robot with video](https://www.hackster.io/jrance/raspberry-pi-web-controlled-robot-with-video-c1b723)


### Pi Wars 2018

![](http://www.piandchips.co.uk/wp-content/uploads/2018/04/IMG_66491-300x225.jpg)

[Pi Wars 2018](http://www.piandchips.co.uk/uncategorized/pi-wars-2018-the-evolution-of-x-bot-360/)


### Robot controlado con Raspberry

* Elegoo con arduino controlado por comandos
* robot controlado electricamente: 
    * cámara con streaming
    * sensor ultrasonidos 
    * 4 motores 
    * baterias
    * Sensor atmosférico
    * Publica los datos en su web que tambien permite controlar el movimiento

### Equipo

* Raspberry Pi 2
* Adaptador wifi usb
* Battery Shield TODO:Buscar enlace. La principal caracter'isticas es que carga mientras funciona. Sorprendemente muchos powerbank no lo hacen
* Motor shield de Adafruit
* 4 motores TT
* 3 sensores ultrasonidos
* Camara Raspberry v1.3
* Caja para 2 x 18650 para los motores
* ¿USB de almacenamiento?

### Instalación

Instalamos la versión mínima de Raspberry Pi OS, pero con escritorio para poder luego hacer pruebas con la cámara más fácilmente.

Ahora conectamos un teclado, ratón y monitor  para una primera configuración:
* Idioma
* Zona horaria
* Conexión al wifi: 
    * Configuración del punto móvil del wifi que usaremos
    * Configuración del wifi local
* Activamos: SSH. VNC, Cámara, I2C, SPI, UART, OneWire
* Actualización
 

### Conexion remota

Creamos una red wifi, preferiblemente con el móvil para poder acceder a internet al mismo tiempo, a la previamente hemos conectado raspicar para que se conecte cuando esté visible

vemos la ip del portátil o del móvil, imaginemos que es 192.168.43.134 y a partir de ella hacemos
```sh
sudo nmap -sP 192.168.43.0-254
```
Así veremos las ips de los otros dispositivos conectados

```

Starting Nmap 7.60 ( https://nmap.org ) at 2020-07-20 16:50 CEST
Nmap scan report for _gateway (192.168.43.1)
Host is up (0.049s latency).
MAC Address: 78:02:F8:24:9C:88 (Xiaomi Communications)
Nmap scan report for raspicar (192.168.43.248)
Host is up (0.054s latency).
MAC Address: 44:33:4C:6E:09:AC (Shenzhen Bilian electronic)
Nmap scan report for toshibaL (192.168.43.237)
Host is up.
Nmap done: 255 IP addresses (3 hosts up) scanned in 3.54 seconds
```

Ya tenemos la IP de raspicar 192.168.43.248 y ya nos podemos conectar con ssh o con vnc sin problema


### Preparando el entorno

* Creamos las claves rsa
* Puesto  que vamos a trabajar directamente en la raspberry, las incluimos en github
* Clonamos el repositorio base 
* creamos uno nuevo desde el que partir
* instalamos modulos
pip3 install python-telegram-bot


## Versiones

V0: robot standar con movimiento normales
V1: añadimos camara y sensores de ultrasonidos
V2: añadimos ruedas onmi
V3: sensores de temperatura y bateria (I2C)
