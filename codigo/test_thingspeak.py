import thingspeak
import time
 
channel_id = 306585 # Ponemos el id de nuestro canal 
write_key  = '11111-6WTOP32JXRWJJBN0-22222' # Ponemos nuesra clave de escritura (WRITE API KEY)
 
def medirCanal(canal):
    try:
        # leemos la temperatura de la Raspberry 
        temperatura = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1000.0 # para leer la temperatura
        # escritura
        response = channel.update({1: temperatura})
        
        # lectura
        lectura = channel.get({})
        print("Leido:", lectura)
    except KeyboardInterrupt:
        print("Interrupcion por teclado")        
    except:
        print("Error de conexión")
 
 
if __name__ == "__main__":
    canal = channel = thingspeak.Channel(id=channel_id, api_key=write_key)
    while True:
        medirCanal(canal)
        # Las cuentas públicas sólo pueden acceder cada 15 segundos
        time.sleep(15)
        