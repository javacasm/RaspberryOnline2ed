# Pantalla TFT táctil

Vamos a conectar una pantalla TFT Táctil de 4"  con una resolución de 800x480. El tamaño de la pantalla es igual al de la Raspberry, lo que lo hace muy adecuado si queremos montar todo en una caja:


![TFT táctil](./images/TFT3.jpg)

La conexión se hace vía HDMI con una doble adaptador HDMI M-M (con HDMI normales los 2 o uno mini si es para Raspberry 4) y GPIO para el sensor táctil. Tamibén incluye un conector jack para la salida del audio (en la Raspberry con figuraremos como Audio HDMI). También dispone de un conector USB por si queremos alimentarla independientemente, alimentándose por defecto por los pines 5V y GND de GPIO.


![TFT táctil](./images/TFT0.jpg)

La conexión de la pantalla usa SPI con los siguientees pines GPIO

GPIO|nombre
---|---
19|	TP_SI
21|	TP_SO
22|	TP_IRQ
23|	TP_SCK
26|	TP_CS

Esta pantalla se puede utilizar con cualquier ordenador, pero la conexión GPIO de la pantalla táctil está pensada para conectarse a una Raspberry.

## Instalación

La instalación es bastante sencilla, con la ayuda de unos scripts y la [documentación del fabricante](http://www.lcdwiki.com/4inch_HDMI_Display-C). 

Recomiendo que hagas los cambios conectado remotamente, bien por ssh o por VNC, pero con la pantalla ya conectada y con el conector correspondiente conectando los HDMIs de la pantalla y de la Raspberry.

Primero clonamos su repositorio [https://github.com/goodtft/LCD-show](https://github.com/goodtft/LCD-show) para obtener los scripts y drivers:

```sh 

git clone https://github.com/goodtft/LCD-show
```

Antes de hacer cambios vamos a hacer una copia del fichero "/boot/config.txt" por si quisiéramos volver a la configuración inicial:

```sh

sudo cp /boot/config.txt /boot/config_antes_cambios_TFT.txt

```

Desde el directorio "LCD-show" ejecutamos el script de instalación como administrador:

```
sudo ./MPI4008-show
```

El script instala los drivers, y configura la pantalla modificando el fichero config.txt.

Cuando termina la instalación reinicia la Raspberry. Al arrancar de nuevo, por defecto nos dejará la pantalla en formato vertical:

![](./images/TFTI.jpg)

Si queremos rotarla a un formato apaisado ejecutaremos el fichero sudo ./rotate.sh 90 que está dentro de LCD-show

```sh
sudo ./rotate.sh 90
```

También podemos rotarlo a 270, si lo preferimos.


## Uso


Una vez instalado y arrancada la Raspberry, comprobamos que la pantalla se ve muy bien, y tiene una resolución adecuada para el tamaño

![TFT táctil](./images/TFT9.jpg)

Incluso un terminal es operativo, eso sí conectando un teclado exteno (bluetooth en este caso)
![TFT táctil](./images/TFT4.jpg)


Los menús son fácilmente accesibles con el puntero
![TFT táctil](./images/TFT6.jpg)


La mayoría de las ventanas cabe bien y se ajusta, como la de apagado:
![TFT táctil](./images/TFT5.jpg)

Si abrimos una aplicación como Thonny, se adapta y se puede utilizar para unos cambios rápidos

![TFT táctil](./images/TFT8.jpg)



