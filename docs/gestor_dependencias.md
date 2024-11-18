# Gestor de dependencias
## Opciones
Durante el objetivo 2, el encargado de trabajar en el repositorio usó [pyproject.toml](../pyproject.toml) como archivo de configuración para el desarrollo del proyecto.  
pyproject.toml se eligió ya que, como se menciona en el [Milestone 0](https://github.com/JLombar/HorariosAutomatricula/milestone/3) se deben seguir las buenas prácticas del lenguaje, para ello se debe crear un pyproject.toml al trabajar con Python.
Si buscamos información en páginas web como [esta](https://www.reddit.com/r/learnpython/comments/yqq551/pyprojecttoml_setupcfg_setuppy_whats_the/) o [esta](https://ericmjl.github.io/blog/2023/8/31/whats-the-difference-between-setupcfg-pyprojecttoml-and-setuppy/), en las que explica que desde el PEP 517 y 518 (El PEP es una Propuesta de Mejora de Python (Python Enhancement Proposal)) se llega al acuerdo de usar pyproject.toml como opción a la hora de configurar las builds en Python y, a no ser que exista un motivo de importancia, se debe evitar usar otros tipos de archivos de configuración en Python. Por ello, algo imprescindible a la hora de elegir un gestor de dependencias, debemos usar uno que sea compatible con pyproject.toml
Requisitos de la herramienta: 
* Compatible con pyproject.toml
* Algo que también será importante a la hora de considerar la elección será utilizar un gestor de dependencias para proyectos más pequeños o simples, al ser innecesario ya que nuestro proyecto no será a gran escala.
* Se valorará que se genere un archivo .lock, garantizando  que todos los desarrolladores estén usando las mismas versiones exactas de las dependencias,
* En última instancia se valorará velocidad y rendimiento del gestor.

Por ello se elegirá un gestor que sea compatible con el mismo. Algunas de las opciones más comunes son:

### 1. Poetry
* [Poetry](https://github.com/python-poetry/poetry) es un gestor de dependencias y un manejador de entornos que permite gestionar dependencias, versiones de Python y la publicación de paquetes. Es popular en proyectos modernos que necesitan un control más preciso de las versiones de los paquetes.
* Ofrece un archivo de configuración más completo (pyproject.toml), controla las versiones de paquetes de manera automática y facilita la creación y administración de entornos virtuales.

### 2. Hatch
* [Hatch](https://github.com/pypa/hatch) es una herramienta de gestión de proyectos para Python que permite administrar tanto dependencias como entornos virtuales, además de soportar un flujo de trabajo basado en pyproject.toml
* Compatible con pyproject.toml y diseñado para proyectos que requieren configuraciones avanzadas, Hatch ofrece control preciso sobre la configuración de los entornos virtuales y el manejo de versiones de paquetes, lo que resulta útil en entornos de desarrollo colaborativos y complejos.

### 3. Flit
* [Flit](https://github.com/pypa/flit) es una herramienta ligera diseñada principalmente para la creación y publicación de paquetes de Python. No es tan completa como Poetry en términos de gestión de dependencias y entornos, pero se integra fácilmente con pyproject.toml para proyectos simples y bibliotecas.
* Se integra fácilmente con pyproject.toml y es ideal para proyectos simples, aunque carece de funciones avanzadas para manejar entornos o versiones de dependencias, lo que limita su uso en proyectos complejos.  
Sin embargo, Flit no genera un archivo de bloqueo como lo hace Poetry. Esto significa que Flit no garantiza que todos los desarrolladores estén usando las mismas versiones exactas de las dependencias, lo cual puede llevar a inconsistencias entre entornos si no se maneja adecuadamente. Por esto la descartaremos directamente

### 4. PDM
[PDM](https://github.com/pdm-project/pdm) es un gestor de dependencias y entornos para Python basado en el estándar PEP 517. Su principal característica es la simplicidad y rapidez, con un enfoque en el archivo de configuración pyproject.toml y el uso de Pipfile para mejorar la gestión de dependencias.  
PDM ofrece un sistema de versiones más ágil y permite gestionar proyectos con varios entornos virtuales. Además, su integración con pip y setuptools lo convierte en una opción muy versátil para desarrolladores que buscan una experiencia más moderna y eficiente.

### 5. UV
(UV[https://github.com/astral-sh/uv]) es un gestor de entornos y dependencias para proyectos Python que pone énfasis en la simplicidad y rapidez. Su enfoque está en utilizar un archivo pyproject.toml para configurar tanto las dependencias como los entornos virtuales.
UV se destaca por su rapidez en la creación y manejo de entornos virtuales, especialmente en proyectos con una configuración minimalista. Además, es muy ligero y fácil de usar, lo que lo hace ideal para desarrolladores que prefieren una herramienta ágil y con una huella pequeña, sin sacrificar funcionalidad.

## Elección
Descartaremos Hatch al ser más adecuado para configuraciones avanzadas, pero Poetry, PDM y UV cubren mejor proyectos sencillos o medianos con menos complicación, lo ideal para nuestro repositorio. Entre las 3 finalistas también descartaremos Poetry y PDM al ser la más lenta de ellas, además de ser la mejor para gestionar proyectos simples con pocas dependencias.

Por lo que usaremos UV como gestor de dependencias.
