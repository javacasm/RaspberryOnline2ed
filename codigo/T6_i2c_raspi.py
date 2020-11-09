import smbus
import time

bus = smbus.SMBus(1)

# Dirección del programa arduino
address = 0x09

def writeNumber(value):
       bus.write_byte(address, value)
       # bus.write_byte_data(address, 0, value)
       return -1

def readNumber():
       number = bus.read_byte(address)
       # number = bus.read_byte_data(address, 1)
       return number

while True:
       var = input("Comando (0 off - 1 On):")
       if not var:
           continue
       writeNumber(ord(var))
       number = readNumber()
       print('Status: ' + str(number))
