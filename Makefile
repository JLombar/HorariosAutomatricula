.PHONY: test

install-uv:
	@echo "Instalando UV..."
	@curl -LsSf https://astral.sh/uv/install.sh | sh

install-dependencies: 
	uv build

install: install-uv install-dependencies

check:
	@echo "Verificando la sintaxis de los archivos .py en horarios_automatricula..."
	@find horarios_automatricula -name "*.py" | while read file; do \
		echo "Verificando $$file..."; \
		python -m py_compile $$file && echo "Sintaxis correcta en $$file" || echo "Error de sintaxis en $$file"; \
	done

test:
	uv run pytest