# Instalación Arduino

Un uso muy frecuente de Raspberry es para trabajar en proyectos de electrónica o robótica donde también contamos con Arduino. Es por ello que resulta interesante tener instalado el entorno de programación de Arduino.

Desgraciadamente la versión que se instala desde sus repositorios es extremadamente antigua, con lo que es mejor instalarlo directamente desde la web de Arduino, donde vemos que en la  [página de descargas de arduino.cc](https://www.arduino.cc/en/Main/Software) sólo tenemos una versión del [IDE de Arduino para Linux ARM para 32bits](https://www.arduino.cc/download_handler.php?f=/arduino-1.8.13-linuxarm.tar.xz) bastante antigua

Una vez descargado extraemos el contenido con 

```sh
tar xvf Downloads/arduino-1.8.13-linuxarm.tar.xz
```

Ejecutamos **Install.sh** para crear el acceso directo de los menús y dar los permisos necesarios.

Cuando termine la instalación intentamos abrir desde el menú (en el vídeo nos da un error que vemos cómo arreglar)

Si queremos abrir el entorno desde consola, sólo tenemos que entrar en la correspondiente carpeta y ejecutar 
```sh
./arduino
```

[![Vídeo: Instalación del IDE de Arduino en Raspberry Pi](https://img.youtube.com/vi/-PdmFyhnQV0/0.jpg)](https://drive.google.com/file/d/1ljtLrWubUC5W_OMOPpD7OaIO4FWISjxz/view?usp=sharing)

[Vídeo: Instalación del IDE de Arduino en Raspberry Pi](https://drive.google.com/file/d/1ljtLrWubUC5W_OMOPpD7OaIO4FWISjxz/view?usp=sharing)

Más adelante en el curso veremos cómo utilizar Arduino junto con Raspberry en nuestros proyectos.
### Fritzing

Otra herramienta relacionada con los proyectos de robótica y electrónica es Fritzing que también podemos usar en nuestra Raspberry Pi. Para ello la instalamos con

En este caso la versión disponible para Raspberry en los repositorios, aunque no es la última, sí que es bastante reciente y usable.

Podemos instalarla desde la Herramienta de Instalación de Software o desde consola:

```sh
sudo apt install fritzing
```


[![Vídeo: Instalación de Fritzing en Raspberry Pi](https://img.youtube.com/vi/P_-ZmPEDHzs/0.jpg)](https://drive.google.com/file/d/1kfjQnGYZxjrY5CO4ebJR38FG6CZiMZj8/view?usp=sharing)

[Vídeo: Instalación de Fritzing en Raspberry Pi](https://drive.google.com/file/d/1kfjQnGYZxjrY5CO4ebJR38FG6CZiMZj8/view?usp=sharing)

