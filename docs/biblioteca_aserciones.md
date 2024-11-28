# Bibliotecas de aserciones
Una biblioteca de aserciones es un conjunto de herramientas o funcinoes que los desarrolladores utilizan para comprobar el funcionamiento del código. Permiten realizar pruebas unitarias para verificar que una aplicación cumple con las expectativas, además de evitar que cambios en un futuro produzcan errores.  

Algunos prerrequisitos a la hora de elegir las bibliotecas:
* Debe tener una buena puntuación en [snyk Advisor](https://snyk.io/advisor/). Tener una buena puntuación en Skyk Advisor implica que la herramienta cumple con altos estándares en áreas como seguridad de datos y gestión de riesgos, demostrando ser una buena herramienta destinada a usar en un repositorio/repositorio
* Se debe comprobar el buen mantenimiento y actualización, disminuyendo la deuda técnica. Para comprobar esto, podemos ayudarnos de [PyPi](https://pypi.org/) para herramientas no nativas de Python, comprobando cuando fue la última actualización del paquete.
* En última instancia se valorará aquella herramienta que incluya una mayor variedad de aserciones, permitiéndonos mayor variedad a la hora de realizar diferentes tests.
## Elección
Estas son algunas de las bibliotecas de aserciones más comunes
### 1. assert
Es una herramienta que viene por defecto en Python que se usa para realizar comprobaciones durante la ejecucuón de un programa. Al ser parte del núcleo de Python está mantenido oficialmente junto con las actualizaciones de Python. Assert nos permite evaluar:
* Supuestos lógicos
* Tipos o estructuras
* Valor dentro de un rango
* Longitud de una estructura
* Relaciones entre valores
* Comprobación de estados o configuraciones específicas
### 2. unittest (PyUnit)
unittest es una biblioteca estándar de Python diseñada para realizar pruebas automatizadas. Es especialmente útil para validar el comportamiento de código mediante aserciones.  
unittest tiene soporte, y dado que es parte de la biblioteca estándar de Python, está mantenido oficialmente junto con las actualizaciones de Python. Incluye estas aserciones:
* assertEqual, assertNotEqual: Para comprobar igualdad o desigualdad
* assertIs, assertIsNot: Para comprobar la indentidad
* assertTrue, assertFalse: Comprueba veracidad/falsedad
* assertGreater, assertLess, etc: Realiza comparaciones de valores
* assertRaises, assertRaisesRegex: Para verificar excepciones
* assertListEqual, assertDictEqual, etc: Verifican estructuras de datos
### 3. pytest
Tiene una gran puntuación en [snyk Advisor](https://snyk.io/advisor/python/pytest), por lo que será una buena herramienta a considerar ya que a esto se le suma que su última versión es de hace sólo 2 meses, por lo que podemos supones que tienen soporte activo y recibe actualizaciones.
Pytest puede usar las típicas aserciones estándar de Python, además de  incluir las siguientes aserciones:
* pytest.raises: Sirve para verificar que una excepción específica es lanzada
* pytest.warns: Para verificar que se lanza una advertencia
* pytest.approx: Se usa para verificar la igualdad aproximada de valores flotantes

Si se necesitan aserciones para para casos más específicas las podemos ampliar con plugins y extensiones a pytest.
### 4. behave
behave es una biblioteca de aserciones basadas en Behavior-Driven Development (BDD), una metodología que enfatiza la colaboración entre desarrolladores, testers y stakeholders mediante un lenguaje común. En lugar de centrarse en aserciones directas como unittest o pytest, behave utiliza un enfoque orientado a escenarios definidos en un lenguaje cercano al natural, lo que permite describir el comportamiento esperado del sistema.
El problema que tiene behave es que si miramos sus calificanciones con [snyk Advisor](https://snyk.io/advisor/python/behave) o el proyecto en [PyPi](https://pypi.org/project/behave/), lleva sin actualizarse siete años, podemos asumir que no tiene soporte, por lo cual lo descartaremos.
### 5. ensure
Es una biblioteca de aserciones para Python, al ver su perfil en [PyPi](https://pypi.org/project/ensure/) está actualizado recientemente, en diciembre de 2023, por lo que podríamos utilizarlo. Sin embargo, su perfil en [snik Advisor](https://snyk.io/advisor/python/ensure) tiene una nota muy baja por lo que no sería una buena opción a utilizar.
### 6. grappa
Otra opción que podríamos contemplar a la hora de elegir una herramienta, pero tiene una baja puntuación en [synk Advisor](https://snyk.io/advisor/python/grappa) y la última versión se publicó hace 4 años.
### 7. PyHamcrest
PyHarmCrest es otra opción, actualizada hace un año y un mes por última vez. El problema que tiene es que al igual que el resto tiene una baja valoación en lo que respecta a su seguridad, por lo que la podemos descartar.

## Elección final
Como hemos visto en las opciones el ecosistema de Python están un limitadas ya que los usuarios se han limitado a usar pytest o unittest y el resto de opciones se han ido abandonado con el tiempo, perdiendo la posibilidad de elegir entre varias herramientas y "monopolizando" la desición.
Entre assert, pytest y unittest será preferible usar [pytest](https://github.com/pytest-dev/pytest). Esto se debe a que pytest incluye las aserciones de unittest y assert, al ser parte del estándar de Python. De esta forma podemos usar las aserciones por defecto, así como algunas añadidas por pytest como pytest.warns, verificando que se lanzan advertencias específicas durante la ejecución de un test. De esta forma se permite mayor flexiblidad a la hora de elaborar los tests.