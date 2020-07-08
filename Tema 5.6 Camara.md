## Recursos
[The camera module](https://www.raspberrypi.org/magpi-issues/Essentials_Camera_v1.pdf)


http://fpaez.com/raspbery-pi-control-de-la-camara-con-python/

### timeLapse

El equipo estarḉa conecta vía wifi y no tendrá conectado ningún períferico, sólo la alimentación que vendrá de adaptador USB

Por ello vamos a instalar Raspberry Pi OS Lite


scp para copiar fotos

scp pi@raspiLapse:~/proyectos/RaspiZeroLapse/code/images/image20200707-10*


TODO: MOVER AL APARTADO CORRESPONDIENTE

![CableCamaraZeroNormal.jpg](./images/CableCamaraZeroNormal.jpg)

![CamaraRaspiZerojpg](./images/CamaraRaspiZero.jpg)

![RaspiZeroCaja.jpg](./images/RaspiZeroCaja.jpg)

![RaspiZeroCajaCerrada.jpg](./images/RaspiZeroCajaCerrada.jpg)

![RaspiZeroCajaCerradaPuertos.jpg](./images/RaspiZeroCajaCerradaPuertos.jpg)

![RaspiZeroAlimantacion.jpg](./images/RaspiZeroAlimantacion.jpg)

https://projects.raspberrypi.org/en/projects/raspberry-pi-zero-time-lapse-cam/2


Cuidado con la alimentación, al usa una batería que daba poca potencia fallaba al encender/apagar la cámara

![Montaje timelapse](./images/TimeLapseSetup.jpg)


```bash
sudo apt install python3-pip

pip3 install python-telegram
pip3 install python-telegram-bot

```





## acceso SSH y SCP

scp pi@raspiLapse:~/proyectos/RaspiZeroLapse/code/images/* .


## Puesta a punto de entorno de programación

git clone url_repositorio.git

git config --global user.name "javacasm"
git config --global user.email "javacasm@gmail.com"


modificamos  y subimos los cambios con 


git add fichero_cambiado.py

git commit -m "correccion del error de login" ficher.py


Si vamos a trabajar durante bastante tiempo con github nos interesa añadir la firma ssh de la raspberry a github

Para ello necesitamos crear una clave SSH en la raspberry. Siguiendo la [documentación de github](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) hacemos:

```sh
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
y definimos dónde se va a guardar el fichero y si queremos ponerle cable

```sh
> Enter a file in which to save the key (/home/you/.ssh/id_rsa): [Press enter]
> Enter passphrase (empty for no passphrase): [Type a passphrase]
> Enter same passphrase again: [Type passphrase again]
```

(en la raspberry Zero tarda casi más de 1 minuto)

Ejecutamos el ssh-agent con

```sh
eval "$(ssh-agent -s)"
```
y añadimos la key generada

```sh
ssh-add ~/.ssh/id_rsa
```


mostramos por consola el fichero con 

cat ~/.ssh/id_rsa.pub

y lo añaidmos a nuestra cuanta github pulsando "New SSH key" in https://github.com/settings/keys

Si estuvieramos en un entorno visual haríamos:

Instalamos xclip (una utilidad para manejar el clipboard)

```sh
sudo apt-get install xclip
```

y copiamos la key al clipboard

```sh
xclip -sel clip < ~/.ssh/id_rsa.pub
```

Ahora ya podemos trabajar con ssh en github, lo que nos ahorra tener que escribir muchas veces nuestro usuario/password de github



