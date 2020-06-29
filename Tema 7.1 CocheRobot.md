# Robotica

![Robot con Raspberry](./images/RobotTop.jpg)


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