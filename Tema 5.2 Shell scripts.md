## Programación en Shell Scripts

Los scripts son ficheros donde introducimos distintas órdenes que se irán ejecutando de forma consecutiva una tras otra.

Una excelente guía para aprender a usar la shell y sus comandos en Raspberry es el libro [Command Line V2](https://magpi.raspberrypi.com/books/command-line-second-edition)

Vamos a ver algunos ejemplos de cómo utilizarlos junto con la cámara. Para ellos usaremos algunos de los comandos que tenemos para controlarla.

### Usando la cámara

Ya vimos que el comando raspistill nos permitía crear un time lapse. Si deseamos utilizar un formato de nombre más complejo, siempre podemos usar un script como el siguiente que además guardará las imágenes en una carpeta


```sh
SAVEDIR=/var/tlcam/stills
while [ true ]; do
filename=$(date -u +"%d%m%Y_%H%M-%S").jpg
/opt/vc/bin/raspistill -o $SAVEDIR/$filename
sleep 4;
done;
```

[![Vídeo: Trabajando con Shell  Scripts Raspberry pi](https://img.youtube.com/vi/L5HfjbKyth0/0.jpg)](https://youtu.be/L5HfjbKyth0)


[Vídeo: Trabajando con Shell  Scripts Raspberry pi](https://youtu.be/L5HfjbKyth0)

Hagamos ahora un script para hacer un timelapse con una webcam:

Primero creamos un fichero con este contenido. Por ejemplo con el editor geany

```sh
geany ~/runtimelapse.sh 
``` 

El contenido será el siguiente

```sh
#!/bin/bash
# Timelapse controller for USB webcam
DIR=/home/pi/timelapse
x=1
while [ $x -le 1440 ]; do
	filename=$(date -u +"%d%m%Y_%H%M-%S").jpg
	fswebcam -d /dev/video0 -r 640x480 $DIR/$filename
	x=$(( $x + 1 ))
	sleep 10;
done;
```

Una vez guardado, vamos a darle permiso para ejecutarlo.

```sh
chmod u+x ~/runtimelapse.sh
```

Lo ejecutamos con
```sh
~/runtimelapse.sh
```

Podemos ver que se están realizando capturas de imágenes cada 10 segundos y como mucho se guardarán 1440 imágenes.

### Control remoto de cámaras

![Controlando una cámara profesional](./images/camaraPro.png)

También podemos controlar cámaras profesionales que suelen admitir conexión USB (como por ejemplo una Canon Rebel T4i / 650D)

Utilizaremos el software gphoto2 que  instalaremos con

```sh
sudo apt-get install gphoto2
```

Podemos controlar casi todos los valores de exposición, ISO, etc de nuestra cámara remotamente, pero para no complicarnos vamos a suponer que la usamos en modo automático.

Podemos capturar una imagen, que se mantendrá en la cámara con:

```sh
$ gphoto2 --capture-image
```

Para tomar una imagen y enviarla a la raspberry usaremos

```sh
$ gphoto2 --capture-image-and-download
```

La librería gphoto2 por defecto guarda las imágenes en la memoria RAM de la Raspberry (no en la SD) con lo que es necesario que lo configuremos para evitar perderlas al cortar la alimentación.

```sh
$ gphoto2 --get-config /main/settings/capturetarget
```

Para establecer nuestro almacenamiento usaremos:

```sh
$ gphoto2 --set-config /main/settings/capturetarget=NuestroDirectorio
```

Veamos ahora como hacer un time-lapse, es decir capturar las imágenes cada
cierto tiempo. Usaremos el siguiente comando.

```sh
$ gphoto2 --capture-image -F 1440 -I 30
```

Que almacenará en la cámara un máximo de 1440 imágenes tomadas cada 30
segundos

### Convertir fotos a vídeo

Una vez tengamos todas las imágenes podemos generar un vídeo con ellas.

Instalamos un software llamado mencoder que será el que genere el vídeo.

```sh
$ sudo apt-get install mencoder
```

 Ahora generamos un fichero que contenga todas las imágenes que queremos unir en el vídeo

```sh
$ cd timelapse
$ ls *.jpg* > list.txt
```


Y ejecutamos memcoder con los parámetros adecuados (es una sóla línea)

```sh
$ mencoder -nosound -ovc lavc -lavcopts vcodec=mpeg4:aspect=16/9:vbitrate=8000000 -vf scale=640:480 -o timelapse.avi -mf type=jpeg:fps=24 mf://@list.txt
```

Con esto generaremos un vídeo de 640x480 de resolución, con nombre timelapse.avi codificado en mpeg4, a 24 frame por segundo y con las imágenes cuyos nombres se incluyen en el fichero list.txt

Si queremos hacer un vídeo a partir de las imágenes tomadas con la cámara original de Raspberry usaremos el siguiente comando

```sh
$ mencoder -nosound -ovc lavc -lavcopts vcodec=mpeg4:aspect=16/9:vbitrate=8000000 -vf scale=1920:1080 -o tlcam.avi -mf type=jpeg:fps=24 mf://list.txt
```

Hay que tener cuidado de no llenar el almacenamiento, puesto que este proceso consume mucho espacio

