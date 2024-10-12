# RaspiFAQ

## General

* ¿Es openSource? 
	* Casi sí, pero [lo será](http://hackaday.com/2017/01/14/blob-less-raspberry-pi-linux-is-a-step-closer/), faltan por liberar algunas partes del software del driver de video que sólo están disponibles como fichero binario (sin código fuente).

* ¿De verdad cuesta 35$? 
	* Aunque originariamente la idea del proyecto era crear un ordenador barato, desde la versión 3 no existe una placa a ese precio. Todavía podemos encontrar la versión 3+ o la 4 de 1Gb de RAM por algo más de unos 40€. De todas formas ese es el precio de la placa, pero por si misma no es más que un pisapapeles Geek, necesitamos cómo mínimo la tarjeta SD y la alimentación.

* ¿Cómo la alimento? 
	* La podemos alimentar con una fuente de alimentación de 2A y cable USB Micro para modelos hasta la versión 3+,  con USB-C y 3A para la 4 y USB-C y al menos 5A para la Raspberry Pi 5.

* ¿Puede funcionar con pilas? 
	* Depende de las pilas, con una batería externa (como las de los móviles), Sí.

* ¿Qué significan las luces en Raspberry Pi? 
	* En la Versión 1
		PWR 5V alimentación ok
		OK 	Acceso a la SD
		FDX 	Ethernet Full Dúplex conectada
		LNK 	Ethernet conectado
		10M	Ethernet de 100 Mbps conectada. 
	* En versiones posteriores (de la V2 hasta la V4), el color verde significa que está encendido y el rojo, acceso a disco.
	* en la V5, hay un único led que está en verde indicando el funcionamiento y rojo cuando está apagado.

* ¿Cómo debo apagar mi Raspberry Pi? 
	* La mejor forma de apagarlas (desde la versión 1 a la 4) es usando el comando  halt
		sudo halt
	ó
		sudo shutdown -h 
		
	* La versión 5, incluye por fin el tan esperado botón de apagado.
	
* ¿Se puede dañar la Raspberry si le quito la alimentación? 
	* No debería romperla nada, pero si corromper la información de la tarjeta SD. Pudiera ocurrir si se están escribiendo muchos datos (es un tema de probabilidad) algunos ficheros queden corruptos y si son importantes para el sistema no arrancaría.
	* En la versión 5, la manera correcta de apagarla es mediante el botón de apagado.

* ¿Qué versión tengo? 
	* Podemos saber la versión de Raspberry que tenemos usando el siguiente comando en las versiones más modernas:
			cat /sys/firmware/devicetree/base/model 
	
		* Obtendremos ésto en una Raspberry 3:
			Raspberry Pi 3 Model B Rev 1.2
			
		* Obtendremos esto en una versión 4:
			Raspberry Pi 4 Model B Rev 1.1
			
		* Obtendremos esto en una versión 5:
			Rasberry Pi 5 Model B Rev 1.0
		
	* También podemos usar ésto, que nos dará información sobre los procesadores:
		cat /proc/cpuinfo 
		
		* Obtendremos una información similar a esta en un Raspberry Pi 3+:

		Processor       : ARMv6-compatible processor rev 7 (v6l)
		BogoMIPS        : 847.05
		Features        : swp half thumb fastmult vfp edsp java tls
		CPU implementer : 0x41
		CPU architecture: 7
		CPU variant     : 0x0
		CPU part        : 0xb76
		CPU revision    : 7
		Hardware        : BCM2708
		Revision        : 0002
		Serial          : 000000000abc0ab1

	En los modelos más modernos al tener varios núcleos el procesador obtendremos la información de cada uno de ellos


## Cacharreo (cables)

* ¿Puedo encender y apagar un led?

	Sí, pero con cuidado, un cortocircuito en la placa puede estropearla definitivamente.

* ¿Puede controlar un motor?

	No directamente, sí con una plaquita que incluya transistores o drivers

* ¿Qué necesito para hacer un robot?

	Una placa controladora, motores, baterías, sensores ...


## Administrando (¡es linux!)

* ¿Cuál es el usuario por defecto?

	Es “pi”

* ¿Cuál es la contraseña por defecto del usuario pi?

	Es “raspberry”

* ¿Cuál es la contraseña del usuario root?

	El usuario root no tiene contraseña para evitar acceso indeseados. Para ejecutar algún comando como root podemos usar el comando “sudo”

		sudo comando

	nos solicitará la contraseña del usuario actual

	Si necesitamos por alguna razón permanecer como root (lo cual se desaconseja en todos los Linux) podemos usar

		sudo su -i

	ó

		sudo su -

	Cuando acabemos podemos salir con Ctrl-D o con “exit”

* Necesito que me de acceso ssh desde el inicio o me el escritorio me ha dado un error y no puedo entrar.

	Crea un fichero vacío llamado **"ssh"** en directorio raíz de la tarjeta y vuelve a arrancar.