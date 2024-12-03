# Test runners
Prerrequisitos a la hora de elegir un test runner serán similares a los de la [biblioteca de aserciones](./biblioteca_aserciones.md):
* Debe tener una buena puntuación en [snyk Advisor](https://snyk.io/advisor/). Tener una buena puntuación en Skyk Advisor implica que la herramienta cumple con altos estándares en áreas como seguridad de datos y gestión de riesgos, demostrando ser una buena herramienta destinada a usar en un repositorio/proyecto.
* Por último se valorará la escalabilidad del test runner en caso de que el proyecto se vuelva más complejo en futuros Milestones. En esta ecalabilidad se valorará características como: un sistema de fixtures y un salida detallada, facilitándo la depuración cuando hay muchos fallos en un gran proyecto.

## Elección
Estas son algunas de los test runners más comunes en Python:
### 1. unittest
Es el módulo estándar de Python para escribir y ejecutar pruebas unitarias, sin embargo también es posible usarlo como test runner que permite ejecutar pruebas unitarias en el proyecto. 

### 2. pytest
[pytest](https://github.com/pytest-dev/pytest) es uno de los test runners más populares y poderosos en Python. Se utiliza para ejecutar pruebas automatizadas y gestionar los resultados de esas pruebas. En nuestro repositorio también se usa como [biblioteca de aserciones](./biblioteca_aserciones.md)

### 3. Nose2
Nose2 es un framework de pruebas y un test runner para Python, que se utiliza para realizar pruebas unitarias y de integración. Es una extensión de unittest, el framework de pruebas estándar de Python, pero con características adicionales que lo hacen más fácil de usar y más flexible. 
### Elección final
Entre las opciones elegiremos pytest por delante de Nose2 o unittest. Nose2 no tiene una buena valoración en [snyk Advisor](https://snyk.io/advisor/python/nose2) por lo que no será una buena opción. Por otro pytest y Nose a diferencia de unittest son herramientas CLI, por lo que anzalizan la salida TAP y producen informes, con una salida de errores más detallada y clara, facilitando la depuración. También incluye un sistema de fixtures que unittest no incluye . Pytest es el único que comparte estas características, por lo que será nuestra elección como test runner.