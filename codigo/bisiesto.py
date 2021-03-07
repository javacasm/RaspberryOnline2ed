# Programa que determina si un año es o no bisiesto
# Divisible por 4
# No divisible por 100 salvo que
# Sea divisible por 400
year = int(input('Introduzca el año: '))

if (year%4)==0 and ( (year%400)==0 or  not ((year%100)== 0)):
  print('Es bisiesto!!')
else:
  print ('No es bisiesto!!')
