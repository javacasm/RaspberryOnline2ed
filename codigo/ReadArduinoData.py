

"""
ReadArduinoData: lee los datos de sensores que envía arduino y los guarda en un fichero
'H' enciende el led
'L apaga el led

La placa Arduino debe tener instalado el código sendData2Raspi

Necesitamos el módulo pyserial que instalamos con

pip3 install pyserial
"""

import serial
import time

commandHIGH = b'H' # Los definimos como bytes, no unicode
commandLOW = b'L' # Los definimos como bytes, no unicode


# según el fabricante puee ser también '/dev/ttyACM0'
serial_port = '/dev/ttyUSB0'
serial_baud = 9600

try:
    arduinoPort = serial.Serial(serial_port, serial_baud)
except:
    print('Error conectando a Arduino por ' + serial_port)
    exit(-1)

ficheroDatos = "datos.txt"

output_file = open(ficheroDatos, "w+")
bRunning = True
while bRunning:

    while arduinoPort.inWaiting()>0 :   # Hay datos pendientes
        datos = arduinoPort.readline()
        linea = datos.decode("utf-8")   # Convertimos de bytes a unicode
        print(linea)
        output_file.write(linea)        # escribmos en el fichero
        time.sleep(0.1)

    time.sleep(0.1)






