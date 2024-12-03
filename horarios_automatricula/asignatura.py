from .grupo import Grupo
from dataclasses import dataclass
from typing import List

@dataclass
class Asignatura_Grupos:
    nombre: str
    grupos: List[Grupo]

    def __post_init__(self):
        if not self.grupos:
            raise ValueError("La lista de grupos no puede estar vacía.")
        
        for grupo in self.grupos:
            if not isinstance(grupo, Grupo):
                raise TypeError("Cada grupo debe ser instancia de la clase Grupo.")