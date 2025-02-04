## Cámaras

Vamos a ver las distintas cámaras para Raspberry Pi. Existen varios modelos  creados por la Fundación Raspberry Pi y otros fabricantes, pero todos son compatibles con el mismo cable y conector.

Para optimizar el rendimiento, está conectada directamente a la GPU, así no ocupa tiempo de procesamiento de la CPU.

Veamos los distintos modelos:

| Modelo  | MegaPixels | Resolución | Sensor            | Tamaño de Sensor | Precio          | Versiones           |
| ------- | ---------- | ---------- | ----------------- | ---------------- | --------------- | ------------------- |
| v1.3    | 5MP        | 2592x1944  | OV5647            | 3.76x2.74mm      | 15€             | Filtro IR y NOIR    |
| v2.1    | 8MP        | 3280x2464  | Sony IMX219       | 3.68x2.76mm      | 25€             | Filtro IR y NOIR    |
| HQ      | 12MP       | 4056x3040  | Sony IMX477       | 6.287x4.712mm    | 59€ + objetivos | Filtro IR           |
| Shutter | 1.6MP      |            | Sony IMX296       | 6,3mm diagonal   | 56,95€          | Obturador preciso   |
| v3      | 12MP       | 4608×2592  | IMX708 Quad Bayer | 7.4mm diagonal   | 29,95€          | Normal o Panorámica |
| IA      | 12.3MP     | 4056×3040  | Sony’s IMX500     | 7.86mm diagonal  | 75,95€          | IA                  |

### Cámaras v1.3 y v2.1

Las versiones v1.3 y v2.1 son muy parecidas. Se trata de cámaras con foco fijo en las que se ha cambiado el modelo de sensor y la resolución. 

| ![Cámara v1.3](./images/RaspiCamera_v1.3_reducida_250.jpg) | ![Cámara v2.1](./images/RaspiCamera_v2_reducida_250.jpg) |
| ---------------------------------------------------------- | -------------------------------------------------------- |
| Cámara v1.3                                                | Cámara v2.1                                              |

Ambas se pueden encontrar en la versión normal con filtro IR (infrarrojo), y la NOIR sin filtro IR,  preparada para una mejor visión nocturna.

![Pi camera NOIR v2.1](./images/pi-camera-noir-front-1227x1080_reducida_200.jpg)

La v1.3, ya está descatalogada pero se puede encontrar en versiones compatibles. Podemos comprar la versión v2, tanto en su [versión IR](https://www.raspberrypi.com/products/camera-module-v2/) como en la versión [NOIR](https://www.raspberrypi.com/products/pi-noir-camera-v2/)

### Cámara HQ

También existe la cámara de alta calidad [HQ Camera](https://www.raspberrypi.com/products/raspberry-pi-high-quality-camera/) 

![Cámara y objetivos HQ](./images/HQ_KIT_reducida_400.jpg)

La cámara HQ amplía la resolución hasta los 12MP, usando además, un sensor de mayor tamaño. El sensor incluye soporte compatible con trípode estándar.

![Cámara HQ](./images/CAM+HERO+ALT+2_reducida_350.jpg)

El disponer de una montura de tipo  C y CS, añade un mundo de posibilidades al poder usar distintos objetivos. De momento están disponibles los de 6mm y 16mm, pero al ser una montura estándar, se podrán incorporar otros objetivos.

![Objetivo 6mm cámara HQ](./images/Raspberry-Pi-HQ-Camera-6mm-Lens_reducida_300.jpg)

![Objetivo 16mm](./images/15882390111_reducida_300.jpg)

### Cámara Global Shutter

La cámara Global Shutter es una versión parecida físicamente a la HQ en cuanto a la montura y a la capacidad de usar objetivos C/CS. Cuenta con 1.6MP y con la característica de obturador global orientado a obtener imágenes en movimiento con alta calidad. 

![Cámara Shutter](./images/Camara_Shutter_reducida_250.png)

Mientras que las cámaras normales van capturando las imágenes línea a línea, esta cámara toma toda la imagen de una vez. Esto evita el que se produzcan "artifacts" (defectos) al capturar imágenes de objetos que se mueven rápidamente, como en el siguiente ejemplo de imagen de la hélice de un avión, generada por la forma de capturar las imágenes en las cámaras normales línea a líneas. La hélice se va moviendo a medida que se van capturando las sucesivas líneas.

![Artefactos visuales debidos al movimiento](./images/plane_blade_artifacts_reducida_300.jpg)

Al tomar la imagen de una sola vez se eliminan estos problemas.

### Cámara v3

La última versión hasta ahora, de la cámara es la _v3_.

![](./images/Cámara%20v3_reducida_500.jpg)

Incluye autofocus, lo que consigue unos mejores resultados en cuanto a nitidez. Además podemos controlar el modo de enfoque por programa. Podemos elegir entre 2 modelos, el normal de 70º de amplitud y el panorámico (ultra-wide field) de 120º.

Esta cámara no está pensada sólo para fotografía estáticas, si no que es capaz de  capturar vídeo en calidad HD a 50fps. Además permite activar el modo HDR, para mejorar el contraste dinámicamente y el autofocus, para obtener vídeo con un enfoque perfecto.

Puedes ver más detalles e incluso ejemplos de grabación con esta cámara en la [página del producto](https://www.raspberrypi.com/products/camera-module-3/).

### Cámara IA

![Cámara con procesamiento IA incluida](./images/camara_ia_reducida_200.jpg)

Recientemente ha aparecido una  cámara que incluye el sensor IMX500 de Sony dotado de visión artificial, es decir, el propio sensor ya es capaz de hacer procesamiento de imágenes sin necesidad de que intervenga el procesador de la Raspberry Pi. Es completamente compatible con todas las cámaras anteriores.

La cámara incluye un procesador capaz de utilizar el modelo de red neural que le carguemos para realizar el procesamiento en tiempo real de las imágenes. Se ha hecho un trabajo muy completo para facilitar enormemente el uso de diversos modelos y el obtener resultados rápidamente.

Puedes ver más detalles en la página de la [cámara IA](https://www.raspberrypi.com/products/ai-camera/) y en la [documentación de uso](https://www.raspberrypi.com/documentation/accessories/ai-camera.html).

Resumiendo, a día de hoy (octubre de 2024), salvo que te interese trabajar con objetivos, o necesites capturar imágenes con movimientos muy rápidos, las alternativas son la V3 y la cámara AI. Las dos tienen un diseño muy parecido con tamaños similares pero cada una apunta a usuarios muy distintos: mientras la V3 va orientada a proyectos simples de tipo hobby, la IA se orienta a aplicaciones más avanzadas donde se busca el uso de modelo neuronales y la detección de objetos en tiempo real.

### Cámaras compatibles

Como los conectores de la cámara son estándar, hay muchos fabricantes que venden modelos totalmente compatibles, como estos modelos nocturnos, algunos de ellos, con lentes ajustables manualmente.

![Cámara Noir con focos IR](./images/pi_cam_3.6mm_600x450-600x600_reducida_350.jpg)

![Cámara Noir con lente de 3.6mm](./images/camara-para-raspberry-pi-5mpx-foco-manual-noir_reducida_250.jpg)

También podemos comprar la cámara y conectarla al módulo directamente:

![Mini cámara IMX219](./images/Mini-c-mara-IMX219-m-dulo-de-c-mara-para-la-placa-oficial-de-c-mara_reducida_250.jpg)


[Datos sobre las distintas versiones](https://www.raspberrypi.com/documentation/accessories/camera.html). Más detalles sobre el hardware de las cámaras en [post asociado](https://dronebotworkshop.com/pi-cameras/) y en [este vídeo](https://www.youtube.com/watch?v=MVgr302PNwY).

### Conectando la cámara

Todos los modelos, hasta la Raspberry Pi 5, usan el mismo conector para la cámara y se conectan de la misma forma.

![Cámara de Raspberry Pi](./images/camara_reducida_300.jpg)

La cámara tiene su propio conector, junto al conector HDMI.

Para conectarla, pondremos el cable plano de la manera que se ve en la imagen inferior (la cinta azul del cable indica la orientación), y por supuesto, con la Raspberry Pi apagada sin alimentación.

![Cable de la Cámara](./images/Pi-camera-Socket_reducida_400.jpg)

En la Raspberry Pi 5, tenemos la posibilidad de conectar 2 cámaras al mismo tiempo, para lo que tenemos 2 conectores pero de un tamaño más reducido, por lo que necesitaremos un cable diferente. En la imagen se ha insertado parcialmente uno de los cables pero falta cerrar el conector para fijar el cable, una vez que esté insertado.

![Conector para la cámara en Raspberry Pi 5](./images/conector_camara_rapi5_reducida_450.jpg)


Podemos ver si se detectan las cámaras haciendo:

```sh
libcamera-hello --list-cameras
```

Éste comando nos dirá las cámaras que ha detectado, si tenemos 2 cámaras conectadas deberíamos verlas, identificadas con el número 0 y 1. 

![Salida del comando listcamera_hello --list-cameras](./images/4.2.0_list_cameras.png)

Vemos que la cámara 0 es un modelo v2.1 con el chip imx219 y la cámara 1 es un modelo v3 con el chip imx708. Además vemos que la 1 tiene mayor resolución

Para referirnos a una de ellas, usaremos ese número, por ejemplo, para usar la cámara 0, usaremos:

```sh
libcamera-hello --camera 0
```

que nos mostrará una previsualización durante 5 segundos de la cámara 0 y luego, se cerrará. 

Si hacemos:

```sh
libcamera-hello -t 0
```

La pantalla de previsualización se mostrará indefinidamente, hasta que pulsemos el botón de cerrar de la ventana.

Para capturar una imagen que guardaremos con el nombre 'imagen.jpg' usaremos:

```sh
libcamera-jpeg -o imagen.jpg
``` 

Por ejemplo, para capturar una imagen tras esperar 10 segundos con resolución 1920x1080 haremos:

```sh
libcamera-jpeg -o test_1920x1080.jpg -t 10000 --width 1920 --height 1080
```
Existe un comando más avanzado (similar al antiguo raspistill): **libcamera-still**

```sh
libcamera-still -o test.jpg
```

También podemos guardarlo en otros formatos como _png_ con la opción '-e png'

```sh
libcamera-still -e png -o test.png
```

Este comando tiene multitud de opciones, que podemos consultar en [su documentación](https://www.raspberrypi.com/documentation/accessories/camera.html#libcamera-still)

También se puede capturar en formato RAW (el formato más profesional que no comprime ni modifica la imagen), con la opción '-r', que se guardará en forma DNG (Adobe Digital Negative)

Para capturar vídeo usaremos el comando libcamera-vid:

```sh
libcamera-vid -t 10000 -o test.h264
```

Capturará un vídeo en formato h264 (también puede ser formato mjpeg o yuv420) durante 10 segundos y lo guardará en el fichero test.h264

También podemos usarlo para hacer un streaming de vídeo con este comando:

```sh
libcamera-vid -t 0 --inline --listen -o tcp://0.0.0.0:8888
```

Podemos ver todas las opciones en [su documentación](https://www.raspberrypi.com/documentation/accessories/camera.html#libcamera-vid)


### Uso de cámaras Webcam

También podemos usar cámaras USB compatibles  como  la PS3 Eye.

Veremos si se ha detectado con:

```sh
$ ls -l /dev/video*
```

Si se detecta:

![Camara USB detectada](./images/webcamdetected.png)

Instalamos fswebcam:

```sh
sudo apt-get install fswebcam
```

Que nos permitirá tomar una imagen con:

```sh
fswebcam -d /dev/video0 -r 640x480 test.jpeg
```
