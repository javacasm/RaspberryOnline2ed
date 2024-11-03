[Configuración visual (desde teclado) de red](https://raspberrytips.com/nmtui-linux-command)

[Usar OpenCV](https://www.luisllamas.es/como-usar-opencv-en-raspberry-pi/)

## Recursos

https://eduengteam.com/2024/08/7-hidden-raspberry-pi-resources-you-must-discover.html


## Raspberry Pi 5

[Raspberry 5 vs 4](https://raspberrytips.com/raspberry-pi-5-vs-pi-4/)

## Versiones Raspberry

https://www.raspberrypi.com/documentation/computers/raspberry-pi.html


## Virtual env 
Thonny y VSCode
## Cámara

Efectivamente en las últimas distribuciones han roto la compatibilidad con las cámaras y está pendiente de ver si lo dejan así, vuelven a la versión anterior o intentan algo nuevo.

Sí que se puede usar OpenCV y creo que se puede activar un modo "Legacy" para poder usar la cámara, pero todo está a expensas de que una actualización no lo rompa.

En mi opinión la fundación Raspberry Pi ha cometido un error al dejar todo esto tan indefinido y romper con todo el software que funcionaba anteriormente.


## Uso de los pines


Como se trata de un curso inicial y no se presupone conocimiento de electrónica he preferido ser un poco alarmista en cuanto a los avisos. Efectivamente se puede estropear una Raspberry si hacemos malas conexiones en los pines o si usamos un sensor que produzca una señal de 5V en las patillas de entrada, pero teniendo un poco de cuidado al elegir los componentes y al hacerlos se pueden hacer montajes, y se pueden conectar multitud de componentes. 

La placa intermedia aísla los dos circuitos y adapta los niveles. Efectivamente podemos usar Arduino, ESPs o cualquier otra placa. 

A lo largo del curso verás montajes que conectan en los pines directamente, pero no quiero que nadie se lance a hacerlo en el capítulo 1 ni tener suficientes conocimientos ni precaución.

https://www.tomshardware.com/how-to/control-raspberry-pi-5-gpio-with-python-3

https://randomnerdtutorials.com/raspberry-pi-digital-outputs-python/

https://projects.raspberrypi.org/en/projects/physical-computing/0

## Acceso remoto

Ya que VNC no está disponible de forma gratuita desde internet

https://raspberrytips.com/raspberry-pi-connect-tutorial/

Efectivamente hace unos días que VNC ha dejado de ser útil para acceder desde internet. Ahora puedes usar [https://connect.raspberrypi.com/](https://connect.raspberrypi.com/)

## Mejoras

Log2RAM para mejorar la vida/salud de la SD https://raspberrytips.com/install-log2ram-raspberry-pi

https://raspberrytips.com/snap-store-raspberry-pi/

https://raspberrytips.com/add-ram-on-raspberry-pi/

### Proyectos 

https://eduengteam.com/2024/08/unleash-your-creativity-7-must-try-raspberry-pi-projects.html


https://raspberrytips.com/android-tv-on-raspberry-pi



## PINN el nuevo Noobs

No he probado [PINN](https://github.com/procount/pinn) ni se incluye en el curso, pero voy a investigarlo para intentar incluirlo. De todas formas no lo veo un producto maduro como para usarlo en "producción".  

Yo también tengo mi Raspi5 con un disco M2 de 256GB, pero de momento sólo uso Raspberry OS y a día de hoy prefiero hacer las pruebas con tarjetas SD y no arriesgar el sistema del M2.
 
## Disco SSD y shield
## Boot USB
[boot Raspberry Pi 5 from USB](https://bret.dk/usb-boot-on-the-raspberry-pi-5/)

## Python

[Entornos virtuales en Raspberry Pi](https://raspberrytips.com/python-virtual-environments/)
## Syncthing

Para que arranque automáticamente
En Raspberry pi sudo systemctl enable syncthing@pi.service ([doc](https://forum.syncthing.net/t/auto-start-syncthing-on-raspberry-pi/14537/8))

## Ver espacio ocupado

[Baobab](https://raspberrytips.com/raspbian-free-disk-space/)

![[Raspberry-pi-baobab.png]]