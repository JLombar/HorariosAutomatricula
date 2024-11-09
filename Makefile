POETRY = poetry
PYTHON = python3

check-python:
	@command -v $(PYTHON_CMD) >/dev/null 2>&1 || (echo "Python no está instalado. Instalando..."; $(MAKE) install-python)

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

check-syntax:
	$(POETRY) run flake8 horarios_automatricula

check: check-syntax