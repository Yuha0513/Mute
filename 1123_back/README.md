$ python -m venv venv
$ source venv/Scripts/activate
$ pip install -r requirements.txt
$ pip list
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py loaddata movies.json
$ python manage.py createsuperuser
$ python manage.py runserver