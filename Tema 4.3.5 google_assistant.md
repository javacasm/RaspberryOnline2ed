# Google Assistant

Algo que siempre queremos ahcer con nuestro sistemas domóticos es integrarlos con sistemas tan "molones" como son Google Assistant o Alexa.

El procedimiento no es demasiado complicado pero sí que necesita de hacer que nuestros equipos (normalmente la Raspberry que actúa como el corazon del sistema) sean accesibles desde Internet, de manera que los servidores de Google o de Alexa puedan actuar sobre nuestro sistema al ejecutar comandos sobre ellos.

Para ello configuramos nuesros sistema para que se pueda actuar sobre él vía web con un API REST determinado. Un ejemplo sencillo sería que el acceso  a http://nuestraIPExterna/luces/Salon/On encienda las luces del salón y http://nuestraIPExterna/luces/Salon/Off las apague.

En resument debemos construir:
* Un servidor web, existen multitud de maneras de hacerlo
* Crear ese API sencillo que actua directamente sobre nuestros dispositivos
* Exponer nuestro servidor desde internet. Podemos hacerlo abriendo puestos, haciendo el servidor como DMZ o usando servicios de internet que se encargan de ello como por ejemplo [dataplicity]( https://www.dataplicity.com)
* Crear unas reglas que vinculen Google Assistant con nuestro API, por ejemplo usando [IFFT](https://ifttt.com/)


En [este artículo de diyodemag](https://diyodemag.com/projects/part_1_google_assistant_controlled_devices) nos explican como hacer todo el proceso.

1. Instalamos **Node.js**
```sh
wget  https://nodejs.org/dist/latest-v9.x/node-v9.11.2-linux-armv6l.tar.xz
tar -xvf node-v9.11.2-linux-armv6l.tar.xz
sudo cp -R node-v9.11.2-linux-armv6l/ /usr/local/
sudo ln -s /usr/local/node-v9.11.2-linux-armv6l/bin/node /usr/bin/node
sudo ln -s /usr/local/node-v9.11.2-linux-armv6l/bin/npm /usr/bin/npm
```
2. Probamos que la instalación va ok haciendo
    ```sh
    node -v
    ```
    obtendremos 

    ```sh
    v9.11.2
    ```

3. Creamos la carpeta donde residirá nuestra web e inicializamos todo lo necesario para creala

    ```sh
    mkdir googleHome
    cd googleHome
    npm init
    npm install express
    npm install onoff
    ```
4. Ahora creamos la definición de la aplicación base que nos permitirá encender o apagar un led conectado al GPIO4. Para ello cremos el fichero app.js con el siguiente contenido:
    ```js
    const express = require("express");
    const Gpio = require("onoff").Gpio;
    const app = express();
    const port = 3000;
    const LED = new Gpio(4, "out");
    app.get("/", (req, res) => res.send ("Hello World!"));
    app.listen(port, () => console.log ("app listening on port " + port));

    app.get("/on", (req, res) => {
    LED.writeSync(1);
    res.send("LED is on");
    });
    app.get("/off", (req, res) => {
    LED.writeSync(0);
    res.send("LED is off");
    });

    ```
5. Lo ejecutamos con 
```sh
node app.js
```
6. Accedmos a la web con http://ipRaspberry:3000/led/on

7. Ahora nos queda hacer que nuestra web sea accesible desde fuera con un servicio como [dataplicity]( https://www.dataplicity.com)

8. El siguiente paso es crear en IFTTT una regla que llame a nuestra web al recibir determindo comando de Google Assistant


