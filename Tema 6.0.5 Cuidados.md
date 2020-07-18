## Cuidados eléctricos

Trabajar con electrónica es siempre algo delicado pero mucho más cuando trabajamos conectados a un ordenador.

* No existe protección en los terminales, con lo que es muy, muy sencillo quemar la placa.
* Cuidado con colocar la placa sobre un instrumento o superficie metálica. Mejor usar una caja
* Cuidado con los dispositivos que conectamos, pudieran demandar más potencia de la que le puede dar
* Antes de realizar cualquier tipo de conexión en los conectores o pines debemos de tener siempre la precaución de tener desconectada la alimentación de la Raspberry Pi.
* Evitaremos derivaciones eléctricas o cortos .
* Conviene recordar que los pines de la CPU de la placa están conectados directamente a los diferentes conectores y pines, con lo que cualquier cosa que hagamos sobre los pines la estamos haciendo directamente sobre la CPU.
* También hay que tener en cuenta que los pines GPIO no soportan 5 V, sólo 3.3V y un máximo de 16 mA, por lo que hay que tomar precauciones en este sentido.


## Adaptadores

Existen diferentes adaptadores que nos facilitan el uso de electrónica y ademas protegen a la Raspberry. En la sección de las placas hablaremos de ellas.

## Potencia

Los pines de la Raspberry no proporcionan potencia, más allá de encender un led. Si necesitas más potencia tendrás que añadir componentes electrónicos capaces de gestionarlo.
