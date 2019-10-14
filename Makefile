setuptools:
	@pip3 install -U pip==18.1
	@pip3 install -U setuptools wheel
	@pip3 install -U pip-tools

requirements: requirements.in
	@pip-compile --no-index -U requirements.in

requirements-dev: requirements-dev.in
	@pip-compile --no-index -U requirements.in requirements-dev.in --output-file=requirements-dev.txt

compile-deps: setuptools requirements requirements-dev clean

install-deps:
	@pip3 install -r requirements-dev.txt -r requirements.txt

clean:
	@rm -f dist/*
	@find . -name '*.pyc' -or -name '*.pyo' -or -name '__pycache__' -type f -delete
	@find . -type d -empty -delete

dist: clean
	@python3 ./setup.py sdist bdist_wheel

init: compile-deps
	@pip3 install -r requirements-dev.txt -r requirements.txt
	@python ./setup.py develop
	@cp env.example .env

lint:
	@echo linting code ...
	@flake8