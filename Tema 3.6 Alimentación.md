## Problemas de alimentación

Si hay poca alimentación se muestra un "rayo" amarillo en la parte superior derecha 

![Indicador de baja alimentación](./images/NESPi_part5_web7.png)

Low Voltage

throttle
https://raspberrypi.stackexchange.com/questions/60593/how-raspbian-detects-under-voltage



https://www.raspberrypi.org/forums/viewtopic.php?f=63&t=147781&start=50#p972790

/opt/vc/bin/vcgencmd get_throttled


throttled=0x0
You're good with the supplied voltage and SoC temperature.  


Bits:

0: under-voltage
1: arm frequency capped
2: currently throttled
3: Soft Temp limit reached  3
16: under-voltage has occurred
17: arm frequency capped has occurred
18: throttling has occurred
19: Soft Temp limit has occurred


El led Rojo est'a conectado al pin +35  
he red power LED is connected to GPIO 35. You can monitor the GPIO to check for an under voltage condition (less than 4.65V).
* Se puede ver si parpadea__
