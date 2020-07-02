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

Realmente el comando **screen** es mucho más potente y nos permite tener varias sesiones abiertas en una misma ventana de terminal, pudiendo cambiar entre ellos.



