Vamosa  ver como actualizar de stretch a buster
o
para ello tenemos que modificar la versión a la apuntan los repositorios de 'stretch' a 'buster'. Podemos hacerlo cambiando a mano el ficherois /etc/apt/sources.list and /etc/apt/sources.list.d/raspi.list,

grep -rl stretch /etc/apt/ | sudo xargs sed -i 's/stretch/buster/g'
sudo apt update
sudo apt dist-upgrade
sudo apt full-upgrade

sudo rpi-update

quitamos aplicaciones que ya no están en buster
sudo apt purge timidity lxmusic gnome-disk-utility deluge-gtk evince wicd wicd-gtk clipit usermode gucharmap gnome-system-tools pavucontrol

ahora actualizamos el aspecto con
When the Pi has rebooted, launch ‘Appearance Settings’ from the main menu, go to the ‘Defaults’ tab, and press whichever ‘Set Defaults’ button is appropriate for your screen size in order to load the new UI theme.

https://www.raspberrypi.org/blog/buster-the-new-version-of-raspbian/
