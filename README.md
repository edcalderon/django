# django
my repo to learn django

#### Requirements
We are going to use pipenv like virtualenv so if you need it, install it as:

#### 1. Create Django Project
```
sudo pip install pipenv
pipenv --python 3.6
pipenv shell
```

now to install the requirements:

```
pipenv install -r requirements.txt
```

#### 2. Create Django Project (created in repo)
```
cd /path/to/dev/folder
mkdir src
cd src
django-admin startproject try_django .
```
#### 2. Run proyect server

```
python manage.py runserver
```
