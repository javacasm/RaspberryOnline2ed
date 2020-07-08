## Problemas de alimentación

Muchos problemas en los montajes con Raspberry Pi vienen de la alimentación. Dependiendo del uso, de los periféricos, de la velocidad a la que esté trabajando el procesar, el consumo varía. Si en un momento es alto, la fuente de alimentación puede no ser capaz de alimentar todo el sistema. 

Cuando esto ocurre, si la alimentación es insuficiente, algnos dispositivos se paran, el micro ralentiza su funcionamiento y se muestra un "rayo" amarillo en la parte superior derecha. 

![Indicador de baja alimentación](./images/NESPi_part5_web7.png)

Desde el sistema podemos ver el estado de la alimentación y de la temperatura del sistema monitorizando el valor de **throttle** (traducible por "sofocado")usando el siguiente comando

```sh
/opt/vc/bin/vcgencmd get_throttled
```

throttled=0x0

Un valor de 0x0 nos dice que el estado de la alimentación  y la temperatura del sistema son aceptable.

A medida que se calienta el sistema o baja la alimentación el valor de **throttle** se va incrementando y el rendimiento del sistema baja.

Los distintos bits de **throttle** tiene distinto significado y nos sirven para conocer el estado del sistema. Un valor de 0 en este bit nos indica que no está activado, un valor 1 nos dice que en este momento ocurre.

```
0: under-voltage
1: arm frequency capped
2: currently throttled
3: Soft Temp limit reached  3
16: under-voltage has occurred
17: arm frequency capped has occurred
18: throttling has occurred
19: Soft Temp limit has occurred
```

Por ejemplo si obtenemos un valor de throttle de 0x50005 en binario sería B1010000000000000101 implicaría que tenemos activos lo bits 0, 2, 16 y 18 lo quiere decir que tenemos un problema de voltaje de alimentación bajo y por ello se ha reducido la frecuencia de la CPU


### Documentación

[How detects under voltage](https://raspberrypi.stackexchange.com/questions/60593/how-raspbian-detects-under-voltage)

[Performance degradation](https://www.raspberrypi.org/forums/viewtopic.php?f=63&t=147781&start=50#p972790)
