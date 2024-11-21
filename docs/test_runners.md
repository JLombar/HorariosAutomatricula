Elegir un test runner adecuado es crucial porque afecta directamente la eficiencia, la efectividad y la calidad del proceso de pruebas en un proyecto de software. Facilitando la automatización de las pruebas, así como poder agruparlas o incluir subtests.
Prerrequisitos a la hora de elegir un test runner serán similares a los de la [biblioteca de aserciones](./biblioteca_aserciones.md):
* Compatibilidad con Python
* Debe tener una buena puntuación en [snyk Advisor](https://snyk.io/advisor/) o [PyPi](https://pypi.org/).
* Se deberá tener en cuenta la comunidad de la que dispone, ya que se busca tener un buen mantenimiento y actualización, disminuyendo la deuda técnica.

## Elección
Estas son algunas de los test runners más comunes en Python:
### 1. pytest
[pytest](https://github.com/pytest-dev/pytest) es uno de los test runners más populares y poderosos en Python. Se utiliza para ejecutar pruebas automatizadas y gestionar los resultados de esas pruebas. En nuestro repositorio también se usa como [biblioteca de aserciones](./biblioteca_aserciones.md)

### 2. Nose
Nose (o nose2) es un framework de pruebas y un test runner para Python, que se utiliza para realizar pruebas unitarias y de integración. Es una extensión de unittest, el framework de pruebas estándar de Python, pero con características adicionales que lo hacen más fácil de usar y más flexible.
Nose genera informes detallados sobre los resultados de las pruebas, lo que te permite identificar rápidamente qué pruebas han pasado, fallado o se han saltado.
El único problema es que su puntuación en [snyk Advisor](https://snyk.io/advisor/python/nose) es muy baja, por lo que será descartado.
### 3. pytest-bdd
pytest-bdd es un plugin para pytest que permite escribir pruebas utilizando el enfoque de Behavior-Driven Development (BDD). BDD es una metodología de desarrollo de software que se enfoca en describir el comportamiento del sistema en un lenguaje que sea comprensible tanto para los desarrolladores como para los interesados no técnicos (por ejemplo, analistas de negocio, testers, etc.).

### pytest vs pytest-bdd
Podríamos usar pytest-bdd al ser más completo que pytest, sin embargo lo descartaremos al tener menor puntuación en [snyk Advisor](https://snyk.io/advisor/python/pytest-bdd) que [pytest](https://snyk.io/advisor/python/pytest). Usaremos pytest también como test runner.