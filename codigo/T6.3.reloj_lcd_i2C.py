# Ejemplo 6.3 de cómo mostrar un sencillo reloj en la  LCD
import I2C_LCD_driver
import time
mylcd = I2C_LCD_driver.lcd()


while True:
	mylcd.lcd_display_string(f'Hora:{time.strftime("%H:%M:%S")}', line = 1, pos = 1)

	mylcd.lcd_display_string(f'Fecha:{time.strftime("%d/%m/%Y")}',line = 2)
	time.sleep(1) # esperamos 1 segundo