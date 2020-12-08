# Working with Multiple Databases in Flask

See [flask-sqlalchemy multiple databases with binds](https://flask-sqlalchemy.palletsprojects.com/en/2.x/binds/).
See [Sqlite in-memory databases](https://sqlite.org/inmemorydb.html).
See [flask-migrate multiple database support](https://flask-migrate.readthedocs.io/en/latest/#multiple-database-support)


## Table of contents

<!-- toc -->

<!-- tocstop -->


## Introduction

It's pretty easy to create and use multiple databases with flask, flask-sqlalchemy and flask-migrate. We will need to:

1. define our additional databases using the `SQLALCHEMY_BINDS` config variable.
2. add the "bind key" to our table Model's
3. add the `multidb` argument to the `db init` command

If you want one of these additional databases to be an Sqlite in-memory database, you'll also need to:

4. create in-memory database tables when the app starts.


## SQLAlchemy Binds

Flask-SQLAlchemy can connect to multiple databases using "binds". A bind specifies which connection engine to use. The bind key is then used at model declaration to associate a model with a specific engine. If no bind key is specified for a model the default connection is used (as configured by SQLALCHEMY_DATABASE_URI).

Binds are declared like so:

```python
# The default database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or \
      'sqlite:///' + os.path.join(basedir, 'app.db')
# Additional databases      
app.config['SQLALCHEMY_BINDS'] = {
      'second_db': 'sqlite:///' + os.path.join(basedir, 'second.db'),
      'memory_db': 'sqlite:///:memory:?cached=shared'
      }
```

Or if you are using a config object:

```python
class Config(object):
    '''Configuration object for Flask app instance'''
    # https://flask.palletsprojects.com/en/1.1.x/config/
    PROJECT_NAME = 'Project Name'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super_secret_password'
    # The default database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    # Additional databases  
    SQLALCHEMY_BINDS = {
        'second_db': 'sqlite:///' + os.path.join(basedir, 'second.db'),
        'memory_db': 'sqlite:///:memory:?cached=shared'
        }
```

## Add a Bind Key to a Model

To associate a model with a specific database, add the `__bind_key__` attribute. Any Models that do not include the `__bind_key__` will use the default SQLALCHEMY_DATABASE_URI.

```python
class Test1(db.Model):
    '''Model for the testing first database'''
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(64), default='red')


class Test2(db.Model):
    '''Model for the testing second database'''
    __bind_key__ = 'second_db'
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(64), default='red')


class Test3(db.Model):
    '''Model for the testing in memory database'''
    __bind_key__ = 'memory_db'
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(64), default='blue')
```


## Tell flask-migrate that we're using multiple databases

When using flask-migrate your tables are initially created with the `flask db init` command. You will need to add the `multidb` argument to this command. If you already ran the command, you'll need to destroy the database and migration repository and re-init.

```
flask db init --multidb
```


## Sqlite In-Memory Databses

An in-memory database can be defined using the special filename `:memory:`. In addition, you can enable a shared-cache with `:memory:?cached=shared`. That being said, [this gist from Miguel](https://gist.github.com/miguelgrinberg/dbeb1a51231921d5fa8b3de218d0c449) indicates that you `sqlite:///` alone will create an in-memory database.

For example, these all seem to work:

```python
SQLALCHEMY_BINDS = {
    'memory_db': 'sqlite:///:memory:?cached=shared'
    }
```

```python
SQLALCHEMY_BINDS = {
    'memory_db': 'sqlite:///:memory:'
    }
```

```python
SQLALCHEMY_BINDS = {
    'memory_db': 'sqlite:///'
    }
```

The final piece of the puzzle for an in-memory database is that we need to create the tables when the app starts (flask-migrate won't help us here). So, somewhere in the app's initialization or, in the example below, using flasks `before_first_request` decorator:

```python
@app.before_first_request
def before_first_request_func():
    '''Create in-memory database tables.'''
    db.create_all(bind='memory_db')
    test1 = Testing1(color='yellow')
    db.session.add(test1)
    db.session.commit()
    print('Commited to memory databases')
```
