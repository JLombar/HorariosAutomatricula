from .asignatura import Asignatura_Grupos
from .horario import Horario
from .grupo import Grupo
import re

class Matricula:
    def __init__(self, asignaturas):
        for asignatura in asignaturas:
            if not isinstance(asignatura, Asignatura_Grupos):
                raise TypeError("Cada asignatura debe instancia de la clase Asignatura_Grupos")
            
        self.asignaturas = asignaturas

def parse_horario(file_path):
    asignaturas = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        raise ValueError("No se ha encontrado el archivo en la ruta correcta.")
    except Exception as e:
        raise RuntimeError(f"Error al leer el archivo: {e}")

    courses = re.split(r"={5,}", content)
    for course in courses:
        rows = course.splitlines()[1:]
        for row in rows:
            if not row.strip() or '|' not in row:
                continue

            cols = [col.strip() for col in row.split("|")]
            
            if len(cols) >= 7:
                nombre_asignatura, grupo_letra, lunes, martes, miercoles, jueves, viernes = cols
                    
                if not nombre_asignatura or not grupo_letra:
                    continue
                
                horarios = []
                dias_horarios = [
                    ('Lunes', lunes), 
                    ('Martes', martes), 
                    ('Miércoles', miercoles), 
                    ('Jueves', jueves), 
                    ('Viernes', viernes)
                ]
                
                for dia, horario in dias_horarios:
                    if horario and horario.strip() and '-' in horario:
                        try:
                            hora_inicio, hora_fin = map(str.strip, horario.split("-"))
                            horarios.append(Horario(dia, hora_inicio, hora_fin))
                        except Exception as e:
                            print(f"Error procesando horario para {dia}: {horario}. {e}")
                
                if horarios:
                    grupo = Grupo(grupo_letra, horarios)
                    
                    asignatura_existente = next((a for a in asignaturas if a.nombre == nombre_asignatura), None)
                    if asignatura_existente:
                        asignatura_existente.grupos.append(grupo)
                    else:
                        asignaturas.append(Asignatura_Grupos(nombre_asignatura, [grupo]))

    return Matricula(asignaturas)