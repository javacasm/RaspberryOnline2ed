## Instalación Raspberry Pi 5.1 en Raspberry Pi 4

configuramos wifi,hostname y ssh desde imager

recuperamos la ip desde el router o con un monitor

sudo apt install screen

screen
sudo raspi-config

interface -> VNC e I2C

Performance ->  Fan -> Temperature control -> GPIO14 & 80C

Advanced -> Expand FileSystem
         -> Boot order
         -> ¿Wayland or X11?

sudo apt update
sudo apt full-upgrade

Conectamos VNC con nuestra cuenta para acceso remoto a la raspi

vncserver-x11