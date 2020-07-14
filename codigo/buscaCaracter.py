# Cuenta las veces que se repite un caracter en una palabra
word= 'palabra' 
caracter = 'a' 
contador=0
mensaje = 'No se ha encontrado el caracter :('
for i in range(len(word)):
  if (word[i]==caracter):
    mensaje='se ha encontrado el caracter!!!'
    contador=contador + 1

print (mensaje)
print ('Se encontrado '+str(contador)+' veces')
