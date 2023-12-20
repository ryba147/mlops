help:
	@echo "\t venv - Create a virtual environment"
	@echo "\t dotenv - Create a .env file for a basic configuration"
	@echo "\t lint - Run code quality tools"
	@echo "\t update-packages - Generate and install from requirements.txt file without package versions conflict"
	@echo "\t run - Run application outside of Docker container"
	@echo "\t up - Run application within the Docker container"
	@echo "\t rebuild - Rebuild the image"

dotenv:
	cp .env.default .env

venv:
	test -d venv || python3.11 -m venv venv
	venv/bin/pip install -Ur requirements.txt

update-packages:
	venv/bin/pip install -U pip pip-tools
	venv/bin/pip-compile -U requirements.in -qo requirements.txt
	venv/bin/pip install -Ur requirements.txt

lint:
	@venv/bin/isort app
	@venv/bin/black app
	@venv/bin/flake8 app
	@venv/bin/mypy app

run:
	uvicorn app.main:app --port 8000 --reload

build:
	echo

up:
	echo