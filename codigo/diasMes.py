# Nos da los dias que tiene el mes seleccionado
mes = input('Introduce el mes:')
year = input('Introuce el anio:')
# Comprobamos si es entero
if type(mes) == int:
  # Comprobamos si esta entre 1 y 12
  if (mes >= 1) and (mes <= 12):
    if mes == 2:
      if(year % 400 == 0) or (year % 100 == 0) or (year % 4 == 0):
        dias = 29
      else:
        dias =28
    elif (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
      dias = 30
    else:
      dias = 31
    print ('El mes '+str(mes) +' del anio '+str(year)+' tiene '+str(dias)+ ' dias')
  else:
    print ('El mes debe ser entre 1 y 12')
else:
  print ('El mes debe ser entero')