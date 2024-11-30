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