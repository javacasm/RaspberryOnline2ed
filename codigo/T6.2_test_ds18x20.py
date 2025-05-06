import time

from w1thermsensor import W1ThermSensor # importamos la librería
sensor = W1ThermSensor()

while True:
    temperature = sensor.get_temperature()
    print(' Temperatura {}º'.format(temperature))
    time.sleep(1) 