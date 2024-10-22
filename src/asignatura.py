from horario import Horario
from mencion import TipoMencion

class Asignatura:
    def __init__(self, nombre, horario: Horario, grupo, profesor=None, mencion: TipoMencion = TipoMencion.BASICA):
        if not isinstance(horario, Horario):
            raise TypeError("El horario debe instancia de la clase Horario")
        if not isinstance(mencion, TipoMencion):
            raise TypeError("La mención debe instancia de TipoMencion")
        
        self.nombre = nombre
        self.horario = horario
        self.grupo = grupo
        self.profesor = profesor
        self.mencion = mencion
    
    def __str__(self):
        return f"Asignatura: {self.nombre}  (Grupo: {self.grupo}) - Horario: {self.horario}"
    
    def asignaturas_solapadas(self, otra_asignatura):
        return self.horario.horas_solapadas(self.horario, otra_asignatura.horario)