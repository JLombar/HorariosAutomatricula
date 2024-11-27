import pytest
from unittest.mock import patch, mock_open
from horarios_automatricula.matricula import parse_horario
from horarios_automatricula.horario import Horario
from horarios_automatricula.grupo import Grupo
from horarios_automatricula.asignatura import Asignatura_Grupos
from horarios_automatricula.matricula import Matricula
from horarios_automatricula.comparador import comparar_horarios
from horarios_automatricula.comparador import convertir_a_minutos
from io import StringIO
from unittest.mock import patch

def test_archivo_no_existente():
    with pytest.raises(ValueError):
        parse_horario("archivo_inexistente.txt")

def test_archivo_vacio():
    file_content = ""
    
    with patch("builtins.open", return_value=StringIO(file_content)):
        matricula = parse_horario("test_file.txt")
        
        assert len(matricula.asignaturas) == 0

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