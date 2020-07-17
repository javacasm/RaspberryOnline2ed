## Mantenimiento

Una vez instalado el sistema, necesitamos de vez en cuando actualizarlo. Veamos como hacerlo.

### Actualización (update)

Desde un terminal/consola tecleamos lo siguiente

Para buscar cambios
```sh
sudo apt update
```
Para instalar estos cambios
```sh
sudo apt upgrade
```
Para actualizar el sistema
```sh
sudo apt dist-upgrade
```
Para actualizar a una nueva distribución
```sh
sudo apt full-upgrade
```

Para instalar un paquete determinado

	sudo apt install paquete

Vemos como en todos los comandos utilizamos la palabra "sudo" esto es debido a que se necesitan privilegios de administrador para todo lo relacionado con la actualización del sistema.

[![Vídeo: Actualizar e instalar software desde terminal en Raspberry Pi](https://img.youtube.com/vi/BaVfTWFUHtU/0.jpg)](https://youtu.be/BaVfTWFUHtU)


[Vídeo: Actualizar e instalar software desde terminal en Raspberry Pi](https://youtu.be/BaVfTWFUHtU)

#### Actualización de los distintos firmwares

Los diferentes componentes de la Raspberry necesitan de varios firmwares para funcionar, que también conviene tener actualizados. Podemos actualizarlos con:

```sh
sudo rpi-update
```

Hay que tener **cuidado con esta comando**: si actualizamos un firmware pero el sistema operativo no lo está y por tanto espera encontrar una versión anterior del firmware, podemos encontrarnos con que nuestra Raspberry se queda completamente bloqueada.

Si tenemos una de las últimas versiones 

#### Actualización de una versión a la siguiente

Aunque es conveniente que cuando salga una nueva versión hagamos una instalación desde cero, a veces tenemos muchas aplicaciones instaladas o mucha información del usuario que nos llevaría mucho tiempo extraer y luego volver a copiar/installar. En ese caso nos podemos plantear hacer una actualización de una versión a otra.

Vamos a ver un ejemplo de cómo actualizar de una versión del SO a la siguiente. En este caso particular cómo pasar de "Stretch" a "Buster".

1. Modificamos la versión a la apuntan los repositorios de 'stretch' a 'buster'. Podemos hacerlo cambiando a mano el ficheros **/etc/apt/sources.list** y **/etc/apt/sources.list.d/raspi.list** o con un comando como el siguiente:

```sh
grep -rl stretch /etc/apt/ | sudo xargs sed -i 's/stretch/buster/g'
```
2. Actualizamos el sistema completamente:

```sh
sudo apt update
sudo apt dist-upgrade
sudo apt full-upgrade
```
3. Actualizamos los firmwares:

```sh
sudo rpi-update
```

4. Quitamos aplicaciones que ya no están en buster
```sh
sudo apt purge timidity lxmusic gnome-disk-utility deluge-gtk evince wicd wicd-gtk clipit usermode gucharmap gnome-system-tools pavucontrol
```
5. Ahora actualizamos el aspecto con la nueva configuración visual abriendo ‘Appearance Settings’ y en la pestaña ‘Defaults’ pulsamos ‘Set Defaults’ lo que debería ponernos un tamaño de fuente y de iconos acorde a la resolución usada.


##### Recursos
[Fuente](https://www.raspberrypi.org/blog/buster-the-new-version-of-raspbian/)

#### Instalación de programas

Además de la línea de comandos, siempre podemos instalar desde la herramienta visual "Añadir programas" en el menú Preferencias.

[![Vídeo: Cómo actualizar e instalar software Raspberry Pi](https://img.youtube.com/vi/3eeIHe-NCZs/0.jpg)](https://youtu.be/3eeIHe-NCZs)


[Vídeo: Cómo actualizar e instalar software Raspberry Pi](https://youtu.be/3eeIHe-NCZs)

#### Instalación de paquetes a partir del código fuente

* Descargamos el código fuente (normalmente comprimido)
* Lo descomprimimos con
```sh
unzip codigo_fuente.zip
```
ó
```sh
tar xvf cofigo_fuente.tgz
```
(según el formato en el que esté comprimido)

Dentro del directorio del código ya descomprimido normalmente encontramos un fichero README o INSTALL que nos dará las instrucciónes, pero suelen ser muy parecidas a estas:

Preparan el código para que compile en nuestro sistema y además comprueban que tengamos las herramientas y librerías necesarias con:
```sh
cmake .
```
ó
```sh
configure
```
Compila el código y generamos un ejecutable
```sh
make
```
Lo instalamos en el sistema (por eso necesitamos usar sudo)
```sh
sudo make install
```
