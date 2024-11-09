# Comprobar sintaxis de fuentes existentes
Durante este objetivo queremos comprobar la sintáxis de los archivos .py que están presentes en el proyecto. Para ello se nos presentan varias herramientas:

## 1. flake8
flake8 es ampliamente utilizada porque es rápida, ligera y fácil de configurar, además de combinar tres herramientas en una: pycodestyle para el estilo, pyflakes para errores de sintaxis, y mccabe para la complejidad ciclomática. Esto lo convierte en una opción integral para análisis estático de código en Python. Flake8 es muy popular en proyectos de código abierto y en equipos de desarrollo que buscan mantener un código limpio y consistente. Además, es altamente extensible, permitiendo la integración con otros complementos y la personalización de reglas.

## 2. pylint 
pylint es otra herramienta popular que, además de verificar el estilo, también analiza la calidad del código y detecta posibles errores lógicos. Ofrece un análisis mucho más detallado y, de hecho, califica el código con una "puntuación de calidad". Esta puntuación puede ser utilizada para evaluar la mejora continua del código y para detectar áreas que requieren refactorización. Pylint también permite configurar reglas personalizadas, y su extensibilidad permite adaptarlo a las necesidades de proyectos grandes o equipos con normativas específicas. Aunque es más lento que flake8, su profundidad en el análisis lo hace invaluable en proyectos complejos.

## 3. black
black es una herramienta de formateo automático que se ha convertido en un estándar en la comunidad Python. A diferencia de flake8 y pylint, black no analiza errores ni complejidad; simplemente ajusta el código al estándar PEP 8.

Entre todas estas opciones descartaremos black por varios motivos:
* black solo formatea el código. Esto significa que flake8 puede identificar errores y malas prácticas, que black no detecta.
* black tiene un enfoque de "todo o nada", aplicando su propio estilo de formateo sin opciones de personalización.
* black: Su único propósito es dar formato al código de forma automática para cumplir con el estándar PEP 8. No realiza ningún análisis de la lógica del código ni verifica posibles errores o mejoras en la calidad del código.

# flake8 vs pylint
flake8 es una herramienta más ligera y rápida que se enfoca principalmente en el estilo de código y algunos errores básicos, lo que lo convierte en una herramienta simple pero efectiva para mantener el código limpio y legible.
pylint, por otro lado, es más detallado y exhaustivo, ofreciendo un análisis más profundo del código. No solo verifica el estilo y los errores de sintaxis, sino que también evalúa la calidad del código, la complejidad, la lógica y posibles errores más complejos, además de asignar una puntuación de calidad. Su análisis es más lento y profundo, lo que puede hacer que no siempre sea necesario en proyectos más pequeños o en fases de desarrollo rápidas.
En ocasiones puede ser interesante usar los dos, podríamos enforcarlo hacia este planteamiento. Sin embargo, en proyectos más pequeños o donde el tiempo de ejecución sea crucial, podría ser más eficiente usar solo una de las dos herramientas según las necesidades del equipo.

## Elección final
Como nuestro proyecto no será de gran escala nos enfocaremos en usar flake8 para asegurarnos de mantener las buenas prácticas del lenguaje y evitar los errores más básicos.