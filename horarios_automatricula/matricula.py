from .asignatura import AsignaturaGrupos


class Matricula:
    def __init__(self, asignaturas):
        for asignatura in asignaturas:
            if not isinstance(asignatura, AsignaturaGrupos):
                raise TypeError(
                    "Cada asignatura debe ser una instancia de la clase "
                    "AsignaturaGrupos"
                )

        self.asignaturas = asignaturas
