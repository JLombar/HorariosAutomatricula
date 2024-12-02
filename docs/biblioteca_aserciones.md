# Bibliotecas de aserciones
Una biblioteca de aserciones es un conjunto de herramientas o funcinoes que los desarrolladores utilizan para comprobar el funcionamiento del código. Permiten realizar pruebas unitarias para verificar que una aplicación cumple con las expectativas, además de evitar que cambios en un futuro produzcan errores.  

Algunos prerrequisitos a la hora de elegir las bibliotecas:
* Debe tener una buena puntuación en [snyk Advisor](https://snyk.io/advisor/). Tener una buena puntuación en Skyk Advisor implica que la herramienta cumple con altos estándares en áreas como seguridad de datos y gestión de riesgos, demostrando ser una buena herramienta destinada a usar en un repositorio.
* En última instancia se valorará aquella herramienta que incluya una mayor variedad de aserciones, permitiéndonos mayor variedad a la hora de realizar diferentes tests.
## Elección
Estas son algunas de las bibliotecas de aserciones más comunes
### 1. unittest (PyUnit)
unittest es una biblioteca estándar de Python diseñada para realizar pruebas automatizadas. Es especialmente útil para validar el comportamiento de código mediante aserciones.  
unittest tiene soporte, y dado que es parte de la biblioteca estándar de Python, está mantenido oficialmente junto con las actualizaciones de Python.
### 2. behave
behave es una biblioteca de aserciones basadas en Behavior-Driven Development (BDD), una metodología que enfatiza la colaboración entre desarrolladores, testers y stakeholders mediante un lenguaje común. En lugar de centrarse en aserciones directas como unittest o pytest, behave utiliza un enfoque orientado a escenarios definidos en un lenguaje cercano al natural, lo que permite describir el comportamiento esperado del sistema.
El problema que tiene behave es que si miramos sus calificanciones con [snyk Advisor](https://snyk.io/advisor/python/behave) o el proyecto en [PyPi](https://pypi.org/project/behave/), lleva sin actualizarse siete años, podemos asumir que no tiene soporte, por lo cual lo descartaremos.
### 3. ensure
Es una biblioteca de aserciones para Python, al ver su perfil en [PyPi](https://pypi.org/project/ensure/) está actualizado recientemente, en diciembre de 2023, por lo que podríamos utilizarlo. Sin embargo, su perfil en [snik Advisor](https://snyk.io/advisor/python/ensure) tiene una nota muy baja por lo que no sería una buena opción a utilizar.
### 4. grappa
Otra opción que podríamos contemplar a la hora de elegir una herramienta, pero tiene una baja puntuación en [synk Advisor](https://snyk.io/advisor/python/grappa) y la última versión se publicó hace 4 años.
### 5. PyHamCrest
PyHarmCrest es otra opción, actualizada hace un año y un mes por última vez. El problema que tiene, es que al igual que resto de herramientas descartadas, tiene una baja valoración en [snyk Advisor](https://snyk.io/advisor/search?source=python&q=pyhamcrest), por lo que no la consideraremos.

## Elección final
Como hemos visto en las opciones el ecosistema de Python están un limitadas ya que los usuarios se han limitado a usar unittest, en ocasiones acompañado de las pocas aserciones que tiene pytest, y el resto de opciones se han ido abandonado con el tiempo, perdiendo la posibilidad de elegir entre varias herramientas y "monopolizando" la decisión.

En este caso, como ya hemos visto las limitadas herramientas que no pertenecen al propio núcleo de Python no son aceptables, por lo que elegiremos unittest como biblioteca de aserciones. Sin embargo, en ocasiones se usarán las aserciones de pytest para comprobar warnings u otro tipo de pruebas unitarias que unittest no sea capaz de comprobar con su biblioteca de aserciones.