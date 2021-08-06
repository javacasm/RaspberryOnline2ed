
## Montar disco externo



montar discos remotos

fstab

sudo apt install smbclient


sudo mkdir /media/discos

sudo chmown pi.pi /media/discos



sudo mount.cifs //<IP>/public /home/pi/Shared/ -o user=pi,password=<PW>

sudo mount -t cifs -o user=javacasm,password=Patatin55,vers=3.0 //192.168.1.210/discos /media/discos


sudo nano /etc/fstab



//192.168.245.150/share   /media/pi/BufNAS    cifs   credentials=/root/.cifuser,nofail,vers=1.0,x-systemd.automount 0 0


then enter your username and password into the file

username=username
password=password
save the file and change its permissions so it is not readable by others.

chmod 600 ~/.smbcredentials
then edit as root the fstab to add your samba share

//server/share  /mnt/abc cifs credentials=/home/pi/.smbcredentials  0  0


## compartir discos locales


Instalamos Samba


sudo apt-get install samba samba-common-bin



sudo cp /etc/samba/smb.conf /etc/samba/smb.conf.old


sudo nano /etc/samba/smb.conf



[share]
comment = Share
path = "/media/USBHDD/share"
writeable = yes
guest ok = yes
create mask = 0777
directory mask = 0777
force user = pi


sudo systemctl restart smbd


https://lefkowitz.me/setup-a-network-share-via-samba-on-your-raspberry-pi/


Cómo acceder remotamente a los discos exportados


