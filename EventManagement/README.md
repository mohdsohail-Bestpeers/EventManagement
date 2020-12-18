# Introduction
## Event Management:
This project is a web app for organizing events. Built with Python, Postgresql, HTML, Js, and CSS using Django Framework. This project is specially designed for help the people who are the event managers. This project helps them in managing the events and save their time.

# How I built this?

* Python
* Django
* Postgresql Database
* Html5
* Css
* Js (Java Scripts)
* jQuery - AJAX

# Installation

* __Click on [Install](https://pypi.org/project/virtualenv/) to create Virtual-Environments__

* __Install python 3.5__
```bash
    sudo apt-get install python3.5
```
* __Install requirements.txt for the project dependencies:__
```bash 
    pip install -r requirements.txt
```

* __Install postgresql database__
```bash
    sudo apt-get install postgresql postgresql-contrib
```
# Create Database:
* _sudo -u postgres psql_
* _CREATE DATABASE event2db;_
* _\l_
* _\q_

# How to Use:
* Update database in settings.py file
```bash
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'event2db',
            'USER': 'root',
            'PASSWORD': 'root',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
```

# Commands to run the code:

* __Activate virtual environment:__
```bash 
    source Environment_name/bin/activate
```

* __Run the migrations Command:__

_Go in project directory and run_
```bash
    Python manage.py makemigrations
```

* __Run the migrate Command:__
```bash
    python manage.py migrate
```

* __Create a superuser:__
```bash
    python manage.py createsuperuser
```

* __Run the Server:__
```bash
    python manage.py runserver
```

* __Endpoint:__
```bash
http://127.0.0.1:8000/
```
* __SignUp Event account using User and EventRoll from django admin__
    * Required Information:
```bash
    username, passwords, firstname
```
* __Start project and login by event credentials__
```bash
    http://127.0.0.1:8000/
```