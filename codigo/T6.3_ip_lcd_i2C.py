# Ejemplo 6.3 de cómo mostrar la IP en la  LCD
import socket
import I2C_LCD_driver

mylcd = I2C_LCD_driver.lcd()

# función para obtener la ip usando una conexión a internet
def get_local_ip_address(target):
  ipaddr = ''
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((target, 8000))
    ipaddr = s.getsockname()[0]
    s.close()
  except:
    pass

  return ipaddr

myIP = get_local_ip_address('google.com')


mylcd.lcd_display_string("IP:",line = 1 )
mylcd.lcd_display_string(myIP, line = 1, pos = 3)