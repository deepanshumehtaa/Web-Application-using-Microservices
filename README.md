# Django with docker, redis, nginx and gunicorn Project 

## General Requirements
* clone the project and go to the project directory using your terminal / CMD
* [Python](https://www.python.org/downloads/) 3.9 or above (if you are using mac or linux, you have to make sure that your default python version is 3.9 or above)

## Requirements for windows
* [Install poetry for windows using bash](https://python-poetry.org/docs/#windows-powershell-install-instructions) or [install poetry for windows using powershell](https://python-poetry.org/docs/#windows-powershell-install-instructions)
* Run in your CMD: `poetry -v`. If the command not found, you may need to pen a new terminal window or add the poetry binaries (usually in `$HOME/.poetry/bin`) in your PATH variable

## Requirements for mac
* the same as windows


## Requirements for linux (Ubuntu/Debian)
* the same as windows

## Project Setup
* run in you terminal / CMD: `docker exec -it test-app bash`
* run in you terminal / CMD: `pip3 install poetry`
* Run in you terminal / CMD: `poetry install` (make sure you are in the project directory)
* Run in you terminal / CMD: `poetry run python manage.py populate_events` (this command will create random data in your database automatically)
* Run in you terminal / CMD: `poetry run python manage.py makemigrations` (make sure you are in the project directory)
* Run in you terminal / CMD: `poetry run python manage.py migrate` (make sure you are in the project directory)
* Run in you terminal / CMD: `poetry run python manage.py createsuperuser` and enter your email, password, repeat password and then you should get a welcome email (make sure you are in the project directory)
* Run in you terminal / CMD: `poetry run python manage.py runserver 0.0.0.0:8000` (make sure you are in the project directory)
* The server should be now running under `0.0.0.0:8090`
* Open your browser and call `0.0.0.0:8090/admin`. You shoulb be able to see the login page for the admin dashboard. You can use the email and password you have entered when creating the superuser.


## Poetry Usage
* Run in you terminal / CMD: `poetry install` to insatll all the necessary modules / packages for your project
* Run in you terminal / CMD: `poetry update` to update all the modules / packages in your project
* Run in you terminal / CMD: `poetry add <module-name>` to add a new module / package to your project
* Run in you terminal / CMD: `poetry add -D <module-name>` to add a new development module / package to your project


## steps we uses in create our containers
* database container: docker run -d --name app-db --cpus 0.5 --memory 512m -e MYSQL_USER=ali -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=test_db --net app-net mysql:5.7

* python container for windows: docker run -itd --name test-app -v %cd%:/code --cpus 0.5 --memory 512m -p 8090:8000 --workdir /code --net app-net -e DOCKER_CONTAINER_ID=1 python:3.9

* python container for linux/mac : docker run -itd --name test-app -v $PWD:/code --cpus 0.5 --memory 512m -p 8090:8000 --workdir /code --net app-net -e DOCKER_CONTAINER_ID=1 python:3.9
