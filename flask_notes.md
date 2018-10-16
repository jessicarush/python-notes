# New Flask project


Command line steps and reminders of packages to install for setting up a new Flask project. Obviously, there are other options, these are just the ones I like to use.

## Directory
```
$ mkdir projectname  
$ cd projectname/  
$ mkdir app  
$ mkdir app/templates  
$ mkdir app/static  
$ mkdir app/static/css  
$ mkdir app/static/js  
$ mkdir app/static/img  
```

## Virtual environment
```
$ python3 -m venv venv  
$ source venv/bin/activate  
```  

## Flask
```
$ pip install flask
```

## Environmental variables
```
$ pip install python-dotenv
```

## Database
```
$ pip install psycopg2  
$ pip install Flask-SQLAlchemy
$ pip install Flask-Migrate
```

## Forms
```
$ pip install Flask-WTF  
```

## User logins  
```
$ pip install Flask-Login
```

## Email & web tokens
```
$ pip install Flask-Mail
$ pip install PyJWT
$ pip install flask-httpauth
```

## Timezones
```
$ pip install Flask-Moment
```

## Gathering Data
```
$ pip install requests
```

## Full-Text Search
```
$ brew install elasticsearch
$ pip install elasticsearch
```

Elasticsearch must be running in order to use it.
First cd to the directory where it lives, then run it.
In my case it's:
```
$ sudo cd /usr/local/bin/
$ elasticsearch
```
Check that it's running here: http://localhost:9200/
To quit elasticsearch, ctrl-c in the terminal window where you launched it.

## Internationalization & Localization (I18n L10n)
```
$ pip install Flask-Babel
```

## Translation
```
$ pip install guess-language_spirit
$ pip install requests
```

## RESTful API
A command-line HTTP client that makes it easy to send API requests:
```
$ pip install httpie
```

Optional:
```
$ pip install Flask-RESTful  
```

## Task Queues
```
$ pip install rq
```

## Git
```
$ git init  
$ touch .gitignore
```
.gitignore contents:  
```
.DS_Store  
\__pycache__  
venv  
.env
```
Initial commit:
```
$ git add -A  
$ git commit -m 'Initial commit'  
```

## Heroku
```
$ touch Procfile  
```
Procfile contents if using gunicorn:
```
web: gunicorn app:app
```
Procfile contents if using uwsgi:  
```
web: uwsgi uwsgi.ini
```
Create a runtime file:
```
$ touch runtime.txt  
```
runtime.txt contents ([check current version on heroku](https://devcenter.heroku.com/articles/python-runtimes)):  
```
python-3.6.4  
```
if using gunicorn:
```
$ pip install gunicorn
```
if using uwsgi:
```
$ pip install uwsgi  
touch uwsgi.ini  
```
for contents of uwsgi.ini see [deployment_heroku.py](https://github.com/jessicarush/python-examples/blob/master/deployment_heroku.md)  
Create your requirements list:
```
$ pip freeze > requirements.txt
```

## Digitalocean  

see [deployment_digitalocean.py](https://github.com/jessicarush/python-examples/blob/master/deployment_digitalocean.md)

# Application Contexts

If you try to perform database operations outside an application context (ie outside a view function), you will see the following error:

> No application found. Either work inside a view function or push an application context.

In a nutshell, do something like this:
```python
def my_function():
    with app.app_context():
        user = db.User(...)
        db.session.add(user)
        db.session.commit()
```

For more explanation see:
[Miguel's explanation](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure)  
<http://flask.pocoo.org/docs/0.12/appcontext/#creating-an-application-context>  
<http://flask-sqlalchemy.pocoo.org/2.3/contexts/>

# Jinja Filters

There are many [pre-built filters](http://jinja.pocoo.org/docs/2.10/templates/#builtin-filters). To use any of these filters in your HTML template:

```
{{ current_user.username|title }}
```
You can chain filters together:

```
{{ current_user.username|reverse|title }}
```

To create a custom filter for a **basic** flask app (in routes.py):
```python
@app.template_filter('testing')
def test(name):
    '''An example of a jinja2 filter'''
    return name[::-1].upper()
```
To create a custom filter for a flask app that uses **blueprints** (in routes.py):
```python
@bp.app_template_filter('testing')
def test(name):
    '''An example of a jinja2 filter'''
    return name[::-1].upper()
```

The argument passed to the decorator is the name of the filter:
```
{{ current_user.username|testing }}
```
