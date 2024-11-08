POETRY = poetry

install:
	$(POETRY) install

check-syntax:
	$(POETRY) run flake8 horarios_automatricula

# Comando para ejecutar pruebas con pytest
check-tests:
	$(POETRY) run pytest

# Regla principal 'check' para ejecutar las dos verificaciones (sintaxis y pruebas)
check: check-syntax check-tests