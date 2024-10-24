from .horario import Horario
from .mencion import TipoMencion

class Asignatura:
    """
    Clase que representa una asignatura con un horario de teoría y varios subgrupos de prácticas.
    """
    def __init__(self, nombre, horario_teoria: Horario, horarios_practicas, grupo, mencion: TipoMencion = TipoMencion.BASICA):
        """
        Inicializa la asignatura con nombre, horario de teoría, horarios de prácticas, grupo y mención.
        :param nombre: Nombre de la asignatura.
        :param horario_teoria: Horario de la clase de teoría.
        :param horarios_practicas: Lista de horarios de prácticas.
        :param grupo: El grupo de la asignatura.
        :param mencion: Tipo de mención, con valor predeterminado BASICA.
        """
        if not isinstance(horario_teoria, Horario):
            raise TypeError("El horario debe instancia de la clase Horario")
        if not isinstance(mencion, TipoMencion):
            raise TypeError("La mención debe instancia de TipoMencion")
        if not isinstance(horarios_practicas, list):
            raise TypeError("Los horarios de prácticas deben ser un vector (lista)")
        
        for horario_p in horarios_practicas:
            if not isinstance(horario_p, Horario):
                raise TypeError("Cada horario de prácticas debe instancia de la clase Horario")
        
        self.nombre = nombre
        self.horario_teoria = horario_teoria
        self.grupo = grupo
        self.horarios_practicas = horarios_practicas
        self.mencion = mencion
        
    
    def __str__(self):
        """
        Representa la asignatura como una cadena, incluyendo el horario de teoría y los horarios de prácticas.
        :return: Una cadena con la información completa de la asignatura.
        """
        practicas_str = ""
        if self.horarios_practicas:
            practicas_str = "\nHorarios de prácticas:\n" + "\n".join([str(horario) for horario in self.horarios_practicas])
        return f"Asignatura: {self.nombre} (Grupo: {self.grupo}) - Horario Teoría: {self.horario_teoria}{practicas_str}"
    
    def asignaturas_solapadas(self, otra_asignatura):
        """
        Verifica si los horarios teóricos y de prácticas de dos asignaturas se solapan.
        - Si los horarios teóricos se solapan, retorna True.
        - Si alguna combinación de horarios de prácticas no se solapa, la imprime y retorna False.
        :param otra_asignatura: Asignatura a comparar.
        :return: True si todos los horarios de teoría y prácticas se solapan, False si alguna combinación de prácticas no se solapa.
        """
        solapamiento_teoria = self.horario_teoria.horas_solapadas(otra_asignatura.horario_teoria)
        
        if solapamiento_teoria:
            return True
        
        practicas_no_solapadas = []
        for horario_p in self.horarios_practicas:
            for horario_p_otra in otra_asignatura.horarios_practicas:
                if not horario_p.horas_solapadas(horario_p_otra):
                    practicas_no_solapadas.append((horario_p, horario_p_otra))
                
        if practicas_no_solapadas:
            print(f"Combinaciones de prácticas que no se solapan entre {self.nombre} y {otra_asignatura.nombre}:\n")
            for combinacion in practicas_no_solapadas:
                print(f"- {combinacion[0]} no se solapa con {combinacion[1]}\n")
            return False
        else:
            print(f"Todas las combinaciones de prácticas entre {self.nombre} y {otra_asignatura.nombre} se solapan.")
            return True