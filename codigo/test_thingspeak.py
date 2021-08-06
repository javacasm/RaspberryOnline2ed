import thingspeak
import time
 
channel_id = 306585 # Ponemos el id del canal creado
write_key  = '6WTOP32JXRWJJBN0' # Ponemos Key de escritura (WRITE API KEY)
read_key   = 'AUREY0AGYDB9ZHM7' # Ponemos Key de lectura (READ API KEY)
 
def medirCanal(canal):
    try:
                #Calculate CPU temperature of Raspberry Pi in Degrees C
        temperatura = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1000.0 # para leer la temperatura
        # escritura
        response = channel.update({1: temperatura})
        
        # lectura
        lectura = channel.get({})
        print("Leido:", lectura)
        
    except:
        print("Error de conexión")
 
 
if __name__ == "__main__":
    canal = channel = thingspeak.Channel(id=channel_id, api_key=write_key)
    while True:
        medirCanal(canal)
        # free account has an api limit of 15sec
        time.sleep(15)
