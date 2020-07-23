import time
import board
import neopixel
# pin for neopixels
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 8

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

pausa = 0.05
while True:
    for i  in  range(0, num_pixels):
        pixels.fill((0 , 0, 0))
        pixels[i] = (255,0,0)
        pixels.show()
        time.sleep(pausa)
    for i  in  range(num_pixels - 1 , -1, -1):
        pixels.fill((0 , 0, 0))
        pixels[i] = (255,0,0)
        pixels.show()
        time.sleep(pausa)


