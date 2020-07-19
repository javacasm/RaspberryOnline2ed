from gpiozero import PWMLED
from time import sleep

led = PWMLED(17)

while True:
    led.value = 0  # apagado
    sleep(1)
    led.value = 0.5  # 50% de brillo
    sleep(1)
    led.value = 1  # a tope e brillo
    sleep(1)