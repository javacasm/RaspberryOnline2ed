# RaspiFAQ

## General

* ¿Es openSource?

	Casi sí, pero [lo será](http://hackaday.com/2017/01/14/blob-less-raspberry-pi-linux-is-a-step-closer/), faltan por liberar algunas partes del software del driver de video que sólo están disponibles como fichero binario (sin código fuente)

* ¿De verdad cuesta 35$?

	La placa sí, pero por si misma no es más que un pisapapeles Geek, necesitamos cómo mínimo la tarjeta SD y la alimentación.

* ¿Cómo la alimento?

	Por USB Micro para modelos hasta la 3+ y con USB tipo C (como los móviles) con 5v y al menos 2A, 3A para la 4

* ¿Puede funcionar con pilas?

	Depende de las pilas, con una batería externa (como las de los móviles) Sí

* ¿Qué significan las luces? En las versiones modernas (2 en adelante), hay un led Rojo de alimentación y uno verde de actividad del sistema. En la  V1

		PWR 	5V alimentación ok
		OK 	Acceso a la SD
		FDX 	Ethernet Full Duplex conectada
		LNK 	Ethernet conectado
		10M	Ethernet de 100 Mbps conectada

* ¿Cómo debo apagar mi raspberry?

	La mejor forma de apagarlas es usando el comando  halt

		sudo halt
	ó

		sudo shutdown -h

* ¿Se rompe si le quito la alimentación?

	No debería romperna nada, pero pudiera ocurrir si se están escribiendo muchos archivos (es un tema de probabilidad) algunos queden corruptos y si son importantes para el sistema no arrancaría

* ¿Qué versión tengo?

	Podemos saber la versión de Raspberry que tenemos usando el siguiente comando en las versiones más modernas
	
		cat /sys/firmware/devicetree/base/model;echo
		
	Obtendremos ésto en una Raspi 3
	
		Raspberry Pi 3 Model B Rev 1.2
		
	También podemos usar ésto, que nos dará información sobre los procesadores

		cat /proc/cpuinfo

	Obtendremos una información similar a esta

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

	Según el valor que aparezca en el campo Revision tendremos una versión u otra

	Existen 3 versiones:

		Modelo y Revision		Hardware Revision Code de cpuinfo
		Model B Revision 1.0				0002
		Model B Revision 1.0 + ECN0001 (no fuses, D14 removed)	0003
		Model B Revision 2.0			0004, 0005, 0006

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