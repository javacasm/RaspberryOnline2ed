## Puesta a punto de entorno de programación con Github

git clone url_repositorio.git

git config --global user.name "javacasm"
git config --global user.email "javacasm@gmail.com"


modificamos  y subimos los cambios con 


git add fichero_cambiado.py

git commit -m "correccion del error de login" ficher.py


Si vamos a trabajar durante bastante tiempo con github nos interesa añadir la firma ssh de la raspberry a github

Para ello necesitamos crear una clave SSH en la raspberry. Siguiendo la [documentación de github](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) hacemos:

```sh
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
y definimos dónde se va a guardar el fichero y si queremos ponerle cable

```sh
> Enter a file in which to save the key (/home/you/.ssh/id_rsa): [Press enter]
> Enter passphrase (empty for no passphrase): [Type a passphrase]
> Enter same passphrase again: [Type passphrase again]
```

(en la raspberry Zero tarda casi más de 1 minuto)

Ejecutamos el ssh-agent con

```sh
eval "$(ssh-agent -s)"
```
y añadimos la key generada

```sh
ssh-add ~/.ssh/id_rsa
```


mostramos por consola el fichero con 

cat ~/.ssh/id_rsa.pub

y lo añaidmos a nuestra cuanta github pulsando "New SSH key" in https://github.com/settings/keys

Si estuvieramos en un entorno visual haríamos:

Instalamos xclip (una utilidad para manejar el clipboard)

```sh
sudo apt-get install xclip
```

y copiamos la key al clipboard

```sh
xclip -sel clip < ~/.ssh/id_rsa.pub
```

Ahora ya podemos trabajar con ssh en github, lo que nos ahorra tener que escribir muchas veces nuestro usuario/password de github

