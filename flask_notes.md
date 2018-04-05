# New Flask project

Command line steps and reminders of packages to install for setting up a new Flask project. Obviously, there are other options, these are just the ones I like to use.

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

```  

## Flask
```
pip install flask
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

## Gathering Data
```
pip install requests
```

## Full-Text Search
```
brew install elasticsearch
pip install elasticsearch
```

Elasticsearch must be running in order to use it.
First cd to the directory where it lives, then run it.
In my case it's:

```
sudo cd /usr/local/bin/
elasticsearch
```
Check that it's running here: http://localhost:9200/
To quit elasticsearch, ctrl-c in the terminal window where you launched it.

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

## Git
```
git init  
touch .gitignore
```
.gitignore contents:  
.DS_Store  
\__pycache__  
venv  
.env
```
git add -A  
git commit -m 'Initial commit'  
```

## Heroku
```
touch Procfile  
```
Procfile contents should be one of the following (gunicorn or uwsgi):  
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
for contents see [deployment_heroku.py](https://github.com/jessicarush/python-examples/blob/master/deployment_heroku.md)

## Digitalocean  

see [deployment_digitalocean.py](https://github.com/jessicarush/python-examples/blob/master/deployment_digitalocean.md)
