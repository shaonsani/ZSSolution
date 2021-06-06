## ZSSolution Backend
Make sure you have python and pip in your system (For this project 3.7 recommended). 
Then run, for installing pipenv module to create virtual environment,

`
$ pip install pipenv
`

After successfully installed pipenv, now time to create virtual environment,below command install all the packages from existing pipfile

`
$ pipenv install  
`

If you want to start from the fresh database file then, delete sqlite file from the project directory and run the migrate command, or skip this step,

`
python manage.py migrate
`

Create a superuser for authentication, run the below command,

`
python manage.py createsuperuser
`

Now, to run the django project,

`
python manage.py runserver
`

For evaluate the test case, below command needed,

`
python manage.py test
`
