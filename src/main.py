from asignatura import Asignatura
from horario import Horario
from mencion import TipoMencion

def calcular_conflictos(asignaturas):
    conflictos = []
    
    for i in range(len(asignaturas)):
        for j in range(i+1, len(asignaturas)):
            if asignaturas[i].asignaturas_solapadas(asignaturas[j]):
                conflictos.append((asignaturas[i], asignaturas[j]))
    
    if conflictos:
        for conflicto in conflictos:
            print(f"Conflicto entre {conflicto[0]} y {conflicto[1]}.")
        return conflictos
    else:
        print("No existen conflictos.")
        return None
    
if __name__ == "__main__":
    horario1 = Horario("Lunes", "10:00", "12:00")
    horario2 = Horario("Lunes", "11:00", "13:00")
    horario3 = Horario("Lunes", "12:00", "14:00")
    horario4 = Horario("Lunes", "09:00", "11:00")

    asignatura1 = Asignatura("Fundamentos Físicos y Tecnológicos", horario1, "Grupo A", mencion=TipoMencion.BASICA)
    asignatura2 = Asignatura("Algorítmica", horario2, "Grupo B", mencion=TipoMencion.OBLIGATORIA)
    asignatura3 = Asignatura("Servidores WEB de Altas Prestaciones", horario3, "Grupo A", mencion=TipoMencion.MENCION_TI)
    asignatura4 = Asignatura("Programación WEB", horario4, "Grupo B", mencion=TipoMencion.MENCION_SI)
    
    asignaturas = [asignatura1, asignatura2, asignatura3, asignatura4]

    calcular_conflictos(asignaturas)