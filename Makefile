check-python:
	@command -v python3 >/dev/null 2>&1 || (echo "Python no está instalado. Instalando..."; $(MAKE) install-python)

install-python:
	@echo "Instalando Python..."
	@wget https://www.python.org/ftp/python/3.13.0/Python-3.13.0.tgz
	@tar -xzf Python-3.13.0.tgz
	@cd Python-3.13.0 && ./configure --prefix=/usr/local && make && make install
	@rm -rf Python-3.13.0.tgz Python-3.13.0

check-poetry:
	@command -v poetry >/dev/null 2>&1 || (echo "Poetry no está instalado. Instalando..."; $(MAKE) install-poetry)

install-poetry: check-python
	@echo "Instalando Poetry..."
	@curl -sSL https://install.python-poetry.org | python3 -

install-dependencies: 
	poetry install

install: check-python check-poetry install-dependencies

check:
	@echo "Verificando la sintaxis de los archivos .py en horarios_automatricula..."
	@find horarios_automatricula -name "*.py" | while read file; do \
		echo "Verificando $$file..."; \
		python3 -m py_compile $$file && echo "Sintaxis correcta en $$file" || echo "Error de sintaxis en $$file"; \
	done