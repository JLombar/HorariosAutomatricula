from .grupo import Grupo

class Asignatura_Grupos:
    def __init__(self, nombre, grupos):
        for grupo in grupos:
            if not isinstance(grupo, Grupo):
                raise TypeError("Cada grupo debe instancia de la clase Grupo")
            
        self.nombre = nombre
        self.grupos = grupos

def leer_asignaturas(archivo):
    asignaturas = []
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            for linea in f:
                asignaturas.append(linea.strip())
        
        if not asignaturas:  
            raise ValueError("El archivo está vacío.")
        
        return asignaturas
    except FileNotFoundError:
        raise ValueError("No se ha encontrado el archivo en la ruta correcta.")  # Lanzar ValueError
    except Exception as e:
        if not isinstance(e, ValueError): 
            print(f"Error al leer el archivo: {e}")
        raise  
