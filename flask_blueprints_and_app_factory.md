# Flask Blueprints and Application Factories

## Table of contents

<!-- toc -->

- [Why Blueprints and App Factories](#why-blueprints-and-app-factories)
- [Directory structure](#directory-structure)
- [Blueprints](#blueprints)
- [Factory function: create_app()](#factory-function-create_app)
- [current_app instead of global app](#current_app-instead-of-global-app)
- [app_context](#app_context)

<!-- tocstop -->

## Why Blueprints and App Factories

In Flask, blueprints and application factories go together. App factories allow us to move the creation of the `app` object into a function, which means you can then create multiple instances of the app later. 

Why would you want to do this?

- Testing: You can have instances of the application with different settings to test every case.
- Multiple instances: Imagine you want to run different versions of the same application. Of course you could have multiple instances with different configs set up in your webserver, but if you use factories, you can have multiple instances of the same application running in the same application process.

Blueprints are an organizational concept built into Flask. Blueprints allow us to structure our application into logical, feature-sized sections. Also, when we convert to an application factory, `@app.route(‘/)` won’t work anymore: now that our application is created at runtime, the `app.route` decorator exists only after the factory function is invoked, which is too late. Instead, we use blueprints. A Blueprint object works similarly to a Flask application object, but it is not actually an application. Rather it is a blueprint of how to construct or extend an application.

More on both of these later.
 
## Directory structure

```
Simple_flask_app
├── app
│   ├── api
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── errors
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── main
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── static
│   ├── templates
│   ├── __init__.py
│   └── models.py
├── logs
├── migrations
├── .env
├── .flaskenv
├── app.db
├── app.py
├── config.py
├── README.md
└── requirements.txt
```

You could also put static and templates in the blueprints or whatever you would like to keep organized together:

```
Simple_flask_app
├── app
│   ├── api
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── errors
│   │   ├── static
│   │   ├── templates
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── main
│   │   ├── static
│   │   ├── templates
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── routes.py
│   └── __init__.py
├── logs
├── migrations
├── .env
├── .flaskenv
├── app.db
├── app.py
├── config.py
├── README.md
└── requirements.txt
```

A larger project might look something like this:

```
Flask_project
├── app
│   ├── api
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── auth
│   │   ├── __init__.py
│   │   ├── email.py
│   │   ├── forms.py
│   │   └── routes.py
│   ├── errors
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── main
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── routes.py
│   ├── static
│   │   ├── css
│   │   ├── fonts
│   │   ├── img
│   │   └── js
│   ├── templates
│   ├── tests
│   └── __init__.py
├── logs
├── migrations
├── .env
├── .flaskenv
├── app.db
├── app.py
├── config.py
├── README.md
└── requirements.txt
```

Flask blueprints can be configured to have a separate directory for templates and for static files. You don't have to do this though. 

In the second example, we've got templates and static files in each blueprint. In the first and last example, we have decided to organize templates into sub-directories in the application's template directory so that all templates are in a single location (same with static files). But if you prefer to have the templates and static files that belong to a blueprint inside the blueprint's package, you simply add arguments when creating the blueprint (shown in the next section).


## Blueprints

In Flask, a blueprint is a logical structure that represents a subset of the application. A blueprint can include elements such as routes, view functions, forms, templates and static files. If you write your blueprint in a separate Python package, then you have a component that organizes the elements related to specific feature of the application.

A blueprint could have many files:

```
main/
├── static
├── templates
├── __init__.py
├── forms.py
├── models.py
└── routes.py
```

...or just a few:

```
main/
├── __init__.py
└── routes.py
```

We can create the blueprint object in the blueprint directory `__init__.py` file:

```python
# /app/main/__init__.py

from flask import Blueprint

bp = Blueprint('main', __name__)

# Blueprint with its own templates and static directories
# bp = Blueprint(
#     'main', 
#     __name__,
#     template_folder='templates',
#     static_folder='static'
# )

from app.main import routes
```

The Blueprint class takes the name of the blueprint, the name of the base module (typically set to `__name__` like in the Flask application instance), and a few optional arguments. After the blueprint object is created, we import any modules from the same directory as this blueprint (e.g. `routes.py`) so that the route handlers are registered with the blueprint. We only need to include modules that import the blueprint. The import at the bottom avoids circular dependencies.

> Note the template and static folder args are given a path that can be relative or absolute. If, for example, 'static' is the folder name given, then the directory in `/app/main/static` will be served.

In the blueprints `routes.py`, we would create our view functions like so:

```python
# ...
from app.main import bp

@bp.route('/about')
def about():
    return render_template('about.html', title='About')
```

Other familiar decorators:

```python
from app.main import bp

@bp.app_template_filter('testing')
def test(name):
    # Like @app.template_filter but for a blueprint.
    # Registers a custom jinja template filter, available application wide.  
    pass

@bp.before_app_request
def before_request():
    # Like @app.before_request but for a blueprint. 
    # Function is executed before each request, even if outside of a blueprint.
    pass

@bp.before_request
def before_bp_request():
    # Function is executed before each request within the blueprint only.
    pass

@bp.after_app_request
def after_request():
    # Like @app.after_request but for a blueprint. 
    # Function is executed after each request, even if outside of the blueprint.
    # If a function raises an exception, any remaining after_request functions 
    # will NOT be called. Therefore, this should not be used for actions that 
    # must execute, such as to close resources. Use teardown_request() for that.
    pass

@bp.after_request
def after_bp_request():
    # Function is executed after each request within the blueprint only.
    pass

@bp.teardown_app_request
def teardown_request():
    # Registers a function to be called at the end of each request whether 
    # it was successful or an exception was raised. It is a good place to 
    # cleanup request scope objects like a database session/transaction.
    pass

@bp.teardown_request
def teardown_bp_request():
     # Function is executed at the end of each request within the blueprint only.
     pass

# @bp.before_app_first_request (like @app.before_first_request) is executed 
# before the first request to the application. However it is deprecated since 
# version 2.2 and will be removed in Flask 2.3. Run setup code when creating 
# the application instead.
```

For error handlers:

```python
from app.errors import bp

@bp.app_errorhandler(404)
def not_found_error(error):
    # Like @app.errorhandler but for a blueprint. 
    # This handler is used for all requests, even if outside of the blueprint.
    return render_template('errors/404.html'), 404

# note there is a bp.errorhandler inherited down from the Flask object, but 
# as far as I can tell, it's useless since and error can't be restricted to 
# the blueprint level
```

The contents of a blueprint are initially in a dormant state. To associate these elements, the blueprint needs to be registered with the application. During the registration, all the elements that were added to the blueprint are passed on to the application. Think of a blueprint as a temporary storage for application functionality that helps in organizing your code. The best place to register blueprints is in the application factory function.


## Factory function: create_app()

Having the application as a global variable introduces some complications, mainly in the form of limitations for some testing scenarios. Before using blueprints, the application had to be a global variable, because all the view functions and error handlers needed to be decorated with decorators that come from app, such as `@app.route`. Now that all routes and error handlers are moved to blueprints `@bp.route`, there are a lot less reasons to keep the application global. So what we do, is define a function called `create_app()` that constructs a Flask application instance, and eliminate the global variable.

```python 
# /app/__init__.py
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Please log in to access that page.'
mail = Mail()
moment = Moment()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)
    moment.init_app(app)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    if not app.debug:
        # file error logs

    return app

from app.main import models
```

Other setups:

```python
# Flask docs
def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    from yourapplication.model import db
    db.init_app(app)

    from yourapplication.views.admin import admin
    from yourapplication.views.frontend import frontend
    app.register_blueprint(admin)
    app.register_blueprint(frontend)

    with app.app_context():
        init_something()

    return app
```

Most Flask extensions are initialized by creating an instance of the extension and passing the application as an argument. When the application does not exist as a global variable, there is an alternative mode in which extensions are initialized in two phases. The extension instance is first created in the global scope as before, but no arguments are passed to it. This creates an instance of the extension that is not attached to the application. At the time the application instance is created in the factory function, the `init_app()` method must be invoked on the extension instances to bind it to the now known application.

To register a blueprint, the register_blueprint() method of the Flask application instance is used. When a blueprint is registered, any view functions, templates, static files, error handlers, etc. are connected to the application. We put the import of the blueprint right before the `app.register_blueprint(`) to avoid circular dependencies.

The `register_blueprint()` call has an optional argument, `url_prefix`. Flask gives you the option to attach a blueprint under a URL prefix, so any routes defined in the blueprint get this prefix in their URLs. In many cases this is useful as a sort of *namespacing* that keeps all the routes in the blueprint separated from other routes in the application or other blueprints. 

For the `auth`, it might be nice to have all the routes starting with `/auth`, so we added the prefix. Now any login URL is going to be `http://localhost:5000/auth/`. Note that if you use `url_for()`, all URLs will automatically incorporate the prefix, however we DO need to update our references to include the blueprint name as shown below (e.g. `url_for('login')` becomes `url_for('auth.login')`).

Lastly, in our main `app.py` file where we're running the app, we would import `create_app` and instantiate it:

```python
# from app import app
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(port=5007, debug=False)
```


## current_app instead of global app

Most references to app went away with the introduction of blueprints, (`@bp.route` instead of `@app.route`) but with our new application factory function, we'll also have to modify all references to `app.config` and their related imports (`from app import app`) since app is now inside the factory function (obv you can still use `app.config` inside `create_app()`). 

Flask tries to make this easy. The `current_app` variable that Flask provides (`from flask import current_app`) is a special *context variable* that Flask initializes with the application before it dispatches a request. We have seen context variables before: the `g` variable and Flask-Login's `current_user`. These are somewhat "magical" variables, in that they work like global variables, but are only accessible during the handling of a request, and only in the thread that is handling it. Replacing `app` with `current_app` eliminates the need of importing the application instance as a global variable. Once we change all our `from app import app` to `from flask import current_app`, we can update all references of `app.config` to `current_app.config`.

```python
# ...
from flask import current_app

# project = app.config['PROJECT_NAME']
project = current_app.config['PROJECT_NAME']
```

## url_for

Update all occurrences of `url_for()` to include the blueprint name. For example: `url_for('login')` might become `url_for('auth.login')`.

```python
@bp.route('/logout')
def logout():
    '''View function for the logout link.'''
    logout_user()
    return redirect(url_for('auth.login')) # <-- url_for('bp_name.route')
```

Also do this in your templates:

```html
<li><a href="{{ url_for('main.index') }}">home</a></li>
```

## app_context 

The application context keeps track of the application-level data during a request, CLI command, or other activity. Rather than passing the application around to each function, the `current_app` and `g` proxies are accessed instead.

There are actually two types of contexts, the application context and the request context. In most cases, these contexts are automatically managed by the framework (e.g. when handling a request), but there may be times when contexts need to be manually pushed.

If you try to access `current_app`, or anything that uses it, outside an application context (e.g. a view function), you’ll get this error message:

> RuntimeError: Working outside of application context.

If you see that error while configuring your application, such as when initializing an extension, you can push a context manually since you have direct access to the app.

```python
def create_app():
    app = Flask(__name__)
    # ...
    with app.app_context():
        init_db()

    return app
```

The application context that is created with the `app.app_context()` call makes the application instance accessible via the current_app variable from Flask.

If you needed access to the app context elsewhere in your app:

```python
def do_something():
    with current_app.app_context():
        # do some database thing
        # TODO...
```

For more explanation see:

- [Flask docs](https://flask.palletsprojects.com/en/2.2.x/appcontext/)
- [Flask-SQLAlchemy docs](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/contexts/)
