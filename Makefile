
S1="Tema 1 Qué es Raspberry.docx"
S2="Tema 2 Características de Raspberry.docx"
S3="Tema 3 Instalación de Raspberry.docx"
S4="Tema 4 Uso de Raspberry.docx"
S5="Tema 5 Programación con Raspberry.docx"
S6="Tema 6 Electrónica con Raspberry.docx"
S7="Tema 7 Proyectos con Raspberry.docx"

SFAQ="RasPi FAQ - Preguntas Frecuentas.docx"
FFAQ="Tema 0.9 RasPi FAQ - Preguntas Frecuentes.md"

SMAT="Materiales necesarios.docx"

FINDEX="Temario 4ed.md"
SINDEX="Índice 4ed.docx"

FCV="Tema 0.5 CV javacasm.md"
SCV="CV javacasm.docx"

DIR_PUBLICACION="./publicación/"

PLANTILLA_DOC_DADI="Plantilla-Prueba-Raspberry-Dadi.odt"

PLANTILLA_DOC="plantilla_raspy_tablas.docx"

CV:
	pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		--reference-doc=$(PLANTILLA_DOC) \
		-o  $(DIR_PUBLICACION)$(SCV)  \
		$(FCV)
MAT:
	pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		-o  $(DIR_PUBLICACION)$(SMAT)  \
		--reference-doc=plantilla_raspy.docx \
		"Tema 0.1.0 Materiales.md" \
		"Tema 3.0.1 Qué Raspberry elegir.md" \
		"Tema 3.0.2 Componentes necesarios.md" \
		"Tema 0.1.3 Material electrónico.md" \
		"Tema 3.0.4 Carcasas.md" \
		"Tema 3.0.5 Dónde encontrarlos.md" \

FAQ:
	pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		-o  $(DIR_PUBLICACION)$(SFAQ)  \
		--reference-doc=$(PLANTILLA_DOC)  \
		"Tema 0.9 Portada.md"        \
		$(FFAQ)

INDEX:
	pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		--reference-doc=$(PLANTILLA_DOC)  \
		-o  $(DIR_PUBLICACION)$(SINDEX)  \
		Portada.md        \
		Cabecera_latex.md \
		$(FINDEX)

1:
	pandoc --pdf-engine=xelatex \
		--from=markdown \
		-V papersize:a4paper \
		--template=./LaTeX_ES.latex \
		--reference-doc=$(PLANTILLA_DOC)  \
		-o $(DIR_PUBLICACION)$(S1) \
		"Tema 1 Portada.md"  \
		"Tema 1.0 Qué es Raspberry.md" \
		"Tema 1.1 Algo de Historia.md" \
		"Tema 1.2 Proyectos donde se usa Raspberry Pi.md" \
		"Tema 1.3 Documentación.md" \
		"Tema 1.9 Atribucion.md"

2:
	pandoc --pdf-engine=xelatex       \
		-V papersize:a4paper        \
		--template=./LaTeX_ES.latex \
		--reference-doc=$(PLANTILLA_DOC)  \
		-o $(DIR_PUBLICACION)$(S2) \
		"Tema 2 Portada.md"  \
		"Tema 2.0 Características de Raspberry.md" \
		"Tema 2.1 Arquitectura.md" \
		"Tema 2.2 Versiones.md" \
		"Tema 2.2.1 Raspberry Pi 400.md" \
		"Tema 2.3 clones.md" \
		"Tema 2.9 Atribucion.md"
		
3:
	pandoc --pdf-engine=xelatex       \
		-V papersize:a4paper        \
		--template=./LaTeX_ES.latex \
		--reference-doc=$(PLANTILLA_DOC) \
		-o $(DIR_PUBLICACION)$(S3) \
		"Tema 3 Portada.md"  \
		"Tema 3.0 Instalación de Raspberry Pi.md" \
		"Tema 3.0.1 Qué Raspberry elegir.md" \
		"Tema 3.0.2 Componentes necesarios.md" \
		"Tema 3.0.4 Carcasas.md" \
		"Tema 3.0.5 Dónde encontrarlos.md" \
		"Tema 3.1 Sistemas operativos disponibles.md" \
		"Tema 3.2 Instalación.md" \
		"Tema 3.2.2 Configuración.md" \
		"Tema 3.2.3 Acceso remoto.md" \
		"Tema 3.3 Instalación manual.md" \
		"Tema 3.3.2 Otras instalaciones.md" \
		"Tema 3.4 Arranque desde USB.md" \
		"Tema 3.5 Instalación en Raspberry Pi Zero W.md"  \
		"Tema 3.6 TFT.md" \
		"Tema 3.7 Alimentación.md" \
		"Tema 3.8 Problemas habituales.md" \
		"Tema 3.9 Atribucion.md"

4:
	pandoc --pdf-engine=xelatex       \
		-V papersize:a4paper        \
		--template=./LaTeX_ES.latex \
		--reference-doc=$(PLANTILLA_DOC) \
		-o $(DIR_PUBLICACION)$(S4) \
		"Tema 4 Portada.md"  \
		"Tema 4.0 Uso de Raspberry Pi.md" \
		"Tema 4.0.2 Instalacion de software.md" \
		"Tema 4.0.3 Descarga de programas.md" \
		"Tema 4.0.5 Programas normales.md" \
		"Tema 4.1.0 Usos.md" \
		"Tema 4.1.2 Comandos.md" \
		"Tema 4.1.4 Mantenimiento.md" \
		"Tema 4.1.5 Instalación de tienda de aplicaciones SNAP.md" \
		'Tema 4.2 Camara_dadi_27enero25.md' \
		"Tema 4.3.0 IOT.md" \
		'Tema 4.3.1 Domotica.md' \
		'Tema 4.3.2 MQTT.md' \
		'Tema 4.3.3 Domotica Casera.md' \
		'Tema 4.3.4 Domotica Profesional.md' \
		'Tema 4.3.5 google_assistant.md' \
		'Tema 4.4 retropie.md' \
		'Tema 4.6.0 multimedia.md' \
		'Tema 4.6.1 kodi.md' \
		'Tema 4.6.2 DLNA.md' \
		'Tema 4.7 aulas.md' \
		'Tema 4.8 Nube_privada.md' \
		'Tema 4.8.1 Syncthing.md' \
		'Tema 4.9 BookServer.md' \
		'Tema 4.B Acceso externo a nuestros servidores.md' \
		'Tema 4.Z Atribucion.md'

5:
	pandoc  --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		--reference-doc=$(PLANTILLA_DOC) \
		-o  $(S5)  \
		'Tema 5 Portada.md'  \
		'Tema 5.0 Programacion.md' \
		'Tema 5.1.0 Scratch3.md' \
		'Tema 5.2 Shell scripts.md' \
		'Tema 5.2.3 Arduino.md' \
		'Tema 5.3.0.0 Python.md' \
		'Tema 5.3.0.1 Entornos virtuales.md' \
		'Tema 5.3.1 Publicacion en servicios externos.md' \
		'Tema 5.3.2 MQTT y python.md' \
		'Tema 5.3.5 Datalogger Arduino.md' \
		'Tema 5.4 Sqlite.md' \
		'Tema 5.4.1 MySQL-MariaDB.md' \
		'Tema 5.4.5 Servidor web - LAMP.md' \
		'Tema 5.5 BotTelegram.md' \
		'Tema 5.6.0 Camara y Python.md' \
		'Tema 5.6.5 Trabajando con github.md' \
		'Tema 5.6.6 TimeLapse.md' \
		'Tema 5.8 PyGame y ProgramacionVideojuegos.md' 

6:
	pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		--reference-doc=plantilla_raspy.docx \				
		-o $(S6)     \
		Portada.md        \
		Cabecera_latex.md \
		'Tema 6.0 - Electrónica con Raspberry.md' \
		'Tema 6.0.5 Cuidados.md' \
		'Tema 6.1 GPIO.md' \
		'Tema 6.2 Sensores.md' \
		'Tema 6.2.5 Neopixels.md' \
		'Tema 6.3 Componentes I2C.md' \
		'Tema 6.4 Medidas analógicas.md' \
		'Tema 6.5 MQTT Leds y sensores.md' \
		'Tema 6.6 motores.md' \
		'Tema 6.7 Hats.md' \
		'Tema 6.8 Otras librerias.md' \
		'Tema 6.9 Conexion con arduino.md'

7:
	pandoc  --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		--reference-doc=plantilla_raspy.docx \				
		-o  $(S7)  \
		Portada.md        \
		Cabecera_latex.md \
		'Tema 7.0 - Robótica con Raspberry.md' \
		'Tema 7.1 CocheRobot.md' \
		'Tema 7.2 Monitoriza tu jardín con Arduino y Raspberry.md'


clean:
	rm $(S5) $(S6) $(S1) $(S2) $(S3) $(S4) $(SFAQ)

publish:
	cp $(s7) $(S5) $(S6) $(S1) $(S2) $(S3) $(S4) $(SFAQ) $(SMAT) $(DIR_PUBLICACION)
	cp *Objetivos*.pdf $(DIR_PUBLICACION)
	cp *Ejercicio*.pdf $(DIR_PUBLICACION)
	cp *Test*.pdf $(DIR_PUBLICACION)


push:
	git commit -m "update" $(S7);
	git commit -m "update" $(S5);
	git commit -m "update" $(S6);
	git commit -m "update" $(S3);
	git commit -m "update" $(S4);
	git commit -m "update" $(S2);
	git commit -m "update" $(S1);
	git push;


