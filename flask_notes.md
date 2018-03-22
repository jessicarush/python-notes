# New Flask project steps (command line)

## Directory
```
mkdir projectname  
cd projectname/  
mkdir app  
mkdir app/templates  
mkdir app/static  
mkdir app/static/css  
mkdir app/static/js  
mkdir app/static/img  
```

## Virtual environment
```
python3 -m venv venv  
source venv/bin/activate  
pip install flask  
```  

## Git
```
git init  
touch .gitignore
```
.gitignore contents:  
.DS_Store  
\__pycache__  
venv  
```
git add -A  
git commit -m 'Initial commit'  
```

## Environmental variables
```
pip install python-dotenv
```

## Database
```
pip install psycopg2  
pip install Flask-SQLAlchemy
pip install Flask-Migrate
```

## Forms
```
pip install Flask-WTF  
```

## User logins  
```
pip install Flask-Login
```

## Email & JSON web tokens
```
pip install Flask-Mail
pip install PyJWT
```
## Timezones
```
pip install Flask-Moment
```

## Internationalization & Localization (I18n L10n)
```
pip install Flask-Babel
```

## Translation
```
pip install guess-language_spirit
pip install requests
```

## RESTful API
```
pip install Flask-RESTful  
```

## Heroku
```
touch Procfile  
```
Procfile contents (gunicorn or uwsgi):  
web: gunicorn app:app  
web: uwsgi uwsgi.ini

```
touch runtime.txt  
```
runtime.txt contents ([check current version on heroku](https://devcenter.heroku.com/articles/python-runtimes)):  
python-3.6.4  

```
pip freeze > requirements.txt
```
if planning on using gunicorn:
```
pip install gunicorn
```
if planning on using uwsgi:
```
pip install uwsgi  
touch uwsgi.ini  
```
uwsgi.ini contents:  
see heroku.py or digitalocean.py

## Digitalocean  
