# TTS

## espeak




	sudo apt install espeak python-espeak

  espeak "hello, this is just a test"

cambiamos a español

  espeak -ves "hola"
  espeak -ves "hola ahora parece español"

cambiamos la voz y la velocidad

  espeak -ves+f4 -s 120 "hola ahora en  español"

instalamos nuevas voces

 sudo apt install mbrola mbrola-es1 mbrola-es2
 2057  espeak -v mb-es1 -s 120 "hola ahora en  español"
 2058  espeak -v mb-es2 -s 120 "hola ahora en  español"

https://travesuras.wordpress.com/2012/01/11/20120111-1/


https://www.lawebdelprogramador.com/foros/Python/1434310-Sintetizador-espeak.html

http://www.sethanil.com/python-for-friends/11
