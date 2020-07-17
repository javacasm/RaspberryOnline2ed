## Datalogger para Arduino con Raspberry

Ya hemos comentado que Arduino y Raspberry se complementan perfectamente.

Vamos a ver cómo comunicarlos usando el puerto serie. De esta manera podemos
* Lectura valores en Raspberry de sensores conectados físicamente a Arduino
* Guardarlos en bd o ficheros
* Gráficos
* Controlar actuadores que están conectados a Arduino

## Controlando Arduino

Vamos a hacer un ejemplo muy sencillo en el que vamos a controlar la iluminación del led del pin 13 de un Arduino desde un programa python. Exactamente el mismo programa nos permitiría controlar relés.

Como programa en Arduino usaremos el ejemplo PhysicalPixel que está en el menú Ejemplos->Comunicaciones

Una vez subido a nuestro Arduino podemos probarlo desde el monitor serie enviando las letras 'H' para encender y 'L' para apagar el led:

```C++
// Ejemplo PhysicalPixel

const int ledPin = 13; // the pin that the LED is attached to
int incomingByte;      // a variable to read incoming serial data into

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    // if it's a capital H (ASCII 72), turn on the LED:
    if (incomingByte == 'H') {
      digitalWrite(ledPin, HIGH);
    }
    // if it's an L (ASCII 76) turn off the LED:
    if (incomingByte == 'L') {
      digitalWrite(ledPin, LOW);
    }
  }
}

```

Vamos a hacer ahora el programa Python que nos va a pedir un comando y actuará sobre Arduino.

Necesitamos tener instaladl pySerial en nuestra Raspberry. Podemos instalarla con

```sh
pip3 install pySerial
```



```python
import serial
import time

commandHIGH = b'H' # Los definimos como bytes, no unicode
commandLOW = b'L' # Los definimos como bytes, no unicode
commandQuite = 'Q'
comandBlink = 'P'

# según el fabricante puee ser también '/dev/ttyACM0'
serial_port = '/dev/ttyUSB0'
serial_baud = 9600

try:
    arduinoPort = serial.Serial(serial_port, serial_baud)
except:
    print('Error conectando a Arduino por ' + serial_port)
    exit(-1)

bRunning = True
while bRunning:
    comamnd = input(' H Encender, L Apaga, P Parpadea, Q Sale ')
    if comamnd == commandQuite:
        print ('bye')
        bRunning = False
    elif comamnd == comandBlink:
        for i in range(0,10):
            arduinoPort.write(commandHIGH)
            time.sleep(0.2)
            arduinoPort.write(commandLOW)
            time.sleep(0.2)
    else:
        arduinoPort.write(comamnd.encode()) # Encode transforma unicode a bytes

```