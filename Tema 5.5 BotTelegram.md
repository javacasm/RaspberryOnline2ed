# Bot de telegram

Una de las funcionalidades más interesantes de Telegram es el uso de Bots, unos sencillos programas que permiten interactuar con dispositivos usando la plataforma de comunicaciones.

Vamos a crear un sencillo Bot de Telegram que nos va a permitir interaccionar remotamente con nuestra Raspberry. 

Ventajas de usar Bot de Telegram:
* Nos resuelve el problema de acceso a nuestro sistema desde cualquier punto de internet sin tener que tocar nuestro router
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
### Creación de nuestro Bot

Para usar un bot tenemos que darlo de alta en la red Telegram. Eso se hace[ "hablando" con @botfather](https://www.instructables.com/id/Set-up-Telegram-Bot-on-Raspberry-Pi/) (sí, yo también pienso que los programadores de Telegram son unos cachondos)

![BotFather-Icon.jpg](./images/BotFather-Icon.jpg)

1. Iniciamos un chat con @BotFather
2. Solicitamos la creación de un nuevo Bot con

```
/newbot
```

Ahora @BotFather nos irá pidiendo datos y damos un nombre (puede ser cualquier cosa pero tiene que estar libre) y un nombre de bot que tiene que terminar en 'bot' y que ha de ser distinto a todos los existentes. 

Cuando lo tengamos definido nos va a dar token para acceder al API y la dirección para acceder al bot.

Necesitaremos un API TOKEN para cada instanacia o tipo de bot que queremos tener en ejecución. Yo personalmente tengo uno por cada proyecto que tengo en funcionamiento más un par de TOKENs que uso para pruebas.

Si queremos podemos entrar en la versión web de telegram [**web.telegram.org**](http://web.telegram.org) en la máquina donde vamos a usar el bot y validamos nuestro inicio de sesión con el código que se nos enviará. De esta manera tenemos acceso al Token para poder usarlo.

Vamos a empezar por el ejemplo [echobot](https://github.com/javacasm/RaspberryOnline2ed/blob/master/codigo/echoBot.py), un ejemplo de Bot de Telegram que repite lo que le decimos. He modificado lévemente el codigo para que en caso de que el mensaje sea "hi" conteste con un mensaje especial usando el nombre del usuario 

Ahora tenemos que **sustituir nuestro token del canal en el código** de echobot.py y lo ejecutamos con 
```sh
python3 echoBot.py
```

Ahora podremos conectarnos desde cualquier aplicación Telegram, bien con la URL o bien buscando el nombre de nuestro Bot

### BaseBot

He preparado un ejemplos sencillo de Bot que ya incluye la mayoría de las funcionalidades que necesitamos en este y en los siguientes proyectos. Las dintintas funcionalidades están separadas en ficheros para así estructurar mejor nuestro código.

Descargamos el [código base](https://github.com/javacasm/telegramBotBase) en el [zip](https://github.com/javacasm/telegramBotBase/archive/master.zip) o clonando el repositorio

```sh
git clone https://github.com/javacasm/telegramBotBase.git
```

Ponemos nuestro Token en el fichero config.py y lo ejecutamos con 

```sh
python3 baseBot.py
```
Debemos ver en la pantalla de la consola un mensaje similar a este:
```
16/07/2020 13:46:00 Bienvenido al Bot de ejemplo 0.9.5
```

Ahora nos conectamos desde alguna aplicación Telegram, bien con el enlace o buscando el nombre de nuestro Bot

Al escribirle no tendremos respuesta, puesto que no hemos incluido nuestro usuario como autorizado y en la consola veremos un error similar a este:
```
16/07/2020 13:48:44 User: Javacasm not allowed. Chat_id 31416 command: Aaa. Will be reported
```

Ahora debemos incluir este chat_id, que identifica al usuario en el fichero config como **ADMIN** o en la lista de **ALLOWED_USERS**

Paramos el bot y lo volvemos a ejecutar.

Al volver a entrar ahora debe respondernos a nuestros comandos.

Si enviamos **/start** nos mostrará un teclado con los comandos posibles
### Añadiendo funcionalidad

Vamos a ver cómo añadir comandos a nuestro Bot.

Por ejemplo un comando **/Temp** pAra ver la temperatura de la raspberry. Cuando recibamos ese comando ejecutaremos **vcgencmd measure_temp** devolviendo el resultado.

* Añadimos la función **executeCommand** antes de la función main
```python
def executeCommand(command): 
    stream = os.popen(command) 
    output = stream.read() 
    return output

```
* Añadimos el código que procesa el comando **/Temp** antes del else del final de baseBot.py (cuidado con respetar el número de espacios para que quede alineado)
```python
            elif comando == '/Temp':
                answer = executeCommand('/opt/vc/bin/vcgencmd measure_temp')
                utils.myLog(answer)
                update.message.reply_text(answer,parse_mode=telegram.ParseMode.MARKDOWN,reply_markup = user_keyboard_markup)
            else:

```

* En la línea donde definimos los posibles comandos cambiamos un **/ejemplo** por **/Temp**
```python
user_keyboard = [['/help','/info'],['/Temp','/ejemplo2'],['/fichero']]
```
* En la línea de la ayuda cambiamos lo mismo
```python
commandList = '/help, /info, /Temp, /ejemplo2, /fichero'
```
* Cambiamos la versión a un valor superior para ver que estamos usando la versión adecuada
```python
v = '0.9.6'
```

Ejercicio: Añadir comando para ver el estado de Throttle (vcgencmd get_throttled)

En el proyecto de TimeLapse añadiremos la funcionalidad de enviar ficheros e imágenes


### Ejemplos de Bots:

En [este enlace](https://www.fwhibbit.es/controla-tu-raspberry-pi-mediante-telegram) nos explican como hacer un bot que controla

* Control de una webcam (fotos, timelapse).
* Información sobre el estado de la Raspberry (ram, hd, temperatura y cpu).
* Envío de comandos de sistema (como en una terminal).
* Comprobación de seguridad para restringir el acceso a ciertas partes.

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

