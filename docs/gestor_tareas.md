# Gestor de tareas
En este caso al estar trabajando en Python, la herramienta de construcción que estamos usando como [gestor de dependencias](./gestor_dependencias.md) lo podemos usar para automatizar ciertas tareas, en este caso queremos automatizar la instalación de las dependencias, que es capaz de realizar apoyándose en el archivo [pyproject.toml](../pyproject.toml). 

## Automatización de tareas
Usar Makefile para ejecuar herramientas en Python es una práctica común, especialmente en proyectos en los que se requieren múltiples tareas repetitivas, como puedens ser pruebas. 

Makefile facilita la automatización de estas tareas con comandos simples y mejorando la organización y eficiencia en el flujo de trabajo. Otras opciones para automatizar tareas disponibles en Python:
### 1. Scripts de Python personalizados
Se puedes escribir scripts en Python que que realice las tareas de configuración, pruebas, limpieza, instalación, etc. Ofrece gran flaxibilidad ya que se puede aprovechar la programación completa en Python, además funciona en cualquier entorno donde Python esté instalado.   
Sin embargo, cada comando requiere llamadas a subprocess, lo que puede hacer que el script sea más detallado y extenso. También se suma que ejecutar tareas individuales requiere conocer la interfaz de Python y el nombre de cada función
### 2. Invoke
Es una biblioteca de Python para automatizar tareas que permite definir comandos y ejecutarlos desde la terminal, similar a make. Ofrece una sintaxis elegante y es multiplataforma, lo que lo hace atractivo para proyectos que necesitan ejecutarse en Windows.
Podemos mirar el [repositorio de Invoke](https://github.com/pyinvoke/invoke). En el mismo se puede ver su buen recibimiento por la comunidad, teniendo más de 4000 estrellas.  
Sin embargo, a pesar de su gran aprovación podemos comprobar que el mismo lleva desde 2023 sin recibir ninguna actualización, por lo que podríamos asumir un descenso en la velocidad de desarrollo del mismo. Este aspecto podría ser preocupante para nuevas versiones de Python, pudiendo resultar en bugs si usamos en un futuro versiones más modernas de Python.
### 3. Tox
[Tox](https://github.com/tox-dev/tox) es una herramienta de automatización y gestión de entornos de pruebas, especialmente útil en proyectos donde se debe verificar la compatibilidad con múltiples versiones de Python o ejecutar tareas en entornos controlados.  
No la usaremos ya que, como se ha comentado, su enfoque está más centrado en la ejecución de pruebas, lo que lo hace menos flexible en comparación con otras herramientas que permiten una mayor diversidad de tareas más allá de las pruebas.
### 4. Fabric
[Fabric](https://github.com/fabric/fabric) es una herramienta para automatizar tareas remotas, especialmente diseñada para desplegar aplicaciones o ejecutar comandos en servidores remotos. Fabric 1.x es bastante popular, pero la versión 2.x se ha reescrito con nuevas características y un enfoque más flexible. Facilita la creación de scripts para tareas de automatización de infraestructura.  
Se centra más en la administración de sistemas y servidores remotos, por lo que no es tan común en tareas de desarrollo local o automatización de pruebas.  
Fabric no es tan común ni está tan destinada como algunas de las ya mencionadas para automatizar tareas dentro de proyectos Python de desarrollo diario (como pruebas o compilación), por ello la descartaremos.
### 6. Ninja
[Ninja](https://github.com/ninja-build/ninja) es una herramienta de construcción que, como Make, se basa en archivos de configuración (build.ninja) para definir reglas y dependencias. A diferencia de Make, Ninja fue diseñada para ser extremadamente rápida y eficiente, especialmente en proyectos con grandes volúmenes de archivos y compilaciones complejas.  
Es ampliamente utilizada en entornos donde la velocidad de compilación es crítica, como en la construcción de navegadores y sistemas operativos. Ninja se enfoca únicamente en la construcción, delegando la generación de archivos de configuración a otras herramientas como CMake, lo que facilita su integración en flujos de trabajo avanzados.
### 7. Taskfile(Task)
[Task](https://github.com/go-task/task) es una herramienta de automatización simple y flexible que utiliza un archivo Taskfile.yml para definir tareas y flujos de trabajo. Su sintaxis basada en YAML facilita la lectura y el mantenimiento de scripts de automatización, y permite definir tareas de manera modular, con soporte para variables y dependencias entre tareas.  
Task es compatible con múltiples lenguajes y plataformas, lo que la convierte en una opción versátil tanto para desarrolladores individuales como para equipos que buscan simplificar tareas repetitivas, como la ejecución de pruebas.

### Conclusión
De todos las opciones para automatizar tareas mencionados, se descartarían los **Scripts de Python**, ya que para ejecutar tareas es necesario conocer la interfaz de Python y el nombre de cada una de las funciones que se quiere ejecutar, siendo menos práctico.

Para este proyecto, la elección de Makefile para la automatización de tareas radica en su simplicidad y eficiencia. Makefile permite una configuración rápida y es ampliamente compatible sin requerir instalaciones adicionales. Es especialmente útil para tareas de construcción repetitivas, permitiendo a los desarrolladores ejecutar comandos de forma rápida y directa sin la carga adicional de un intérprete.

Otras opciones como Invoke, Fabric, y Task presentan funcionalidades valiosas, pero agregan complejidad innecesaria cuando el objetivo es mantener la simplicidad. Por ejemplo, Invoke y Task requieren configuraciones adicionales y actualizaciones de dependencias, lo cual puede añadir sobrecarga sin beneficios frente a Makefile. En conclusión, en proyectos donde prima la sencillez como este, Makefile es la herramienta ideal, al ser fácil de usar con un rendimiento robusto.