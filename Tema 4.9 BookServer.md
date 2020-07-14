## Servidor de libros electronicos (BookServer con calibre)

Vamos a instalar un sencillo sistema que nos va a permitir acceder a tu Biblioteca de libros electrónicos desde cualquier parte del mundo:

Usaremos [Calibre](https://calibre-ebook.com/), un gestor de bibliotecas open source que nos permite organizar y almacenar nuestros ebooks.

![](./images/Calibre_libros.png)

Podemos filtrar buscando por título, autor, agrupar por colecciones, convertir entre formatos y exportar a nuestros lectores de ebooks

![](./images/Calibre_Filtro_autor.png)


La instalación no puede ser más sencilla
```sh
sudo apt install calibre
```

Importamos nuestros libros y ya lo podemos usar...

Aunque está pensado como una aplicación de escritorio también incluye un Servidor web incorporado con el que podemos acceder a los ebooks. 

Podemos acceder al servidor desde cualquier ordenadore o tableta

![Calibre wn Tablet](./images/CalibreTablet.jpg)

Incluso haciendo búsquedas

![Calibre Buscar en Tablet](./images/CalibreBuscarTAbleta.jpg)

Podemos leer directamente sin necesitad de ninguna aplicación además del navegador

![Calibre Leyendo Online](./images/CalibreLeyendoOnline.jpg)

Para activarlos entramos en las preferencias:
![Botón Preferencias](./images/Calibre_preferencias.png)
![Menú preferencias](./images/Calibre_conf.png)

Ahora en la configuración de "Compartir por la red" donde vamos a activar el sevidor, con su puerto (8080 por defecto) y si así lo queremos marcaremos la opción para se arranca cada vez que abrimos Calibre

![Configuracion Servidor](./images/Calibre_Conf_servidor.png)

Es el momento de configurar los usuarios, a los que le podremos dar permiso o no de escritura para modificar los libros

![Gestión de usuarios](./images/Calibre_Usuarios.png)

## Acceso desde internet

Si queremos acceder desde fuera de nuestra red, configuraremos el router en la opción de NAT para el puerto usado

![Configuración Router](./images/EbookRouter.png)

Para poder acceder remotamente sin saber nuestra IP  configuraremos un servicio de Dynamic DNS (DDNS) 

Estos son algunos proveedores gratuitos de servicios de DDNS

![Free DDNS](./images/FreeDDNS.png)

En mi caso usaré el servicio de NoIP

![Free DDNS](./images/NoIP.png)

Ahora configuramos en el router la cuenta para que automáticamente se refresque

![Conf DDNS](./images/ConfDDNS.png)

Y ya podremos acceder remotamente tras logarnos

![](./images/CalibreUsuarios.jpg)


![](./images/CalibreBiblioteca.jpg)

