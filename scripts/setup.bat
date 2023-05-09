@echo off

:: Create virtual environment
if not exist .venv\ (
	python -m venv .venv
)

:: Activate virtual environment
if not defined VIRTUAL_ENV (
	call .venv\Scripts\activate
)

:: Update virtual environment
python -m pip install -U pip setuptools wheel

:: Install dependencies
pip install -r requirements-dev.txt

:: Install pre-commit
:: pre-commit install

:: Create .env from example
if not exist .env (
	copy .env.example .env
)

:: Delete the existing database
if exist db.sqlite3 (
	del db.sqlite3
)

:: Initialize a clean database
python app/manage.py makemigrations
python app/manage.py migrate

:: Delete migrations during development
del app\beer\migrations\0001_initial.py
del app\brewery\migrations\0001_initial.py
del app\image\migrations\0001_initial.py
del app\location\migrations\0001_initial.py
del app\user\migrations\0001_initial.py

:: Create super user
if not defined DJANGO_SUPERUSER_USERNAME (
    set DJANGO_SUPERUSER_USERNAME=user
    set DJANGO_SUPERUSER_PASSWORD=pass
    set DJANGO_SUPERUSER_EMAIL=user@email.com
)

python app\manage.py createsuperuser --noinput

:: Load data
python app/manage.py loaddata users
python app/manage.py loaddata breweries
python app/manage.py loaddata brewery_images
python app/manage.py loaddata locations
python app/manage.py loaddata location_images
python app/manage.py loaddata location_reviews
python app/manage.py loaddata beers
python app/manage.py loaddata beer_images
python app/manage.py loaddata beer_reviews
