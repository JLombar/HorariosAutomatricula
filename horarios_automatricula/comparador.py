from datetime import datetime

def convertir_a_minutos(hora_str):
    try:
        hora = datetime.strptime(hora_str, "%H:%M")
        return hora.hour * 60 + hora.minute
    except ValueError:
        return None

def comparar_horarios(asignatura1, asignatura2):
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
                            return False  
    return True
