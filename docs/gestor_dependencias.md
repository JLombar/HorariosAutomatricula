# Gestor de dependencias
## Opciones
Durante el objetivo 2, el encargado de trabajar en el repositorio usó [pyproject.toml](../pyproject.toml) como archivo de configuración para el desarrollo del proyecto.  
pyproject.toml se eligió ya que, como se menciona en el [Milestone 0](https://github.com/JLombar/HorariosAutomatricula/milestone/3) se deben seguir las buenas prácticas del lenguaje, para ello se debe crear un pyproject.toml al trabajar con Python.
Si buscamos información en páginas web como [esta](https://www.reddit.com/r/learnpython/comments/yqq551/pyprojecttoml_setupcfg_setuppy_whats_the/) o [esta](https://ericmjl.github.io/blog/2023/8/31/whats-the-difference-between-setupcfg-pyprojecttoml-and-setuppy/), en las que explica que desde el PEP 517 y 518 (El PEP es una Propuesta de Mejora de Python (Python Enhancement Proposal)) se llega al acuerdo de usar pyproject.toml como opción a la hora de configurar las builds en Python y, a no ser que exista un motivo de importancia, se debe evitar usar otros tipos de archivos de configuración en Python.

Por ello se elegirá un gestor que sea compatible con el mismo. Algunas de las opciones más comunes son:

### 1. Poetry
* Poetry es un gestor de dependencias y un manejador de entornos que permite gestionar dependencias, versiones de Python y la publicación de paquetes. Es popular en proyectos modernos que necesitan un control más preciso de las versiones de los paquetes.
* Ofrece un archivo de configuración más completo (pyproject.toml), controla las versiones de paquetes de manera automática y facilita la creación y administración de entornos virtuales.

### 2. Hatch
* Hatch es una herramienta de gestión de proyectos para Python que permite administrar tanto dependencias como entornos virtuales, además de soportar un flujo de trabajo basado en pyproject.toml
* Compatible con pyproject.toml y diseñado para proyectos que requieren configuraciones avanzadas, Hatch ofrece control preciso sobre la configuración de los entornos virtuales y el manejo de versiones de paquetes, lo que resulta útil en entornos de desarrollo colaborativos y complejos.

### 3. Flit
* Flit es una herramienta ligera diseñada principalmente para la creación y publicación de paquetes de Python. No es tan completa como Poetry en términos de gestión de dependencias y entornos, pero se integra fácilmente con pyproject.toml para proyectos simples y bibliotecas.
* Se integra fácilmente con pyproject.toml y es ideal para proyectos simples, aunque carece de funciones avanzadas para manejar entornos o versiones de dependencias, lo que limita su uso en proyectos complejos.

## Elección
También descartaremos Hatch por los siguientes motivos:  
* Manejo de dependencias: Hatch no ofrece un sistema de bloqueo de versiones tan avanzado como Poetry, lo que complica la creación de entornos reproducibles.
* Hatch es más adecuado para configuraciones avanzadas, pero Poetry y Flit cubren mejor proyectos sencillos o medianos con menos complicación.

### Flit vs Poetry
Es cierto que Flit puede ser mejor para proyectos pequeños por su simplicidad y velocidad, sin embargo nosotros escogeremos Poetry por los siguientes motivos:
* Poetry ofrece un sistema completo de gestión de dependencias, con la posibilidad de bloquear versiones mediante el archivo poetry.lock, asegurando que las dependencias sean consistentes en todos los entornos.
* Poetry crea y gestiona automáticamente entornos virtuales, lo que simplifica aún más la configuración del proyecto, algo que Flit no hace.
* Aunque tu proyecto sea pequeño ahora, Poetry es más flexible y escalable, por lo que si el proyecto se desarrolla en los futuros objetivos, por lo que se puede seguir usando sin necesidad de cambiar de herramienta.