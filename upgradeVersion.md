### Actualización de una versión a la siguiente

Aunque es conveniente que cuando salga una nueva versión hagamos una instalación desde cero, a veces tenemos muchas aplicaciones instaladas o mucha información del usuario que nos llevaría mucho tiempo extraer y luego volver a copiar/installar. En ese caso nos podemos plantear hacer una actualización de una versión a otra.

Vamos a ver un ejemplo de cómo actualizar de una versión del SO a la siguiente. En este caso particular cómo pasar de "Stretch" a "Buster".

1. Modificamos la versión a la apuntan los repositorios de 'stretch' a 'buster'. Podemos hacerlo cambiando a mano el ficheros **/etc/apt/sources.list** y **/etc/apt/sources.list.d/raspi.list** o con un comando como el siguiente:

```sh
grep -rl stretch /etc/apt/ | sudo xargs sed -i 's/stretch/buster/g'
```
2. Actualizamos el sistema completamente:

```sh
sudo apt update
sudo apt dist-upgrade
sudo apt full-upgrade
```
3. Actualizamos los firmwares:

```sh
sudo rpi-update
```

4. Quitamos aplicaciones que ya no están en buster
```sh
sudo apt purge timidity lxmusic gnome-disk-utility deluge-gtk evince wicd wicd-gtk clipit usermode gucharmap gnome-system-tools pavucontrol
```
5. Ahora actualizamos el aspecto con la nueva configuración visual abriendo ‘Appearance Settings’ y en la pestaña ‘Defaults’ pulsamos ‘Set Defaults’ lo que debería ponernos un tamaño de fuente y de iconos acorde a la resolución usada.


#### Recursos
[Fuente](https://www.raspberrypi.org/blog/buster-the-new-version-of-raspbian/)
