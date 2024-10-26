## Manejando tu Raspberry Pi

Vamos a ver cómo manejar alguno de los programas más habituales de Raspberry Pi OS.

### Administrando ficheros

Para trabajar con nuestros ficheros usaremos la aplicación "Gestor de archivos PCManFM" en el menú Accesorios

![](icono_gestor_ficheros.png)

Al abrirlo encontramos la típica aplicación de gestión de ficheros.

![](gestor_ficheros.png)
Veamos algunas de las partes:
1. Panel con los volúmenes o particiones disponibles y los marcadores (directorios marcados como favoritos).
2. Vista en árbol de la estructura de directorios
3. Panel con el contenido de la carpeta seleccionada. Podemos reordenar el contenido  tocando en la cabera de las columnas.
4. Podemos usar estos iconos para ver gráficamente el contenido de la carpeta o los detalles en forma de lista.
5. Directorio que estamos viendo, podemos editar su contenido para movernos a otra carpeta.
6. Podemos ir a nuestra carpeta personal (carpeta "home"), o al anterior o al directorio que contiene al actual.
7.  Desde el menú podemos crear directorios, archivos, movernos a las carpetas más frecuentes, copiar y pegar,....
### Navegador Web

En el menú "Internet" tenemos disponibles el navegador Chromium, la versión de código abierto 100% del navegador Chrome . También podemos instalar Firefox

![](menu_internet.png)

### Accesorios

En el menú "Accesorios" vamos a encontrar muchas aplicaciones útiles:

![](aplicaciones_menu_accesorios.png)

Editores de texto
* **Archiver** para Comprimir/extraer ficheros
* **Calculator**: una calculadora
* **LXTerminal**: terminal/consola
* **Mousepad**: un aparentemente sencillo editor de texto que nos permite crear documentos en muchos formatos
* **Raspberry Pi Diagnostics**: realiza un test de rendimiento sobre una tarjeta recién formateada.
* **SD Card Copier**: nos permite realizar copias de tarjetas SD, muy útil para clonar tarjetas una vez que tengamos una instalación operativa.
* **Visor de documentos**: nos permite ver los ficheros PDF



### Capturas de la pantalla

Podemos hacer capturas del escritorio usando la tecla Imprimir Pantalla si nuestro teclado la tiene o bien usando el comando **Scrot**, que pondrá un fichero con la captura en directorio home del usuario (/home/pi por defecto) con un nombre dado por la fecha, hora y resolución. Por ejemplo "2021-02-26-194221_1024x768_scrot.png".

Podemos hacer que la captura se haga después de un determinado retardo usando la opción **-d**. Por ejemplo para hacer la captura a los 10 segundos. 

```sh
scrot -d 10
```

También podemos darle un nombre concreto al fichero resultado al usar el comando

```sh
scrot ficheroCaptura.png
```

Si necesitamos más opciones podemos instalar un programa como **Gnome Screenshot** que nos dará más opciones. Lo instalaremos como siempre con

```sh
sudo apt install gnome-screenshot
```
Y aparecerá en el menú de "Accesorios"

Nos permitirá capturar todo el escritorio, una ventana, una zona, definiendo un determinado retardo. También nos permite tras hacer la captura seleccionar el nombre y carpeta del fichero o si queremos que se copie la imagen en el clipboard.

![gnome-screenshot](./images/gnome-screenshot.png)


## Usos

Veamos cómo podemos utilizar lo aprendido...

### Para hacer cálculos con Mathematica

Hay una versión gratuita (para uso no comercial) de Wolfram  Mathematica instalada por defecto en Raspbian

![Mathematica en Raspberry Pi](./images/Mathematica.png)

[![Vídeo: Trabajando con Mathematica en Raspberry](https://img.youtube.com/vi/VVHoREZ8Rc4/0.jpg)](https://drive.google.com/file/d/1oXjMaNmL4gpaTHPePZYbIb6_lRsAGODi/view?usp=sharing)


[Vídeo: Trabajando con Mathematica en Raspberry](https://drive.google.com/file/d/1oXjMaNmL4gpaTHPePZYbIb6_lRsAGODi/view?usp=sharing)


### Vigilancia

Podemos usar su cámara (la original o una USB)

Usaremos un software standard de Linux: **motion**

```sh
sudo apt-get install motion
```

Editamos la configuración

```sh
sudo nano /etc/motion/motion.conf
```

![usando motion](./images/motion.jpg)

Lo arrancamos
```sh
motion -n
```

Podremos acceder a la imagen en vivo de la cámara con

```sh
http://raspberry_ip:8081
```
 
