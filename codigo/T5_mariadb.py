# Ejemplo sencillo de acceso a base de datos mariaDB 
# T5_mariadb
import time
import pymysql as mariadb

def insertarDato(id_sensor, valor):
    db = mariadb.connect(host='raspi4',
                            user='javacasm',
                            passwd='Patatin5.5',
                            db='datos_db')

    cursor = db.cursor() # abrimos el cursor

    insertSql = 'INSERT INTO datos_sensores (id_sensor,fecha,valor) values ({},now(),{});'.format(str(id_sensor),str(valor))

    try:
        cursor.execute(insertSql) # Executamos la sentencia insert
        db.commit() # si todo va bien la confirmamos
        print('Insertado valor:' + str(valor))
    except Exception as e:
        print('Error en la sentencia({}):{}'.format(insertSql,str(e)))
        db.rollback() # Si hay un error cancelamos la transacción

    cursor.close() # Cerramos el cursor
    db.close() # Cerramos el acceso a la db


for i in range (0,50):
    insertarDato(0,i)
    time.sleep(0.5)
 

