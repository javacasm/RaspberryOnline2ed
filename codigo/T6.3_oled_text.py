# Adaptado por @javacasm del ejemplo ssd1306_pillow_shapes.py de Adafruit ssd1306 
# SPDX-FileCopyrightText: 2021 Melissa LeBlanc-Williams for Adafruit Industries
# SPDX-License-Identifier: MIT

# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!
#
# Ported to Pillow by Melissa LeBlanc-Williams for Adafruit Industries from Code available at:
# https://learn.adafruit.com/adafruit-oled-displays-for-raspberry-pi/programming-your-display

# Importamos los módulo necesarios...
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import time



i2c = board.I2C()  # uses board.SCL and board.SDA

# Creamos un objeto de tipo SSD1306 OLED
# Los dos primeros argumentos son ancho y alto.
# También podíamos pasar la dirección i2c con addr=0x3c
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)


# Borramos la pantalla
oled.fill(0)


# Creamos una imagen en blanco donde dibujaresmo.
image = Image.new("1", (oled.width, oled.height))
# accedemos al objeto que dibujará en la imagen
draw = ImageDraw.Draw(image) 

# cargamos 2 fuentes de 2 tamaños distintos. Puedes usar los que quieras de esa cartpeta o descargar nuevos
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)

# Dibujamos circulos
for i in range(40,5,-5):
    draw.ellipse((80, 5, 80+i, 5+i), outline=255, fill=0)
# añadimos texto
draw.text((0, 0), "¡Hola!", font=font, fill=255)

# primero dibujamos el rectángulo 
draw.rectangle((0, 29, 70, 45), outline=255, fill=0)
#luego el texto que contiene
draw.text((5, 30), f'{time.strftime("%H:%M:%S")}', font=font2, fill=255)

# ... marco
draw.rectangle((30, 47, 115, 60), outline=255, fill=0)
# ... texto enmarcado
draw.text((34, 46), f'{time.strftime("%d/%m/%Y")}', font=font2, fill=255)

# Copiamos la imagen en pantalla 
oled.image(image)
# Actualizamos la pantalla
oled.show()