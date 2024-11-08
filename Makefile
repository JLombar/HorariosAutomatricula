POETRY = poetry

install-poetry:
	@echo "Instalando Poetry..."
	@curl -sSL https://install.python-poetry.org | python3 -

install: 
	$(POETRY) install

check-syntax:
	$(POETRY) run flake8 horarios_automatricula

check: check-syntax
