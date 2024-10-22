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