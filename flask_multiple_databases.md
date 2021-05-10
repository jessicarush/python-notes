# Working with Multiple Databases in Flask

## Table of contents

<!-- toc -->

- [Introduction](#introduction)
- [SQLAlchemy Binds](#sqlalchemy-binds)
- [Add a Bind Key to a Model](#add-a-bind-key-to-a-model)
- [Tell flask-migrate that we're using multiple databases](#tell-flask-migrate-that-were-using-multiple-databases)
- [Sqlite In-Memory Databses](#sqlite-in-memory-databses)
- [Cross database joins](#cross-database-joins)

<!-- tocstop -->

See also:
- [flask-sqlalchemy multiple databases with binds](https://flask-sqlalchemy.palletsprojects.com/en/2.x/binds/)  
- [flask-migrate multiple database support](https://flask-migrate.readthedocs.io/en/latest/#multiple-database-support)  
- [Sqlite in-memory databases](https://sqlite.org/inmemorydb.html)  
- [In-memory SQLite database and Flask: a threading trap](https://gehrcke.de/2015/05/in-memory-sqlite-database-and-flask-a-threading-trap/)

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
    # This table will be built in the default database
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

The final piece of the puzzle for an in-memory database is that we need to create the tables when the app starts (flask-migrate won't help us here). The example below uses Flask's `before_first_request` decorator. Be sure to read the link at the top of this page about SQLite in-memory and threading.

```python
@app.before_first_request
def before_first_request_func():
    '''Create in-memory database tables.'''
    db.create_all(bind='memory_db')
    print('Tables built in memory database')
```

## Cross database joins

Here's where the bus stops. It seems like creating a foreign key a table in another database should be possible using Flask-SQLAlchemy but I hit a road block when I would try to build my tables using flask-migrate.

The error would be something like:
```
sqlalchemy.exc.NoReferencedTableError: Foreign key associated with column 'tablename.field' could not find table 'tablename' with which to generate a foreign key to target column 'field'
```

Searches seemed to indicate that you could references tables in other databases by adding the "schema name" to the foreign key definition like so:

```python
class Nuts(db.Model):
    '''Model for a table to store nuts'''
    __tablename__ = 'nuts'
    __bind_key__ = 'in_memory_db'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(16), index=True)
    # many to one relationship:
    tree_name = db.Column(db.String(32), db.ForeignKey('main_schema.tree.name'))
```

The schema name is supposedly defined using the `__table_args__` attribute:

```python
class Tree(db.Model):
    '''Model for a table to store Trees'''
    __tablename__ = 'tree'
    __table_args__ = {'schema': 'main_schema'}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), index=True)
```

However, this did not work for me and I have not found a solution.
