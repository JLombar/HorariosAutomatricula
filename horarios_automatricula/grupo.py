from .horario import Horario

class Grupo:
    def __init__(self, letra, horarios: Horario):
        if not (isinstance(horarios, list) and all(isinstance(h, Horario) for h in horarios)):
            raise TypeError("El horario debe ser una lista de instancias de la clase Horario")
        self.letra = letra
        self.horarios = horarios
