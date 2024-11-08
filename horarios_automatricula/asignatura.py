from .grupo import Grupo


class AsignaturaGrupos:
    def __init__(self, nombre, grupos):
        for grupo in grupos:
            if not isinstance(grupo, Grupo):
                raise TypeError(
                    "Cada grupo debe ser una instancia de la clase Grupo"
                )

        self.nombre = nombre
        self.grupos = grupos
