# Nos da los dias que tiene el mes seleccionado
mes = int(input('Introduce el mes:'))
year = int(input('Introuce el anio:'))
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
    print (f'El mes {mes} del año {year} tiene {dias} dias')
else:
    print ('El mes debe ser entre 1 y 12')