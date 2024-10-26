## Instalación

La Fundación Raspberry Pi ha publicado una herramienta gratuita llamada [**Raspberry Pi Imager**](https://www.raspberrypi.com/software/) que  hace aún más sencilla la instalación del sistema operativo, permitiéndonos elegir entre muchísimos sistemas operativos, encargándose de formatear la tarjeta SD, de descargar el sistema operativo y escribir la imagen del sistema directamente en la tarjeta. 

También nos permite hacer una primera configuración, como es el usuario, contraseña, wifi, nombre del equipo... que se grabarán en la tarjeta SD, arrancando ya el sistema con esa configuración.

Podemos descargarlo desde el apartado de [Software de la página de Raspberry Pi](https://www.raspberrypi.com/software/) eligiendo la versión adecuada para nuestro sistema operativo.

![Instalador de Raspberry Pi Imager para varios sistemas operativos](./images/rpi-imager_instalador_so_reducida_75.jpg)


Tras descargarlo, lo instalaremos.

Para ejecutarlo, necesitamos estar conectados a Internet para que se pueda descargar la lista de los sistemas operativos disponibles y las imágenes que vamos a usar.

Al ejecutarlo, tendremos la siguiente pantalla:

![Raspberry Pi Imager 1.8.5](./images/rpi-imager_1.8.5_reducida_50.jpg)

En primer lugar selecciona el tipo de Raspberry Pi que vamos a usar, para filtrar los sistemas operativos compatibles con el dispositivo seleccionado:

![Selector del modelo de Raspberry para instalar](./images/rpi-imager_1.8.5_dispositivo_reducida_60.jpg)

La versión 1.8.5  nos permite instalar los siguientes sistemas operativos:

![Selección del sistema operativo a instalar en la tarjeta SD](./images/rpi-imager_1.8.5_sos_reducida_60.jpg)

Al seleccionar el sistema operativo veremos distintas opciones, como por ejemplo al seleccionar Ubuntu:

![Distintas versiones de Ubuntu que podemos instalar](./images/rpi-imager_1.8.5_ubuntu_os_reducida_60.jpg)

Donde vemos que aparecen opciones de instalar diferentes versiones de 32 o de 64 bits.

A día de hoy (octubre de 2024) existen 2 versiones disponibles de Raspberry Pi OS:

* La versión derivada de **Bullseye**, que es la más reciente, pero que hasta ahora mismo no es compatible al 100% con algunas librerías de Python. Cada vez son menos las aplicaciones que no son compatibles.
* La versión **Legacy** que es una actualización de la versión anterior **Buster**, que sí es compatible con las librerías de Python antiguas, por ejemplo las de usar la cámara.

![[Versiones de Raspberry Pi disponibles](./images/rpi-imager_1.8.5_sos_raspian_reducida_60.jpg)

Elegiremos una u otra, según el tipo de aplicación que queramos usar. Ante la duda, mejor instalar la versión más moderna de 64 bits.

Por último seleccionaremos  la tarjeta SD o el dispositivo  donde vamos a escribir la imagen (los datos de la tarjeta se borrarán).

 Nos preguntará si queremos configurar la instalación, lo que nos permitirá definir usuario, idioma, teclado, nombre de la máquina, conexión wifi y acceso remoto.

  ![Configuración de la Instalación Raspberry Pi Imager](./images/Raspi-imager-config-0_reducida_60.jpg)

Configuramos nuestra instalación con:

* Nombre de nuestra máquina (necesario para acceder remotamente). Importante que no se repita en la red.
* Usuario/contraseña (no podemos olvidarlo o no podremos acceder).
* SSID y contraseña del wifi.

	![Configuración de la Instalación Raspberry Pi Imager](./images/Raspi-imager-Config-1_reducida_50.jpg)
	
* En la pestaña Servicios: activamos acceso ssh para poder conectarnos remotamente:

	![Configuración Servicios Raspberry Imager](./images/Raspi-imager-Config-servicios_reducida_50.jpg)

Ésta es una gran ventaja, pues al arrancar, ya tendremos toda esta configuración realizada. Además esta configuración se guarda en el instalador y podremos fácilmente reutilizar los datos para posteriores instalaciones.

En las versiones actuales ya se permite que el usuario no sea "pi", pudiendo poner cualquier nombre de usuario.

A día de hoy RPI Imager no permite instalar varios sistemas operativos en la misma tarjeta, pero sí que nos permite seleccionar entre muchos sistemas, además de los propios de raspberrypi.org como podemos ver en el siguiente vídeo.

[![Vídeo: Nuevo instalador RPI Imager: 64 bits, configuración y bootloader](https://img.youtube.com/vi/hRkOoSDu6FM/0.jpg)](https://drive.google.com/file/d/15T_fPbQdCdTvPMLpMd4RLAzlFYYnDi-c/view?usp=sharing)

[Vídeo: Nuevo instalador RPI Imager: 64 bits, configuración y bootloader](https://drive.google.com/file/d/15T_fPbQdCdTvPMLpMd4RLAzlFYYnDi-c/view?usp=sharing)

Al pulsar **Write** se descargará la imagen desde Internet, se escribirá en el soporte elegido y posteriormente se verificará si se ha grabado correctamente.  

También podemos usar RPI Imager para formatear la tarjeta, para crear tarjetas SD capaces de recuperar una instalación con problemas, para escribir imágenes que ya hemos descargado, etc.

[![Vídeo: Instalación de Raspberry Pi OS usando Imager](https://img.youtube.com/vi/DDfkkG4-gq8/0.jpg)](https://drive.google.com/file/d/1vZCdJa2551mNAdr1cwsOAJMn440eqXMG/view?usp=sharing)

[Vídeo: Instalación de Raspberry Pi OS usando Imager](https://drive.google.com/file/d/1vZCdJa2551mNAdr1cwsOAJMn440eqXMG/view?usp=sharing)

Si todo va bien al cabo de unos segundos y si tenemos conectado un monitor,  veremos el escritorio, un escritorio ligero pero con buen aspecto y con la funcionalidad a la que estamos acostumbrados hoy en día.

![Menú del Escritorio Pixel](./images/PixelMenu_reducida_75.jpg)

La primera vez que arranquemos tendremos que configurar, si no lo hemos hecho ya, el idioma y la zona horaria, establecer la contraseña del usuario por defecto “pi”  y el sistema se actualizará.

Si no tenemos monitor conectado, pasados unos segundos ya podemos intentar conectarnos por __ssh__, siempre que la hayamos activado en la configuración de la imagen. (Un poco más adelante vamos a tratar el tema de la conexión ssh en mayor detalle).

* En Linux, Mac o Windows 11 lo podemos hacer directamente en la línea de comandos (consola o terminal).
```python
ssh nombre_usuario@nombre_maquina.local
```
* En Windows anteriores a 11 instalamos [Putty](https://putty.org), herramienta open source y, a pesar del  nombre, totalmente confiable. Desde ahí podremos acceder usando el nombre de usuario elegido y el nombre de la máquina. [Putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html "http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html") es una herramienta open source disponible para muchos sistemas operativos pensada para conectar remotamente con equipos usando distintos protocolos como ssh, telnet, serie, etc. Permite guardar las credenciales de cada sistema, facilitando la conexión.

	![Putty herramienta para conectar equipos remotamente](./images/Putty_reducida_60.jpg)

* Introducimos la contraseña (que no se ve al escribirla, tampoco) y accedemos a nuestra Raspberry Pi por línea de comandos.

## ¿Escritorio o línea de comandos?

La Raspberry Pi (y todos los ordenadores que usan Linux/Unix) se puede usar con el ratón o con comando desde el terminal del sistema: 

* El ratón es más intuitivo, sólo hay que ir mirando por las opciones de menú, que suelen ser bastante descriptivas.
* La línea de comandos da un control más detallado y una vez que te acostumbras, es más productiva, sobre todo porque se pueden automatizar tareas con facilidad.

![Ejemplo de uso de consola/terminal](./images/contenidowww_recortada.jpg)

Sobre los comandos de consola, hay libros y libros, en este curso hemos intentado incluir algunas de las "recetas" más habituales. Muchos de ellos están incluidos en la documentación del curso.  

Por ejemplo, como veremos un poco más adelante, para instalar software, podemos hacerlo usando el ratón desde la opción "Add/Remove software" del menú "Preferencias" o desde la consola con:

```bash
sudo apt update
sudo apt install wolfram-engine # Instala el  programa Mathematica de Wolfram
```

Hay gente a la que le gusta usar los comandos y otros son más de ratón, puedes hacer casi lo mismo con los dos sistemas. Usa el que más cómodo te sea. 

## Uso del escritorio

Vamos a ver algunos de los menús e iconos más importantes de Pixel Raspberry Pi.

A la izquierda tenemos el menú de aplicaciones.

![Menú de configuración de Raspberry](./images/ConfiguracionRaspberry_reducida_60.jpg)

A la derecha, podemos pulsar sobre el icono del Wifi o de la red para configurarla, si fuera necesario.

![Configuración Wifi de Raspberry](./images/wifi2_reducida_75.jpg)

Demos un paseo por el interfaz del escritorio.

En este [vídeo](https://drive.google.com/file/d/1Xctv-39GG117f1Zm_0QbfQbRZoZd_MKG/view?usp=sharing) podéis ver el uso del entorno visual  Pixel de Raspberry Pi.

[![](https://img.youtube.com/vi/IrjWoxWfewo/0.jpg)](https://drive.google.com/file/d/1Xctv-39GG117f1Zm_0QbfQbRZoZd_MKG/view?usp=sharing)

### Usando Pixel el entorno de Raspberry Pi en tu PC

![Pixel entorno gráfico de Raspberry Pi](./images/newdesk-500x281.jpg)

Puedes usar Pixel el entorno gráfico de Raspberry Pi en tu PC o MAC, solo necesitas descargar la [imagen](http://downloads.raspberrypi.org/pixel_x86/images/pixel_x86-2016-12-13/2016-12-13-pixel-x86-jessie.iso) desde un CD o USB.

Más detalles en [esta página](https://www.raspberrypi.com/news/pixel-pc-mac/)


