# Ejemplo 6.3 de cómo mostrar texto en LCD
import I2C_LCD_driver

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("Hola",line = 1 )
mylcd.lcd_display_string("Raspberry Pi!", line = 2)