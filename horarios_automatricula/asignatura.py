from .horario import Horario

class Asignatura:
    """
    Clase que representa una asignatura con un horario.
    """
    def __init__(self, nombre, horario: Horario, grupo):
        """
        Inicializa la asignatura con nombre, horario de teoría, horarios de prácticas, grupo y mención.
        :param nombre: Nombre de la asignatura.
        :param horario: Horario de la asignatura.
        :param grupo: El grupo de la asignatura.
        """
        if not isinstance(horario, Horario):
            raise TypeError("El horario debe instancia de la clase Horario")
        
        self.nombre = nombre
        self.horario = horario
        self.grupo = grupo