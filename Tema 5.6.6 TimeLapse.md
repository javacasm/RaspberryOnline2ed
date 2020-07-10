### timeLapse

El equipo estarḉa conecta vía wifi y no tendrá conectado ningún períferico, sólo la alimentación que vendrá de adaptador USB (también podemos alimentarlo desde los pines de GPIO como ya vimos)

Por ello vamos a instalar Raspberry Pi OS Lite


scp para copiar fotos

scp pi@raspiLapse:~/proyectos/RaspiZeroLapse/code/images/image20200707-10*


TODO: MOVER AL APARTADO CORRESPONDIENTE

![CableCamaraZeroNormal.jpg](./images/CableCamaraZeroNormal.jpg)

![CamaraRaspiZerojpg](./images/CamaraRaspiZero.jpg)

![RaspiZeroCaja.jpg](./images/RaspiZeroCaja.jpg)

![RaspiZeroCajaCerrada.jpg](./images/RaspiZeroCajaCerrada.jpg)

![RaspiZeroCajaCerradaPuertos.jpg](./images/RaspiZeroCajaCerradaPuertos.jpg)

![RaspiZeroAlimantacion.jpg](./images/RaspiZeroAlimantacion.jpg)

https://projects.raspberrypi.org/en/projects/raspberry-pi-zero-time-lapse-cam/2


Cuidado con la alimentación, al usa una batería que daba poca potencia fallaba al encender/apagar la cámara

![Montaje timelapse](./images/TimeLapseSetup.jpg)


```bash
sudo apt install python3-pip

pip3 install python-telegram
pip3 install python-telegram-bot

```





## acceso SSH y SCP

scp pi@raspiLapse:~/proyectos/RaspiZeroLapse/code/images/* .


