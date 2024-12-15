# Imagen para el contenedor
La imagen deberá cumplir los siguientes requisitos:
* Mantenimiento: debe tener un buen mantenimiento en activo para reducir la deuda técnica en el futuro
* Se tendrá en cuenta que la imagen pese poco, optimizando recursos al necesitar menos memoria.
* Debe ser segura, es decir, que no tenga vulnerabilidades. Podemos comprobar las vulnerabilidades en la propia web de [Docker Hub](https://hub.docker.com/), en la pestaña de tags de cada imagen.
## Algunas opciones
Debemos elegir una imagen de Docker para nuestro proyecto, para ello revisaremos las siguientes imágenes, teniendo en mente los requisitos que hemos listado:

### Alpine Linux
La imagen de [Alpine Linux](https://hub.docker.com/_/alpine) tiene un mantenimiento en activo, siendo su última versión hace sólo 3 meses. Alpine presume de ser una imagen que pesa únicamente 5MB, por lo que no incluye funcionalidades extras por defecto, ya que su propósito principal es ser mínima y eficiente.  
Las últimas versiones estables se publicaron hace una semana, por lo que es seguro que tiene mantenimiento en activo. No tiene vulnerabilidades en su última versión estable, por lo que es segura para ser usada.

### Ubuntu
[Ubuntu](https://hub.docker.com/_/ubuntu) cuenta con mantenimiento activo y soporte. Las imágenes pesan un poco menos de 30MB, un peso bastante bajo, cumpliendo con los requisitos. Por último podemos concluir que es una buena opción al contar únicamente con la instalación base del sistema.  
Su imagen latest, tiene muchas vulnerabilidades, por lo que no es seguro utilizarla.

### Debian
La imagen de [Debian](https://hub.docker.com/_/debian) última imagen se hizo hace menos de una semana, por lo que tiene soporte activo. Pesa alrededor de 50MB. Al igual que ubuntu, suelen ofrecer la versión base del sistema operativo, sin funcionalidades extra en estas variantes:
* bullseye-slim: basada en Debian 11 optimizada, sólo contiene los paquetes esenciales, con un tamaño aprocimado de 22MB
* bookworm-slim: es como bullseye pero basada en Debian 12, también pesa sobre los 30MB
* debian:stable-slim: descargará la versión de Debian que sea la última versión "estable" en el momento.
Como otras imágenes de las que hemos hablado, tiene gran cantidad de vulnerabilidades em todas sus variantes (tanto bookworm, como bullseye, las variantes slim...) que no la hacen segura de usar.
### Imagen "oficial" de Python
Otra alternativa la [imagen oficial de python del propio Docker](https://hub.docker.com/_/python). Viene preinstalada con diferentes versiones de python y tiene diferentes variantes:
* Alpine Linux: al igual que la ya explicada, es muy ligera y no incluye dependencias adicionales más allá de la instalación del sistema.
* Debian "bookworm": el peso es de 149MB, excesivo ya que incluye muchas dependencias preinstaladas
* Debian "bookworm-slim": la imagen es mucho mas pequeña que bookworm normal al no incluir funcionalidades más allá del sistema operativo básico y las dependencias mínimas necesarias para ejecutar Python, su peso en el disco es 52MB.

Todas sus imágenes cuentan con vulnerabilidades de importancia severa, por lo que no son apropiadas para su uso.
### bitnami/python
La [imagen de bitnami para Python](https://hub.docker.com/r/bitnami/python), es actualizada rápidamente nuevas versiones de la imagen, recibiendo su última actualización hace menos de una semana, por lo que podemos asumir que tiene mantenimiento en activo. La imagen pesa sobre los 190MB, siendo un tamaño grande en comparación del resto de imágenes, pero no un gran tamaño como para descartar esta opción.
Las imágenes de bitnami se basan en un minideb o scratch, por lo que tendrá funcionalidades extra, pero pocas.

## Elección final
Usaremos la última versión estable de Alpine, que no cuenta con vulnerabilidades, un peso reducido, cuenta con mantenimiento en activo y sin funcionalidades extra.  
Para poder usar la imagen de Alpine Linux debemos instalar Python en la propia imagen, junto con todas las dependencias que esto conlleva. Para ello podemos aplicar la construcción de nuestra imagen en dos fases, reduciendo el peso de la imagen, eliminando las herramientas de desarrollo, consiguiendo menor exposición a vulnerabilidades y una aplicación aislada y segura.  
Es cierto que al final resulta una imagen algo pesada comparada con el resto tras instalar python, pesando algo mas de 400MB. Sin embargo, no es un peso excesivamente grande como para que la descartemos al no ocupar demasiado en disco y sólo tardará en construirse la primera vez, ya que si queremos hacer cambios en la imagen los podemos hacer en la segunda fase, de forma que no debe construise entera de nuevo gracias a la construcción en fases.