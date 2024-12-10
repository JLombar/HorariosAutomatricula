# Imagen para el contenedor
La imagen deberá cumplir los siguientes requisitos:
* Mantenimiento: debe tener un buen mantenimiento en activo para reducir la deuda técnica en el futuro
* Se tendrá en cuenta que la imagen pese poco, optimizando recursos al necesitar menos memoria y mayor velocidad de despliegue.
* Debe ser segura, es decir, que no tenga vulnerabilidades. Podemos comprobar las vulnerabilidades en la propia web de [Docker Hub](https://hub.docker.com/), en la pestaña de tags de cada imagen.
* No se piden funcionalidades extras al sólo ser usada para testear el proyecto
## Algunas opciones
Debemos elegir una imagen de Docker para nuestro proyecto, para ello revisaremos las siguientes imágenes, teniendo en mente los requisitos que hemos listado:

### Alpine Linux
La imagen de [Alpine Linux](https://hub.docker.com/_/alpine) tiene un mantenimiento en activo, siendo su última versión hace sólo 3 meses. Alpine presume de ser una imagen que pesa únicamente 5MB, por lo que no incluye funcionalidades extras por defecto, ya que su propósito principal es ser mínima y eficiente.  
Su problema es que todas sus versiones tienen vulnerabilidades que comprometen la seguridad del sistema, es cierto que su última versión no tiene, pero al ser publicada hace menos de una semana es posible asumir que todavía no se han descubierto.
### Ubuntu
[Ubuntu](https://hub.docker.com/_/ubuntu) cuenta con mantenimiento activo y soporte. Las imágenes pesan un poco menos de 30MB, un peso bastante bajo, cumpliendo con los requisito. Por último podemos concluir que es una buena opción al contar únicamente con la instalación base del sistema.  
Al igual que con Alpine Linux, tiene muchas vulnerabilidades, por lo que no es seguro utilizarla.
### Debian
La imagen de [Debian](https://hub.docker.com/_/debian) última imagen se hizo hace menos de una semana, por lo que tiene soporte activo. Pesa alrededor de 50MB, al igual que ubuntu, suelen ofrecer la versión base del sistema operativo, sin funcionalidades extra.  
Al igual que que el resto de imágenes de las que hemos hablado, tiene gran cantidad de vulnerabilidades que no la hacen segura de usar.
### Imagen "oficial" de Python
Otra alternativa la [imagen oficial de python del propio Docker](https://hub.docker.com/_/python). Viene preinstalada con diferentes versiones de python y tiene diferentes variantes:
* Alpine Linux: al igual que la ya explicada, es muy ligera y no incluye dependencias adicionales más allá de la instalación del sistema.
* Debian "bookworm": el peso es de 149MB, excesiva ya que incluye muchas dependencias preinstaladas
* Debien "bookworm-slim": la imagen es mucho mas pequeña que bookworm normal, su peso en el disco es 52MB. No incluye funcionalidades más allá del sistema operativo básico y las dependencias mínimas necesarias para ejecutar Python. 

Las vulnerabilidades no están disponibles en la pestaña tags. Si miramos la web de [snyk Advisor](https://snyk.io/advisor/docker/python) tampoco podemos ver las vulnerabilidades, por lo que no es seguro usar estas imágenes al no tener la información necesaria.
### bitnami/python
La [imagen de bitnami para Python](https://hub.docker.com/r/bitnami/python), es actualizada rápidamente nuevas versiones de la imagen, recibiendo su última actualización hace menos de una semana, por lo que podemos asumir que tiene mantenimiento en activo. La imagen pesa sobre los 190MB, siendo un tamaño grande en comparación del resto de imágenes, pero no un gran tamaño como para descartar esta opción.
Las imágenes de bitnami se basan en un minideb o scratch, por lo que tendrá funcionalidades extra, pero muy limitadas.

## Elección final
La imágen de python the bitnami será la elegida para nuestro proyecto ya que:
* Tiene mantenimiento en activo, con actualizaciones automáticas cuando sale una nueva versión
* Es segura, al no tener vulnerabilidades
* Tiene un número muy pequeño de dependencias extra
* Es cierto que es una imágen algo más pesada comparada con las demás, pero no lo suficiente como para que sea descartada simplemente por este motivo