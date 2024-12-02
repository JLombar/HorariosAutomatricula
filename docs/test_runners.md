# Test runners
Elegir un test runner adecuado es crucial porque afecta directamente la eficiencia, la efectividad y la calidad del proceso de pruebas en un proyecto de software. Facilitando la automatización de las pruebas, así como poder agruparlas o incluir subtests.
Prerrequisitos a la hora de elegir un test runner serán similares a los de la [biblioteca de aserciones](./biblioteca_aserciones.md):
* Debe tener una buena puntuación en [snyk Advisor](https://snyk.io/advisor/). Tener una buena puntuación en Skyk Advisor implica que la herramienta cumple con altos estándares en áreas como seguridad de datos y gestión de riesgos, demostrando ser una buena herramienta destinada a usar en un repositorio/proyecto.
* Por último se valorará la escalabilidad del test runner en caso de que el proyecto se vuelva más complejo en futuros Milestones.

## Elección
Estas son algunas de los test runners más comunes en Python:
### 1. unittest
Es el módulo estándar de Python para escribir y ejecutar pruebas unitarias, sin embargo también es posible usarlo como test runner que permite ejecutar pruebas unitarias en el proyecto. 

### 2. pytest
[pytest](https://github.com/pytest-dev/pytest) es uno de los test runners más populares y poderosos en Python. Se utiliza para ejecutar pruebas automatizadas y gestionar los resultados de esas pruebas. En nuestro repositorio también se usa como [biblioteca de aserciones](./biblioteca_aserciones.md)

### 3. Nose2
Nose2 es un framework de pruebas y un test runner para Python, que se utiliza para realizar pruebas unitarias y de integración. Es una extensión de unittest, el framework de pruebas estándar de Python, pero con características adicionales que lo hacen más fácil de usar y más flexible. 
### Elección final
Entre las 3 opciones que tenemos Nose2 directamente será descartada de la valoración ya que, aunque ha sido actualizado hace poco su puntuación en [snyk Advisor](https://snyk.io/advisor/python/nose2) es baja, no cumpliendo con los requisitos.  
Entre pytest y unittest elegiremos pytest como test runner al ser considerado más escalables por diferentes motivos como:
* Mayor facilidad a a hora de gestionar grandes conjuntos de pruebas
* pytest proporciona una salida de errores más detallada y clara, lo que facilita la depuración cuando se tienen muchos fallos en una gran proyecto
* Si en un futuro se quieren usar dependencias en las pruebas para futuros Milestones, pytest ofrece un sistema de fixtures, inyectando dependencias en las pruebas de forma eficiente  

Por estos motivos la escalabilidad de pytest es superior a la de unittest, por lo que lo seleccionaremos como test runner.