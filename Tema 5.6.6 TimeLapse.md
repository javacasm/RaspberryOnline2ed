### Grabación de Time Lapse

Ya hemos visto un par de formas de crear Time Lapse:

* Con el comando raspistill y el **-tl**
* Usando un shell script

Ahora vamos a crearlos de una forma distinta: con Python. Para ello sólo vamos a tener que juntar algunas de las partes que ya hemos elaborado:

* Usaremos un bot de Telegram como sistema de control y de comunicaciones
* Capturaremos imágenes con la cámara controlando los parámetros para poder hacer fotos de día y de noche
* Como no necesitamos mucho procesamiento utilizaremos una Raspberry Pi Zero W conectada vía wifi y no tendrá conectado ningún periférico, sólo la alimentación que vendrá de adaptador USB (también podemos alimentarlo desde los pines de GPIO como ya vimos)

Por ello vamos a instalar Raspberry Pi OS Lite, como vimos en un capítulo anterior

### Montaje


Para conectar la cámara a la Raspberry Zero, necesitamos un cable especial que suele venir incluido con el kit.

![Cable Camara Zero vs Normal](./images/CableCamaraZeroNormal.jpg)

Lo conectamos de esta forma (ojo a la posición del cable )

![Camara Raspberry Pi Zero](./images/CamaraRaspiZero.jpg)

Y lo integramos en la caja con la tapa que tiene el hueco para la cámara.

![Raspberry Pi Zero Caja](./images/RaspiZeroCaja.jpg)

Que queda perfectamente integrada y muy compacta

![Raspberry Pi Zero Caja Cerrada](./images/RaspiZeroCajaCerrada.jpg)

Ahora sólo nos falta conectar la alimentación al usb marcado como "Power"

![Puertos de conexión](./images/RaspiZeroCajaCerradaPuertos.jpg)

Y nos queda un equipo muy, muy compacto

![Alimentación Raspberry Pi Zero](./images/RaspiZeroAlimantacion.jpg)

[![Vídeo: Montaje de una Raspberry Pi Zero W para realizar timeLapses](https://img.youtube.com/vi/rhzX1TbOddY/0.jpg)](https://drive.google.com/file/d/1Suec5Q8iQP8J25kktUA8kNM0Muf39usJ/view?usp=sharing)

[Vídeo: Montaje de una Raspberry Pi Zero W para realizar timeLapses](https://drive.google.com/file/d/1Suec5Q8iQP8J25kktUA8kNM0Muf39usJ/view?usp=sharing)

### Instalación

Ahora vamos a instalar los módulos necesarios de python

```sh
sudo apt install python3-picamera
sudo apt install python3-pip

pip3 install python-telegram
pip3 install python-telegram-bot
```

Usaremos un código basado en los anteriores ejemplos al que le hemos añadido:

* Medida de la temperatura de la CPU **/temp**
* Medida del espacio en disco **/df**
* Creamos un time lapse con el comando /TTiempoEntreImagenes, con /T0 se termina el time lapse
* Podemos establecer un modo noche **/night** y día **/day**
* Podemos tomar una foto con **/foto**
* Recuperar la última foto con **/last**

1. Descargamos el código del ejemplo [RaspiZeroLapse](https://github.com/javacasm/RaspiZeroLapse/archive/master.zip)
1. Lo descomprimimos
1. Ponemos el TOKEN que vamos a usar con este Bot en el fichero config.py
1. Añadimos el chat_id de usuario como ADMIN
1. Cambiamos el directorio donde queremos guardar las imágenes
1. Ejecutamos el bot con:

```sh
python3 timeLapseBot.py
```

Nos conectamos desde cualquier App de Telegram y lo probamos.

### Puesta en marcha de un time lapse

Una vez que lo tenemos todo listo llega el momento de conseguir un buen enfoque del objetivo que queremos fotografiar

* Si lo vamos a tener un tiempo largo, hay que conseguir que el sistema esté estable (cuidado con colocarlo en el borde la ventana).

![Montaje timelapse](./images/TimeLapseSetup.jpg)

![Otro montaje timelapse](./images/TimeLapseSetup2.jpg)

* Normalmente fijo la cámara con gomas o similar para evitar movimientos debidos al viento. También uso una carcasa impresa en 3D para la cámara con unos imanes que me permite fijarlo fácilmente

* Si el montaje es en el exterior hay que proteger a los equipos del sol y por supuesto de posibles lluvias.

* A veces uso cables extralargos para la cámara, de esta manera puedo separar más de la Raspberry.

* Una vez preparado el montaje, para ajustar el enfoque utilizo una tableta y con la app de Telegram, voy pidiéndole al bot que haga y envíe una imagen con **/foto**

* Cuando tenemos el enfoque deseado programamos el tiempo entre imágenes con **/Ttiempo**. Para el crecimiento de plantas suelo poner 120 segundos, para las capturas de amaneceres o atardeceres 30 segundos.

### Cómo recuperar las fotos

Desde el bot de telegram podemos recuperar las imágenes, pero una a una. Para descargar varias de golpe podemos usar el comando **scp** pensado para copiar ficheros entre equipos que están conectados por ssh.

Para copiar al directorio local todas las imágenes del día 7 podemos hacer:
```sh
scp pi@raspiLapse:~/proyectos/RaspiZeroLapse/code/images/image20200707-* .
```

Después de copiarlas habrá que borrarlas de la Raspberry

### Cuidados

* Cuidado con la alimentación, al usar una batería que daba poca potencia fallaba al encender/apagar la cámara.

* Si vamos a usar sólo baterías hay que medir el tiempo que estas aguantan.

* Se puede utilizar un panel solar para que recargue las baterías, pero tenemos que asegurarnos de que proporciona la energía necesaria
![Alimentación Solar](./images/AlimentacionSolar.png)

* Cuidado con llenar el almacenamiento, debemos tener en cuenta el espacio libre, el tamaño de cada foto y sobre todo el número de imágenes que vamos a tomar. Por ejemplo:
    * 1 foto ocupa 3.5Mb
    * Hacemos 1 foto cada minuto
    * 3.5Mb x 60 fotos/minuto x 24 horas = 5000 Mb/Día

* Utilizar un almacenamiento externo (pendrive o similar) o una partición distinta para guardar las imágenes. Así si se llena no se impedirá el correcto  funcionamiento del sistema.


### Creación del vídeo

Ya vimos anteriormente  cómo generar un vídeo a partir de  nuestras imágenes. En los ejemplos que os muestro he usado este comando.

```sh
ffmpeg -framerate 30 -r 30 -pattern_type glob -i 'image*.jpg' -c:v libx264 ajo.mp4
```

También hay en el código un ejemplo de cómo generar gif a partir de las imágenes. En un futuro añadiré esa funcionalidad al bot.


### Ejemplos de time lapse

Todos estos time lapses los he creado con este sistema:

[![Vídeo: TimeLapse de un atardecer de tormenta](https://img.youtube.com/vi/fERbhBKDMPw/0.jpg)](https://drive.google.com/file/d/1IjZ3fFteKNsAt-aaeCcN-R57rGL0_epD/view?usp=sharing)

[![Vídeo: Timelapse de una tarde de tormenta](https://img.youtube.com/vi/RWBErTv-6BY/0.jpg)](https://drive.google.com/file/d/1hUDYtfYeCW_zxonzhlDIn90BlemF3q72/view?usp=sharing)

[![Vídeo: TimeLapse de una tarde de verano con algunas nubes](https://img.youtube.com/vi/IkCq2M1CAfQ/0.jpg)](https://drive.google.com/file/d/1Ssi2ke90wRbvk6NrqMomsYxTwkQrbobV/view?usp=sharing)

[![Vídeo: TimeLapse del crecimiento de una planta de ajo](https://img.youtube.com/vi/e1enNTsTPHM/0.jpg)](https://drive.google.com/file/d/15RoVrNnysunFro-_uv_e_H0I4sCUukYJ/view?usp=sharing)
 
[![Vídeo: TimeLapse del crecimiento de una planta de ajo II](https://img.youtube.com/vi/L63nfxi4e6E/0.jpg)](https://drive.google.com/file/d/1Z7ZmsiUjvc7W_r3Nhj5DQTNVcu3QuS4-/view?usp=sharing)

[![Vídeo: Time lapse del crecimiento de una planta de patata](https://img.youtube.com/vi/uhzFmH66MGE/0.jpg)](https://drive.google.com/file/d/12DVjQd6_sJpJ3xiuO5a6eE7lbZGF-Xps/view?usp=sharing)

### Recursos 

Este proyecto está inspirado por [este otro creado por la Fundación Raspberry](https://projects.raspberrypi.org/en/projects/raspberry-pi-zero-time-lapse-cam/)

