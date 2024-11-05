from .horario import Horario

class Asignatura:
    """
    Clase que representa una asignatura con un horario de teoría y varios subgrupos de prácticas.
    """
    def __init__(self, nombre, horario_teoria: Horario, horarios_practicas, grupo):
        """
        Inicializa la asignatura con nombre, horario de teoría, horarios de prácticas, grupo y mención.
        :param nombre: Nombre de la asignatura.
        :param horario_teoria: Horario de la clase de teoría.
        :param horarios_practicas: Lista de horarios de prácticas.
        :param grupo: El grupo de la asignatura.
        """
        if not isinstance(horario_teoria, Horario):
            raise TypeError("El horario debe instancia de la clase Horario")
        if not isinstance(horarios_practicas, list):
            raise TypeError("Los horarios de prácticas deben ser un vector (lista)")
        
        for horario_p in horarios_practicas:
            if not isinstance(horario_p, Horario):
                raise TypeError("Cada horario de prácticas debe instancia de la clase Horario")
        
        self.nombre = nombre
        self.horario_teoria = horario_teoria
        self.grupo = grupo
        self.horarios_practicas = horarios_practicas