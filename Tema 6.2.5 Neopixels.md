## Programando y usando NeoPixels en Raspberry Pi  con Python

Este tutorial explica cómo configurar y programar NeoPixels (LEDs WS2812), leds RGB a los podemos asignar un color individualmente.

Utilizaremos un entorno virtual para gestionar los paquetes de Python, asegurando un entorno limpio y aislado. No usaremos la biblioteca `adafruit-circuitpython-neopixel`, sino que nos centraremos en `rpi_ws281x`, optimizada para Raspberry Pi. 
## Requisitos

- **Hardware**:
    - Raspberry Pi 4 ó 5 (con Raspberry Pi OS, preferiblemente la versión de 64 bits más reciente).
    - Tira, anillo o matriz de NeoPixels (por ejemplo, LEDs basados en WS2812B).
    - Placa de prototipado (breadboard) y cables de conexión.
    - Fuente de alimentación de 5V (para muchos LEDs, asegúrate de que proporcione suficiente corriente).
    - Conversor de nivel lógico (recomendado, ya que los NeoPixels requieren lógica de 5V y la Pi usa 3.3V).
    - Resistencia de 330–470Ω (para estabilidad en la línea de datos).
- **Software**:
    - Raspberry Pi OS (Bookworm o posterior) instalado.
    - Acceso a terminal (local o por SSH).
    - Conexión a Internet para instalar paquetes.

### Configuración del Hardware

1. **Consideraciones de Alimentación**:
    
    - Los NeoPixels consumen mucha corriente (hasta 60mA por LED a máximo brillo).
    - Para configuraciones pequeñas (<10 LEDs), los pines de 5V de la Pi pueden ser suficientes. Para configuraciones grandes, usa una fuente de alimentación externa de 5V con tierra común con la Pi.
    
2. **Conexiones**:
    
    - Conecta el **GND** del NeoPixel a un pin GND de la Pi (por ejemplo, pin 6).
    - Conecta el **5V** del NeoPixel a una fuente de 5V (pin de 5V de la Pi o fuente externa).
    - Conecta el **DIN** (entrada de datos) del NeoPixel a un pin GPIO (por ejemplo, GPIO18, pin 12) a través de una resistencia de 330–470Ω.
    - Si usas un conversor de nivel (por ejemplo, 74AHCT125), conecta la señal GPIO de 3.3V de la Pi a la entrada del conversor, y la salida de 5V del conversor al DIN del NeoPixel.
    
3. **Consejos de Seguridad**:
    
    - Verifica las conexiones para evitar cortocircuitos.
    - Apaga la Pi mientras haces las conexiones.
    - Si usas una fuente externa, asegúrate de que esté aislada del riel de 5V de la Pi.

Para utilizar los neopixels necesitamos  **habilitar SPI** (necesario para algunas configuraciones de NeoPixels):

- Ejecuta `sudo raspi-config`.
- Ve a **Opciones de Interfaz** > **SPI** > Habilita.
- Reinicia tu Raspberry Pi

Dentro de nuestro entorno virtual instalaremos el módul `rpi_ws281x`, que es eficiente y está diseñada específicamente para controlar NeoPixels en Raspberry Pi.

```bash
pip install rpi_ws281x
```

Un [código](https://github.com/javacasm/RaspberryOnline2ed/blob/master/codigo/test_neopixels.py) para usar los neopixels puede ser el siguiente:

```python
import time
from rpi_ws281x import PixelStrip, Color

# Configuración de los NeoPixels
LED_COUNT = 8        # Número de LEDs en la tira/anillo
LED_PIN = 18         # GPIO18 (pin 12)
LED_FREQ_HZ = 800000 # Frecuencia de la señal (800kHz para WS2812)
LED_DMA = 10         # Canal DMA para generar la señal
LED_BRIGHTNESS = 50  # Brillo (0-255, 50 es ~20% para reducir consumo)
LED_CHANNEL = 0      # Canal PWM (0 para GPIO18)

# Inicializar la tira de NeoPixels
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, False, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

def color_wipe(color, wait_ms=50):
	"""Aplicar un color a todos los LEDs uno por uno."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms / 1000.0)

def rainbow_cycle(wait_ms=20):
	"""Ciclo de colores arcoíris."""
	for j in range(256):
		for i in range(strip.numPixels()):
			pixel_index = (i * 256 // strip.numPixels()) + j
			strip.setPixelColor(i, wheel(pixel_index & 255))
		strip.show()
		time.sleep(wait_ms / 1000.0)

def wheel(pos):
	"""Generar colores arcoíris para posiciones de 0 a 255."""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)

try:
	while True:
		print("Barrido rojo")
		color_wipe(Color(255, 0, 0), 50)  # Rojo
		color_wipe(Color(0, 0, 0), 50)    # Apagar
		print("Barrido verde")
		color_wipe(Color(0, 255, 0), 50)  # Verde
		color_wipe(Color(0, 0, 0), 50)    # Apagar
		print("Barrido azul")
		color_wipe(Color(0, 0, 255), 50)  # Azul
		color_wipe(Color(0, 0, 0), 50)    # Apagar
		print("Ciclo arcoíris")
		rainbow_cycle(20)                  # Efecto arcoíris

except KeyboardInterrupt:
	print("Saliendo...")
	color_wipe(Color(0, 0, 0), 10)  # Apagar todos los LEDs

finally:
	strip._cleanup()  # Limpiar recursos
```

Para ejecutarlo tenemos que usar permisos de administrador porque la biblioteca `rpi_ws281x` requiere acceso de root para controlar los GPIOs:
    
```bash
sudo python3 prueba_neopixel.py
```

Si todo va bien:

- Los NeoPixels mostrarán un barrido de colores rojo, verde y azul, seguido de un ciclo arcoíris.
- Presiona `Ctrl+C` para detener el programa, lo que apagará los LEDs.

###  Solución de Problemas

- **Sin Luces**:

    - Verifica las conexiones y la fuente de alimentación.
    - Asegúrate de usar el GPIO correcto (GPIO18 en el ejemplo).
    - Confirma que el entorno virtual está activo (`source neopixel_env/bin/activate`).

- **Errores de Permisos**:

    - Ejecuta el script con `sudo`.
    - Asegúrate de que el usuario esté en el grupo `gpio`:
        
	```bash
	sudo usermod -aG gpio $USER
	```
	Cierra sesión y vuelve a iniciarla o reinicia.

- **Parpadeo o Colores Incorrectos**:

	- Usa un conversor de nivel para señales de 5V confiables.
    - Añade un condensador de 1000µF en la fuente de alimentación para estabilizar el voltaje.

- **Errores de Biblioteca**:

	- Reinstala la biblioteca:
        
        ```bash
        pip install rpi_ws281x --force-reinstall
        ```
        
Si quieres ampliar tu proyecto:

- **Ampliar el Código**:

    - Añade patrones (por ejemplo, persecución, pulso).
    - Controla los NeoPixels con sensores o interfaces web.
    - Explora más funciones de `rpi_ws281x` (consulta su documentación).
    
- **Proyectos**:

    - Crea una lámpara de ambiente, un indicador de estado o una pantalla animada.
    - Integra con plataformas IoT como Home Assistant.

- **Explorar Otras Bibliotecas**:

    - Investiga `luma.led_matrix` para matrices de LEDs.
    - Prueba otras bibliotecas compatibles con WS2812.

