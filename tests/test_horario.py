import pytest
from unittest.mock import patch, mock_open
from horarios_automatricula.matricula import parse_horario
from horarios_automatricula.matricula import read_file
from horarios_automatricula.matricula import split_courses
from horarios_automatricula.matricula import process_course
from horarios_automatricula.matricula import process_horarios
from horarios_automatricula.matricula import add_grupo_to_asignaturas
from horarios_automatricula.horario import Horario
from horarios_automatricula.grupo import Grupo
from horarios_automatricula.asignatura import Asignatura_Grupos
from horarios_automatricula.matricula import Matricula
from horarios_automatricula.asignatura import comparar_horarios
from horarios_automatricula.asignatura import convertir_a_minutos
from io import StringIO
from unittest.mock import patch

def test_read_file_correcto():
    fake_content = "Este es el contenido del archivo."
    fake_path = "test_file.txt"
    
    with patch("builtins.open", mock_open(read_data=fake_content)) as mocked_file:
        result = read_file(fake_path)
        assert result == fake_content
        mocked_file.assert_called_once_with(fake_path, "r", encoding="utf-8")

def test_read_file_no_encontrado():
    fake_path = "non_existent_file.txt"
    
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(ValueError, match=f"No se ha encontrado el archivo en la ruta {fake_path}"):
            read_file(fake_path)

def test_read_file_error_inesperado():
    fake_path = "test_file.txt"
    
    with patch("builtins.open", side_effect=OSError("Fallo inesperado")):
        with pytest.raises(RuntimeError, match="Error al leer el archivo: Fallo inesperado"):
            read_file(fake_path)

def test_read_file_error_de_permisos():
    fake_path = "restricted_file.txt"
    
    with patch("builtins.open", side_effect=PermissionError("Permiso denegado")):
        with pytest.raises(RuntimeError, match="Error al leer el archivo: Permiso denegado"):
            read_file(fake_path)

def test_read_file_archivo_vacio():
    fake_path = "empty_file.txt"

    with patch("builtins.open", mock_open(read_data="")) as mocked_file:
        with pytest.raises(ValueError, match="El archivo está vacío."):
            read_file(fake_path)
        mocked_file.assert_called_once_with(fake_path, "r", encoding="utf-8")

def test_split_courses_secciones():
    content = "1er Curso (Primer Año)\nContenido del primer curso\n2do Curso (Segundo Año)\nContenido del segundo curso"
    expected = [
        "1er Curso (Primer Año)\nContenido del primer curso",
        "2do Curso (Segundo Año)\nContenido del segundo curso"
    ]
    result = split_courses(content)
    assert result == expected

def test_split_courses_seccion_unica():
    content = "1er Curso (Primer Año)\nContenido del curso único"
    expected = ["1er Curso (Primer Año)\nContenido del curso único"]
    result = split_courses(content)
    assert result == expected

def test_split_courses_vacio():
    content = ""
    expected = [""]
    result = split_courses(content)
    assert result == expected

def test_process_course_fila_valida():
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

def test_process_course_multiple_filas():
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

def test_process_course_columna_erronea():
    course_data = """1er Curso (Ciencias)
Nombre | Grupo | Lunes | Martes | Miércoles | Jueves | Viernes
Matemáticas | A | 08:00-10:00 |  |  | 10:00-12:00 |  
Física | B | InvalidData |  |  |  |  
"""
    result = process_course(course_data)
    assert len(result) == 1
    assert result[0].nombre == "Matemáticas"

def test_process_course_curso_vacio():
    course_data = """1er Curso (Ciencias)
Nombre | Grupo | Lunes | Martes | Miércoles | Jueves | Viernes
"""
    result = process_course(course_data)
    assert result == []

def test_process_course_datos_parciales():
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

def test_process_horarios_datos_validos():
    lunes = "08:00-10:00"
    martes = "09:00-11:00"
    miercoles = ""
    jueves = "10:00-12:00"
    viernes = ""
    
    result = process_horarios(lunes, martes, miercoles, jueves, viernes)
    assert len(result) == 3

    assert result[0].dia == "Lunes"
    assert result[0].hora_inicio == "08:00"
    assert result[0].hora_fin == "10:00"

    assert result[1].dia == "Martes"
    assert result[1].hora_inicio == "09:00"
    assert result[1].hora_fin == "11:00"

    assert result[2].dia == "Jueves"
    assert result[2].hora_inicio == "10:00"
    assert result[2].hora_fin == "12:00"

def test_process_horarios_vacio_datos():
    lunes = ""
    martes = ""
    miercoles = ""
    jueves = ""
    viernes = ""
    
    result = process_horarios(lunes, martes, miercoles, jueves, viernes)
    assert result == []

def test_process_horarios_datos_incompletos():
    lunes = "08:00-10:00"
    martes = ""
    miercoles = "10:00-11:00"
    jueves = ""
    viernes = ""
    
    result = process_horarios(lunes, martes, miercoles, jueves, viernes)
    assert len(result) == 2

    assert result[0].dia == "Lunes"
    assert result[0].hora_inicio == "08:00"
    assert result[0].hora_fin == "10:00"

    assert result[1].dia == "Miércoles"
    assert result[1].hora_inicio == "10:00"
    assert result[1].hora_fin == "11:00"

def test_process_horarios_datos_incorrectos():
    lunes = "08:00-10:00"
    martes = "invalid-data"
    miercoles = "10:00-11:00"
    jueves = "12:00"
    viernes = "15:00-16:00"
    
    result = process_horarios(lunes, martes, miercoles, jueves, viernes)
    assert len(result) == 3

    assert result[0].dia == "Lunes"
    assert result[0].hora_inicio == "08:00"
    assert result[0].hora_fin == "10:00"

    assert result[1].dia == "Miércoles"
    assert result[1].hora_inicio == "10:00"
    assert result[1].hora_fin == "11:00"

    assert result[2].dia == "Viernes"
    assert result[2].hora_inicio == "15:00"
    assert result[2].hora_fin == "16:00"

def test_process_horarios_tiempo_malformulado():
    lunes = "08:00-10:00"
    martes = "09:00-11"
    miercoles = "10-11:00"
    jueves = ""
    viernes = "15:00-16:00"
    
    result = process_horarios(lunes, martes, miercoles, jueves, viernes)
    assert len(result) == 2

    assert result[0].dia == "Lunes"
    assert result[0].hora_inicio == "08:00"
    assert result[0].hora_fin == "10:00"

    assert result[1].dia == "Viernes"
    assert result[1].hora_inicio == "15:00"
    assert result[1].hora_fin == "16:00"

def test_process_horarios_espacios_blancos():
    lunes = "  08:00 - 10:00  "
    martes = "   "
    miercoles = "10:00 -  11:00"
    jueves = ""
    viernes = " 15:00 - 16:00 "
    
    result = process_horarios(lunes, martes, miercoles, jueves, viernes)
    assert len(result) == 3

    assert result[0].dia == "Lunes"
    assert result[0].hora_inicio == "08:00"
    assert result[0].hora_fin == "10:00"

    assert result[1].dia == "Miércoles"
    assert result[1].hora_inicio == "10:00"
    assert result[1].hora_fin == "11:00"

    assert result[2].dia == "Viernes"
    assert result[2].hora_inicio == "15:00"
    assert result[2].hora_fin == "16:00"

def test_add_grupo_to_asignaturas_nueva_asignatura():
    asignaturas = []
    grupo = Grupo("A", [Horario("Lunes", "08:00", "10:00")])
    
    add_grupo_to_asignaturas(asignaturas, "Matemáticas", grupo)
    
    assert len(asignaturas) == 1
    assert asignaturas[0].nombre == "Matemáticas"
    assert len(asignaturas[0].grupos) == 1
    assert asignaturas[0].grupos[0].letra == "A"
    assert asignaturas[0].grupos[0].horarios[0].dia == "Lunes"

def test_add_grupo_to_asignaturas_asignatura_existente():
    grupo_existente = Grupo("A", [Horario("Lunes", "08:00", "10:00")])
    asignaturas = [Asignatura_Grupos("Matemáticas", [grupo_existente])]

    grupo_nuevo = Grupo("B", [Horario("Martes", "10:00", "12:00")])
    add_grupo_to_asignaturas(asignaturas, "Matemáticas", grupo_nuevo)
    
    assert len(asignaturas) == 1
    assert asignaturas[0].nombre == "Matemáticas"
    assert len(asignaturas[0].grupos) == 2
    assert asignaturas[0].grupos[1].letra == "B"
    assert asignaturas[0].grupos[1].horarios[0].dia == "Martes"

def test_add_grupo_to_asignaturas_conjunto_asignaturas():
    grupo_matematicas = Grupo("A", [Horario("Lunes", "08:00", "10:00")])
    grupo_fisica = Grupo("B", [Horario("Martes", "10:00", "12:00")])
    asignaturas = [
        Asignatura_Grupos("Matemáticas", [grupo_matematicas]),
        Asignatura_Grupos("Física", [grupo_fisica]),
    ]

    grupo_nuevo = Grupo("C", [Horario("Miércoles", "12:00", "14:00")])
    add_grupo_to_asignaturas(asignaturas, "Química", grupo_nuevo)
    
    assert len(asignaturas) == 3
    quimica = next(a for a in asignaturas if a.nombre == "Química")
    assert quimica.nombre == "Química"
    assert len(quimica.grupos) == 1
    assert quimica.grupos[0].letra == "C"
    assert quimica.grupos[0].horarios[0].dia == "Miércoles"

def test_add_grupo_to_asignaturas_grupos_duplicados():
    grupo_existente = Grupo("A", [Horario("Lunes", "08:00", "10:00")])
    asignaturas = [Asignatura_Grupos("Matemáticas", [grupo_existente])]

    add_grupo_to_asignaturas(asignaturas, "Matemáticas", grupo_existente)
    
    assert len(asignaturas) == 1
    assert asignaturas[0].nombre == "Matemáticas"
    assert len(asignaturas[0].grupos) == 1 

def test_add_grupo_to_asignaturas_lista_vacia():
    asignaturas = []
    grupo = Grupo("A", [Horario("Lunes", "08:00", "10:00")])
    
    add_grupo_to_asignaturas(asignaturas, "Historia", grupo)
    
    assert len(asignaturas) == 1
    assert asignaturas[0].nombre == "Historia"
    assert len(asignaturas[0].grupos) == 1
    assert asignaturas[0].grupos[0].letra == "A"

def test_parse_horario_correcto():
    file_path = "docs/asignaturas.txt"
    
    with open(file_path, "r", encoding="utf-8") as file:
        file_content = file.read()
    
    with patch("builtins.open", return_value=StringIO(file_content)):
        matricula = parse_horario(file_path)
    
        assert len(matricula.asignaturas) == 40
        
        asignatura_calculo = matricula.asignaturas[0]
        assert asignatura_calculo.nombre == "Cálculo I"
        
        assert len(asignatura_calculo.grupos) == 1
        assert asignatura_calculo.grupos[0].letra == "A"

def test_convertir_a_minutos_valido():
    assert convertir_a_minutos("09:00") == 540
    assert convertir_a_minutos("14:30") == 870
    assert convertir_a_minutos("00:00") == 0
    assert convertir_a_minutos("23:59") == 1439

def test_convertir_a_minutos_invalido():
    with pytest.raises(ValueError):
        convertir_a_minutos("09:60")
        convertir_a_minutos("25:00")
        convertir_a_minutos("abc")

def test_comparar_horarios_sin_superposicion():
    horario1 = Horario("Lunes", "09:00", "11:00")
    grupo1 = Grupo("A", [horario1])
    asignatura1 = Asignatura_Grupos("Matemáticas", [grupo1])

    horario2 = Horario("Lunes", "11:30", "13:00")
    grupo2 = Grupo("B", [horario2])
    asignatura2 = Asignatura_Grupos("Física", [grupo2])

    assert comparar_horarios(asignatura1, asignatura2) is True 

def test_comparar_horarios_con_superposicion():
    horario1 = Horario("Lunes", "09:00", "11:00")
    grupo1 = Grupo("A", [horario1])
    asignatura1 = Asignatura_Grupos("Matemáticas", [grupo1])

    horario2 = Horario("Lunes", "10:30", "12:00")
    grupo2 = Grupo("B", [horario2])
    asignatura2 = Asignatura_Grupos("Física", [grupo2])

    with pytest.raises(ValueError):
        comparar_horarios(asignatura1, asignatura2)

def test_comparar_horarios_diferentes_dias():
    horario1 = Horario("Lunes", "09:00", "11:00")
    grupo1 = Grupo("A", [horario1])
    asignatura1 = Asignatura_Grupos("Matemáticas", [grupo1])

    horario2 = Horario("Martes", "10:30", "12:00")
    grupo2 = Grupo("B", [horario2])
    asignatura2 = Asignatura_Grupos("Física", [grupo2])

    assert comparar_horarios(asignatura1, asignatura2) is True