# New Flask Project


This is a collection of notes, command line steps and reminders of packages to install for setting up a new Flask project. Obviously, there are many options, these are just the ones I like to use.

## Table of contents

<!-- toc -->

- [Directory structure](#directory-structure)
- [Virtual environment](#virtual-environment)
- [Packages](#packages)
  * [Flask](#flask)
  * [Environmental variables](#environmental-variables)
  * [Database](#database)
  * [Forms](#forms)
  * [User logins](#user-logins)
  * [Email & web tokens](#email--web-tokens)
  * [Timezones](#timezones)
  * [Gathering Data](#gathering-data)
  * [Full-Text Search](#full-text-search)
  * [Internationalization & Localization (I18n L10n)](#internationalization--localization-i18n-l10n)
  * [Translation](#translation)
  * [RESTful API](#restful-api)
  * [Task Queues](#task-queues)
- [Git](#git)
- [Heroku requirements](#heroku-requirements)
- [Digitalocean requirements](#digitalocean-requirements)
- [Application Contexts](#application-contexts)
- [Jinja Filters](#jinja-filters)
- [JSON strings](#json-strings)
- [Request object](#request-object)

<!-- tocstop -->

## Directory structure
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

## Packages

### Flask
```
$ pip install flask
```

### Environmental variables
```
$ pip install python-dotenv
```

### Database
```
$ pip install psycopg2  
$ pip install Flask-SQLAlchemy
$ pip install Flask-Migrate
```

### Forms
```
$ pip install Flask-WTF  
```

### User logins  
```
$ pip install Flask-Login
```

### Email & web tokens
```
$ pip install Flask-Mail
$ pip install PyJWT
$ pip install flask-httpauth
```

### Timezones
```
$ pip install Flask-Moment
```

### Gathering Data
```
$ pip install requests
```

### Full-Text Search
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

### Internationalization & Localization (I18n L10n)
```
$ pip install Flask-Babel
```

### Translation
```
$ pip install guess-language_spirit
$ pip install requests
```

### RESTful API
A command-line HTTP client that makes it easy to send API requests:
```
$ pip install httpie
$ pip install Flask-RESTful  
```

### Task Queues
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
__pycache__  
venv  
.env
working_files
```

Initial commit:
```
$ git add -A  
$ git commit -m 'Initial commit'  
```

## Heroku requirements
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

## Digitalocean requirements

see [deployment_digitalocean.py](https://github.com/jessicarush/python-examples/blob/master/deployment_digitalocean.md)

## Application Contexts

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

## Jinja Filters

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

## Jinja misc notes

To use a jinja variable in a `<script>` in your document you must either add a filter, usually either `safe` if working with lists or data objects or `tojson` if working with strings.

```html
<script type="text/javascript">
  let my_string = {{ name|tojson }};
  let my_array = {{ list|safe }};
</script>
```

## JSON strings

If you want to pass a python data structure to a javascript `<script>` in your HTML template, first pass the encoded object to the template using `json.dumps()`:

```python
@app.route('/', methods=['GET', 'POST'])
def index():
    '''View function for the main landing page.'''
    data = {
        '2019-04-10': 6,
        '2019-04-8': 2,
        '2019-04-6': 8
        }
    return render_template('index.html', data=json.dumps(data))
```

In your template, if you just wanted to print the data as a string you could access it normally through the template variable `{{ data }}`. However, if you want to be able to use that data as a JSON object in a script, you will need to explicitly confirm that any special characters such as `"` or  `'` which would normally be escaped, should be left alone applying the `safe` filter. For example:

In the html template:
```
{{ data }}
```

outputs to the browser and in the source as:
```
{"2019-04-10": 6, "2019-04-8": 2, "2019-04-6": 8}
```

used in a script however:
```html
<div>
  <script type="text/javascript">
    let data = {{ data }};
    // do stuff
  </script>
</div>
```

the source code will look like:
```html
<script type="text/javascript">
    let data = {&#34;2019-04-10&#34;: 6, &#34;2019-04-8&#34;: 2, &#34;2019-04-6&#34;: 8};
    // do stuff
</script>
```

so here we need to apply the safe filter:
```html
<div>
  <script type="text/javascript">
    let data = {{ data|safe }};
    // do stuff
  </script>
</div>
```

source is now what we want:
```html
<script type="text/javascript">
    let data = {"2019-04-10": 6, "2019-04-8": 2, "2019-04-6": 8};
    // do stuff
</script>
```


## Request object

Flask's `request` object (`from flask import request`), is a subclass of the [Werkzeug Request](https://werkzeug.palletsprojects.com/en/0.15.x/wrappers/#base-wrappers) and provides all of the attributes Werkzeug defines plus a few Flask specific ones. See the [flask docs for a complete list](http://flask.pocoo.org/docs/1.0/api/?highlight=make_response#incoming-request-data).

In short, there are various ways to get at the data being sent, depending on how it is being sent, for example:

```python
@app.route('/demo', methods=['GET', 'POST'])
def demo():
    # For url query parameters:
    data = request.args
    data = request.args.get('key')

    # For form input:
    data = request.form
    data = request.form.get('key')
    data = request.form.getlist('key')

    # For content-type application/json, use request.get_json():
    data = request.get_json()

    # As a last resort use request.data:
    data = request.data
```

Some other helpful attributes:

```python
@app.route('/demo', methods=['GET', 'POST'])
def demo():

    print(request.path)
    # /demo
    print(request.full_path)
    # /demo?x=y
    print(request.url)
    # http://127.0.0.1:5007/demo?x=y
    print(request.base_url)
    # http://127.0.0.1:5007/demo
    print(request.url_root)
    # http://127.0.0.1:5007/
    print(request.content_type)
    # application/json (for example)
    print(request.args)
    # The parsed URL parameters (the part in the URL after the question mark).
```
