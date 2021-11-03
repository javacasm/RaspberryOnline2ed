## Publicación de datos de IOT en servicios externos

Vamos a aprovechar nuestros conocimientos de python para trabajar en proyectos IOT.

Existen muchos servicios externos donde podemos publicar nuestros datos y representarlos gráficamente.

Estos servicios online, o en la nube como ahora se suele decir, exponen una serie de reglas para acceder a ellos.

Es lo que se conoce de forma genérica como un API (Application Programming Interface). 

Existen multitud de estos servicios, algunos nos permiten publicar contenidos en redes sociales (como Twitter y Facebook) otros nos facilitan el almacenar nuestros datos y mostrarlos como gráficas. Además estos servicios  dan una dimensión social a nuestros datos pudiendo compartirlos con otros usuarios.


### Plataformas de publicación de datos

La mayoría de estas plataformas nos permiten subir nuestros datos y obtener gráficas con ellos

![Gráficos online de thingSpeak](./images/TS_ML_Cropped_Visulaization_11001.png)

Casi todas tienen una versión limitada (limitación en la frecuencia de envío de los datos o en el volumen de estos) gratuita y otra profesional de pago.

Además algunas nos permiten establecer disparadores (trigger) para vigilar que algún dato tome cierto valor, en cuyo caso envían un aviso a nuestro sistema.

* Adafruit IO https://io.adafruit.com/
* Blynk  https://blynk.io/
* Cayenne https://mydevices.com/ 
* Grafana https://grafana.com/
* Connect2me https://www.c2m.net
* All Things Talk https://www.allthingstalk.com/
* Thingspeak https://thingspeak.com/


## Publicación en ThingSpeak

ThingSpeak es una servicio web que nos permite publicar datos de las medidas de nuestros dispositivos IOT (o de cualquier otro).

![](./images/ThingSpeak1.png)

Es gratuito para cierto número de datos y nos permite de manera muy sencilla subir datos.

### Creación del canal (Channel)

* Nos hacemos una cuenta en ThingSpeak, recibiremos un email y lo verificamos.

* Entramos en Channels->My Channels y pulsamos en "New Channel".

![ThingSpeak New Channel](./images/ThingSpeakNewChannel.png)

* Configuraremos el canal, indicando los datos que se van a enviar. Podemos añadir una descripción y datos como la web, canal de youtube, etc...

![Configuración del canal](./images/ThingSpeakConfiguracionCanal.png)

* Para poder enviar datos al canal necesitamos el API KEY que lo identifica que incluiremos en nuestro código.

![ThingSpeak API Keys](./images/ThingSpeakAPIKeys.png)

* Para que cualquiera pueda ver los datos, podemos hacer que el canal sea público, desde la pestaña Sharing.

![Sharing](./images/ThingSpeakCanalPublico.png)

* Una vez creado el canal podemos configurar los detalles de cada gráfico, para lo que pulsaremos sobre el icono "lápiz" de cada uno.

* En cualquier momento podemos importar/exportar los datos de un gráfico dado.

![ThingSpeak Import-Export](./images/ThingSpeakImport-Export.png)

![ThingSpeak Configuración de un gráfico](./images/ThingSpeakConfiguracionGrafico.png)

### Código Raspberry 

Éste es el código de ejemplo para Raspberry Pi que nos va a enviar datos sobre el uso de CPU de nuestra Raspberry

Instalamos el paquete thingspeak con

```sh
pip3 install thingspeak
```

En el código cambiaremos las claves de thingspeak escritura y el código de nuestro canal:


```python
import thingspeak
import time
 
channel_id = 306585 # Ponemos el id de nuestro canal 
write_key  = '0000CLAVE0000' # Ponemos nuestra clave de escritura (WRITE API KEY)
 
def medirCanal(canal):
    try:
        # leemos la temperatura de la Raspberry 
        temperatura = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1000.0 # para leer la temperatura
        # escritura
        response = channel.update({1: temperatura})
        
        # lectura
        lectura = channel.get({})
        print("Leído:", lectura)
    except KeyboardInterrupt:
        print("Salimos")        
    except:
        print("Error de conexión")
 
 
if __name__ == "__main__":
    canal = channel = thingspeak.Channel(id=channel_id, api_key=write_key)
    while True:
        medirCanal(canal)
        # Las cuentas públicas sólo pueden acceder cada 15 segundos
        time.sleep(15)
```

[Código del ejemplo](https://github.com/javacasm/RaspberryOnline2ed/blob/master/codigo/test_thingspeak.py)

Para ejecutarlo:

```sh
python3 test_thingspeak.py
```

Podremos ver el gráfico en su correspondiente canal

![ThingSpeak channel](./images/Check-ThingSpeak-site-for-Data-Logging.png)


## Instalación y uso de Grafana

[Grafana](https://grafana.com/) es una herramienta open source de representación gráfica y procesado de datos.

![Grafana](./images/redesign-dashboard_home.png)

La instalación es sencilla y vamos a seguir los pasos que nos recomiendan en la [web de Grafana](https://grafana.com/tutorials/install-grafana-on-raspberry-pi/#3)

Añadimos la clave APT del repositorio de Grafana y luego de haber actualizado el sistema, instalamos el paquete grafana:

```sh
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
sudo apt update
sudo apt full-upgrade
sudo apt install grafana
```

Activamos ahora el servidor de Grafana y lo arrancamos

```sh
sudo /bin/systemctl enable grafana-server
sudo /bin/systemctl start grafana-server
```

Si todo ha ido bien, podremos acceder a la página inicial de desde un navegador poniendo http://ip_raspberry:3000

![Pantalla inicial de Granada](./images/inicioGrafana.png)

Accederemos con el usuario 'admin' y contraseña 'admin', y que nos pedirá que cambiemos al entrar.

Ahora configuramos nuestra fuente de datos, en este ejemplo usaremos una base de datos mysql/mariaDB

![Configuración DB en Grafana](./images/ConfDBGrafana.png)

Ahora configuramos la consulta que haremos sobre la base de datos y seleccionamos el tipo de gráficos

![Configuración de la consulta y tipo de gráficos](./images/ConfiguracionPanel.png)

Podemos ver [tutoriales más detallados en la web de grafana](https://grafana.com/tutorials/)

### Tutoriales para otras plataformas

La mayoría de las plataformas tienen tutoriales detallados, y muchas de ellas como por ejemplo Blynk incluso generan el código necesario para utilizarlas, con lo que nosotros sólo tenemos que personalizarlo con nuestro sensores y preferencias.

[Blynk](https://blynk.io/en/getting-started) [Instructable](https://www.instructables.com/id/Blynk-JavaScript-in-20-minutes-Raspberry-Pi-Edison/)

[Cayenne](https://www.instructables.com/id/Platform-IoT-Cayenne-Mydevices-ESP8266-12E-NodeMCU/) ([Librería mqtt](https://github.com/myDevicesIoT/Cayenne-MQTT-ESP))

[Grafana](https://www.spainlabs.com/foros/tema-SpainLabsIoT2018-Grafana-Dashboard-Open-Source)

Más adelante, cuando ya sepamos programar haremos otros ejemplos de publicación como por ejemplo vía Telegram.

