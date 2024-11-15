check-poetry:
	@command -v poetry >/dev/null 2>&1 || (echo "Poetry no está instalado. Instalando..."; $(MAKE) install-poetry)

install-poetry: check-python
	@echo "Instalando Poetry..."
	@curl -sSL https://install.python-poetry.org | python -

install-dependencies: 
	poetry install

install: check-poetry install-dependencies

check:
	@echo "Verificando la sintaxis de los archivos .py en horarios_automatricula..."
	@find horarios_automatricula -name "*.py" | while read file; do \
		echo "Verificando $$file..."; \
		python -m py_compile $$file && echo "Sintaxis correcta en $$file" || echo "Error de sintaxis en $$file"; \
	done