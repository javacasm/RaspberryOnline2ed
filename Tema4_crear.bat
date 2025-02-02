pandoc --pdf-engine=xelatex       \
        -V papersize:a4paper        \
        --template=./LaTeX_ES.latex \
        --reference-doc="plantilla_raspy_tablas.docx" \
        -o "./publicación/""Tema 4 Uso de Raspberry.docx" \
        "Tema 4 Portada.md"  \
        "Tema 4.0 Uso de Raspberry Pi.md" \
        "Tema 4.0.2 Instalacion de software.md" \
        "Tema 4.0.3 Descarga de programas.md" \
        "Tema 4.0.5 Programas normales.md" \
        "Tema 4.1.0 Usos.md" \
        "Tema 4.1.2 Comandos.md" \
        "Tema 4.1.4 Mantenimiento.md" \
        "Tema 4.1.5 Instalación de tienda de aplicaciones SNAP.md" \
        "Tema 4.2 Camara_dadi_27enero25.md" \
        "Tema 4.3.0 IOT.md" \
        "Tema 4.3.1 Domotica.md" \
        "Tema 4.3.2 MQTT.md" \
        "Tema 4.3.3 Domotica Casera.md" \
        "Tema 4.3.4 Domotica Profesional.md" \
        "Tema 4.3.5 google_assistant.md" \
        "Tema 4.4 retropie.md" \
        "Tema 4.6.0 multimedia.md" \
        "Tema 4.6.1 kodi.md" \
        "Tema 4.6.2 DLNA.md" \
        "Tema 4.7 aulas.md" \
        "Tema 4.8 Nube_privada.md" \
        "Tema 4.8.1 Syncthing.md" \
        "Tema 4.9 BookServer.md" \
        "Tema 4.B Acceso externo a nuestros servidores.md" \
        "Tema 4.Z Atribucion.md"
        