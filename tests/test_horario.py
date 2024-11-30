import pytest
from unittest.mock import patch, mock_open
from horarios_automatricula.matricula import parse_horario
from horarios_automatricula.matricula import read_file
from horarios_automatricula.matricula import split_courses
from horarios_automatricula.matricula import process_course
from horarios_automatricula.horario import Horario
from horarios_automatricula.grupo import Grupo
from horarios_automatricula.asignatura import Asignatura_Grupos
from horarios_automatricula.matricula import Matricula
from horarios_automatricula.asignatura import comparar_horarios
from horarios_automatricula.asignatura import convertir_a_minutos
from io import StringIO
from unittest.mock import patch

def test_read_file_success():
    fake_content = "Este es el contenido del archivo."
    fake_path = "test_file.txt"
    
    with patch("builtins.open", mock_open(read_data=fake_content)) as mocked_file:
        result = read_file(fake_path)
        assert result == fake_content
        mocked_file.assert_called_once_with(fake_path, "r", encoding="utf-8")

def test_read_file_not_found():
    fake_path = "non_existent_file.txt"
    
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(ValueError, match="No se ha encontrado el archivo en la ruta correcta."):
            read_file(fake_path)

def test_read_file_unexpected_error():
    fake_path = "test_file.txt"
    
    with patch("builtins.open", side_effect=OSError("Fallo inesperado")):
        with pytest.raises(RuntimeError, match="Error al leer el archivo: Fallo inesperado"):
            read_file(fake_path)

def test_read_file_permission_error():
    fake_path = "restricted_file.txt"
    
    with patch("builtins.open", side_effect=PermissionError("Permiso denegado")):
        with pytest.raises(RuntimeError, match="Error al leer el archivo: Permiso denegado"):
            read_file(fake_path)

def test_read_file_empty_file():
    fake_path = "empty_file.txt"

    with patch("builtins.open", mock_open(read_data="")) as mocked_file:
        with pytest.raises(ValueError, match="El archivo está vacío."):
            read_file(fake_path)
        mocked_file.assert_called_once_with(fake_path, "r", encoding="utf-8")

def test_split_courses_multiple_sections():
    content = "1er Curso (Primer Año)\nContenido del primer curso\n2do Curso (Segundo Año)\nContenido del segundo curso"
    expected = [
        "1er Curso (Primer Año)\nContenido del primer curso",
        "2do Curso (Segundo Año)\nContenido del segundo curso"
    ]
    result = split_courses(content)
    assert result == expected

def test_split_courses_single_section():
    content = "1er Curso (Primer Año)\nContenido del curso único"
    expected = ["1er Curso (Primer Año)\nContenido del curso único"]
    result = split_courses(content)
    assert result == expected

def test_split_courses_no_content():
    content = ""
    expected = [""]
    result = split_courses(content)
    assert result == expected

def test_process_course_single_valid_row():
    course_data = """1er Curso (Ciencias)
Nombre | Grupo | Lunes | Martes | Miércoles | Jueves | Viernes
Matemáticas | A | 08:00-10:00 |  |  | 10:00-12:00 |  
"""
    result = process_course(course_data)
    assert len(result) == 1
    assert result[0].nombre == "Matemáticas"
    assert len(result[0].grupos) == 1
    grupo = result[0].grupos[0]
    assert grupo.letra == "A"
    assert len(grupo.horarios) == 2
    assert grupo.horarios[0].dia == "Lunes"
    assert grupo.horarios[0].hora_inicio == "08:00"
    assert grupo.horarios[0].hora_fin == "10:00"
    assert grupo.horarios[1].dia == "Jueves"
    assert grupo.horarios[1].hora_inicio == "10:00"
    assert grupo.horarios[1].hora_fin == "12:00"

def test_process_course_multiple_rows():
    course_data = """1er Curso (Ciencias)
Nombre | Grupo | Lunes | Martes | Miércoles | Jueves | Viernes
Matemáticas | A | 08:00-10:00 |  |  | 10:00-12:00 |  
Física | B |  | 09:00-11:00 |  |  |  
"""
    result = process_course(course_data)
    assert len(result) == 2

    matematicas = next(a for a in result if a.nombre == "Matemáticas")
    assert len(matematicas.grupos) == 1
    assert matematicas.grupos[0].letra == "A"

    fisica = next(a for a in result if a.nombre == "Física")
    assert len(fisica.grupos) == 1
    assert fisica.grupos[0].letra == "B"
    assert len(fisica.grupos[0].horarios) == 1
    assert fisica.grupos[0].horarios[0].dia == "Martes"
    assert fisica.grupos[0].horarios[0].hora_inicio == "09:00"
    assert fisica.grupos[0].horarios[0].hora_fin == "11:00"

def test_process_course_invalid_row_ignored():
    course_data = """1er Curso (Ciencias)
Nombre | Grupo | Lunes | Martes | Miércoles | Jueves | Viernes
Matemáticas | A | 08:00-10:00 |  |  | 10:00-12:00 |  
Física | B | InvalidData |  |  |  |  
"""
    result = process_course(course_data)
    assert len(result) == 1
    assert result[0].nombre == "Matemáticas"

def test_process_course_empty_data():
    course_data = """1er Curso (Ciencias)
Nombre | Grupo | Lunes | Martes | Miércoles | Jueves | Viernes
"""
    result = process_course(course_data)
    assert result == []

def test_process_course_partial_data():
    course_data = """1er Curso (Ciencias)
Nombre | Grupo | Lunes | Martes | Miércoles | Jueves | Viernes
Matemáticas | A | 08:00-10:00 |  |  |  |  
"""
    result = process_course(course_data)
    assert len(result) == 1
    matematicas = result[0]
    assert matematicas.nombre == "Matemáticas"
    assert len(matematicas.grupos) == 1
    grupo = matematicas.grupos[0]
    assert grupo.letra == "A"
    assert len(grupo.horarios) == 1
    assert grupo.horarios[0].dia == "Lunes"
    assert grupo.horarios[0].hora_inicio == "08:00"
    assert grupo.horarios[0].hora_fin == "10:00"