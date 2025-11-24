ISORT := poetry run isort
BLACK := poetry run black
MYPY := poetry run mypy --show-error-codes --pretty --explicit-package-bases --check-untyped-defs
LINT := poetry run pylint --rcfile=pyproject.toml
FOLDERS = app/ 

install: 
	poetry install --no-root

build:
	docker-compose up --build -d

db:
	docker-compose up -d db

create-tables:
	docker-compose exec web poetry run python utils.create_tables.py

seed:
	docker-compose exec web poetry run python utils.seed_db.py

build-db:
	docker-compose up --build -d db
	${MAKE} create-tables
	wait 3
	${MAKE} seed


down:
	docker-compose down

run:  ## Run API with uvicorn
	poetry run python -m uvicorn todo_app.main:app --reload --host 0.0.0.0 --port 8000

dev:  ## Run API with uvicorn after creating tables and seeding DB
	poetry run python utils.create_tables.py
	poetry run python utils.seed_db.py
	poetry run python -m uvicorn todo_app.main:app --reload --host 0.0.0.0 --port 8000

format:
	$(ISORT) $(FOLDERS)
	$(BLACK) $(FOLDERS)

format-check:
	$(ISORT) --check $(FOLDERS)
	$(BLACK) --check $(FOLDERS)

lint: 
	$(LINT) $(FOLDERS)

mypy:
	$(MYPY) $(FOLDERS)


test: 
	poetry run pytest -vv ./tests/$(M)

coverage: py_clean ## Add the coverage for the project
	poetry run pytest \
	--junitxml=coverage/test-results.xml \
	--cov-report html:coverage/htmlcov \
	--cov-report xml:coverage/coverage.xml \
	--cov-report term-missing \
	--cov=api/ \
	--cov=services/ \
	tests/

show-coverage: coverage 
	open coverage/htmlcov/index.html

py_clean: ## Remove unused python files
	@find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf
	@find . -type d -empty -delete
	@rm -rdf coverage/

check: format-check lint mypy ## Run the linters and static analysis tools

