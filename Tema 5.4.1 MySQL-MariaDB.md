## Instalación de MySQL/MariaDB

Empecemos por aclarar el tema del nombre: originariamente la base de datos se llamaba MySQL, pero tras ser adquirida por Oracle, su creador Michael Monty Widenius, decidió hacer una versión libre derivada (un fork) llamada MariaDB, en honor a su hija.

La instalación es muy sencilla. Una vez nos hemos asegurado de que tenemos el sistema actualizado (con el clásico sudo apt update), instalamos el paquete MariaDB con 

```sh
sudo apt install mariadb-server
```

Y para configurarla con un acceso más seguro ejecutamos el siguiente script

```sh
sudo mysql_secure_installation
```

Para probar que está funcionando vamos a conectarnos y crear una base de datos de ejemplo

```sh
mariadb -u root -p -h localhost
```

Una vez dentro, creamos un usuario para no tener que usar siempre el usuario root con 

![Test MariaDB](./images/test_mariaDB.png)


```SQL
CREATE USER 'javacasm'@'localhost' IDENTIFIED BY 'my_password';
```

Ahora creamos una base de datos y le damos acceso al usario que hemos creado

```SQL
CREATE DATABASE datos_db;
GRANT ALL PRIVILEGES ON datos_db.* TO 'javacasm'@'localhost';
FLUSH PRIVILEGES;
```
Y salimos con 'quit;'


Ahora reiniciamos la base de datos para que se actualicen los cambios en los permisos

```sh
sudo service mariadb restart    
```

Si todo ha ido bien ya podremos crear una tabla e insertar datos. Entramos con nuestro usuario

```sh
mariadb -u javacasm -p -h localhost
```

Creamos la tabla 'datos_sensores' en la base de datos 'datos_db' con

```SQL
use datos_db;
CREATE TABLE datos_sensores (
  id bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  id_sensor int NOT NULL,
  fecha datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  valor decimal(10,2)
);
```
Para insertar algunos valores podemos hacer:

```SQL
INSERT INTO datos_sensores (id_sensor,fecha,valor) values (0,now(),1.3);
INSERT INTO datos_sensores (id_sensor,fecha,valor) values (0,now(),1.5);
INSERT INTO datos_sensores (id_sensor,fecha,valor) values (0,now(),1.2);
```

Que podemos recuperar con un sencillo 'select'

```SQL
select * from datos_sensores
```

![Select de datos en MariaDB](./images/Datos_mariaDB.png)

Veamos ahora un sencillo código python para insertar datos. Antes instalamos el módulo pymqsl con

```sh
pip3 install pymysql
```


