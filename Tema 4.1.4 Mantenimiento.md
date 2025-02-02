## Mantenimiento

Una vez instalado el sistema, necesitamos de vez en cuando actualizarlo. Veamos cómo hacerlo.

El sistema periódicamente comprueba si hay actualizaciones, y si es así aparecerá un icono arriba a la derecha.  ![Icono de actualizaciones disponibles](./images/icono-actualizaciones-disponibles.png)

Si lo pulsamos, podemos ver las actualizaciones pendientes o hacer que estas se instalen.

![Icono de que existen actualizaciones disponibles](./images/icono_updated_available_reducida_200.jpg)

![Ventana mostrando paquetes actualizables](./images/paquetes_disponibles_actualizacion_reducida_375.jpg)

### Actualización (update)

Desde un terminal/consola tecleamos lo siguiente:

Para buscar cambios en los repositorios:

```sh
sudo apt update
```

Para instalar estos cambios:

```sh
sudo apt upgrade
```

Para actualizar el sistema, no sólo actualizando los paquetes:

```sh
sudo apt dist-upgrade
```

Para actualizar a una nueva distribución (si está disponible):

```sh
sudo apt full-upgrade
```

Para instalar un paquete determinado, haremos lo siguiente:

```sh
sudo apt install paquete
```

Vemos como en todos los comandos utilizamos la palabra "sudo", esto es debido a que se necesitan privilegios de administrador para todo lo relacionado con la actualización del sistema.

[![Vídeo: Actualizar e instalar software desde terminal en Raspberry Pi](./images/Actualizar%20e%20instalar%20software%20desde%20terminal.jpg)](https://drive.google.com/file/d/1tWwCM229eJSLx0h_iZxk-3A7VHJu2jYr/view?usp=sharing)

[Vídeo: Actualizar e instalar software desde terminal en Raspberry Pi](https://drive.google.com/file/d/1tWwCM229eJSLx0h_iZxk-3A7VHJu2jYr/view?usp=sharing)

### Eliminación de paquetes obsoletos

Con la instalación y actualización de los paquetes a lo largo del tiempo, algunas de las dependencias se quedan desfasadas e incluso algunos de los paquetes, puede que ya no sean necesarios. 

Por eso es necesario que cada cierto tiempo, eliminemos los paquetes  "huérfanos" que ya no se necesitan por el sistema, haciendo:

```sh
sudo apt autoremove
```

También podemos hacer:

```sh
sudo apt autoclean
```

Para eliminar los paquetes que ya quedaron obsoletos.

#### Actualización de los distintos firmwares

Los diferentes componentes de la Raspberry Pi necesitan de varios firmwares para funcionar, que también conviene tenerlos al día. Podemos actualizarlos con:

```sh
sudo rpi-update
```

Hay que tener **cuidado con este comando**: si actualizamos un firmware pero el sistema operativo no lo está, y por tanto, espera encontrar una versión anterior del firmware, podemos encontrarnos con que nuestra Raspberry Pi, se queda completamente bloqueada.

A veces, puede ocurrir que nos encontremos con que un cambio nos da algún problema que antes no teníamos. En ese caso, podemos volver a la versión anterior estable, haciendo lo siguiente:

```sh
sudo apt-get update
sudo apt-get install --reinstall libraspberrypi0 libraspberrypi-{bin,dev,doc} raspberrypi-bootloader
sudo reboot
```

#### Actualización de una versión a la siguiente

Aunque es conveniente que cuando salga una nueva versión hagamos una instalación desde cero, a veces tenemos muchas aplicaciones instaladas o mucha información del usuario que nos llevaría mucho tiempo extraer y luego volver a copiar/instalar. En ese caso, nos podemos plantear hacer una actualización de una versión a otra.

Vamos a ver un ejemplo de cómo actualizar de una versión del SO a la siguiente. En este caso particular, cómo pasar de "Stretch" a "Buster".

1. Modificamos la versión a la que apuntan los repositorios de 'stretch' a 'buster'. Podemos hacerlo cambiando a mano el ficheros **/etc/apt/sources.list** y **/etc/apt/sources.list.d/raspi.list** o con un comando como el siguiente:

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

4. Quitamos aplicaciones que ya no están en buster:

    ```sh
    sudo apt purge timidity lxmusic gnome-disk-utility deluge-gtk evince wicd wicd-gtk clipit usermode gucharmap gnome-system-tools pavucontrol
    ```

5. Ahora, actualizamos el aspecto con la nueva configuración visual abriendo ‘Appearance Settings’ y en la pestaña ‘Defaults’, pulsamos ‘Set Defaults’, lo que debería ponernos un tamaño de fuente y de iconos, acorde a la resolución usada.

Podemos hacer este cambio entre diferentes versiones con sólo cambiar los nombres de las versiones.

#### Instalación de paquetes a partir del código fuente

Hay varias razones para instalar software desde el código fuente:

1. Personalización y control:

- Puedes modificar las opciones de compilación para optimizar el rendimiento.
- Permite habilitar o deshabilitar características específicas.
- Puedes aplicar parches o modificaciones personalizadas.

2. Acceso a las últimas versiones:

- Los repositorios oficiales de las distribuciones suelen tener versiones más antiguas por estabilidad.
- Algunas características nuevas o correcciones de bugs solo están disponibles en las versiones más recientes.
- Ideal para desarrolladores que necesitan probar las últimas funcionalidades.

3. Compatibilidad y requisitos específicos:

- Cuando necesitas una versión específica que no está en los repositorios.
- Para resolver incompatibilidades con otro software.
- Cuando requieres optimizaciones para hardware específico.

4. Aprendizaje:

- Ayuda a entender mejor cómo funciona el software.
- Proporciona experiencia práctica con el proceso de compilación.
- Permite aprender sobre las dependencias y la estructura del software.

5. Casos especiales:

- Software que no está disponible en los repositorios oficiales.
- Cuando necesitas depurar problemas específicos.
- Para desarrollo y pruebas de software.

Sin embargo, también hay desventajas a considerar:

- Requiere más tiempo y conocimientos técnicos.
- Las actualizaciones no son automáticas.
- Puede ser más difícil de desinstalar.
- Mayor responsabilidad en la gestión de dependencias y seguridad.

Veamos los pasos para instalar un software a partir de su código fuente:

* Antes de instalar nuestro paquete, necesitamos tener instaladas las herramientas básicas de compilación:

```bash
sudo apt-get install build-essential
```

* Descargamos el código fuente (normalmente comprimido) desde su página web, generalmente desde github.com
* Lo descomprimimos con:
```sh
unzip codigo_fuente.zip
```
ó
```sh
tar xvf codigo_fuente.tgz
```
(según el formato en el que esté comprimido).

* Dentro del directorio del código ya descomprimido, normalmente encontramos un fichero README.md o INSTALL que nos dará las instrucciones, que suelen ser muy parecidas a estas:

1. Prepara el código para que compile en nuestro sistema y además, comprueba que tengamos las herramientas y librerías necesarias con:
	```sh
	cmake .
	```
	ó
	```sh 
	configure 
	```
2. Compila el código y generamos un ejecutable:
	```sh
	make
	```
3. Lo instalamos en el sistema (por eso necesitamos usar sudo).
	```sh
	sudo make install
	```

Consejos importantes:

- Siempre lee la documentación (README, INSTALL) antes de comenzar.
- Verifica las dependencias requeridas.
- Si hay problemas durante la configuración, revisa el archivo `config.log`
- Algunos paquetes pueden requerir pasos adicionales o diferentes.

