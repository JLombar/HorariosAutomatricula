# HorariosAutomatrícula
Repositorio de Jorge Lombardo de la asignatura IV.

## Descripción del problema
Todos los años, una gran cantidad de alumnos de Ingeniería Informática de la UGR tienen problemas con su horario al comenzar el curso tras realizar la automatrícula, ya que el resultado suele incluir asignaturas cuyos horarios coinciden. A pesar de que los horarios se pueden encontrar en la web de la ETSIIT y el horario es pensado a priori por los estaudiantes, nunca resulta de la forma que ellos desean y muchas veces provoca mala combinación de asignaturas. Por este motivo, es necesario modificar la matrícula, lo que provoca que muchos de ellos se incorporen a una o varias asignaturas ya iniciadas, durante un par de semanas o incluso hasta un mes si hablamos de subgrupos de prácticas, generando numerosos problemas al iniciar el curso académico.

## Biblioteca de aserciones y test runners
Se pueden comprobar los ficheros [biblioteca de aserciones](./docs/biblioteca_aserciones.md) y [test runners](./docs/test_runners.md) para ver las explicaciones sobre por qué se usa pytest como ambas

# Tareas automatizadas
Se puede consultar el fichero [iv.yaml](./iv.yaml) para consultar el  de fichero que se usa para automatizar tareas y la orden necesaria para ejecutarlo.

## Comprobar sintaxis del proyecto
Si se quiere comprobar la sintaxis del proyecto se debe ejecutar según las claves de [iv.yaml](./iv.yaml) "orden check", que en nuestro caso sería: 
```bash
make check
```

## Ejecutar tests
Para ejecutar los test del proyecto se debe ejecutar según las claves de [iv.yaml](./iv.yaml) "orden test", que en nuestro caso sería: 
```bash
make test
```

## Imagen base para Docker
La documentación sobre la imagen de base elegida para Docker se encuentra [aquí](./docs/imagen_docker.md)