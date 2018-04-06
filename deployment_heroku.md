# Deployment to Heroku

[Heroku](https://www.heroku.com/) is a container-based cloud Platform as a Service (PaaS). What this means is all you need to provide to have your application deployed is the actual application and a few instruction files. The hardware, operating system, scripting language interpreters, database, etc. are all managed by the service.


Heroku uses an ephemeral file system that runs on a virtualized platform. They use the term 'dynos'. What it means is that at any time, Heroku can reset the virtual server on which your server runs back to a clean state. You cannot assume that any data that you save to the file system will persist, and in fact, Heroku recycles servers very often.

This means there are limitations in terms of what you can do. For example, Heroku does not do caching or things that require a lot of memory, or things that require writing to a file. Sqlite3 is one of the things it doesn't do as it requires writing data to a disk file (a better alternative is PostgreSQL). We also can't write log files or compile language translation repos as these are all written to local files. Some solutions below.

Note you can also have more than one dyno associated with a single app to extend the apps capabilities... essentially multiple dynos mean you can run scripts side by side and have them interact with shared resources like a database. Multiple dynos is part of the pay services.


## Install the Heroku CLI

You can create a new python app through your Heroku dashboard or via the command line. First, make sure you've created an account and downloaded the Heroku Command Line Interface (CLI). You can install this with brew:
```
$ brew install heroku/brew/heroku
```

Now you should be able to login via the the command line (you'll need your Heroku account email, password):
```
$ heroku login
```

## Create a Heroku App
Next, create an app by giving it a name. Note, the name may not be available if it's already being used by someone else. Once
again, you can do this via your dashboard, or through the command line:
```
$ heroku create kusshi
```

Nate that `heroku create` is a shorthand alias for `heroku apps:create`. With either command the resulting URL would be:  

https://kusshi.herokuapp.com/ | https://git.heroku.com/kusshi.git


## Install Gunicorn

[Gunicorn](https://devcenter.heroku.com/articles/python-gunicorn) is a Python WSGI HTTP Server for UNIX. Note you can also use uWSGI (see instructions below).

You can install Gunicorn in your local virtual env, or just manually add it to your requirements.txt below. The main thing is it needs to get installed on the herokuapp (which happens via requirements.txt).

```
$ pip install gunicorn
```

### uWSGI

Another process for running your app (instead of gunicorn) is uwsgi. uWSGI makes Heroku a little more flexible. Like gunicorn you don't need to install uwsgi on your own system, just manually add uwsgi it to your requirements.txt below.

Create a file in the same directory as the app called uwsgi.ini

In this file add the following where *app:app* is *python_filename:flask_variable*:
```
[uwsgi]
http-socket = :$(PORT)
master = true
die-on-term = true
module = app:app
memory-report = true
```


## Create Instruction Files for Heroku

Now we need to make sure to include three files before we upload. These should be located in the same directory as our start script/program file.

1. **requirements.txt**  
   see:  [virtual_environments.md](https://github.com/jessicarush/python-examples/blob/master/virtual_environments.md#keep-track-of-requirements)  
   ```
   $ pip freeze > requirements.txt
   ```
   Add to this file: *gunicorn* or *uwsgi* and *psycopg2* if you're going to use a PostgreSQL database.

2. **Procfile**  
   see: <https://devcenter.heroku.com/articles/procfile>  
   This is a file (no extension) that tells Heroku what web server we want to use with our application. Choose the first one if you're using gunicorn or the second for uwsgi. The first 'app' is the name of your main python file (app.py) without the extension and the second 'app' is the variable name of your Flask app (app = Flask(__name__)).
   ```
   web: gunicorn app:app
   ```
   or:
   ```
   web: uwsgi uwsgi.ini
   ```

3. **runtime.txt**  
   see: <https://devcenter.heroku.com/articles/python-runtimes>  
   This tells Heroku what python version you would like to run your your app with. If you don't specify, it'll be Python 2.7 (ew!). Check the link above to see which runtime versions are available and enter one:
   ```
   python-3.6.4
   ```

## Upload files to Heroku using a local Git repo

If you haven't already set up Git, do it now:
```
$ git init
$ git add -A
$ git commit -m 'Initial commit'
```

Upload to Heroku (where kusshi is your app name):
```
$ heroku git:remote --app kusshi
$ git push heroku master
```

Provided the push was successful, you can now navigate to the URL in the browser (https://kusshi.herokuapp.com/) or using the command line:
```
$ heroku open
```

When you make changes, you'll want to test them in your local environment. When you're ready, you'll need to git commit the changes before pushing to your 'production' server on heroku.


## Upload files to Heroku using a GitHib repo

From the Deploy tab of your Heroku app dashboard, choose GitHub as the deployment method. Then click the button below to connect to github. You get redirected to an authorization window. Allow and enter your password. Next you'll see your github username listed.  Beside it type the name of the repo you want to use, click search, then connect.

From there you have the option of enabling automatic deploys or manual deploys. A good practice for automatic deploys is to set up auto
deploy for branch master. Then, when you're making changes create a new branch first:
```
$ git branch new_features
```
switch to the new branch:
```
$ git checkout new_features
```
Make your changes as you normally would. Git add and commit as normal. When you're ready to push your new branch to github:
```
$ git push --set--upstream origin new_features
```
Once you're confident your app is working, merge your new branch to your master branch:
```
$ git checkout master
$ git merge new_features
$ git push
```
That final push to the master will auto deploy to Heroku.

## Misc

One thing I discovered is Heroku doesn't like regular 'http://' links to external sources like googlefonts. Instead, change those to 'https://' and everything should work fine.

Check if your local repo has the heroku app assigned to it (I think this happens when you run `heroku git:remote --app kusshi`):
```
$ git remote -v
heroku	https://git.heroku.com/kusshi.git (fetch)
heroku	https://git.heroku.com/kusshi.git (push)
```

You can see all your apps with this command:
```
$ heroku apps
```

You can view log files like so:
```
$ heroku logs --app kusshi
```
You can also get some bits of information by using this command:
```
$ heroku info
```
The above command is helpful in terms of telling you whether you're connected to your app at the moment. You can see a list of all commands with:
```
$ heroku help
```

See here for some [Heroku tips](https://www.airpair.com/heroku/posts/heroku-tips-and-hacks)


## Creating a PostgreSQL database on Heroku

Databases are included as add-ons in Heroku. You can create a database through the website or (a better way) through the command line. There are a number of database options available through Heroku, the hobby-dev one is free but FYI you are limited to 10,000 rows (records) in your database.

This allows you to connect the database to your Heroku app:

```
$ heroku addons:create heroku-postgresql:hobby-dev --app kusshi
```
The URL for the newly created database is stored in a DATABASE_URL environment variable that will be available when the application runs. This is very convenient, if your application already looks for the database URL in that variable.

```python
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
```

If you want to add the Heroku database URL directly:
```
$ heroku config --app kusshi
```
This will print out your database url like so:
```
DATABASE_URL: postgres://lfhrlgygusjxap:ec6f16796c...
```

You can also get this url from the settings tab of your app dashboard, under the button 'Reveal Cofig Vars'. You could then copy the URL and paste it into your .py file where you were connecting to your sqlite3 or local PostgreSQL database. Add the following to the end of the Heroku database url string:
```
?sslmode=require
```

### Build your Tables with db.create_all()

Keep in mind, what we've got so far is an empty database. It will not have any tables yet. You will need to run a command to build your tables. For example:

Start a python session in the command line on Heroku:
```
$ heroku run python3
>>> from survey_app import db
>>> db.create_all()
```

After this if you query your postgresql table (steps below) you should see the table and columns.

### Build your tables using Flask-Migrate

You can add the `flask db upgrade` function to your procfile like so:

**Procfile**
```
web: flask db upgrade; gunicorn microblog:app
```
Because the first command is based on the flask command, I need to add the FLASK_APP environment variable:
```
$ heroku config:set FLASK_APP=microblog.py
```

### Query the Heroku PostgreSQL database

If you want to query the database locally, you'll need to make sure that you have [PostgreSQL installed in your system](https://github.com/jessicarush/python-examples/blob/master/postgreSQL_example.py) and that the "local psql command path" is updated. To do this type the following, where the path is pointing to your own installation of PostgreSQL:
```
$ export PATH=$PATH:/Library/PostgreSQL/10/bin
```

Once that's in place you can type something like this:
```
$ heroku pg:psql --app kussi
```

The prompt will look something like this: `kusshi::DATABASE=>`, and now you can start querying the database:
```sql
SELECT * FROM data;
```

When you're ready to quit this PostrgeSQL utility, type `\q`

Final note: If you created your database on Heroku only, don't forget to add **psycopg2** to your requirements.txt. SQLAlchemy requires it to communicate with PostgreSQL.

## Logging to stdout

If your app currently writes its own logs to file, you'll need to make some changes. Heroku expects applications to log directly to stdout. Anything the application prints to the standard output is saved and returned when you use the heroku logs command `heroku logs --app kusshi`.

See [Miguel's instructions here.](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xviii-deployment-on-heroku)

## Language Translation Compiling

Just like `flask upgrade db`, we can also add our translation compiler to the procfile:

**Procfile**
```
web: flask db upgrade; flask translate compile; gunicorn microblog:app
```
Remember to set FLASK_APP for this:
```
$ heroku config:set FLASK_APP=microblog.py
```

## Elasticsearch hosting

This service is offered by third-party partners that provide add-ons. Be aware that Heroku requires your account to have a credit card on file before you can install any third-party addons, even if you stay within the free tiers.

[SearchBox](https://elements.heroku.com/addons/searchbox) is one of these and comes with a free starter plan. To add SearchBox to your account, you have to run the following command (while logged in)
```
$ heroku addons:create searchbox:starter
```
Also, try this (I don't know if it will work or if there's any point):
```
$ heroku addons:create searchbox:starter ----app kusshi
```

This command will deploy an Elasticsearch service and leave the connection URL for the service in a SEARCHBOX_URL environment variable associated with your application. My application looks for the Elasticsearch connection URL in the ELASTICSEARCH_URL variable, so I need to add this variable and set it to the connection URL assigned by SearchBox:
```
$ heroku config:get SEARCHBOX_URL
<your-elasticsearch-url>
$ heroku config:set ELASTICSEARCH_URL=<your-elasticsearch-url>
```
