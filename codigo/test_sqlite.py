import sqlite3


ficheroBaseDatos = 'datosSensores.db'

def guardaDatos(sensor1,sensor2, sensor3):
    conn=sqlite3.connect(ficheroBaseDatos) # abrimos la base de datos
    c=conn.cursor()

    c.execute("""INSERT INTO sensores (sensor1,
        sensor2, sensor3, fecha , hora) VALUES((?), (?), (?) date('now'),
        time('now')""", sensor1,sensor2,sensor3 ) # insertamos los valores

    conn.commit()  # confirmamos la transacción
    conn.close()  # cerramos la conexión