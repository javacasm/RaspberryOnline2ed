## Nube privada con SyncThing

![Syncthing logo](https://syncthing.net/img/logo-horizontal.svg)

[SyncThing](https://syncthing.net/) es una aplicación open source disponible para la mayoría de los sistemas operativos, Windows, Linux, Android, MacOS, ... de forma gratuita y también para alguna en forma de pago como por ejemplo para los iPhone/iPad. Su [código fuente](https://github.com/syncthing/) está accesible y además dispone de una [gran documentación](https://docs.syncthing.net/) tanto técnica como para el usuario normal.

Syncthing permite la sincronización de contenidos, compartiendo carpetas entre diferentes dispositivos. Para ello, todos los equipos deben estar conectados, tener instalada la aplicación Syncthing y que ésta se esté ejecutando.

No es necesario que los equipos estén en la misma red, puesto que Syncthing utiliza unos servidores en internet (relay) a los que se conecta siempre la aplicación para localizar los equipos. Una vez que dos equipos se han "encontrado", la comunicación se hará por el método más eficiente: si están en la misma red se hará una conexión directa y si no es posible se utilizarán los servidores de relay para enrutar el tráfico.

Actúa de forma descentralizada es decir, el almacenamiento en la nube se consigue por medio de los diferentes equipos que han de estar conectados para que los ficheros estén disponibles, no existe un almacenamiento centralizado. Por esto decimos que es una red P2P (Peer 2 Peer) o punto a punto.

![Red centralizada vs red descentralizada](./images/arquitectura_centralizada_vs_deslocalizada.png)

Por ejemplo, si comparto una carpeta entre mi portátil y el móvil, para el móvil pueda sincronizar el contenido,  necesito que el portátil  esté encendido, conectado y ejecutando Syncthing

Para resolver esto, y que tus  contenidos más importantes  estén siempre disponibles, vas a necesitar que un ordenador esté permanentemente conectado.  Sólo tienes que instalar Syncthing en una Raspberry Pi y que ésta esté encendida todo el tiempo compartiendo esos contenidos.
### Instalación

La instalación es muy sencilla simplemente tenemos que:

* Descargar la aplicación desde la [página de descargas de Syncthing](https://syncthing.net/downloads/) en los equipos que queramos que  compartan contenido. En el caso de la Raspberry Pi descargaría la versión "ARM (64-bit)" que instalaremos

	![](./images/Página%20de%20descargas%20de%20syncthing.png)

* En la Raspberry Pi podemos hacerlo con 1 solo comando, instalando el servicio Synthing y la aplicación de configuración (el servicio incluye la opción de configuración web sin necesidad de aplicación de configuración)

```sh
	sudo apt install syncthing syncthing-gtk
```

Lo que nos va crear 3 entradas en el menú "Internet"

![Menús referentes a Syncthing](./images/syncthon_iconos_menu.png)

1.  **Start Syncthing** arranca la aplicación para poder compartir y ver lo que otros equipos han compartido. Cuando se ejecuta lo hace como  servicio, es decir, no vemos una ventana de aplicación, si no que se está ejecutando en segundo plano. 
2. **Synthing GTK** arranca la aplicación de configuración de escritorio 

	![Aplicación de escritorio de configuración de Syncthing](./images/syncthing_configuracion_gtk.png)
	
	Para ir comprendiendo la interfaz, en verde vemos los recursos disponibles, en gris lo que no.

3. **Syncthing Web UI**  abre la configuración del servicio Syncthing en un navegador web.
	
	![Configuración de Syncthing en versión web](./images/syncthing_configuracion_web.png)

La configuración es la misma independientemente de que usemos la versión aplicación o web. Personalmente encuentro más cómoda la versión web. 

Veamos el interfaz y luego el proceso para compartir contenidos:

1. Menú con las diferentes acciones que podemos hacer
2. Configuración y detalles del servicio en nuestro ordenador
3. Otros dispositivos conocidos con Syncthing y su estado. Si pulsamos sobre uno de ellos veremos los detalles

	 ![Detalles equipo syncthing](./images/syncthing_detalles_equipo.png)

4. Carpetas compartidas. Si pulsamos sobre ella veremos sus detalles.

	![Detalles de una carpeta compartida](./images/syncthing_folder_properties.png)
## Dispositivos

Antes de compartir contenidos tenemos que conectar con los otros equipos. Veamos cómo funciona antes de hacerlo.

Todo dispositivo está identificado con un ID, un  dato alfanumérico bastante largo y que lo va a identificar de forma única. Se suele ver mostrar  la primera parte como identificador  y  un pequeño icono asociado formado por el ID en formato binario, para que sea fácil de reconocerlo.

![](./images/syncthing_device_details.png)

Cuando lo damos de alta, asociamos a ese ID un nombre que será el que veamos.

También tienen asociado un código QR que podemos visualizar en pantalla y escanear desde otros dispositivos móviles.

![](./images/syncthing_device_QR.png)

Para que los dispositivos se conozcan entre sí podemos hacerlo de varias formas:

* Podemos escanear la red automáticamente, la aplicación siempre busca a ver si hay disponibles otros  
* Podemos añadir directamente el ID. En dispositivos móviles  se puede escanear el QR con la cámara.

Cuando ejecutamos una nueva aplicación SyncThing en una red, automáticamente va a buscar si existieran otros dispositivos y nos propondrá si queremos añadirla a nuestra lista de dispositivos.

Cuando nosotros añadimos un dispositivo no tiene que estar en nuestra red,  simplemente al añadir el ID se buscará 

En la zona de de dispositivos de nuestra aplicación aparecerán todos aquellos que se conocen entre sí y indicando si están disponibles online o no

Para empezar a compartir lo primero que tenemos e

* Tenemos que identificar cada uno de los equipos en la red que tendrán un código de identificación y que los demás dispositivos con los que vamos a compartir archivos han de conocer si estamos trabajando en una red local se produce un autodescubrimiento decirse detectan uno a otro y si no lo que podemos es pasar la información el código de identificación que también se puede pasar por en formato de código QR
* Los contenidos que queramos compartir se organizan en carpetas compartidas a las que seleccionamos a qué dispositivo queremos y qué dispositivo las tengan accesibles
* Se puede elegir si un dispositivo publica contenido o solo lo recibe
* Y también se pueden activar diferentes opciones en cuanto al versionado de ficheros se puede hacer que se mantengan distintas versiones o bien que solamente se guarde la última edición
### Cómo se comparten los contenidos

Para compartir una nueva carpeta en el botón **+Agregar Carpeta** debajo de todas las carpetas compartidas en la versión Web

O en la opción correspondiente tras pulsar el botón **+** en la aplicación de configuración:
![](./images/syncthing_add_folder_app.png)

En la pestaña **General**

![](./images/syncthing_create_shared_folder.png)
1. La etiqueta es el nombre con el que veremos la carpeta compartida
2. El ID es un código con el que identificamos de manera unívoca la carpeta. Personalmente le suelo añadir la etiqueta de la carpeta para reconocerla más fácilmente. El ID es muy importante y servirá para identificar dos carpetas compartidas por dos servidores como un mismo contenido.
3. La ruta donde se almacenan localmente los ficheros compartidos

En la pestaña **Compartiendo** marcaremos los dispositivos con los que queremos compartir la carpeta (en cualquier momento podemos modificarlo, añadiendo o quitando dispositivos de la lista)

![](./images/syncthing_add_folder_sharing.png)

En la pestaña de **Versionado de ficheros** podemos elegir qué tipo de versionado de ficheros queremos para esta carpeta, desde "Sin versionado", en el que sólo se guardará la última versión hasta un versionado profesional con una herramienta externa que tendremos que configurar.

![](./images/syncthing_versioning_folder_setting.png)

Si marcamos alguno de los intermedios, se conservarán copias de las distintas versiones en la carpeta .stversions por defecto (aunque podemos establecer otra carpeta) cuando sean reemplazados o borrados. También podemos establecer un número de días tras los que se borraran las versiones antiguas o un número máximo de versiones que se guardarán.

También podemos establecer patrones de nombres que se ignorarán, como por ejemplo las copias de seguridad que hacen algunos programas o carpetas temporales en la pestaña **Patrones a ignorar**

En la pestaña **Avanzado** vamos a encontrar una gran cantidad de opciones, como por ejemplo:

* Si queremos que se realice un monitoreo contante de cambios
* Cada cuando tiempo se vuelve a escanean la carpeta completa 
* El **Tipo de carpeta** 
* Si se sincronizan permisos o datos sobre el propietario de los archivos

Si dejamos de compartir una carpeta, lo ficheros seg uirán disponibles localmente, en ningún caso se borrarán.
## Conflictos

A veces ocurre que por falta de disponibilidad de alguna de esas carpetas online, dos ordenadores modifican un mismo fichero sin tener en cuenta los cambios del otro. Cuando vuelvan a estar disponibles online se van a generar duplicados de los archivos, cada uno con las diferentes versiones, para evitar la pérdida de los cambios. El nombre de estos ficheros duplicados será __fichero_sync-conflict-fecha-IDequipo__. Tendremos que resolver manualmente los cambios.

### Syncthing para móvil y tablets

Existe una versión de syncthing para dispositivos Android, pero debido a problemas de mantenimiento y a la dificultad de publicar aplicaciones en Google play, [en breve desaparecerá](https://forum.syncthing.net/t/discontinuing-syncthing-android/23002).

En la aplicación Android tenemos que establecer cada carpeta que recibimos para compartir  estableciendo dónde se va a almacenar y también hay que darle permisos de acceso a esa carpeta.

Por defecto en el móvil solo se sincronizará si estamos conectados a un wifi y podemos seleccionar aquellos wifi en los que queremos que esté activo. Evidentemente el que esté activo implica un mayor consumo de batería .

Para iPad  existe una [aplicación de pago](https://mobiussync.com/)  que personalmente ya lo he amortizado solamente con un par de viajes. Además la empresa que comercializa la versión para para iPad soporta económicamente el desarrollo de syncthing.
