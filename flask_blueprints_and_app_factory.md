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

The contents of a blueprint are initially in a dormant state. To associate these elements, the blueprint needs to be registered with the application. During the registration, all the elements that were added to the blueprint are passed on to the application. Think of a blueprint as a temporary storage for application functionality that helps in organizing your code.

```python
Todo...
# Blueprint with its own templates and static dirs
```

```python
# example routes with @bp.route
```

The Blueprint class takes the name of the blueprint, the name of the base module (typically set to `__name__` like in the Flask application instance), and a few optional arguments. After the blueprint object is created, we import any modules from the same directory as this blueprint (e.g. `routes.py`) so that the route handlers are registered with the blueprint. We only need to include modules that import the blueprint. The import at the bottom avoids circular dependencies.


## Factory function: create_app()

Having the application as a global variable introduces some complications, mainly in the form of limitations for some testing scenarios. Before using blueprints, the application had to be a global variable, because all the view functions and error handlers needed to be decorated with decorators that come from app, such as `@app.route`. Now that all routes and error handlers are moved to blueprints, there are a lot less reasons to keep the application global. So what we do, is define a function called `create_app()` that constructs a Flask application instance, and eliminate the global variable.

```python 
Todo...
# __init__.py
```

Most Flask extensions are initialized by creating an instance of the extension and passing the application as an argument. When the application does not exist as a global variable, there is an alternative mode in which extensions are initialized in two phases. The extension instance is first created in the global scope as before, but no arguments are passed to it. This creates an instance of the extension that is not attached to the application. At the time the application instance is created in the factory function, the `init_app()` method must be invoked on the extension instances to bind it to the now known application.

To register a blueprint, the register_blueprint() method of the Flask application instance is used. When a blueprint is registered, any view functions, templates, static files, error handlers, etc. are connected to the application. We put the import of the blueprint right before the `app.register_blueprint(`) to avoid circular dependencies.

The `register_blueprint()` call for the `api_bp` has an extra argument, `url_prefix`. This is entirely optional. Flask gives you the option to attach a blueprint under a URL prefix, so any routes defined in the blueprint get this prefix in their URLs. In many cases this is useful as a sort of *namespacing* that keeps all the routes in the blueprint separated from other routes in the application or other blueprints. 

For the `api`, it might be nice to have all the routes starting with `/api`, so we added the prefix. Now any login URL is going to be `http://localhost:5000/auth/`. Note that if you use `url_for()`, all URLs will automatically incorporate the prefix.


## current_app instead of global app

Most references to app went away with the introduction of blueprints, (`@bp.route` instead of `@app.route`) but with our new application factory function, we'll also have to modify all references to `app.config` and their related imports (`from app import app`) since app is now inside the factory function. 

Flask tries to make this easy. The `current_app` variable that Flask provides (`from flask import current_app`) is a special *context variable* that Flask initializes with the application before it dispatches a request. We have seen context variables before: the `g` variable and Flask-Login's `current_user`. These are somewhat "magical" variables, in that they work like global variables, but are only accessible during the handling of a request, and only in the thread that is handling it. Replacing `app` with `current_app` eliminates the need of importing the application instance as a global variable. Once we change all our `from app import app` to `from flask import current_app`, we can update all references of `app.config` to `current_app.config`.

```python
# except in factory function itself
app.config 
```

## app_context 

```python
with app.app_context():
````

```python
app_context.push()
```

