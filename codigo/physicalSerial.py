"""
physicaSerial: el usuario puede encender remotamente el led 13
'H' enciende el led
'L apaga el led
'P' parpadea 10 veces
'Q' para salir

La placa Arduino debe tener instalado el ejemplo PhysicalPixel

Necesitamos el módulo pyserial que instalamos con

pip3 install pyserial
"""
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

