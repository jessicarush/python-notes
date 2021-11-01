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
- [The g object](#the-g-object)
- [The session object](#the-session-object)
- [Jinja delimiters](#jinja-delimiters)
- [Jinja Filters](#jinja-filters)
  * [selectattr() & map() filters](#selectattr--map-filters)
- [Jinja variables in script elements](#jinja-variables-in-script-elements)
- [Jinja whitespace](#jinja-whitespace)
- [JSON strings](#json-strings)
- [Request object](#request-object)
- [Flask-wtf csrf protection](#flask-wtf-csrf-protection)
- [Flask-SQLAlchemy notes](#flask-sqlalchemy-notes)
  * [.count()](#count)
  * [.all()](#all)
  * [.first()](#first)
  * [.one()](#one)
  * [.filter()](#filter)
  * [.filter_by()](#filter_by)
  * [.join()](#join)
  * [.add_columns()](#add_columns)
  * [.with_entities()](#with_entities)
  * [.delete()](#delete)
  * [session.add()](#sessionadd)
  * [session.delete()](#sessiondelete)
- [Flask-moment notes](#flask-moment-notes)
- [Testing a Flask on on your network](#testing-a-flask-on-on-your-network)

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
<https://flask.palletsprojects.com/en/1.1.x/appcontext/>  
<http://flask-sqlalchemy.pocoo.org/2.3/contexts/>

## The g object

## The session object

## Jinja delimiters

`{% ... %}` for [Statements](https://jinja.palletsprojects.com/en/2.11.x/templates/#list-of-control-structures)

`{{ ... }}` for [Expressions](https://jinja.palletsprojects.com/en/2.11.x/templates/#expressions) to print to the template output

`{# ... #}` for Comments not included in the template output

## Jinja Variables

```
{% set icon %}
  <img src="{{ url_for('static', filename='img/icon.svg')}}" />
{% endset %}
```
or

```
{% set something = false %}
```

Keep in mind you cannot use variables set inside a scoped block (like a for loop) outside of the block. See the [Jinja docs on assignments](https://jinja.palletsprojects.com/en/2.11.x/templates/#assignments). But there is a weird thing called namespace objects which you can use like so:

```
{% set ns = namespace(found=false) %}
{% for item in items %}
    {% if item.check_something() %}
        {% set ns.found = true %}
    {% endif %}
    * {{ item.title }}
{% endfor %}
Found item having something: {{ ns.found }}
```

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

### selectattr() & map() filters

```
{{ activities|selectattr("name", "equalto", name)|map(attribute='day')|first }}

{{ activities|selectattr("name", "equalto", name)|map(attribute='count')|first|strip_decimal_zeros }}
{{ activities|selectattr("name", "equalto", name)|map(attribute='unit')|first }}
{% if activities|selectattr("name", "equalto", name)|map(attribute='reps')|first %}
of {{ activities|selectattr("name", "equalto", name)|map(attribute='reps')|first }}
{% endif %
```

## Jinja variables in script elements

To use a jinja variable in a `<script>` in your document you must either add a filter, usually either `safe` if working with lists or data objects or `tojson` if working with strings.

```html
<script type="text/javascript">
  let my_string = {{ name|tojson }};
  let my_array = {{ list|safe }};
</script>
```

## Jinja whitespace

Note that jinja templates will leave whitespace in the rendered code in place of the blocks. If you want to remove all these spaces you can set `trim_blocks` and `lstrip_blocks` on the env:

```python
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
```

...or you can manage it manually in each block, for example:
```
{%- if ... %} strips space before
{%- if ... -%} strips space before and after
{%+ if ... %} preserves space before
{%+ if ... -%} preserves space before and strips after
```

The first option is untested. For more information see the [Jinja Environment API](https://jinja.palletsprojects.com/en/2.11.x/api/?highlight=trim_blocks#jinja2.Environment).

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
from flask import request


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
    # application/json
    print(request.args)
    # the parsed URL parameters (the part in the URL after the question mark).
```

Note that in order to work with the request object, your route must specify `methods=['GET', 'POST']` even if the request is sent via a GET request with query parameters OR works with the `socketio.on` decorator.


```python
referrer = request.headers.get('Referer')
print('referrer', referrer)
```


## The response object

```python
response.headers['Access-Control-Allow-Origin'] = '*'
```

Note the `Access-Control-Allow-Origin` header. In order for requests outside the response origin to access the response, this header must be set. `*` is a wildcard allowing any site to receive the response. You should only use this for public APIs. Private APIs should never use `*`, and should instead have a specific domain or domains set. In addition, the wildcard only works for requests made with the crossorigin attribute set to anonymous, and it prevents sending credentials like cookies in requests. [See MDN for more on this](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS/Errors/CORSMissingAllowOrigin).

## Flask-wtf csrf protection

Flask-wtf has csrf protection built-in by default when you build your forms off of `FlaskForm` for example:

```python
class MyForm(FlaskForm):
    pass
```

The csrf token is generated when the form is initially rendered (i.e. when the page is loaded) and by default expires after 3600 seconds (1 hour). This is means that if you leave the page open for more than than hour without reloading/refreshing, the csrf token will be expired and if you try to submit the form, it will be a quiet failure. There are a number of ways around this but the simplest is to change the global timeout from 3600 seconds to something more reasonable or to not have an expiry at all.

To do this you would set the constant variable in your config:

```python
# Extend csrf token expiry to 1 week
WTF_CSRF_TIME_LIMIT = 3600 * 24 * 7

# If set to None, the CSRF token is valid for the life of the session
WTF_CSRF_TIME_LIMIT = None
```

## Flask-SQLAlchemy notes

### .count()
### .all()
### .first()
### .one()
### .filter()
### .filter_by()
### .join()
### .add_columns()
### .with_entities()

If you only want to get the results a specific (1 or more columns) you would normally have to do something like `session.query(Model.col)`. For some reason if you try to at call brackets to a Model query like `Model.query(Model.code)` you'll get an error: `'BaseQuery' object is not callable`.

Instead, you can use `with_entities()`:

```python
codes = Alert.query.with_entities(Alert.code).filter_by(device_name=device, type='fault').all()
```

### .delete()

For example:
```python
Activity.query.filter_by(session_id=session_id).delete()
```

### session.add()

### session.delete()

For example:
```python
activities = Activity.query.filter_by(session_id=session_id).all()
for activity in activities:
    db.session.delete(activity)
```

## Flask-moment notes

{{ moment(activities|selectattr("name", "equalto", name)|map(attribute='day')|first, local=True).format('ll') }}


## Testing a Flask on your network

```
flask run --host=0.0.0.0
```
or
```python
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
```

Then find your machines ip (e.g. 10.0.0.57)

```
http://10.0.0.57:5000
```

If you have a login in your site, you'll be blocked for privacy. You're supposed to be able to apply temporary ssl certs with:

```
flask run --cert=adhoc
```
or
```python
if __name__ == '__main__':
    app.run(port=5000, debug=True, ssl_context='adhoc')
```

To use adhoc certificates with Flask, you need to install an additional dependency in your virtual environment:
```
pip install pyopenssl
```

Even with this though, you'll be presented with a non-private connection page which you'll have to dig through the advanced button in order to ok the site.

Do these things together:
```
flask run --host=0.0.0.0 --cert=adhoc
```
or
```python
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True, ssl_context='adhoc')
```

Then find your machines ip (e.g. 10.0.0.57)
```
https://10.0.0.57:5000
```
