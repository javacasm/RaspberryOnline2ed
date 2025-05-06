import smbus2
import bme280

port = 1
address = 0x76 # usaremos la dirección que hemos encontrado
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address) # parámetros de compensación

# leemos los datos
data = bme280.sample(bus, address, calibration_params) 

# mostramos los datos 
print(data.id) # ID del sensor
print(data.timestamp) # fecha y hora UTC
print(data.temperature)
print(data.pressure)
print(data.humidity)

# los mostramos en otro formato
print(data)