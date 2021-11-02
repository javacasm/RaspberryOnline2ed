## Aulas con Raspberry Pi

Como ya hemos visto, se usa bastante Raspberry Pi en las aulas informáticas de colegios de todo el mundo

![Aula con Raspberry Pi](./images/AulaPi.jpg)

Desde hace mucho tiempo recomiendo a los profesores el uso de Raspberry Pi como base de las aulas informáticas por varias razones:

* El coste del equipo:
    * Raspberry Pi
    * Alimentación
    * Monitor (que puede ser reciclado)
    * Teclado y ratón USB (que pueden ser reciclados)
    * Tarjeta SD, que en muchos casos recomiendo que sea del propio alumno, así puede llevarse a casa. El coste es mínimo
    * Carcasa transparente para hacer más apetecible el interior
* Al estar basado en Linux nos permite usar casi cualquier herramienta open source, pudiendo crear un laboratorio con todo tipo de servidores.
* Hay una gran cantidad de documentación y de gran calidad sobre su uso
* Existen infinidad de proyectos publicados de todos los niveles de complejidad
* El usarla con una carcasa abierta o transparente incita la curiosidad de los alumnos, incluso hasta el punto de comprarse una particular.
* Podemos usar en multitud de asignaturas:
    * Como ordenador de propósito general
    * Para aprender a programar, ya que podemos usar casi todos los lenguajes disponibles: Scratch, Python, C, ...
    * Para introducir técnicas más avanzadas como la inteligencia artificial o el reconocimiento de imágenes 
    * Para aprender electrónica digital usando la conectividad de GPIO
    * Es ideal para hacer proyectos de robótica
    * Para trabajar todo lo relacionado con redes creando y configurando routers, servidores, equipos ligeros, ... hasta soluciones en telecomunicaciones como son [Asterisk](https://www.asterisk.org/)
    * Permiten una Integración muy buena con las herramientas Google, muy usadas en las clases

Con la llegada de la Raspi 4 el panorama ha mejorado aún más:

* Permite arrancar desde USB (todavía en Beta pero va bastante bien), lo que permite usar un disco SSD barato de capacidad, velocidad y duración mucho mayores que las tarjetas SD. 
* La cantidad de RAM hace totalmente posible el uso en el día a día. Yo creo que 4Gb son suficientes para un uso normal, pero si te da el presupuesto incluye 8Gb

Algunas ideas para mejorar el funcionamiento:

* El usar teclados y ratones inalámbricos tiene la ventaja de que el consumo por USB es menor 
* Arduino y microbit funcionan perfecto, pero hasta donde yo sé Lego no está soportado
* Uso de arranque por USB: Aunque seguimos necesitando una tarjeta SD para configurar inicialmente las raspi4, ya no se usan para que arranquen en el día a día. 
* Para mejorar el rendimiento podemos usar discos SSD con USB 3.0. Yo estoy haciendo pruebas con una versión de 128Gb de [este disco](https://es.aliexpress.com/item/33053472759.html?spm=a2g0s.9042311.0.0.274263c0sLwovz) que me costó 25$
* Si vamos a usarla en un aula de propósito general podemos incluir

## Clonado de tarjetas

Aunque existen herramientas más sofisticadas, la misma herramienta SD Copier nos permite crear un clon de un sistema ya en funcionamiento. 

Podemos crear un sistema con todo lo necesario y a partir de él clonar las tarjetas del resto.
