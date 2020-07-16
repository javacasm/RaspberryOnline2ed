# Bot de telegram

Vamos a crear un sencillo Bot de Telegram que nos va a permitir interaccionar remotamente con nuestra Raspberry. 

Ventajas de usar Bot de Telegram:
* Nos resuelve el problema de acceso a nuestro sistema desde cualquier parte
* Utiliza encriptación en las comunicaciones
* Podemos utilizar clientes de telegram en móviles, tabletas, PC, incluso desde un navegador
* Nos proporciona un sistema de control de

Nuestro Bot de Telegram con Raspberry podrá hacer lo siguiente:
* Envía datos
* Comprueba que el usuario está autorizado
* Recibe y ejecuta comandos
* Envía ficheros
* Envía imágenes


### Instalación

Instalamos las librerías de python para trabajar con telegram


```bash
sudo apt install python3-pip

pip3 install python-telegram
pip3 install python-telegram-bot

```

Descargamos el [código base](https://github.com/javacasm/telegramBotBase) en el [zip](https://github.com/javacasm/telegramBotBase/archive/master.zip) o clonando el repositorio

```sh
git clone https://github.com/javacasm/telegramBotBase.git
```

### Creación de nuestro Bot

Para usar un bot tenemos que darlo de alta en la red Telegram. Eso se hace "hablando" con @botfather (sí, yo también pienso que los programadores de Telegram son unos cachondos)

![BotFather-Icon.jpg](./images/BotFather-Icon.jpg)

1. Iniciamos un chat con @BotFather
2. Solicitamos la creación de un nuevo Bot con

```
/newbot
```

Ahora @BotFather nos irá pidiendo datos y damos un nombre (puede ser cualquier cosa pero tiene que estar libre) y un nombre de bot que tiene que terminar en 'bot' y que ha de ser distinto a todos los existentes. 

Cuando lo tengamos definido nos va a dar token para acceder al API y la dirección para acceder al bot.

Si queremos podemos entrar en la versión web de telegram [**web.telegram.org**](http://web.telegram.org) en la máquina donde vamos a usar el bot y validamos nuestro inicio de sesión con el código que se nos enviará. De esta manera tenemos acceso al Token para poder usarlo.

Vamos a empezar por el ejemplo echoBot, que repite lo que le decimos. He modificado lévemente el codigo para que en caso de que el mensaje sea "hi" conteste con un mensaje especial usando el nombre del usuario 

[echobot](./codigo/echobot.py)


Ahora tenemos que **sustituir nuestro token del canal en el código**

Para copi



### Añadiendo funcionalidad

Vamos a añadir unos comandos básicos para nuestra Raspberry

PAra ver la temperatura de la raspberry 
vcgencmd measure_temp

Para ver el estado de Throttle 
vcgencmd get_throttled

En el proyecto de TimeLapse añadiremos la funcionalidad de enviar ficheros e imágenes


### Ejemplos de Bots:

[Bot basico que enciende un led](https://www.hackster.io/Salmanfarisvp/telegram-bot-with-raspberry-pi-f373da)

[Control de plantas en la terraza](https://www.hackster.io/zenofall/community-iot-garden-using-raspberry-pi-and-telegram-bot-ef4989) https://zenofall.com/iot-robot-using-bluetooth-communication-between-raspberry-pi-and-microbit/

[Control de acceso con alarma de cámara](https://www.hackster.io/wia/security-system-w-motion-sensor-camera-wia-raspberry-pi-07e15e)

[Control de GPIO y camara con telegram](https://www.hackster.io/idreams/control-gpio-and-pi-camera-using-raspberry-pi-telegram-app-3a776a) [Código telegram](https://github.com/vysheng/tg) [Codigo bot](https://gist.github.com/idreamsi/2972ba872df05cb5f0c3)

[Bot de telegram en python](https://medium.com/@goyoregalado/bots-de-telegram-en-python-134b964fcdf7)


## Bot python for telegram
[Bot python for telegram](https://github.com/python-telegram-bot/python-telegram-bot) 
[Web](https://python-telegram-bot.org/)
[Documentation](https://python-telegram-bot.readthedocs.io/en/stable/)   
[Examples](https://github.com/python-telegram-bot/python-telegram-bot/tree/master/examples) 

