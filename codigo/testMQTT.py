import paho.mqtt.client as mqtt # Importamos  MQTT library
import time # The time library is useful for delays
import datetime

v = '1.0'

# Se llamará a esta función cada vez que nos llegue un mensaje
def messageFunction (client, userdata, message):
    topic = str(message.topic)
    message = str(message.payload.decode("utf-8"))
    print(str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S.%f "))+ topic + message)

ourClient = mqtt.Client("NuestroClienteDeEjemplo") # Creamos un cliente y le damos un id
ourClient.connect("192.168.1.200", 1883) # IP del servidor MQTT
ourClient.subscribe("MeteoSalon/#") # Nos suscribimos a todos los topic que empiecen por MeteoSalon
ourClient.on_message = messageFunction # Funciń a la que se llamará cuando llegue un mensaje
ourClient.loop_start() # Arrancamos el cliente

# Main program loop
last_pub = int(round(time.time() * 1000))
while(1):
    now = int(round(time.time() * 1000))
    if (now - last_pub) > 30000: # Revisamos cada 30 segundos 
        ourClient.publish("MeteoSalon/Test", "Just Testing") # Publicamos un mensaje de teste
        last_pub = now
    time.sleep(0.1) # Esperamos 1 segundo