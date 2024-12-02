import re
from dataclasses import dataclass

@dataclass
class Horario:
    dia: str
    hora_inicio: str
    hora_fin: str

    DIAS_VALIDOS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    HORA_REGEX = r"^(?:[01]?\d|2[0-3]):([0-5]?\d)$"

    def __post_init__(self):
        if self.dia not in self.DIAS_VALIDOS:
            raise ValueError(f"El día '{self.dia}' no es válido. Debe ser uno de {self.DIAS_VALIDOS}.")
        
        if not re.match(self.HORA_REGEX, self.hora_inicio):
            raise ValueError(f"La hora de inicio '{self.hora_inicio}' no tiene el formato correcto (HH:MM o HH).")
        
        if not re.match(self.HORA_REGEX, self.hora_fin):
            raise ValueError(f"La hora de fin '{self.hora_fin}' no tiene el formato correcto (HH:MM o HH).")
