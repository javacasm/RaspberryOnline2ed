## Retropie

Una de las aplicaciones más usadas de Raspberry es usarla como una bartop o máquina recreativa donde podmoes jugar a juegos arcade antiguos.

![mage](./images/mage.jpg)

**Retropie** es un distribución para Raspberry que nos permite ejecutar una gran cantidad de emuladores, configurar los mandos y gestionar las ROMs de los juegos. 

Está basada en Raspbian, a la que añaden [EmulationStation](EmulationStation.org) y [RetroArch](http://retroarch.com/)



El proceso de instalación no puede ser más sencillo:
1. Descargamos la imagen de [Retropie](https://retropie.org.uk/download)
2. Tras descomprimilar, la grabamos en una tarjeta SD 
3. Arrancamos y seguimos el proceso de configuración
4. Si tenemos conectado algún mando nos pedirá que lo configuremos
![Configuring.png](./images/Configuring.png)
5. Al arrancar aparecerá solo la opción de ejecutar Retropie que es donde configuramos todo. Cuando añadamos más juegos irán apareciendo los restantes emuladores.
6. Dentro de Retropie configuraremos el acceso al Wifi
7. En "RetroPie Setup" seleccionamos "Configuration Tools" y ahí activamos "Samba" para poder acceder a ficheros externos y podremos acceder a él desde otros equipos, que lo verán como "Retropie"
8. Ahora ya podemos descargar los juegos y copiarlos vía Samba. Por ejemplo podemos descargar [BladeBuster](http://magpi.cc/bladebuster) y copiamos el fichero zip sin descomprimir en "Retropie".
9. Al entrar de nuevo veremos que tenemos disponible "NES" y ahí nuestro juego.

El tema de los ficheros ROMs de juegos originales es complicado: a pesar de que la mayoría de los juegos ya no se venden, es ilegal el utilizarlos sin haberlos comprado.

Existen muchas alternativas legales como podemos ver en este [post de los foros de retropie](https://retropie.org.uk/forum/topic/10918/where-to-legally-acquire-content-to-play-on-retropie)

También podemos hacer una [instalación manual](https://retropie.org.uk/docs/Manual-Installation/)

### Referencias

[Tutorial de programoergosum](https://www.programoergosum.es/tutoriales/consola-arcade-basada-en-raspberry-pi-con-retropie)

[Revista TheMagPi 81 I](https://www.raspberrypi.org/blog/retro-console-with-retropie-raspberry-pi-1/) y [II](https://www.raspberrypi.org/blog/retro-console-with-retropie-raspberry-pi-2/)

[How to download games Rom for retropie](https://raspberrytips.com/download-retropie-roms/)