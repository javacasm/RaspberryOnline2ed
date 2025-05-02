import time
from pigpio_dht import DHT22

# Conecta el sensor en GPIO4
sensor = DHT22(4)

try:
    while True:
        result = sensor.read()
        if result['valid']:
            print(f"Temperatura: {result['temp_c']:.1f}°C")
            print(f"Humedad: {result['humidity']:.1f}%")
        else:
            print("Error al leer el sensor")
        time.sleep(2)
except KeyboardInterrupt:
    print("\nPrograma terminado")