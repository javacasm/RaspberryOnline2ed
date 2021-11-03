from pyfirmata import Arduino, util

board = Arduino('/dev/ttyUSB0') # Conectamos con la placa conectada al puerto serie

board.digital[2].write(1)  # accedemos al pin digital 2 y escribimos el valor 1 == digitalWrite(2,HIGH)
print(board.digital[2].read()) # leemos el valor del pin digital 2

# otra forma más sistemática de acceder
pin2 = board.getpin('d:2:o') # creamos una variable que representa al pin digital 2 como salida
pin2.write(1)                # ahora usamos esa variable


# acceso a pines analógicos
it = util.Iterator(board)
it.start()                  # se encarga de actualizar el valor analógico
board.analog[0].enable_reporting()
print (board.analog[0].read()) # imprimimos el valor

# La otra forma de acceder
analog_0 = board.get_pin('a:0:i') # Leemos el valor analogico de A0
print(analog_0.read())

# Acceso a PWM
pin3PWM = board.get_pin('d:3:p')  # Pin 3 con acceso PWM
pin3.write(0.6)                 # Ponemos el pin al 60%
