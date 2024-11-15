## Python y la cámara

En un capítulo anterior vimos cómo conectar y configurar la cámara

Veamos un par de sencillos ejemplos sobre cómo utilizar la cámara de python

Seguiremos las indicaciones del [manual de la cámara Pycamera2](https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf)

Instalamos la librería picamera2 para Python

```sh
sudo apt install -y python3-picamera2
```

Una vez instalado podemos hacer un sencillo ejemplo de visualización y captura de una imagen con el siguiente código:

```python
from picamera2 import Picamera2, Preview # importamos todo lo necesario
import time
picam2 = Picamera2() # creamos el objeto para acceder a la cmámara
# vamos a hacer una configuración por defecto para que se previsualice
# en el escritorio
camera_config = picam2.create_preview_configuration() 
picam2.configure(camera_config)
# arrancamos la previsualización
picam2.start_preview(Preview.QTGL)
picam2.start()
# mantenemos la previsualización durante 2 segundos
time.sleep(2)
# guardamos la captura en el fichero "test.jpg"
picam2.capture_file("test.jpg")
```

Si lo que queremos es grabar un vídeo, esta vez sin previsualización usaremos este código:

```python
# Ejemplo básico de captura de video con la camara
# T5_camara_captura_video.py
# Mas detalles en https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf

from picamera2 import Picamera2
picam2 = Picamera2()
picam2.start_and_record_video("test.mp4", duration=5)

```