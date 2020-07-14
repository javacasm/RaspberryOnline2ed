## Programación en Shell Scripts

Los scripts son ficheros donde introducimos distintas órdenes que se irán ejecutando de forma consecutiva una tras otra.

Vamos a ver algunos ejemplos de cómo utilizarlos junto con la cámara. Para ellos usaremos algunos de los comandos que tenemos para usar la cámara.

### Usando la cámara

Existen varios modelos creados por la Fundación Raspberry y otros compatibles

|Modelo|MegaPixels|Precio|Información|
|---|---|---|---
|v1.3|5MP|15|Modelo estándar
|noir|5MP|15|Optimizada para ver en la oscuridad
|v2|8MP|25| Nueva versión con más resolución
|HD|12MP|25 + objetivos|[Descripción](https://www.raspipc.es/public/docs/RPIHQCameraRaspiPC.pdf) [Producto](https://www.adafruit.com/product/4561) [Infor](https://www.raspberrypi.org/blog/new-product-raspberry-pi-high-quality-camera-on-sale-now-at-50/)

Todos los modelos usan el mismo conector y se conectan de la misma forma

Empezaremos conectando la cámara

![Camara de Raspberry Pi](./images/camara.jpg)

La cámara tiene su propio conector, junto al conector HDMI

Para conectarla pondremos el cable de la manera que se ve en la imagen

![Cable de la Cámara](./images/Pi-camera-Socket.jpg)


Antes de poder utilizarla tenemos que activarla

```sh
sudo raspi-config
```
En el menú de "Interfacing Options"

![Configuración para activar la cámara](./images/activaCamara.png)

Necesitamos reiniciar para que arranquen adecuadamente los drivers.

Podemos probarla con este comando

```sh
raspistill -v -o test.jpg
```        

Que mostrará lo que enfoca la cámara durante 5 segundos y luego guardará una imagen en el fichero test.jpg


Tenemos 2 aplicaciones para usar la cámara

```sh
raspistill
```

Tomará imágenes fijas

```sh
raspivid
```

grabará un vídeo

### Imágenes estáticas

Si queremos cambiar el retardo con el se captura, usamos la opción -t indicando el tiempo en milisegundos:

```sh
raspistill -o myimage.jpg -t 3000
```

Este programa tiene muchas opciones que podemos ver con "raspistill --help | less"

```sh

"raspistill" Camera App (commit 6e6a2c859a17 Tainted)

Runs camera for specific time, and take JPG capture at end if requested

usage: raspistill [options]

Image parameter commands

-q, --quality	: Set jpeg quality <0 to 100>
-r, --raw	: Add raw bayer data to jpeg metadata
-l, --latest	: Link latest complete image to filename <filename>
-t, --timeout	: Time (in ms) before takes picture and shuts down (if not specified, set to 5s)
-th, --thumb	: Set thumbnail parameters (x:y:quality) or none
-d, --demo	: Run a demo mode (cycle through range of camera options, no capture)
-e, --encoding	: Encoding to use for output file (jpg, bmp, gif, png)
-x, --exif	: EXIF tag to apply to captures (format as 'key=value') or none
-tl, --timelapse	: Timelapse mode. Takes a picture every <t>ms. %d == frame number (Try: -o img_%04d.jpg)
-fp, --fullpreview	: Run the preview using the still capture resolution (may reduce preview fps)
-k, --keypress	: Wait between captures for a ENTER, X then ENTER to exit
-s, --signal	: Wait between captures for a SIGUSR1 or SIGUSR2 from another process
-g, --gl	: Draw preview to texture instead of using video render component
-gc, --glcapture	: Capture the GL frame-buffer instead of the camera image
-bm, --burst	: Enable 'burst capture mode'
-dt, --datetime	: Replace output pattern (%d) with DateTime (MonthDayHourMinSec)
-ts, --timestamp	: Replace output pattern (%d) with unix timestamp (seconds since 1970)
-fs, --framestart	: Starting frame number in output pattern(%d)
-rs, --restart	: JPEG Restart interval (default of 0 for none)

GL parameter commands

-gs, --glscene	: GL scene square,teapot,mirror,yuv,sobel,vcsm_square
-gw, --glwin	: GL window settings <'x,y,w,h'>

Common Settings commands

-?, --help	: This help information
-w, --width	: Set image width <size>
-h, --height	: Set image height <size>
-o, --output	: Output filename <filename> (to write to stdout, use '-o -'). If not specified, no file is saved
-v, --verbose	: Output verbose information during run
-cs, --camselect	: Select camera <number>. Default 0
-md, --mode	: Force sensor mode. 0=auto. See docs for other modes available
-gps, --gpsdexif	: Apply real-time GPS information to output (e.g. EXIF in JPG, annotation in video (requires libgps.so.23)

Preview parameter commands

-p, --preview	: Preview window settings <'x,y,w,h'>
-f, --fullscreen	: Fullscreen preview mode
-op, --opacity	: Preview window opacity (0-255)
-n, --nopreview	: Do not display a preview window
-dn, --dispnum	: Display on which to display the preview window (dispmanx/tvservice numbering)

Image parameter commands

-sh, --sharpness	: Set image sharpness (-100 to 100)
-co, --contrast	: Set image contrast (-100 to 100)
-br, --brightness	: Set image brightness (0 to 100)
-sa, --saturation	: Set image saturation (-100 to 100)
-ISO, --ISO	: Set capture ISO
-vs, --vstab	: Turn on video stabilisation
-ev, --ev	: Set EV compensation - steps of 1/6 stop
-ex, --exposure	: Set exposure mode (see Notes)
-fli, --flicker	: Set flicker avoid mode (see Notes)
-awb, --awb	: Set AWB mode (see Notes)
-ifx, --imxfx	: Set image effect (see Notes)
-cfx, --colfx	: Set colour effect (U:V)
-mm, --metering	: Set metering mode (see Notes)
-rot, --rotation	: Set image rotation (0-359)
-hf, --hflip	: Set horizontal flip
-vf, --vflip	: Set vertical flip
-roi, --roi	: Set region of interest (x,y,w,d as normalised coordinates [0.0-1.0])
-ss, --shutter	: Set shutter speed in microseconds
-awbg, --awbgains	: Set AWB gains - AWB mode must be off
-drc, --drc	: Set DRC Level (see Notes)
-st, --stats	: Force recomputation of statistics on stills capture pass
-a, --annotate	: Enable/Set annotate flags or text
-3d, --stereo	: Select stereoscopic mode
-dec, --decimate	: Half width/height of stereo image
-3dswap, --3dswap	: Swap camera order for stereoscopic
-ae, --annotateex	: Set extra annotation parameters (text size, text colour(hex YUV), bg colour(hex YUV), justify, x, y)
-ag, --analoggain	: Set the analog gain (floating point)
-dg, --digitalgain	: Set the digital gain (floating point)
-set, --settings	: Retrieve camera settings and write to stdout


Notes

Exposure mode options :
off,auto,night,nightpreview,backlight,spotlight,sports,snow,beach,verylong,fixedfps,antishake,fireworks

Flicker avoid mode options :
off,auto,50hz,60hz

AWB mode options :
off,auto,sun,cloud,shade,tungsten,fluorescent,incandescent,flash,horizon,greyworld

Image Effect mode options :
none,negative,solarise,sketch,denoise,emboss,oilpaint,hatch,gpen,pastel,watercolour,film,blur,saturation,colourswap,washedout,posterise,colourpoint,colourbalance,cartoon

Metering Mode options :
average,spot,backlit,matrix

Dynamic Range Compression (DRC) options :
off,low,med,high
```
Entre estas opciones podemos encontrar **-tl** que nos va a permitir tomar una imagen cada cierto tiempo. Con ello podemos generar una secuencia de imágenes con una sola línea de comando

```sh
raspistill -o myimage_%d.jpg -tl 2000 -t 25000
```

Una imagen cada 2 segundos durante 25 segundos Cada foto tendrá un número de secuencia

```sh
myimage_1.jpg
myimage_2.jpg
myimage_3.jpg
myimage_4.jpg
...
```

Si deseamos utilizar un formato de nombre más complejo, siempre podemos usar un script como el siguiente que además guardará las imágenes en una carpeta

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

### Vídeo

El comando **raspivid**  nos va a permitir grabar vídeos. Para capturar 5s de vídeo en formato h264 utilizaremos:

```sh
raspivid -o video.h264
```

Si queremos capturar 10 segundos usaremos:

```sh
raspivid -o video.h264 -t 10000
```

Para ver todas las opciones disponibles podemos hacer

```sh
$raspivid | less
```

Para una documentación más detallada sobre las opciones del ejecutable se puede consultar el siguiente [enlace](https://www.raspberrypi.org/documentation/raspbian/applications/camera.md)

### Webcam

También podemos usar cámaras USB compatibles  como  la PS3 Eye.

Veremos si se ha detectado con:

```sh
$ ls -l /dev/video*
```

Si se detecta

![Camara USB detectada](./images/webcamdetected.png)

Instalamos fswebcam

```sh
sudo apt-get install fswebcam
```

Que nos permitirá tomar una imagen con

```sh
fswebcam -d /dev/video0 -r 640x480 test.jpeg
```

Hagamos ahora un script para hacer un timelapse, que nos es otra cosa que un programa que ejecuta comandos de una forma determinada.

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

