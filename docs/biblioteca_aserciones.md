# Bibliotecas de aserciones
Una biblioteca de aserciones es un conjunto de herramientas o funcinoes que los desarrolladores utilizan para comprobar el funcionamiento del código. Permiten realizar pruebas unitarias para verificar que una aplicación cumple con las expectativas, además de evitar que cambios en un futuro produzcan errores.  

Algunos prerrequisitos a la hora de elegir las bibliotecas:
* Que sea compatible con Python.
* Debe tener una buena puntuación en [snyk Advisor](https://snyk.io/advisor/) o [PyPi](https://pypi.org/).
* Se deberá tener en cuenta la comunidad de la que dispone, ya que se busca tener un buen mantenimiento y actualización, disminuyendo la deuda técnica.
* En última instancia se valorará aquella herramienta que incluya una mayor variedad de aserciones, permitiéndonos mayor variedad a la hora de realizar diferentes tests.
## Elección
Estas son algunas de las bibliotecas de aserciones más comunes
### 1. unittest (PyUnit)
unittest es una biblioteca estándar de Python diseñada para realizar pruebas automatizadas. Es especialmente útil para validar el comportamiento de código mediante aserciones.  
unittest tiene soporte, y dado que es parte de la biblioteca estándar de Python, está mantenido oficialmente y es confiable para escribir y ejecutar pruebas.
### 2. pytest
pytest es una biblioteca de pruebas para Python que ofrece una manera más flexible y moderna de realizar pruebas automatizadas, incluyendo un potente conjunto de aserciones que no se encuentran disponibles en Python  
Tiene una gran puntuación en [snyk Advisor](https://snyk.io/advisor/python/pytest), por lo que será una buena herramienta a considerar ya que a esto se le suma que su última versión es de hace sólo 2 meses, por lo que podemos supones que tienen soporte activo y recibe actualizaciones.
### 3. behave
behave es una herramienta para pruebas basadas en Behavior-Driven Development (BDD), una metodología que enfatiza la colaboración entre desarrolladores, testers y stakeholders mediante un lenguaje común. En lugar de centrarse en aserciones directas como unittest o pytest, behave utiliza un enfoque orientado a escenarios definidos en un lenguaje cercano al natural, lo que permite describir el comportamiento esperado del sistema.
El problema que tiene behave es que si miramos sus calificanciones con [snyk Advisor](https://snyk.io/advisor/python/behave) o el proyecto en [PyPi](https://pypi.org/project/behave/), lleva sin actualizarse siete años, podemos asumir que no tiene soporte, por lo cual lo descartaremos.

## pytest vs unittest
Entre pytest y unittest será preferible usar [pytest](https://github.com/pytest-dev/pytest) ya que incluye las mismas aserciones que unittest, más unas cuantas que son añadidas por la misma biblioteca, permitiendo mayor flexiblidad a la hora de elaborar los tests.