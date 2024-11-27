import re

class Horario:
    DIAS_VALIDOS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    HORA_REGEX = r"^(?:[01]?\d|2[0-3]):([0-5]?\d)$"

    def __init__(self, dia, hora_inicio, hora_fin):
        if dia not in self.DIAS_VALIDOS:
            raise ValueError(f"El día '{dia}' no es válido. Debe ser uno de {self.DIAS_VALIDOS}.")
        
        if not re.match(self.HORA_REGEX, hora_inicio):
            raise ValueError(f"La hora de inicio '{hora_inicio}' no tiene el formato correcto (HH:MM o HH).")
        
        if not re.match(self.HORA_REGEX, hora_fin):
            raise ValueError(f"La hora de fin '{hora_fin}' no tiene el formato correcto (HH:MM o HH).")
        
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
