from src.asignatura import Asignatura
from src.horario import Horario
from src.mencion import TipoMencion

def calcular_conflictos(asignaturas):
    conflictos = []
    
    for i in range(len(asignaturas)):
        for j in range(i+1, len(asignaturas)):
            if asignaturas[i].asignaturas_solapadas(asignaturas[j]):
                conflictos.append((asignaturas[i], asignaturas[j]))
    
    if conflictos:
        for conflicto in conflictos:
            print(f"Conflicto entre {conflicto[0].nombre} y {conflicto[1].nombre}.")
        return conflictos
    else:
        print("No existen conflictos.")
        return None
    
if __name__ == "__main__":
    horario1 = Horario("Lunes", "10:00", "12:00")
    horario2 = Horario("Lunes", "11:00", "13:00")
    horario3 = Horario("Lunes", "12:00", "14:00")
    horario4 = Horario("Lunes", "09:00", "11:00")
    
    practicas1 = [Horario("Martes", "09:00", "11:00"), Horario("Miércoles", "08:00", "10:00")]
    practicas2 = [Horario("Martes", "10:00", "12:00"), Horario("Miércoles", "09:00", "11:00")]
    practicas3 = [Horario("Jueves", "08:00", "10:00"), Horario("Viernes", "10:00", "12:00")]
    practicas4 = [Horario("Jueves", "12:00", "14:00"), Horario("Viernes", "09:00", "11:00")]

    asignatura1 = Asignatura("Fundamentos Físicos y Tecnológicos", horario1, practicas1, "Grupo A", mencion=TipoMencion.BASICA)
    asignatura2 = Asignatura("Algorítmica", horario2, practicas2, "Grupo B", mencion=TipoMencion.OBLIGATORIA)
    asignatura3 = Asignatura("Servidores WEB de Altas Prestaciones", horario3, practicas3, "Grupo A", mencion=TipoMencion.MENCION_TI)
    asignatura4 = Asignatura("Programación WEB", horario4, practicas4, "Grupo B", mencion=TipoMencion.MENCION_SI)
    
    asignaturas = [asignatura1, asignatura2, asignatura3, asignatura4]

    calcular_conflictos(asignaturas)