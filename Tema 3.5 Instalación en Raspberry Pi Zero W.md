## Instalación en una Raspberry Pi Zero W (o Zero 2 W)

Vamos a hacer una instalación ahora en una Raspberry Pi Zero W que vamos a utilizar para tomar fotos remotamente, con lo que normalmente no va a tener ni monitor, ni teclado conectados. Ello unido a su menor potencia nos va a llevar a usar una versión del SO sin escritorio visual, ni las aplicaciones asociadas.

Una vez conectada al Wifi, accederemos a ella vía ssh, usando terminal/consola.

1. Instalaremos Raspberry Pi OS Lite usando Imager.
1. Inicialmente conectaremos un teclado y una pantalla HDMI para una primera configuración por consola.
1. Colocamos la Raspberry Pi Zero W en su caja, y la cerramos con cuidado.
1. Conectaremos un adaptador HDMI.
1. Conectaremos el cable adaptador USB.
1. Alimentamos con el cable USB de alimentación desde la batería.

Colocamos la Raspberry Pi Zero W en su caja y conectamos la alimentación, y queda así de reducido.

![Raspberry Pi Zero con alimentación](./images/RaspiZeroAlimantacion.jpg)

Ahora ya arrancamos para hacer la configuración necesaria desde la consola, haciendo la configuración inicial:

* Cambiamos contraseña.
* Configuramos Wifi.
* Configuración del hostname (nombre que identifica a la Raspberry desde la red).
* Activamos ssh.
* Configuramos idioma, zona horaria y teclado.

Todo ello lo haremos usando la configuración por consola con _raspi-config_:

```sh
sudo raspi-config
```
### Configuración de asignación de IP fija en el router

Puesto que vamos a acceder remotamente a la Raspberry, necesitamos que el router siempre nos asigne la misma dirección IP. Para ello configuraremos en la sección de DHCP la asignación de una IP dada, para el MAC (número de serie que identifica inequívocamente nuestro dispositivo) de nuestra Zero.

Al configurar un  hostname, si nuestro router lo permite, podremos acceder también usando el nombre.

### Resto de la configuración 

Una vez hecho esto ya podemos conectarnos por ssh
```sh
ssh pi@NombreRaspiZero
```
 y configurar el resto de opciones:

* Activamos la cámara.
* Actualización del SO.
* Instalamos los paquetes de Python necesarios para nuestra aplicación


[![Vídeo: Instalación y configuración desde consola de Raspberry Pi Zero W](https://img.youtube.com/vi/YIW2HbepDKg/0.jpg)](https://drive.google.com/file/d/1mzqEEelZxZ3ofI_K0_njGzZrkpYRJn5U/view?usp=sharing)

[Vídeo: Instalación y configuración desde consola de Raspberry Pi Zero W](https://drive.google.com/file/d/1mzqEEelZxZ3ofI_K0_njGzZrkpYRJn5U/view?usp=sharing)

En las instalaciones del OS versión "Lite", podemos hacer que por defecto se active el acceso ssh desde el inicio.

Para ello basta con crear un fichero vacío llamado **"ssh"** en directorio raíz de la tarjeta y vuelve a arrancar.

### "Trucos" desde la consola

* Podemos saber la dirección IP usando el comando **ifconfig**
* Para saber la red Wifi a la que estamos conectados usaremos, **iwconfig**
* Podemos añadir acceso a una red wifi editando el fichero _wpa_suplicant_ con:

    ```sh
    sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
    ```
    y añadiendo el siguiente texto

    ```
    network={
            ssid="ssidDelaRed"
            psk="contraseña"
    }
    ```
* Para apagar la Raspberry usaremos **sudo halt**
* Para reiniciar **sudo reboot**
