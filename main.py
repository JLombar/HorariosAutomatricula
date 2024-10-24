from src.asignatura import Asignatura
from src.horario import Horario
from src.mencion import TipoMencion

def calcular_conflictos(asignaturas):
    """
    Función que calcula si hay solapamientos entre asignaturas.
    Revisa los solapamientos de los horarios de teoría y prácticas de cada asignatura.

    :param asignaturas: Lista de objetos Asignatura que se quieren comparar.
    :return: Lista de tuplas con asignaturas que presentan conflictos, o None si no hay conflictos.
    """
    conflictos = []
    
    # Compara cada asignatura con todas las demás para verificar si hay solapamientos
    for i in range(len(asignaturas)):
        for j in range(i+1, len(asignaturas)):
            # Si hay solapamientos, añade el par de asignaturas conflictivas a la lista
            if asignaturas[i].asignaturas_solapadas(asignaturas[j]):
                conflictos.append((asignaturas[i], asignaturas[j]))
    
    # Si hay conflictos, se imprimen y se retornan
    if conflictos:
        for conflicto in conflictos:
            print(f"Conflicto entre {conflicto[0].nombre} y {conflicto[1].nombre}.")
        return conflictos
    else:
        # Si no hay conflictos, se indica que no existen
        print("No existen conflictos.")
        return None

# Punto de entrada del programa
if __name__ == "__main__":
    # Crear los horarios de teoría para cada asignatura
    horario1 = Horario("Lunes", "10:00", "12:00")
    horario2 = Horario("Lunes", "11:00", "13:00")
    horario3 = Horario("Lunes", "12:00", "14:00")
    horario4 = Horario("Lunes", "09:00", "11:00")
    
    # Crear los subgrupos de prácticas para cada asignatura
    practicas1 = [Horario("Martes", "09:00", "11:00"), Horario("Miércoles", "08:00", "10:00")]
    practicas2 = [Horario("Martes", "10:00", "12:00"), Horario("Miércoles", "09:00", "11:00")]
    practicas3 = [Horario("Jueves", "08:00", "10:00"), Horario("Viernes", "10:00", "12:00")]
    practicas4 = [Horario("Jueves", "12:00", "14:00"), Horario("Viernes", "09:00", "11:00")]

    # Crear objetos Asignatura con sus horarios de teoría y de prácticas
    asignatura1 = Asignatura("Fundamentos Físicos y Tecnológicos", horario1, practicas1, "Grupo A", mencion=TipoMencion.BASICA)
    asignatura2 = Asignatura("Algorítmica", horario2, practicas2, "Grupo B", mencion=TipoMencion.OBLIGATORIA)
    asignatura3 = Asignatura("Servidores WEB de Altas Prestaciones", horario3, practicas3, "Grupo A", mencion=TipoMencion.MENCION_TI)
    asignatura4 = Asignatura("Programación WEB", horario4, practicas4, "Grupo B", mencion=TipoMencion.MENCION_SI)
    
    # Lista de asignaturas para las que se calcularán los conflictos
    asignaturas = [asignatura1, asignatura2, asignatura3, asignatura4]

    # Llama a la función que calculará los conflictos entre las asignaturas
    calcular_conflictos(asignaturas)