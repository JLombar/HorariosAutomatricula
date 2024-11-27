# Bibliotecas de aserciones
Una biblioteca de aserciones es un conjunto de herramientas o funcinoes que los desarrolladores utilizan para comprobar el funcionamiento del código. Permiten realizar pruebas unitarias para verificar que una aplicación cumple con las expectativas, además de evitar que cambios en un futuro produzcan errores.  

Algunos prerrequisitos a la hora de elegir las bibliotecas:
* Debe tener una buena puntuación en [snyk Advisor](https://snyk.io/advisor/). Tener una buena puntuación en Skyk Advisor implica que la herramienta cumple con altos estándares en áreas como seguridad de datos y gestión de riesgos, demostrando ser una buena herramienta destinada a usar en un repositorio/repositorio
* Se debe comprobar el buen mantenimiento y actualización, disminuyendo la deuda técnica. Para comprobar esto, podemos ayudarnos de [PyPi](https://pypi.org/) para herramientas no nativas de Python, comprobando cuando fue la última actualización del paquete.
* En última instancia se valorará aquella herramienta que incluya una mayor variedad de aserciones, permitiéndonos mayor variedad a la hora de realizar diferentes tests.
## Elección
Estas son algunas de las bibliotecas de aserciones más comunes
### 1. unittest (PyUnit)
unittest es una biblioteca estándar de Python diseñada para realizar pruebas automatizadas. Es especialmente útil para validar el comportamiento de código mediante aserciones.  
unittest tiene soporte, y dado que es parte de la biblioteca estándar de Python, está mantenido oficialmente junto con las actualizaciones de Python.
### 2. pytest
pytest es una biblioteca de pruebas para Python que ofrece una manera más flexible y moderna de realizar pruebas automatizadas.
Tiene una gran puntuación en [snyk Advisor](https://snyk.io/advisor/python/pytest), por lo que será una buena herramienta a considerar ya que a esto se le suma que su última versión es de hace sólo 2 meses, por lo que podemos supones que tienen soporte activo y recibe actualizaciones.
Pytest puede usar las típicas aserciones estándar de Python inclye las siguientes aserciones:
* pytest.raises: Sirve para verificar que una excepción específica es lanzada
* pytest.warns: Para verificar que se lanza una advertencia
* pytest.approx: Se usa para verificar la igualdad aproximada de valores flotantes

Si se necesitan aserciones para para casos más específicas las podemos ampliar con plugins y extensiones a pytest.

## pytest vs unittest
Entre pytest y unittest será preferible usar [pytest](https://github.com/pytest-dev/pytest). Esto se debe a que pytest incluye las aserciones de unittest, al ser la biblioteca estándar de Python. De esta forma podemos usar las aserciones por defecto, así como algunas añadidas por pytest como pytest.raises, verificando que se lanzan excepciones específicas durante la ejecución de un test. De esta forma se permite mayor flexiblidad a la hora de elaborar los tests.