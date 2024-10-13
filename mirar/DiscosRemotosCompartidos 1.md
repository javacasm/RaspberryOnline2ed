## Montar disco externo

Vamos a ver cómo podemos acceder a un disco externo que se ha compartido desde otra máquina. Usaremos en el ejemplo una unidad de un servidor NAS que se comparte con protocolo Samba(compatible con windows) y que está compartida con el nombre "Discos" desde la ip 192.168.1.210

Instalamos Samba y todos sus componentes clientes

```sh
sudo apt install samba samba-common-bin
sudo apt install smbclient
```

Ahora creamos el directorio donde montaremos la unidad remota, que llamaremos con mucha imaginación "discos"

```sh
sudo mkdir /media/discos
```

Hacemos propietario del directorio  al usario "pi" para que pueda acceder

```sh
sudo chown pi.pi /media/discos
```

Para acceder necesitamos saber un usuario válido (javacasm en nuestro ejemplo) para acceder al disco remoto y su contraseña:

```sh
sudo mount -t cifs //192.168.1.210/Discos /media/discos -o user=javacasm,password=ContraseñaCompartida
```

Para hacerlo permamente vamos a añadir el directorio al fichero fstab, donde se guardan las unidades que se van a montar por defecto

```sh
sudo nano /etc/fstab
```

Donde añadiremos una línea al final como la siguiente

```
//192.168.1.210/discos   /media/discos    cifs   user=javacasm,password=ContraseñaCompartida 0 0
```

Si no queremos poner nuestra contraseña en claro podemos poner nuestro usuario y contraseña en un fichero, por ejemplo en /home/pi/.smbcredentials con el siguiente contenido:

```
username=username
password=password
```

y le cambiamos los permisos para que sólo sea legible por nosotros con:

```
chmod 600 ~/.smbcredentials
```

y ahora cambiamos el fichero fstab con

```
//192.168.1.210/discos   /media/discos    cifs   credentials=/home/pi/.smbcredentials  0  0
```

## Cómo compartir discos locales

Vamos a ver ahora cómo compartir una carpeta local. Necesitamos tener instalado samba, como hicimos en el apartado anterior.

Instalamos Samba y todos sus componentes clientes

```sh
sudo apt install samba samba-common-bin
```

Ahora editamos el fichero de configuración smb.conf.

Primero hacemos una copia del original:

```
sudo cp /etc/samba/smb.conf /etc/samba/smb.conf.old
```

Y lo editamos 

```
sudo nano /etc/samba/smb.conf
```

Y añadimos un bloque con el directorio que queremos compartir

```
[share]
    comment = directorio compartido
    path = /media/directorio
    writeable = yes # quien acceda puede escribir
    guest ok = no # sólo usuarios autentificados
    create mask = 0777
    directory mask = 0777
    force user = pi # ha de ser el usuario "pi"
```

Establecemos la contraseña del usuario "pi" para samba con

```sh
sudo smbpasswd -a pi
```

Ahora rearrancamos el servicio:

```sh
sudo systemctl restart smbd
```

