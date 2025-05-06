from gpiozero import Button # importamos los módulos necesarios

button = Button(2) # Declaramos un pulsador conectado al GPIO 2

button.wait_for_press() # Espera hasta que se pulse el boton
print('Me has pulsado') # Nos informa de que se ha pulsado
