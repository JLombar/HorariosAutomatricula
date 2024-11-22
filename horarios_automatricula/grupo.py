from .horario import Horario

class Grupo:
    def __init__(self, letra, horarios):
        if not all(isinstance(h, Horario) for h in horarios):
            raise TypeError("Todos los horarios deben ser instancias de la clase Horario.")
        
        self.letra = letra
        self.horarios = horarios
