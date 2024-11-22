import pytest
import os

from horarios_automatricula.asignatura import leer_asignaturas

def test_leer_asignaturas(tmp_path):
    archivo_temporal = tmp_path / "asignaturas.txt"

    contenido = "Sistemas Operativos - Grupo A - Lunes 10:00\nInfraestructura Virtual - Grupo B - Miércoles 12:00\n"
    archivo_temporal.write_text(contenido, encoding='utf-8')

    resultado = leer_asignaturas(archivo_temporal)

    esperado = [
        "Sistemas Operativos - Grupo A - Lunes 10:00",
        "Infraestructura Virtual - Grupo B - Miércoles 12:00",
    ]
    assert resultado == esperado, "La función leer_asignaturas no leyó el contenido correctamente"

def test_archivo_no_encontrado():
    archivo_inexistente = "archivo_no_existe.txt"
    
    resultado = leer_asignaturas(archivo_inexistente)
    
    assert resultado is None, f"Se esperaba None al no existir el archivo, pero se obtuvo {resultado}"

def test_archivo_vacio(tmp_path):
    archivo_vacio = tmp_path / "archivo_vacio.txt"
    archivo_vacio.write_text("", encoding='utf-8')  # Crear un archivo vacío

    with pytest.raises(ValueError, match="El archivo está vacío."):
        leer_asignaturas(archivo_vacio)
