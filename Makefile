POETRY = poetry
PYTHON = python3

check-python:
	@command -v $(PYTHON) >/dev/null 2>&1 || (echo "Python no está instalado. Instalando..."; $(MAKE) install-python)

install-python:
	@echo "Instalando Python..."
	@sudo apt update
	@sudo apt install -y python3 python3-pip

check-poetry:
	@command -v $(POETRY) >/dev/null 2>&1 || (echo "Poetry no está instalado. Instalando..."; $(MAKE) install-poetry)

install-poetry: check-python
	@echo "Instalando Poetry..."
	@curl -sSL https://install.python-poetry.org | $(PYTHON) -

install-dependencies: 
	$(POETRY) install

install: check-python check-poetry install-dependencies

FILE = horarios_automatricula/asignatura.py
check-syntax:
	@echo "Verificando la sintaxis de los archivos .py en horarios_automatricula..."
	@find horarios_automatricula -name "*.py" | while read file; do \
		echo "Verificando $$file..."; \
		$(PYTHON) -m py_compile $$file && echo "Sintaxis correcta en $$file" || echo "Error de sintaxis en $$file"; \
	done

check: check-syntax