## Manejando tu Raspberry Pi

Como sabes Raspberry es una máquina Linux, con lo que podrás manejarla igual que se maneja cualquier otra equipo Linux.

### Capturas de la pantalla

Podemos hacer capturas del escritorio usando la tecla ImprimirPantalla si nuestro teclado la tiene o bien usando el comando **Scrot**, que pondrá un fichero con la captura en directorio home del usuario (/home/pi por defecto) con un nombre dado por la fecha, hora y resolución. Por ejemplo "2021-02-26-194221_1024x768_scrot.png".

Podemos hacer que la captura se haga después de un determinado retardo usando la opción **-d**. Por ejemplo para hacer la captura a los 10 segundos. 

```sh
scrot -d 10
```

También podemos darle un nombre concreto al fichero resultado al usar el comando

```sh
scrot ficheroCaptura.png
```

Si necesitamos más opciones podemos instalar un programa como **Gnome Screenshot** que nos dará más opciones. Lo instalaremos como siempre con

```sh
sudo apt install gnome-screenshot
```
Y aparecerá en el menú de "Accesorios"

Nos permitirá capturar todo el escritorio, una ventana, una zona, definiendo un determinado retardo. También nos permite tras hacer la captura seleccionar el nombre y carpeta del fichero o si queremos que se copie la imagen en el clipboard.

![gnome-screenshot](./images/gnome-screenshot.png)


### Consola (línea de comandos)

Podemos hacer casi todo desde el habitual entorno gráfico, pero también desde el terminal o la consola, también llamada líneas de comandos.

Si te acostumbras a usarla verás que ganas en productividad y además verás que puedes automatizar muchas tareas. 

![Consola](./images/console.png)

#### Comandos básicos:

Como ya hemos dicho, Raspbian es una versión de [Linux](https://es.wikipedia.org/wiki/GNU/Linux), que nos más que una versión moderna del sistema operativo [Unix](https://es.wikipedia.org/wiki/Unix). Por esto tenemos acceso a los comandos de esos sistemas operativos.

Veamos algunos de los comandos más utilizados:

* La tecla Tabulador nos permite completar el nombre del fichero/directorio
* **ls** : muestra los archivos y directorios ( **ls -l** para más detalles y **ls -a** para mostrar todos)
* **cd** : cambia de directorio (**cd ~** nos lleva a nuestro directorio home y **cd ..** sale del directorio actual)
* **chmod** : cambia los permisos de un fichero/directorio (**chmod ugo-w fichero** quita todos los permisos de escritura)
* **pwd** : nos dice el directorio actual
* **mv** : mueve directorios/ficheros a un nuevo destino
* **rm** : borra directorios/ficheros
* **mkdir** : crea un directorio
* **passwd** : cambia la contraseña del usuario actual
* **ps -ef** : muestra los procesos en ejecución
* **top** : administrador de tareas
* **clear** : borra todo el contenido del terminal
* **df** : muestra el % de disco ocupado
* **nano** : editor de texto básico
* **vi** : editor de texto avanzado pero complejo
* **du** : muestra lo que ocupa un directorio (**du -s *** muestra lo que ocupa un directorio y todo lo que contiene)
* **sudo halt** apaga la raspberry
* **sudo shutdown -h now** apaga la raspberry
* **history** : muestra todos los comandos que se han ejecutado antes. Podemos ejecutar el comando de la posición n, con !n . Las teclas abajo/arriba del cursor nos permiten iterar por los comandos usados.
* **man comando**: Para obtener ayuda sobre comando
* Para hacer fichero script: añadimos los comandos, chmod u+x fichero y para ejecutarlo ./fichero

[![Vídeo: Uso del terminal y comandos Linux en Raspberry Pi](https://img.youtube.com/vi/BF0Kjb4g454/0.jpg)](https://drive.google.com/file/d/1a2UjGmzv0XXMpadJ1iItbat_ibDuG6Sl/view?usp=sharing)

[Vídeo: Uso del terminal y comandos Linux en Raspberry Pi](https://drive.google.com/file/d/1a2UjGmzv0XXMpadJ1iItbat_ibDuG6Sl/view?usp=sharing)

#### Estructura de directorios y ficheros

Algunas características de sistema de fichero de linux

* Usa un formato de partición ext4 (también existen aunque en desuso el ext3 y el ext2), aunque permite usar FAT, el típico sistema de archivos de Windows.
* El árbol de directorios tiene un único directorio raíz del que cuelga todo. Todos los dispositivos (pen drives, discos externos, discos de red) se integran dentro de este árbol, **montando** su raiz en un directorio determinado (montamos y desmontamos con __mount__ y __unmonut__ )

El usuario sólo acceso a su directorio y el solo el administrador (**root**) puede acceder al resto de directorios

##### Algunos directorios

* / directorio raiz
* /etc configuración
* /home usuario
* /usr programas para usuarios
* /usr/share recursos de programas (imágenes, traducciones)
* /usr/share/doc documentación
* /bin ejecutables del sistema
* /lib librerías
* /boot Arranque del sistema
* /usr/bin ejecutables para usuarios
* /media o /mnt punto de montaje de dispositivos de almacenamiento externo


#### Usuarios

El usuario por defecto es "**pi**" con contraseña "**raspberry**" por defecto

#### Cuidado con sudo

Los usuarios normales pueden hacer muchas cosas, pero las tareas más importantes (y por tanto peligrosas si se hacen mal), como pueden ser la configuración o borrado de ficheros críticos no están permitidas.

Esas tareas sólo las puede hacer el usuario administrador, llamado **root**, que puede hacer cualquier cosa. 

Como hay veces que un usuario necesita hacer alguna de estas tareas, por ejemplo editar un fichero de configuración, podemos solicitar permisos para hacer esa tarea anteponiento al comando la palabra "sudo". Algunas acciones nos pedirán que introduzcamos el password de nuestro usuario como medida de seguridad.	

Por ejemplo si queremos editar un fichero de la carpeta de configuración etc llamado ftab, haremos

```sh
sudo geany /etc/fstab
```
	
geany es el editor de ficheros de texto, y al usar "sudo" estamos pidiendo permiso para hacer algo como root

Esto nos sirve para ver que podemos abrir aplicaciones de escritorio desde la consola.

Si en un momento dado necesitamos hacer muchas tareas como root podemos abrir una consola con este usuario haciendo

```sh
sudo su -
```

Pero mucho cuidado que esto nos da todo el poder del usuario administrador(**root**) y por tanto toda la responsabilidad

### Interface gráfico

Para arrancar el interface gráfico desde consola si no está arrancado usando
```sh
startx
```


![startx](./images/raspX.png)

### Acceso remoto

Algo muy frecuente es que queramos acceder a nuestra Raspberry Pi remotamente, es decir sin un teclado ni monitor conectado directamente. Evidentemente necesitamos tener un SO instalado y habilitar el acceso remoto. Veamos algunas de las formas de hacerlo.

### SSH (vía consola)

SSH es el protocolo de acceso remoto por consola (o terminal). Se suele utilizar cuando no necesitamos (o no tenemos) entorno gráfico. Es una forma de conexión segura (usa encriptación y verificación a ambos lados) utilizada para acceder a router y otros dispositivos remotos

Tenemos que activarlo en la configuración para poder acceder desde fuera.Entramos en la configuración avanzada

```sh
sudo raspi-config
```

![ssh](./images/ssh.png)

Podemos hacerlo también por comandos con

```sh
sudo service ssh start
sudo insserv ssh
```

Ahora podremos conectarnos remotamente con ssh, desde Linux con el comando **ssh** o con otras herramientas que veremos a continuación

```sh
ssh pi@192.189.0.123
```

Si lo vamos a activar se recomienda cambiar la contraseña para evitar que cualquiera pueda acceder a nuestro equipo.

[![Vídeo: Conexión vía SSH a Raspberry Pi](https://img.youtube.com/vi/-BH3spberkc/0.jpg)](https://drive.google.com/file/d/1Eu0yXNhgxUOZj9TjB35dlq-3y1--L4Lq/view?usp=sharing)

[Vídeo: Conexión vía SSH a Raspberry Pi](https://drive.google.com/file/d/1Eu0yXNhgxUOZj9TjB35dlq-3y1--L4Lq/view?usp=sharing)


### Herramientas de conexión ssh

Son muchas la herramientas que exiten para poder conectarnos entre equipos usando SSH, vamos a ver un par de ellas.

#### Putty 


[Putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html) es una herramienta opensource disponible para muchos sistemas operativos pensada para conectar remotamente con equipos usando distintos protocolos como ssh, telnet, serie, etc

![Putty](./images/Putty_0.58_on_fvwm.png)

Permite guardar las credenciales de cada sistema, facilitándo la conexión.

#### JuiceSSH

[JuiceSSH](https://play.google.com/store/apps/details?id=com.sonelli.juicessh) es una herramienta de conexión ssh para móviles y tabletas Android.

También nos permite gestionar las credenciales de acceso y los diferentes equipos a los que conectarnos:

![juicessh1.png](./images/juicessh1.png)

El uso incluso en un móvil es más cómodo de lo que parece, puesto que permite el uso de teclas como TAB, ctrl, cursor, etc.

![juicessh2.png](./images/juicessh3.png)


[![Cliente SSH para móviles y tabletas Android: juicceSSH](https://img.youtube.com/vi/LLiZ52ss2DQ/0.jpg)](https://drive.google.com/file/d/1GG4mscjTBS9VqsDxgyXM6n1UopfQzrIB/view?usp=sharing)

[Cliente SSH para móviles y tabletas Android: juicceSSH](https://drive.google.com/file/d/1GG4mscjTBS9VqsDxgyXM6n1UopfQzrIB/view?usp=sharing)

### Automatizar conexiones

Si vamos a conectarnos frecuentemente a un mismo equipo puede resultar pesado tener que poner siempre usuario y contraseña. 

El protocolo ssh permite automatizarlo sin más que añadir nuestra **clave pública ssh** a la lista de host autorizados del servidor al que nos vamos a conectar, haciendo lo siguiente:

1. Generar nuestra **clave pública ssh**, asociada al usuario y la máquina
```sh
ssh-keygen -t rsa -b 4096 -C user@email.com
```
2. Ahora copiamos nuestra clave pública ssh a 
```sh
cat ~/.ssh/id_rsa.pub | ssh username@server.address.com 'cat >> ~/.ssh/authorized_keys'
```
La siguiente vez que nos conectemos lo haremos sin necesidad de instroducir la clave.

Como podemos ver en el último comando que hemos usado, podemos usar ssh de muchas formas diferentes:
* Para conectarnos de manera interactiva a otro ordenadore
* Para enviar ficheros entre equipos. En proyecto más adelante lo usaremos bastante.
* Para enviar contenido entre equipos como hemos hecho con el comando 'cat'
* Para ejecutar comandos remotamente. Por ejemplo si hacemos
```sh
ssh pi@raspi4 df -h
```
Nos permitirá saber cómo de llenos están los discos en el ordenadore raspi4

```sh
ssh pi@raspi4 df -h
```

### VNC

VNC es un protocolo que nos permite acceder remotamente al escritorio de otra máquina.

En las nuevas versiones de Raspbian podemos activar VNC desde la configuración (o desde raspi-config), en el apartado de Interfaces

### Cambio de resolución del escritorio

Cuando arrancamos una Raspberry Pi sin tener monitor conectado y la tenemos configurada para que se cree el escritorio gráfico suele crearse con una resolución pequeña.

En el siguiente vídeo vamos a ver cómo hacer para modificar esa resolución. No hay más que entrar en Configuración de Raspberry -> Display y pulsar en Set Resolution

[![Vídeo: Cambio resolución del escritorio de una Raspberry Pi](https://img.youtube.com/vi/RWX2UWwgP4I/0.jpg)](https://drive.google.com/file/d/1o8hYMcc-zDuWLMg7_wBSPXxQGDwuB7Np/view?usp=sharing)

[Vídeo: Cambio resolución del escritorio de una Raspberry Pi](https://drive.google.com/file/d/1o8hYMcc-zDuWLMg7_wBSPXxQGDwuB7Np/view?usp=sharing)

#### VNC en equipos antiguos

Si no está disponible en nuestra instalación podemos instalarlo de manera sencilla con:

```sh
sudo apt-get install tightvncserver
```

Este software requiere que un servicio se ejecute al arrancar si queremos acceder en cualquier momento. Podemos instalarlo añadiendo la siguiente línea al archivo **/etc/rc.local**

```sh
su -c "/usr/bin/tightvncserver :1 -geometry 800x600 -depth 16" pi
```

![vnc](./images/vnc.png)

Ahora accederemos usando un cliente vnc, como por ejemplo [VNC Viewer](https://www.realvnc.com/es/connect/download/viewer/) de RealVNC. Si nos creamos una cuenta en RealVNC podremos acceder desde cualquier parte, incluso desde internet, sorteando nuestro router.

![Acceso con cuenta de usuario VNC](./images/VNC_CuentaUsuario.png)

Existen clientes de VNC para teléfonos móviles y tabletas, lo que nos da muchas posibilidades

La conexión por VNC nos permite acceder como si estuvieramos conectados directamente

### Conexión y acceso directo

Vamos a configurar nuestra raspberry y un portátil con Ubuntu para facilitar al máximo la conexión y así no tener que utilizar muchos componentes. De esta manera podremos trastear con un kit mínimo, evitando tener que usar un teclado, ratón y sobre todo un monitor.

![Conexión directa entre Raspberry y Portatil](http://blog.elcacharreo.com/wp-content/uploads/2013/05/20130501_003523-150x150.jpg)

En concreto usaremos símplemente un cable de red (ethernet) y un cable micro-usb para alimentar la raspberry.

Con esta configuración no podemos consumir en total más de los 500mA que proporciona el USB.

Tendremos que modificar ficheros de configuración en el PC y en la raspberry.

Asumiremos que tenemos conexión a internet via Wifi y utilizaremos el cable ethernet para dar conectividad a la raspberry. Crearemos una red entre el portátil y la raspberry creando una subred distinta y haremos que el portátil actúe como gateway de esa red enrutando los paquetes hacia la raspberry y dándole acceso a internet.

Comencemos editando la configuración del pc, para lo que ejecutaremos en el pc:

```sh
sudo vi /etc/network/interfaces
```
y dejamos el contenido del fichero (la red que se usa normalmente es las 192.168.1.x de ahí que el gateway sea 192.168.1.1 que es el real)

![Configuración inicial de la red local](http://blog.elcacharreo.com/wp-content/uploads/2013/05/paso1.png)

Ahora vamos a editar la configuración de la raspberry. La forma más sencilla es editando los ficheros de configuración desde el pc, para lo que insertamos la tarjeta sd de la raspberry (obviamente con esta apagada) en el pc y ejecutamos en este:
```sh
sudo vi /media/10b4c001-2137-4418-b29e-57b7d15a6cbc/etc/network/interfaces
```
Quedando el mismo:

![Configuración final de la red local](http://blog.elcacharreo.com/wp-content/uploads/2013/05/paso2.png)

Ahora, colocamos la tarjeta sd en la raspberry y volvemos a encenderla


Conectamos el cable ethernet entre los dos

En el PC hacemos comprobamos que la tarjeta eth0 está ok y con la ip correspondiente, haciendo

```sh
ifconfig /all
```
Veremos que aparece el interface eth0 con ip 192.168.0.80

Ahora vamos a hacer que el portátil actúe como router. Para ello ejecutamos los siguientes comandos

```sh
sudo su -
root@ubuntu-asus:~# echo 1 > /proc/sys/net/ipv4/ip_forward
root@ubuntu-asus:~# /sbin/iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
```

Por último editamos el fichero de configuración de DNS con
```sh
sudo vi /etc/resolv.conf
```

y lo dejamos así

![Configuración de servidor de nombres](http://blog.elcacharreo.com/wp-content/uploads/2013/05/paso3.png)


Ahora solo falta probar que tenemos conectividad, haciendo un ping
```sh
ping 192.168.0.90
```

Si todo es correcto ya podremos acceder via ssh o  VNC

## Usos

Veamos cómo podemos utilizar lo aprendido...

### Para hacer cálculos con Mathematica

Hay una versión gratuita (para uso no comercial) de Worlfram  Mathematica instalada por defecto en Raspbian

![Mathematica en Raspberry Pi](./images/Mathematica.png)

[![Vídeo: Trabajando con Mathematica en Raspberry](https://img.youtube.com/vi/VVHoREZ8Rc4/0.jpg)](https://drive.google.com/file/d/1oXjMaNmL4gpaTHPePZYbIb6_lRsAGODi/view?usp=sharing)


[Vídeo: Trabajando con Mathematica en Raspberry](https://drive.google.com/file/d/1oXjMaNmL4gpaTHPePZYbIb6_lRsAGODi/view?usp=sharing)


### Vigilancia

Podemos usar su cámara (la original o una USB)

Usaremos un software standard de Linux: **motion**

```sh
sudo apt-get install motion
```

Editamos la configuracion

```sh
sudo nano /etc/motion/motion.conf
```

![usando motion](./images/motion.jpg)

Lo arrancamos
```sh
montion -n
```

Podremos acceder a la imagen en vivo de la cámara con

```sh
http://raspberry_ip:8081
```
 
