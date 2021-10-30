## Trabajando y Programando en la misma Raspberry

En el desarrollo de cualquier proyecto necesitamos hacer muchas pruebas, y a veces lo más sencillo es hacer las correcciones sobre nuestro código rápidamente para volver a probar.

La Raspberry tiene una capacidad suficiente para que trabajemos directamente en ella, con lo que en muchos casos podemos conseguir un ciclo de trabajo Programación->Test->Corrección/Mejoras de una forma ágil.

Vamos a ver cómo prepar un entorno de trabajo en una raspberry pi desde la consola, sin necesidad de escritorio.

### Sincronización remota

Cuando trabajamos en local necesitamos un sistema que nos permita sincronizar con el exterior. Podemos usar una solución como la de OwnCloud que vimos anteriormente.

También podemos trabajar con git/Github, un estándar de hecho en los sistemas de gestión de versiones Open Source. Git permite sincronizar archivos y es capaz de mezclar los cambios incluso cuando diferentes personas han modificado un mismo fichero.

#### Puesta a punto de entorno de programación con Github

Instalamos la herramientas de git

```sh
sudo apt install git
``` 

Ahora vamos a ver cómo clonar un repositorio remoto. 
* Si el repositorio no es nuestro, pero queremos modificarlo, crearemos un Fork (copia) pulsando el botón Fork. A partir de este momento trabajaremos con nuestra copia.
* Obtenemos la url del repositorio en la página de github, pulsando el botón verde "Code". Obtendremos algo parecido a esto:
```
https://github.com/usuario/Repositorio.git
```
* Ahora clonamos el repositorio:
```sh
git clone https://github.com/usuario/Repositorio.git
```

Ya podemos trabajar sobre los ficheros. 

Antes de enviar nuestros cambios al repositorio tenemos que definir en el entorno nuestro usuario de github
```sh
git config --global user.name "usuario"
git config --global user.email "usuario@mail.com"
```

Ahora vamos a definir los cambios que vamos a enviar:
* Si hemos creado ficheros nuevos los añadimos a git con
```sh
git add fichero_nuevo1 fichero_nuevo2 ....
```
Y ahora preparamos el lote de cambios o hacemos un Commit en lenguaje de git:
```sh
git commit -m "Comentario explicando los cambios" fichero_nuevo1 fichero_nuevo2 
```

Podemos hacer todos los lotes que queramos, dado que se suelen agrupar los cambios por el tema/motivo del cambio o la funcionalidad.

Cuando queramos sincronizar con github hacemos un push (empujar)
```sh
git push
```
Nos pedirá nuestro usuario y contraseña de github y se enviarán los cambios.

### Actualización del contenido local

Si en alguna ocasión el contenido local se ha quedado retrasado con lo que hay en el servidor podemos volver a sincronizar con 
```sh
git pull
``` 

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

## Ejecutar scripts en background

Si nos conectamos por una terminal, vía ssh, y ejecutamos, al desconectarnos se dejará de ejecutar todo aquello que ejecutamos de forma interactiva.

Una alternativa para que se queden en ejecución nuestros scripts es usar el comando **screen** que nos permite que nuestra sesión shell se siga ejecutando  cuando salimos.

Cuando volvamos a conectarnos podemos volver a conectarnos a esa sesión que dejamos

Lo instalamos con:

```sh
sudo apt install screen
```

Tras conectanos la primera vez ejecutamos **screen**, nos mostrará la ayuda y las correspondientes licencias, tras pulsar Space salimos a una shell normal

Ahora ejecutamos los scripts que queramos y cuando queramos desconectarnos pulsamos **Ctrl-A Ctrl-D** dejando todo en ejecución

Cuando queremos recuperar esta sesión hacemos **screen -R** y volvemos a conectarnos

Realmente el comando **screen** es mucho más potente y nos permite tener varias sesiones abiertas en una misma ventana de terminal, pudiendo cambiar entre ellos. Podemos crear una sesión nueva con **Ctrl-A Ctrl-C** pudiendo pasar de una sesión a la siguiente con **Ctrl-A Ctrl-N**


[![Vídeo: Usando el comando 'screen' para dejar un script en ejecución (background)](https://img.youtube.com/vi/_BcIQ1eEFQs/0.jpg)](https://drive.google.com/file/d/12IKnmcK-hqesS2_904uY9zGTQLhnfC5i/view?usp=sharing)

[Vídeo: Usando el comando 'screen' para dejar un script en ejecución (background)](https://drive.google.com/file/d/12IKnmcK-hqesS2_904uY9zGTQLhnfC5i/view?usp=sharing)

