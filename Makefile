SFAQ="RasPi FAQ - Preguntas Frecuentas.docx"
FFAQ="RasPi FAQ - Preguntas Frecuentas.md"
S1="Tema 1 - Qué es Raspberry.docx"
S2="Tema 2 - Características de Raspberry.docx"
S3="Tema 3 - Instalación de Raspberry.docx"
S4="Tema 4 - Uso de Raspberry.docx"
S5="Tema 5 - Programación con Raspberry.docx"
S6="Tema 6 - Electrónica con Raspberry.docx"
S7="Tema 7 - Proyectos con Raspberry.docx"

FMAT="Materiales.md"
SMAT="Materiales necesarios.docx"

DIR_PUBLICACION="./publicacion"


all: 1 2 3 4 5 6 7 FAQ MAT

MAT:
	pandoc --latex-engine=xelatex   \
					-V papersize:a4paper    \
					--template=./LaTeX_ES.latex    \
					-o  $(SMAT)  \
					Cabecera.md        \
					Cabecera_latex.md \
					$(FMAT)


FAQ:
	pandoc --latex-engine=xelatex   \
					-V papersize:a4paper    \
					--template=./LaTeX_ES.latex    \
					-o  $(SFAQ)  \
					Cabecera.md        \
					Cabecera_latex.md \
					$(FFAQ)


1:
	pandoc --latex-engine=xelatex \
					--from=markdown \
					-V papersize:a4paper \
					--template=./LaTeX_ES.latex \
					-o $(S1) \
					Cabecera.md        \
					Cabecera_latex.md \
					"Tema 1.0 Qué es Raspberry.md" \
					"Tema 1.1 Algo de Historia.md" \
					"Tema 1.2 Proyectos donde se usa Raspberry Pi.md" \
					"Tema 1.3 Documentación.md" 

2:
	pandoc --latex-engine=xelatex       \
					-V papersize:a4paper        \
					--template=./LaTeX_ES.latex \
					-o $(S2) \
					Cabecera.md           \
					"Tema 2.0 Características de Raspberry.md" \
					"Tema 2.1 Arquitectura.md" \
					"Tema 2.2 Versiones.md" \
					"Tema 2.2.1 Raspberry Pi 400.md" \
					"Tema 2.3 clones.md"
					
3:
	pandoc --latex-engine=xelatex       \
					-V papersize:a4paper        \
					--template=./LaTeX_ES.latex \
					-o $(S3) \
					Cabecera.md        \
					Cabecera_latex.md \
					"Tema 3.0 Instalación de Raspberry Pi.md" \
					"Tema 3.1 Sistemas operativos disponibles.md" \
					"Tema 3.2 Instalación.md" \
					"Tema 3.3 Raspberry Pi i4.md" \
					"Tema 3.4 Raspberr Pi Zero W.md" \
					"Tema 3.6 Alimentación.md"

4:
	pandoc --latex-engine=xelatex       \
					-V papersize:a4paper        \
					--template=./LaTeX_ES.latex \
					-o $(S4) \
					Cabecera.md        \
					Cabecera_latex.md \
					"Tema 4.0 Uso de Raspberry Pi.md" \
					"Tema 4.1 Matenimiento.md" \
					"Tema 4.1.5 Usos.md" \
					'Tema 4.2 Arduino.md' \
					'Tema 4.3.0 IOT.md' \
					'Tema 4.3.1 Domotica.md' \
					'Tema 4.3.2 MQTT.md' \
					'Tema 4.3.3.1 Domotica Casera.md' \
					'Tema 4.3.4 HomeAutomation.md' \
					'Tema 4.3.5 google_assistant.md' \
					'Tema 4.4 retropie.md' \
					'Tema 4.5 Servidor web - LAMP.md' \
					'Tema 4.6.0 multimedia.md' \
					'Tema 4.6.1 kodi.md' \
					'Tema 4.7 aulas.md' \
					'Tema 4.8 Nube_privada.md' \
					'Tema 4.9 BookServer.md' 

5:
	pandoc  --latex-engine=xelatex   \
					-V papersize:a4paper    \
					--template=./LaTeX_ES.latex    \
					-o  $(S5)  \
					Cabecera.md        \
					Cabecera_latex.md \
					'Tema 5.0 Programacion.md' \
					'Tema 5.1.0.Scratch3.md' \
					'Tema 5.1.5 Camara.md' \
					'Tema 5.2 Shell scripts.md' \
					'Tema 5.3 Aprender a programar python con Raspberry.md' \
					'Tema 5.3.1 Publicacion en servicios externos.md' \
					'Tema 5.3.2 MQTT y python.md' \
					'Tema 5.3.5 Datalogger Arduino.md' \
					'Tema 5.4 Sqlite.md' \
					'Tema 5.5 BotTelegram.md' \
					'Tema 5.6 Camara y python.md' \
					'Tema 5.6.1 Trabajando con github.md' \
					'Tema 5.6.6 TimeLapse.md' \
					'Tema 5.8 PyGame y ProgramacionVideojuegos.md' 

6:
	pandoc --latex-engine=xelatex   \
					-V papersize:a4paper    \
					--template=./LaTeX_ES.latex    \
					-o $(S6)     \
					Cabecera.md        \
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
	pandoc  --latex-engine=xelatex   \
					-V papersize:a4paper    \
					--template=./LaTeX_ES.latex    \
					-o  $(S7)  \
					Cabecera.md        \
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
