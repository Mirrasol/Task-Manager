install:
	poetry install

start:
	poetry run python manage.py runserver 127.0.0.1:8000

migrate:
	poetry run python manage.py migrate

shell:
	poetry run python manage.py shell

lint:
	poetry run flake8 task_manager
