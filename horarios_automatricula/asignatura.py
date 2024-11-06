from .horario import Horario

class Asignatura:
    def __init__(self, nombre, horario: Horario, grupo):
        if not isinstance(horario, Horario):
            raise TypeError("El horario debe instancia de la clase Horario")
        
        self.nombre = nombre
        self.horario = horario
        self.grupo = grupo