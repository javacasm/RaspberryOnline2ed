# Cuenta las veces que se repite un carácter en una palabra
word= 'palabra' 
caracter = 'a' 
contador=0
mensaje = 'No se ha encontrado el carácter :('
for i in range(len(word)):
  if (word[i]==caracter):
    mensaje='se ha encontrado el carácter!!!'
    contador=contador + 1

print (mensaje)
print ('Se ha encontrado '+str(contador)+' veces')