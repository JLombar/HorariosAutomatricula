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

def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            if not content:
                raise ValueError("El archivo está vacío.")
            return content
    except FileNotFoundError:
        raise ValueError("No se ha encontrado el archivo en la ruta correcta.")
    except ValueError:
        raise
    except Exception as e:
        raise RuntimeError(f"Error al leer el archivo: {e}")
        
def split_courses(content):
    if not content:
        return ['']
    
    sections = re.split(r'(?=\d+(?:er|do) Curso \(.*?\))', content)
    
    return [section.strip() for section in sections if section.strip()]

def process_course(course):
    rows = course.splitlines()[1:]
    asignaturas = []
    for row in rows:
        if not row.strip() or '|' not in row:
            continue
        cols = [col.strip() for col in row.split("|")]
        if len(cols) >= 7:
            nombre_asignatura, grupo_letra, lunes, martes, miercoles, jueves, viernes = cols
            if not nombre_asignatura or not grupo_letra:
                continue
            horarios = process_horarios(lunes, martes, miercoles, jueves, viernes)
            if horarios:
                grupo = Grupo(grupo_letra, horarios)
                add_grupo_to_asignaturas(asignaturas, nombre_asignatura, grupo)
    return asignaturas

def process_horarios(lunes, martes, miercoles, jueves, viernes):
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
    return horarios