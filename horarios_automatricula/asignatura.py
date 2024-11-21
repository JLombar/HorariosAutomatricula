from .grupo import Grupo

class Asignatura_Grupos:
    def __init__(self, nombre, grupos):
        for grupo in grupos:
            if not isinstance(grupo, Grupo):
                raise TypeError("Cada grupo debe instancia de la clase Grupo")
            
        self.nombre = nombre
        self.grupos = grupos

def leer_asignaturas():
    asignaturas = []
    try:
        with open('../docs/asignaturas.txt', 'r', encoding='utf-8') as f:
            for linea in f:
                asignaturas.append(linea.strip())
        return asignaturas
    except FileNotFoundError:
        print("No se ha encontrado el archivo 'asignaturas.txt' en la ruta correcta.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")