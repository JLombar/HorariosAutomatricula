# Gestor de dependencias
## Opciones
Algunas de las opciones más comunes son:

### 1. pip
* Es el gestor de paquetes oficial de Python y viene preinstalado con la mayoría de las instalaciones de Python.

### 2. Poetry
* Poetry es un gestor de dependencias y un manejador de entornos que permite gestionar dependencias, versiones de Python y la publicación de paquetes. Es popular en proyectos modernos que necesitan un control más preciso de las versiones de los paquetes.
* Ofrece un archivo de configuración más completo (pyproject.toml), controla las versiones de paquetes de manera automática y facilita la creación y administración de entornos virtuales.

### 3. Conda
* Conda es un sistema de gestión de paquetes y entornos que funciona no solo para Python, sino también para otros lenguajes. Es especialmente útil en proyectos de ciencia de datos y aprendizaje automático debido a que maneja tanto paquetes de Python como bibliotecas externas.
* Maneja dependencias más allá del ecosistema Python, como bibliotecas en C, por lo que es útil para paquetes de ciencia de datos (e.g., NumPy, pandas) que tienen dependencias complejas.

## Elección
Durante el objetivo 2, el encargado de trabajar en el repositorio usó [pyproject.toml](../pyproyect.toml) como archivo de configuración para el desarrollo del proyecto, por ello se elegirá un gestor de los mencionados que sea compatible con el mismo.

De los mencionados únicamente Poetry y pip son compatibles. Sin embargo, pip sólamente soporta parcialmente pyproject.toml, ya que reconoce este archivo gracias a la PEP 518 (que define pyproject.toml para definir configuraciones de construcción de paquetes). Sin embargo, pip no maneja las dependencias directamente desde pyproject.toml sin ayuda adicional, por ello se procederá a usar Poetry como gestor de dependencias