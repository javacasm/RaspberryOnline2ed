## Arranque desde USB

En las nuevas Raspberry Pi (a partir de la 4), también podemos hacer la instalación en un disco USB (o pendrive USB), para usarlo como disco del sistema sin necesidad de tarjeta SD.

 Podemos aprovechar esto para instalar  versiones  experimentales, todavía en estado beta. [Más información](https://forums.raspberrypi.com/viewtopic.php?t=275370), descargando las imágenes desde la [página de la beta](https://downloads.raspberrypi.org/raspios_arm64/images/)

### Instalación para arranque con disco USB

Vamos a usar un disco USB para instalar y arrancar nuestro SO. Necesitamos un pendrive rápido (o un disco SSD). Debe ser USB 3.0 y de alta velocidad para aprovechar su rendimiento.

Necesitaremos una tarjeta SD para crear la imagen y copiarla al pen USB.

1. Instalamos un sistema limpio en la tarjeta SD.
2. Actualizamos el SO con:


```sh
sudo apt update
sudo apt full-upgrade
```

3. Copiamos el contenido de nuestra tarjeta SD al disco USB con el programa **SD Card Copier** de nuestra Raspberry Pi.

4. Ahora vamos a actualizar la EEPROM para activar el arranque desde USB. Editaremos el fichero _/etc/default/rpi-eeprom-update_ cambiando "critical" por _"stable"_.

```sh
sudo nano /etc/sudo nano /etc/default/rpi-eeprom-update
```

5. Comprobamos que tenemos disponible el firmware que vamos a escribir en la versión stable que será  posterior al 15 de Junio. Lo haremos con el comando:

```sh
ls /lib/firmware/raspberrypi/bootloader/stable/
```

![](./images/USB4_eeprom_files.png)


6. Ahora escribimos los cambios en la EEPROM con:

```sh
sudo rpi-eeprom-update  -d -f /lib/firmware/raspberrypi/bootloader/stable/pieeprom-2020-06-15.bin 
```

![](./images/USB4_eeprom_update.png)

7. Si todo ha ido bien, apagamos la Raspberry Pi, quitamos la tarjeta SD y probamos a arrancar.

[Vídeo: Cómo arrancar Raspberry Pi 4 desde USB](https://drive.google.com/file/d/12cLBP4SUQRcx7pZciu3VnC-YwB73_Jyd/view?usp=sharing)

[![Vídeo: Cómo arrancar Raspberry Pi 4 desde USB](https://img.youtube.com/vi/jgCfJbiEbHE/0.jpg)](https://drive.google.com/file/d/12cLBP4SUQRcx7pZciu3VnC-YwB73_Jyd/view?usp=sharing)

En [este enlace](https://www.jeffgeerling.com/blog/2020/im-booting-my-raspberry-pi-4-usb-ssd) se ve que la mejora de rendimiento puede ser realmente importante.


