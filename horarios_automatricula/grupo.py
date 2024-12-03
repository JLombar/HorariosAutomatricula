from .horario import Horario
from dataclasses import dataclass
from typing import List

@dataclass
class Grupo:
    letra: str
    horarios: List[Horario]

    def __post_init__(self):
        if not self.horarios:
            raise ValueError("La lista de horarios no puede estar vacía.")
        
        if not (isinstance(self.horarios, list) and all(isinstance(h, Horario) for h in self.horarios)):
            raise TypeError("El horario debe ser una lista de instancias de la clase Horario.")

