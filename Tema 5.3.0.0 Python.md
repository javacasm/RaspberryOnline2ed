## Python

Python es un lenguaje interpretado moderno de gran productividad, sencillo, potente y con millones de líneas ya desarrolladas que se pueden usar directamente por medio de paquetes instalables.

Se utiliza en la web, en aplicaciones de escritorio, etc... Gran parte del interfaz de Linux lo utiliza.

Podemos utilizar varias herramientas para programar con Python como **Thonny** un simple editor de texto o trabajar directamente sobre el intérprete python y directamente programar con él.

![Herramienta idle](./images/idle.png)

En las últimas versiones se incluye el editor Thonny, que nos permite trabajar con python con facilidad

![Editor Thonny](./images/Thonny.png)

También podemos programar Python con Geany o incluso podemos [instalar](https://pimylifeup.com/raspberry-pi-visual-studio-code/) Visual Studio Code, el entorno de Microsoft.

También podemos trabajar en modo interactivo sin más que ejecutar el intérprete:

```
~/ $ python3
>>>

```

Aunque es más sencillo si escribimos nuestro código en un fichero (con cualquier editor de texto) y luego lo ejecutamos o bien abriéndolo con idle, thonny o haciendo:

```
python3 fichero.py
```

Aunque éste no pretende ser un curso sobre python, veamos algunos ejemplos.

## Operaciones numéricas y petición de datos al usuario

Es sencillo crear variables, que el usuario les de valores y hacer operaciones entre ellos:

[Código de Suma](https://github.com/javacasm/RaspberryOnline2ed/raw/master/codigo/suma.py)

```python
# Programa que realiza la suma de dos valores
a = input('numero 1 ')  # pedimos el primer numero
b = input('numero 2 ')  # pedimos el segundo numero
suma = int(a) + int (b)  # calculamos la sumas
print (suma)  # imprimimos su valor
```

**Ejercicio**: cambia la operación a realizar

### Sentencias de control condicionales

En este ejemplo vamos a ver cómo utilizar sentencias condicionales, para ejecutar un código o no según se cumpla la condición establecida:

[Código de Bisiesto](https://github.com/javacasm/RaspberryOnline2ed/raw/master/codigo/bisiesto.py)

```python
# Programa que determina si un año es o no bisiesto
# Divisible por 4
# No divisible por 100 salvo que
# Sea divisible por 400
year = int(input('Introduzca el año: '))

if (year%4)==0 and ( (year%400)==0 or  not ((year%100)== 0)):
  print('Es bisiesto!!')
else:
  print ('No es bisiesto!!')
```

[Código de días por mes](https://github.com/javacasm/RaspberryOnline2ed/raw/master/codigo/diasMes.py)

```python
# Nos da los dias que tiene el mes seleccionado
mes = int(input('Introduce el mes:'))
year = int(input('Introduce el año:'))
# Comprobamos si esta entre 1 y 12
if 1 <= mes <= 12:
    if mes == 2:
        if (year%4)==0 and ( (year%400)==0 or  not ((year%100)== 0)):
            dias = 29
        else:
            dias =28
    elif (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
        dias = 30
    else:
        dias = 31
    print (f'El mes {mes} del año {year} tiene {dias} días')
else:
    print ('El mes debe ser entre 1 y 12')
```

### Sentencias de control de repetición

Veamos cómo realizar bucles:

[Código de Buscando Caracteres](https://raw.githubusercontent.com/javacasm/RaspberryOnline2ed/master/codigo/buscaCaracter.py)

```python
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
```

**Ejercicio**: haz que el usuario pueda introducir la cadena donde buscar y el carácter

