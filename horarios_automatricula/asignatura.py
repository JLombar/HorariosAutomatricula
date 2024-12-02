from .grupo import Grupo
from datetime import datetime

class Asignatura_Grupos:
    def __init__(self, nombre: str, grupos: Grupo):
        for grupo in grupos:
            if not isinstance(grupo, Grupo):
                raise TypeError("Cada grupo debe instancia de la clase Grupo")
            
        self.nombre = nombre
        self.grupos = grupos

def convertir_a_minutos(hora_str: str):
    try:
        hora = datetime.strptime(hora_str, "%H:%M")
        return hora.hour * 60 + hora.minute
    except ValueError:
        raise ValueError

def comparar_horarios(asignatura1: Asignatura_Grupos, asignatura2: Asignatura_Grupos):
    for grupo1 in asignatura1.grupos:
        for grupo2 in asignatura2.grupos:
            for horario1 in grupo1.horarios:
                for horario2 in grupo2.horarios:
                    if horario1.dia == horario2.dia:
                        hora_inicio1 = convertir_a_minutos(horario1.hora_inicio)
                        hora_fin1 = convertir_a_minutos(horario1.hora_fin)
                        hora_inicio2 = convertir_a_minutos(horario2.hora_inicio)
                        hora_fin2 = convertir_a_minutos(horario2.hora_fin)
                        
                        if hora_inicio1 < hora_fin2 and hora_fin1 > hora_inicio2:
                            raise ValueError  
    return True