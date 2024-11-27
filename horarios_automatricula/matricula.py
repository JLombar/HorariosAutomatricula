from .asignatura import Asignatura_Grupos

class Matricula:
    def __init__(self, asignaturas):
        for asignatura in asignaturas:
            if not isinstance(asignatura, Asignatura_Grupos):
                raise TypeError("Cada asignatura debe instancia de la clase Asignatura_Grupos")
        
        self.asignaturas = asignaturas