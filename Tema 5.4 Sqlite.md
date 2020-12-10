## Bases de datos con SQLite

[SQLite](https://www.sqlite.org/index.html) es un base de datos madura completamente profesional pero con la sencillez del funcionamiento con ficheros.

Para instalarla hacemos

```sh
sudo apt install sqlite
```

Las bases de datos de sqlite se usan un único fichero .db

Vamos a empezar creando la base de datos llamadas datosSensores.db. Hacemos

```sh
sqlite3 atosSensores.db
```

Ahora estaremos dentro de la herramienta de consola con el prompt **sqlite>**
Vamos a crear nuestra tabla que guardará los valores de los 3 sensores del ejemplo anterior con
```
CREATE TABLE sensores(id INTEGER PRIMARY KEY AUTOINCREMENT, sensor1 NUMERIC, sensor2 NUMERIC, sensor3 NUMERIC, fecha DATE, hora TIME);
```

Para guardar ahora los datos de los sensores en la base de datos solo tendríamos que añadir una función como esta a nuestro programa 

```python

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
```

[Ejemplo SQLite](./codigo/test_sqlite.py)

Ahora para ver los datos podemos usar sqlite
```sh
sqlite3 datosSensores.db
```

y desde dentro hacemos una consulta SELECT sobre la tabla 'sensores' con

```SQL
SELECT * from sensores;
```

Para ver el contenido y la estructura de una base de datos sqlite  podemos usar [sqlitebrowser](https://sqlitebrowser.org/), una herramienta visual que nos facilita mucho el trabajo.


