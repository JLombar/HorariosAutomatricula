# Imagen para el contenedor
La imagen deberá cumplir los siguientes requisitos:
* Mantenimiento: debe tener un buen mantenimineto en activo para reducir la deuda técnica en el futuro
* Se tendrá en cuenta que la imagen pese poco, optimizando recursos al necesitar menos memoria y mayor velocidad de despliegue.
* No se piden funcionalidades extras al sólo ser usada para testear el proyecto
## Algunas opciones
Debemos elegir una imagen de Docker para nuestro proyecto, para ello revisaremos las siguientes imágenes, teniendo en mente los requisitos que hemos listado:

### Alpine Linux
La imagen de [Alpine Linux](https://hub.docker.com/_/alpine) tiene un mantenimiento en activo, siendo su última versión hace sólo 3 meses. Alpine presume de ser una imagen que pesa únicamente 5MB, por lo que no incluye muchas funcionalidades extras por defecto, ya que su propósito principal es ser mínima y eficiente.
### Ubuntu
[Ubuntu] https://hub.docker.com/_/ubuntu cuenta con mantenimiento activo y soporte. Las imágenes pesan un poco menos de 30MB, un peso bastante bajo, cumpliendo con los requisito. Por último podemos concluir que es una buena opción al contar únicamente con la instalación base del sistema
### Debian
La imagen de [Debian](https://hub.docker.com/_/debian/tags) última imagen se hizo hace menos de una semana, por lo que tiene soporte activo. Pesa alrededor de 50MB, al igual que ubuntu, suelen ofrecer la versión base del sistema operativo, sin funcionalidades extra.
### Imagen "oficial" de Python
Otra alternativa la [imagen oficial de python del propio Docker](https://hub.docker.com/_/python). Viene preinstalada con diferentes versiones de python y tiene diferentes variantes:
* Alpine Linux, ya explicada
* Debian "bookworm": el peso es de 149MB, excesiva ya que incluye muchas dependencias preinstaladas
* Debien "bookworm-slim": la imagen es mucho mas pequeña que bookworm normal, su peso en el disco es 52MB. No incluye funcionalidades más allá del sistema operativo básico y las dependencias mínimas necesarias para ejecutar Python.
### bitnami/python
La [imagen de bitnami para Python](https://hub.docker.com/r/bitnami/python), es actualizada rápidamente nuevas versiones de la imagen, recibiendo su última actualización hace menos de una semana, por lo que podemos asumir que tiene mantenimiento en activo. La imagen pesa sobre los 190MB, siendo un tamaño grande en comparación del resto de imágenes, pero no un gran tamaño como para descartar esta opción.
Las imágenes de bitnami se basan en un minideb o scratch, por lo que no tendrá funcionalidades extra.