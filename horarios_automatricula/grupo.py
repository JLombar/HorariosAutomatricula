from .horario import Horario

class Grupo:
    def __init__(self, nombre, horario: Horario):
        if not isinstance(horario, Horario):
            raise TypeError("El horario debe instancia de la clase Horario")
        
        self.nombre = nombre
        self.horario = horario