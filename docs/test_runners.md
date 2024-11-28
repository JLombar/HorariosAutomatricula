Elegir un test runner adecuado es crucial porque afecta directamente la eficiencia, la efectividad y la calidad del proceso de pruebas en un proyecto de software. Facilitando la automatización de las pruebas, así como poder agruparlas o incluir subtests.
Prerrequisitos a la hora de elegir un test runner serán similares a los de la [biblioteca de aserciones](./biblioteca_aserciones.md):
* Debe tener una buena puntuación en [snyk Advisor](https://snyk.io/advisor/). Tener una buena puntuación en Skyk Advisor implica que la herramienta cumple con altos estándares en áreas como seguridad de datos y gestión de riesgos, demostrando ser una buena herramienta destinada a usar en un repositorio/repositorio
* Se debe comprobar el buen mantenimiento y actualización, disminuyendo la deuda técnica. Para comprobar esto, podemos ayudarnos de [PyPi](https://pypi.org/) para herramientas no nativas de Python, comprobando cuando fue la última actualización del paquete.
* Por último se valorará la simplicidad a la hora de usar la herramienta por parte de la herramienta por parte del programador.

## Elección
Estas son algunas de los test runners más comunes en Python:
### 1. unittest
Es el módulo estándar de Python para escribir y ejecutar pruebas unitarias, sin embargo también es posible usarlo como test runner que permite ejecutar pruebas unitarias en el proyecto. 

### 2. pytest
[pytest](https://github.com/pytest-dev/pytest) es uno de los test runners más populares y poderosos en Python. Se utiliza para ejecutar pruebas automatizadas y gestionar los resultados de esas pruebas. En nuestro repositorio también se usa como [biblioteca de aserciones](./biblioteca_aserciones.md)

### 1. Nose
Nose (o nose2) es un framework de pruebas y un test runner para Python, que se utiliza para realizar pruebas unitarias y de integración. Es una extensión de unittest, el framework de pruebas estándar de Python, pero con características adicionales que lo hacen más fácil de usar y más flexible.
Nose genera informes detallados sobre los resultados de las pruebas, lo que te permite identificar rápidamente qué pruebas han pasado, fallado o se han saltado.
El único problema es que su puntuación en [snyk Advisor](https://snyk.io/advisor/python/nose) es muy baja, por lo que será descartado.

### pytest vs unittest
pytest detevta las pruebas en cualquier archivo mientras siga el patrón test_*.py, sin neceidad de clases y métodos específicos, reduciendo la configuración inicial.
Si en un futuro se quieren usar dependencias en las pruebas para futuros Milestones, pytest ofrece un sistema de fixtures, inyectando dependencias en las pruebas de forma eficiente. En unittest, tendríamos que configurar todo esto manualmente usando métodos como setUp o tearDown, complicando el uso de la herramienta.

### pytest vs pytest-bdd
Podríamos usar pytest-bdd al ser más completo que pytest, sin embargo lo descartaremos al tener menor puntuación en [snyk Advisor](https://snyk.io/advisor/python/pytest-bdd) que [pytest](https://snyk.io/advisor/python/pytest). Usaremos pytest también como test runner.