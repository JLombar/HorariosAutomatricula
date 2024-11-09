# Gestor de tareas
En este caso al estar trabajando en Python, la herramienta de construcción que estamos usando como [gestor de dependencias](./gestor_dependencias.md) lo podemos usar para automatizar ciertas tareas, en este caso queremos automatizar la instalación de las dependencias, que es capaz de realizar apoyándose en el archivo [pyproject.toml](../pyproject.toml). 

## Automatización de tareas
Usar Makefile para ejecuar herramientas en Python es una práctica común, especialmente en proyectos en los que se requieren múltiples tareas repetitivas, como puedens ser pruebas. 

Makefile facilita la automatización de estas tareas con comandos simples y mejorando la organización y eficiencia en el flujo de trabajo. Otras opciones para automatizar tareas disponibles en Python:
### 1. Scripts de Python personalizados
Se puedes escribir scripts en Python que que realice las tareas de configuración, pruebas, limpieza, instalación, etc. Ofrece gran flaxibilidad ya que se puede aprovechar la programación completa en Python, además funciona en cualquier entorno donde Python esté instalado.   
Sin embargo, cada comando requiere llamadas a subprocess, lo que puede hacer que el script sea más detallado y extenso. También se suma que ejecutar tareas individuales requiere conocer la interfaz de Python y el nombre de cada función
### 2. Invoke
Es una biblioteca de Python para automatizar tareas que permite definir comandos y ejecutarlos desde la terminal, similar a make. Ofrece una sintaxis elegante y es multiplataforma, lo que lo hace atractivo para proyectos que necesitan ejecutarse en Windows.
### 3. Tox
Es una herramienta de automatización y gestión de entornos de pruebas, especialmente útil en proyectos donde se debe verificar la compatibilidad con múltiples versiones de Python o ejecutar tareas en entornos controlados. No la usaremos por su Curva de aprendizaje para tareas que no están relacionadas con pruebas o dependencias, además de ser muy flexible para tareas generales fuera de las pruebas.

De todos las opciones para automatizar tareas mencionados, se descartaría también los **Scripts de Python**, ya que para ejecutar tareas es necesario conocer la interfaz de Python y el nombre de cada una de las funciones que se quiere ejecutar, siendo menos práctico.

### Invoke vs Makefile
Makefile es el más común pero su elección no se dictaminará sólamente por esto. 
+ Makefile es mejor por simplicidad, es más facil de entender para tareas básicas.
- Invoke requiere instalación adicional, ecesita instalarse como un paquete adicional. 
+ Make está diseñado para ser rápido y eficiente, sin la sobrecarga de iniciar un intérprete de Python y cargar bibliotecas. Esto lo hace más rápido en proyectos que requieren ejecutar múltiples tareas cortas consecutivamente.
- Invoke, al ser una herramienta de Python, necesita iniciar el intérprete y cargar el módulo, lo cual puede ser una sobrecarga innecesaria para tareas rápidas y sencilla.

Si considero que algo he aprendido a lo largo de los diferentes objetivos de este proyecto, ha sido el realizar lo que se pide limitándose estríctamente a ello, sin necesidad de complicar las cosas. Por ello creo que existiendo Makefile como una herramienta tan poderosa, sin necesidad de instalación adicional, no hay necesidad de elegir otras herramientas que hacen esencialmente lo mismo, complicando las cosas.

