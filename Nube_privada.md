Onwcloud

## Usando SQLite

Actualizamos

```sh
sudo apt update
sudo apt upgrade
```

Requsitos https://doc.owncloud.org/server/10.4/admin_manual/installation/manual_installation.html#prerequisites

Instalamos apache, php5, curl (Se están usando las ultimas versiones de php a día de hoy 7/5/2020)
```sh
sudo apt-get install apache2 php7.3   php7.3-json php7.3-xml php7.3-gd php7.3-sqlite3 curl libcurl4  php7.3-curl php7.3-common php7.3-zip php7.3-xml php7.3-intl 
```
Descargamos la ultima version de owncloud
wget https://download.owncloud.org/community/owncloud-10.4.1.tar.bz2

Descargamos el fichero md5

wget https://download.owncloud.org/community/owncloud-10.4.1.tar.bz2.md5
  
Comprobamos la integridad del fichero

md5sum -c owncloud-10.4.1.tar.bz2.md5 <  owncloud-10.4.1.tar.bz2



![Check_md5_owncloud](./images/Check_md5_owncloud.png)


Descomprimimos

tar xvf owncloud-10.4.1.tar.bz2 

copiamos el contenido en el directorio raiz del servidor apache

sudo cp -r owncloud /var/www/


Creamos el fichero de configuracion del sito en 

```sh
/etc/apache2/sites-available/owncloud.conf
```
con 

```sh
sudo nano /etc/apache2/sites-available/owncloud.conf
```
Poniendo el siguiente contenido

```xml
Alias /owncloud "/var/www/owncloud/"

<Directory /var/www/owncloud/>
  Options +FollowSymlinks
  AllowOverride All

 <IfModule mod_dav.c>
  Dav off
 </IfModule>
</Directory>
```

y ahora creamos un enlace a  /etc/apache2/sites-enabled con 

```sh
sudo ln -s /etc/apache2/sites-available/owncloud.conf /etc/apache2/sites-enabled/owncloud.conf
```

Ahora comprobamos que tenemos todos los módulos  necesarios de apache activos y reiniciamos el servidor apache

```sh
sudo a2enmod headers
sudo a2enmod env
sudo a2enmod dir
sudo a2enmod mime
sudo a2enmod unique_id 
sudo systemctl restart apache2
```


Probamos a acceder

http://raspi4/owncloud/


![firstown Cloud](./images/firstownCloud.png)


https://geekytheory.com/tutorial-raspberry-pi-crea-una-nube-privada-con-pydio
http://www.electroensaimada.com/owncloud.html#

## Usando MariaDB o MySQL


https://computerhoy.com/noticias/tecnologia/haz-raspberry-pi-sea-nube-personal-412645
https://blog.desdelinux.net/convierte-tu-raspberry-pi-en-una-nube-personal-con-owncloud/


