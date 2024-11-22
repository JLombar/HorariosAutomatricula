from .grupo import Grupo

class Asignatura_Grupos:
    def __init__(self, nombre, grupos):
        if not all(isinstance(grupo, Grupo) for grupo in grupos):
            raise TypeError("Cada grupo debe ser instancia de la clase Grupo")
        
        self.nombre = nombre
        self.grupos = grupos