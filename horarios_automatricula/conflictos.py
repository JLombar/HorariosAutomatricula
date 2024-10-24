from .asignatura import Asignatura

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
        for j in range(i + 1, len(asignaturas)):
            if asignaturas[i].asignaturas_solapadas(asignaturas[j]):
                conflictos.append((asignaturas[i], asignaturas[j]))
    
    # Si hay conflictos, se imprimen y se retornan
    if conflictos:
        for conflicto in conflictos:
            print(f"Conflicto entre {conflicto[0].nombre} y {conflicto[1].nombre}.")
        return conflictos
    else:
        print("No existen conflictos.")
        return None