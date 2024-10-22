from horario import Horario

class Asignatura:
    def __init__(self, nombre, horario, grupo, profesor=None, mencion=None):
        self.nombre = nombre
        self.horario = horario
        self.grupo = grupo
        self.profesor = profesor
        self.mencion = mencion
    
    def __str__(self):
        return f"Asignatura: {self.nombre}  (Grupo: {self.grupo}) - Horario: {self.horario}"