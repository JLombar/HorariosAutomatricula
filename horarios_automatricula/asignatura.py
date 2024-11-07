from .grupo import Grupo

class Asignatura:
    def __init__(self, nombre, grupos):
        for grupo in grupos:
            if not isinstance(grupo, Grupo):
                raise TypeError("Cada grupo debe instancia de la clase Grupo")
            
        self.nombre = nombre
        self.grupos = grupos