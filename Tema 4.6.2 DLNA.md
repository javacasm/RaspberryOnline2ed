## Servidor multimedia

Sería interesante poder ver en una TV los contenidos multimedia que tenemos en nuestra Raspberry Pi. La mayoría de las TV modernas soporta un protocolo llamado [DLNA](https://es.wikipedia.org/wiki/Digital_Living_Network_Alliance), adoptador por la mayoría de fabricantes de dispositivos multimedia.

Para que nuestra Raspberry comparta los contenidos multimedia almacenados tendremos que instalarle un servidor DLNA. Una opción puede ser si ya tenemos instalado Kodi, activar en Settings > Services > UPnP la opción "Share video and music libraries through UPnP" (UPnP es un servicio más antiguo del que deriva DLNA)

Otra opción es instalar un  servidor DLNA en la Raspberry Pi, es más ligero y podemos seguir usando nuestra Raspberry para otro temas. Lo instalamos con:
```sh
sudo apt update
sudo apt upgrade 
sudo apt install minidlna
 ```

 Ahora editamos el archivo de configuración __/etc/minidlna.conf__ indicando los directorios que queremos compartir con la opción __media_dir__, el tipo de contenido que tienen (V para vídeo, P para imágenes y A para sonido) y con el nombre con el que queremos que se muestre nuestra Raspberry con __friendly_name__.

 Editamos el fichero __/etc/minidlna.conf__ 

 ```sh
sudo nano /etc/minidlna.conf 
```

y lo dejamos así:

```
media_dir=V,/media/myDisk/series # carpeta de tipo Vídeo
media_dir=V,/media/myDisk/pelis # carpeta de tipo Vídeo
media_dir=A,/media/myDisk/musica # carpeta con música
media_dir=PV,/media/myDisk/Fotos # carpeta con fotos y videos

friendly_name=raspi4 # nombre con el que veremos nuesro equipo
```

Donde hemos añadido las carpetas de la Raspberry Pi donde tenemos los contenidos.

Reiniciamos el servicio y listo

```sh
sudo service minidlna restart
sudo service minidlna force-reload 
```

Ahora sólo nos falta buscar en nuestra TV los servicios multimedia de red