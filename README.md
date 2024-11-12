# HorariosAutomatrícula
Repositorio de Jorge Lombardo de la asignatura IV.

## Descripción del problema
Todos los años, una gran cantidad de alumnos de Ingeniería Informática de la UGR tienen problemas con su horario al comenzar el curso tras realizar la automatrícula, ya que el resultado suele incluir asignaturas cuyos horarios coinciden. A pesar de que los horarios se pueden encontrar en la web de la ETSIIT y el horario es pensado a priori por los estaudiantes, nunca resulta de la forma que ellos desean y muchas veces provoca mala combinación de asignaturas. Por este motivo, es necesario modificar la matrícula, lo que provoca que muchos de ellos se incorporen a una o varias asignaturas ya iniciadas, durante un par de semanas o incluso hasta un mes si hablamos de subgrupos de prácticas, generando numerosos problemas al iniciar el curso académico.

## Gestor de dependencias y automatización de tareas
Las elecciones sobre el [gestor de dependencias](./docs/gestor_dependencias.md) y la [herramienta de automatización de tareas](./docs/gestor_tareas.md) están enlazadas en este texto en caso de que quieran consularse.

## Instalación
Si queremos instalar todo lo necesario para ejecutar el programa debemos instalar Python, Poetry así como las dependencias necesarias:
```bash
make install
```

## Comprobar sintaxis del proyecto
Si se quiere comprobar la sintaxis del proyecto se debe ejecutar: 
```bash
make check
```

## Instalación y comprobación
Si se quieren realizar ambas tareas anteriores a la vez se debe ejecutar:
```bash
make install check
```