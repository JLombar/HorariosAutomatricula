import re
from dataclasses import dataclass
from datetime import datetime

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

def convertir_a_minutos(hora_str: str):
    try:
        hora = datetime.strptime(hora_str, "%H:%M")
        return hora.hour * 60 + hora.minute
    except ValueError:
        raise ValueError

def solapamiento(horario1: Horario, horario2: Horario):
    if horario1.dia == horario2.dia:
        hora_inicio1 = convertir_a_minutos(horario1.hora_inicio)
        hora_fin1 = convertir_a_minutos(horario1.hora_fin)
        hora_inicio2 = convertir_a_minutos(horario2.hora_inicio)
        hora_fin2 = convertir_a_minutos(horario2.hora_fin)
        
        if hora_inicio1 < hora_fin2 and hora_fin1 > hora_inicio2:
            return True 
    return False