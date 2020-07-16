### timeLapse

El equipo estarḉa conecta vía wifi y no tendrá conectado ningún períferico, sólo la alimentación que vendrá de adaptador USB (también podemos alimentarlo desde los pines de GPIO como ya vimos)

Por ello vamos a instalar Raspberry Pi OS Lite

[![Vídeo: Montaje de una Raspberry Pi Zero W para realizar timeLapses](https://img.youtube.com/vi/rhzX1TbOddY/0.jpg)](https://www.youtube.com/watch?v=rhzX1TbOddY)


Instalamos los módulos necesarios de python

sudo apt install python3-picamera


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





TODO: Comentar el tema del espacio en disco


## acceso SSH y SCP

scp pi@raspiLapse:~/proyectos/RaspiZeroLapse/code/images/* .


### Creación del vídeo

```sh
ffmpeg -framerate 30 -r 30 -pattern_type glob -i 'image*.jpg' -c:v libx264 ajo.mp4
```





### Recursos 

https://projects.raspberrypi.org/en/projects/raspberry-pi-zero-time-lapse-cam/2


### Ejemplos

Timelapse creado con una raspberry pi Zero
Más información en https://cursoraspberrypi.es/

Licencia CC by SA by @javacasm

[![Vídeo: TimeLapse de un atardecer de tormenta](https://img.youtube.com/vi/fERbhBKDMPw/0.jpg)](https://youtu.be/fERbhBKDMPw)

[![Vídeo: Timelapse de una tarde de tormenta](https://img.youtube.com/vi/RWBErTv-6BY/0.jpg)](https://youtu.be/RWBErTv-6BY)

[![Vídeo: TimeLapse de una tarde de verano con algunas nubes](https://img.youtube.com/vi/IkCq2M1CAfQ/0.jpg)](https://youtu.be/IkCq2M1CAfQ)

[![Vídeo: TimeLapse del crecimiento de una planta de ajo](https://img.youtube.com/vi/e1enNTsTPHM/0.jpg)](https://youtu.be/e1enNTsTPHM)
 
[![Vídeo: TimeLapse del crecimiento de una planta de ajo II](https://img.youtube.com/vi/L63nfxi4e6E/0.jpg)](https://youtu.be/L63nfxi4e6E)

[![Vídeo: Time lapse del crecimiento de una planta de patata](https://img.youtube.com/vi/uhzFmH66MGE/0.jpg)](https://youtu.be/uhzFmH66MGE)
