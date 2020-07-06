## Mantenimiento

Una vez instalado el sistema, necesitamos de vez en cuando actualizarlo. Veamos como hacerlo.

### Actualización (update)

Desde un terminal/consola tecleamos lo siguiente

Para buscar cambios

	sudo apt update

Para instalar estos cambios

	sudo apt upgrade

Para actualizar el sistema

	sudo apt dist-upgrade

Para instalar un paquete determinado

	sudo apt install paquete

Vemos como en todos los comandos utilizamos la palabra "sudo" esto es debido a que se necesitan privilegios de administrador para todo lo relacionado con la actualización del sistema.

[![Vídeo: Actualizar e instalar software desde terminal en Raspberry Pi](https://img.youtube.com/vi/BaVfTWFUHtU/0.jpg)](https://youtu.be/BaVfTWFUHtU)


[Vídeo: Actualizar e instalar software desde terminal en Raspberry Pi](https://youtu.be/BaVfTWFUHtU)

#### Actualización de los distintos firmware

Los diferentes componentes de la Raspberry necesitan de varios firmwares para funcionar, que también conviene tener actualizados. Podemos actualizarlos con


	sudo rpi-update

#### Instalación de programas

Además de la línea de comandos, siempre podemos instalar desde la herramienta visual "Añadir programas" en el menú Preferencias.

[![Vídeo: Cómo actualizar e instalar software Raspberry Pi](https://img.youtube.com/vi/3eeIHe-NCZs/0.jpg)](https://youtu.be/3eeIHe-NCZs)


[Vídeo: Cómo actualizar e instalar software Raspberry Pi](https://youtu.be/3eeIHe-NCZs)

#### Instalación de paquetes a partir del código fuente

* Descargamos el código fuente (normalmente comprimido)
* Lo descomprimimos con

	unzip codigo_fuente.zip

ó

	tar xvf cofigo_fuente.tgz

(según el formato en el que esté comprimido)

Dentro del directorio del código ya descomprimido normalmente encontramos un fichero README o INSTALL que nos dará las instrucciónes, pero suelen ser muy parecidas a estas:

Preparan el código para que compile en nuestro sistema y además comprueban que tengamos las herramientas y librerías necesarias con:

	cmake .

ó

	configure

Compila el código y generamos un ejecutable

	make

Lo instalamos en el sistema (por eso necesitamos usar sudo)

	sudo make install