# Requirements compilation and installation
.PHONY: compile-deps
compile-deps:
	chmod 755 ./shell-scripts/check-req-exists.sh
	./shell-scripts/check-req-exists.sh
	pip install --upgrade pip pip-tools
	pip-compile --output-file requirements.txt 
				--resolver=backtracking

.PHONY: install-deps
install-deps: compile-deps
	pip-sync requirements.txt

.PHONY: compile-deps-dev
compile-deps-dev:
	chmod 755 ./shell-scripts/check-req-dev-exists.sh
	./shell-scripts/check-req-dev-exists.sh
	pip install --upgrade pip pip-tools
	pip-compile --extra=dev
				--output-file requirements-dev.txt
				--resolver=backtracking

.PHONY: install-deps-dev
install-deps-dev: compile-deps compile-deps-dev
	pip-sync requirements.txt requirements-dev.txt

# Start services
.PHONY: runserver
runserver:
	cd src && ./manage.py runserver
	# cd src && ./manage.py migrate && ./manage.py runserver

.PHONY: migrations
migrations:
	cd src && ./manage.py makemigrations && ./manage.py migrate

.PHONY: run-celery-worker
run-celery-worker:
	cd src && celery -A app worker -E --purge

# Style, code formatting
.PHONY: fmt
fmt:
	cd src && autoflake --in-place --remove-all-unused-imports --recursive .
	cd src && isort .
	cd src && black .

.PHONY: lint
lint:
	cd src && ./manage.py makemigrations --check --no-input --dry-run
	flake8 src
	mypy

# Testing
.PHONY: test
test:
	cd src && pytest --ff -x --cov-report=html --cov=. --cov-append
	# cd src && pytest --dead-fixtures

# Debugging
.PHONY: djangoshell
djangoshell:
	cd src && ./manage.py shell