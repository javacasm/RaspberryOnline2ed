## Aulas con Raspberry Pi

Como ya hemos visto, se usa bastante Raspberry Pi en las aulas informáticas de colegios de todo el mundo

![Aula con Raspberry Pi](./images/AulaPi.jpg)

Desde hace mucho tiempo recomiendo a los profesores el uso de Raspberry Pi como base de las aulas informáticas por varias razones:

* El coste del equipo:
    * Raspberry Pi
    * Alimentación
    * Monitor (que puede ser reciclado)
    * Teclado y ratón USB (que pueden ser reciclados)
    * Tarjeta SD, que en muchos casos recomiendo que sea del propio alumno, así puede llevársela a casa. El coste es mínimo
    * Carcasa transparente para hacer más apetecible el interior y despertar la curiosidad.
* Al estar basado en Linux nos permite usar casi cualquier herramienta open source, pudiendo crear un laboratorio con todo tipo de servidores.
* Hay una gran cantidad de documentación y de gran calidad sobre su uso
* Existen infinidad de proyectos publicados de todos los niveles de complejidad
* El usarla con una carcasa abierta o transparente incita la curiosidad de los alumnos, incluso hasta el punto de comprarse una propia.
* Podemos usar en multitud de asignaturas:
    * Como ordenador de propósito general
    * Para aprender a programar, ya que podemos usar casi todos los lenguajes disponibles: Scratch, Python, C, ...
    * Para introducir técnicas más avanzadas como la inteligencia artificial o el reconocimiento de imágenes 
    * Para aprender electrónica digital usando la conectividad de GPIO
    * Es ideal para hacer proyectos de robótica
    * Para trabajar todo lo relacionado con redes creando y configurando routers, servidores, equipos ligeros, ... hasta soluciones en telecomunicaciones como es [Asterisk](https://www.asterisk.org/)
    * Permiten una Integración muy buena con las herramientas Google, muy usadas en las clases

Con la llegada de la Rasperry 4 el panorama ha mejorado aún más:

* Permite arrancar desde USB, lo que permite usar un disco SSD barato de capacidad, velocidad y duración mucho mayores que las tarjetas SD. 
* La cantidad de RAM hace totalmente posible el uso en el día a día. Yo creo que 4GB son suficientes para un uso normal, pero si te da el presupuesto incluye 8GB

Algunas ideas para mejorar el funcionamiento:

* El usar teclados y ratones inalámbricos tiene la ventaja de que el consumo por USB es menor 
* Arduino y microbit funcionan perfecto, pero hasta donde yo sé Lego no está soportado
* Uso de arranque por USB: Aunque seguimos necesitando una tarjeta SD para configurar inicialmente las raspi4, ya no se usan para que arranquen en el día a día. 
* Para mejorar el rendimiento podemos usar discos SSD con USB 3.0. Yo estoy haciendo pruebas con una versión de 128GB de [este disco](https://es.aliexpress.com/item/33053472759.html?spm=a2g0s.9042311.0.0.274263c0sLwovz) que me costó 25$
* Si vamos a usarla en un aula de propósito general podemos incluir la distribución completa.

## Clonado de tarjetas

Para trabajar con un aula básicamente vamos a necesitar el hardware y un montón de tarjetas SD que podemos clonar directamente a partir de una instalación, salvo que queramos que el propio alumnado se instale su propio SO, lo cual también es interesante.

Aunque existen herramientas más sofisticadas, la misma herramienta **SD Card Copier** incluida en Raspberry Pi OS nos permite crear un clon de un sistema  en funcionamiento. 

El uso es muy sencillo, seleccionando el dispositivo origen y el destino. Para ello necesitamos usar varios dispositivos USB.

![Aplicación para duplicar tarjetas o discos USB](./images/sd_card_copier.png)

Podemos crear un sistema con todo lo necesario y a partir de él clonar las tarjetas del resto.

Recuerda que para hacer pequeñas modificaciones en una tarjeta la puedes abrir en cualquier ordenador y editar o modificar el fichero que queramos (por ejemplo el nombre del equipo),

