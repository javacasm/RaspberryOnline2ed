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
    