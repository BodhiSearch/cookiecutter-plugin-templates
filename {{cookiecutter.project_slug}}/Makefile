.PHONY: clean clean-build clean-pyc clean-test coverage dist docs help install lint lint/flake8
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr dist/

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint/ruff: ## check style with ruff
	ruff .

lint: lint/ruff ## check style

test: ## run unit tests
	poetry run pytest

test-all: ## run all tests including integration tests
	poetry run pytest -m all

coverage: ## check code coverage quickly with the default Python
	poetry run pytest --cov-report html --cov=src tests_{{ cookiecutter.__project_underscore }}
	$(BROWSER) htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	docs/build_docs.sh

servedocs: docs ## compile the docs watching for changes
	python -m http.server -d docs/api/_build -b localhost 8000

release: dist ## package and upload a release
	poetry publish

dist: clean ## builds source and wheel package
	poetry build
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	poetry install
