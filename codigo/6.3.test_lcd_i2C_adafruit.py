from adafruit_character_lcd import Character_LCD_I2C
lcd = Character_LCD_I2C(0x26, 16, 2)
lcd.message = "Hola LCD\nRaspberry Pi"