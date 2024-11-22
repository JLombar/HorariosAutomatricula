from horarios_automatricula.parser import Parser
from horarios_automatricula.comparador import comparar_horarios
from horarios_automatricula.horario import Horario
from horarios_automatricula.grupo import Grupo
from horarios_automatricula.asignatura import Asignatura_Grupos
from horarios_automatricula.matricula import Matricula

def ejemplo_parser():
    file_path = "docs/asignaturas.txt" 
    parser = Parser(file_path)
    matricula = parser.parse_horario()

    for asignatura in matricula.asignaturas:
        print(f"Asignatura: {asignatura.nombre}")
        for grupo in asignatura.grupos:
            print(f"  Grupo {grupo.letra}:")
            for horario in grupo.horarios:
                print(f"    {horario.dia}: {horario.hora_inicio}-{horario.hora_fin}")

def ejemplo_solapamiento():
    horario1 = Horario("Lunes", "9:00", "11:00")
    horario2 = Horario("Miércoles", "9:00", "11:00")
    grupo_a = Grupo("A", [horario1, horario2])

    horario3 = Horario("Lunes", "10:00", "12:00")
    grupo_b = Grupo("B", [horario3])

    asignatura1 = Asignatura_Grupos("Cálculo I", [grupo_a])
    asignatura2 = Asignatura_Grupos("Fundamentos de Programación", [grupo_b])

    resultado = comparar_horarios(asignatura1, asignatura2)
    if resultado:
        print("Las asignaturas tienen horarios que se solapan.")
    else:
        print("Las asignaturas no tienen horarios que se solapan.")

def main():
    horario1 = Horario("Lunes", "9:00", "11:00")
    horario2 = Horario("Miércoles", "9:00", "11:00")
    grupo_a = Grupo("A", [horario1, horario2])

    horario3 = Horario("Lunes", "11:30", "13:30")
    horario4 = Horario("Martes", "9:00", "11:00")
    grupo_b = Grupo("B", [horario3, horario4])

    asignatura1 = Asignatura_Grupos("Cálculo I", [grupo_a])
    asignatura2 = Asignatura_Grupos("Fundamentos de Programación", [grupo_b])

    resultado = comparar_horarios(asignatura1, asignatura2)
    if resultado:
        print("Las asignaturas tienen horarios que se solapan.")
    else:
        print("Las asignaturas no tienen horarios que se solapan.")

if __name__ == "__main__":
    ejemplo_parser() 