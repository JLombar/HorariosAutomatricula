from .asignatura import Asignatura_Grupos

class Matricula:
    def __init__(self, asignaturas):
        if not all(isinstance(asignatura, Asignatura_Grupos) for asignatura in asignaturas):
            raise TypeError("Cada asignatura debe ser instancia de la clase Asignatura_Grupos")
        
        self.asignaturas = asignaturas