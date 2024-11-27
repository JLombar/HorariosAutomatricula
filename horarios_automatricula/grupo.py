from .horario import Horario

class Grupo:
    def __init__(self, letra, horario):
        if not isinstance(horario, Horario):
            raise TypeError("El horario debe instancia de la clase Horario")
        
        self.letra = letra
        self.horarios = horarios
