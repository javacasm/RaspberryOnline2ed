# Ejemplo 6.3 parpadeo en lcd
import time
import I2C_LCD_driver
mylcd = I2C_LCD_driver.lcd()

while True:
	mylcd.lcd_display_string("TEXTO", line=1, pos=5)
	mylcd.lcd_display_string("PARPADEANTE", line=2, pos=3)
	time.sleep(1)
	mylcd.lcd_clear()
	time.sleep(1)