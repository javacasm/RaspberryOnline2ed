from gpiozero import Motor  # Importamos los modulos
from time import sleep

#Definimos Motor izquierdo (L) conectando a los pines 7 y 8 a la placa L298
motorL = Motor(forward = 7, backward = 8)
#Definimos Motor derecho (R) conectando a los pines 9 y 9 a la placa L298
motorR = Motor(forward = 9, backward = 10)

while True:  # Bucle para siempre
	motorL.forward()  # Motor L hacia adelante
	motorR.forward()  # Motor R hacia adelante
	sleep(5)		  # Esperamos 5 segundos
	motorL.backward() # Motor L hacia atras
	motorR.backward() # Motor R hacia atras
	sleep(5)		  # Esperamos 5 segundos
