'''Web Libraries and Frameworks'''


# http and urllib modules
# -----------------------------------------------------------------------------
# Python 3 has bundled all its web client and server modules into 2 packages:

# http manages all the client-server HTTP details:
# - client does the client-side stuff
# - server helps you write Python web servers
# - cookies and cookiejar manage cookies, which save data between site visits

# urllib runs on top of http:
# - request handles the client request
# - response handles the server response
# - parse cracks the parts of a URL

from urllib import request

url = 'http://cyan.red'
conn = request.urlopen(url)
print(conn)
# <http.client.HTTPResponse object at 0x103313470>

# conn is an HTTPResponse object with a number of methods. It's read() method
# will give us data from the web page:

data = conn.read()
print(data)
# prints the html as a big, continuous blob

# An important part of an HTTP response is the status code:

print(conn.status)
# 200

# A 200 means everything is good. There dozens of HTTP status codes grouped
# into five rages by their first digit:

# 1.. (information)
#     server received the request but has some extra information for the client
# 2.. (success)
#     it worked, every success code other than 200 conveys extra details
# 3.. (redirection)
#     the resource moved, so the response returns the new URL to the client
# 4.. (client error)
#     some problem from the client side such as the 404(not found)
# 5.. (server error)
#     500 is the generic, you might see 502(bad gateway) if there's a
#     disconnect between web server and backend application server.

# Web servers can send data back in any format. The data format is specified by
# the HTTP response header value with the name Content-Type:

print(conn.getheader('Content-Type'))
# text/html

# The above returns a MIME type: text/plain and text/html are two examples.

# Other HTML header information can be retrieved too:

for key, value in conn.getheaders():
    print(key, ':\t', value)
# Date :              Fri, 02 Mar 2018 19:52:00 GMT
# Server :            Apache
# Last-Modified :     Mon, 27 Mar 2017 18:59:53 GMT
# Accept-Ranges :     bytes
# Content-Length :    6175
# Connection :        close
# Content-Type :      text/html


# Requests Library
# -----------------------------------------------------------------------------
# install: $ pip3 install requests
# documentation: http://docs.python-requests.org/en/master/

# a simple HTTP library (module) for Python web client tasks

import requests

url = 'http://cyan.red'
resp = requests.get(url)
print(resp)
# <Response [200]>

print(resp.text)
# prints the html formatted nicely


# Web Servers
# -----------------------------------------------------------------------------
# Python is an excellent language for writing web servers and server-side
# programs. This has led to a huge variety of Python-based web frameworks.
# A web framework provides features with which you can build websites, so it
# does more than a simple web (HTTP) server such as routing (URL to server
# function), templates (HTM with dynamic inclusions), debugging, and more.

# The Simplest Python Web Servers:

# $ python3 -m http.server

# This implements a bare-bones Python HTTP server. If there are no problems,
# it prints an initial status: Serving HTTP on 0.0.0.0 port 8000...
# The 0.0.0.0 means any TCP address, so web clients can access the server no
# matter what address it has.

# Type http://localhost:8000 in your web browser to see a listing of your
# current directory. The server will print access log lines like:

# 127.0.0.1 - - [14/Aug/2017 13:10:46] "GET / HTTP/1.1" 200 -

# localhost and 127.0.0.1 are TCP for your local computer.

# 127.0.0.1 is the client's IP address
# The first '-' is the remote username, if found
# The second '-' is the login username, if required
# [14/Aug/2017 13:10:46] is the access date and time
# "GET / HTTP/1.1" is the command sent to the web server:
# - The HTTP method (GET)
# - The resource requested (/, the top) - The HTTP version (HTTP/1.1)
# The final 200 is the HTTP status code returned by the web server

# the default port is 8000 but you can choose your own:

# $ python3 -m http.server 9999

# This Python-only server is best used for quick tests. It has no way to
# handle dynamic content. Stop it by killing its process (ctrl+c). For a busy
# website you would use a traditional web server such as Apache or nginx.


# Web Server Gateway Interface - WSGI
# -----------------------------------------------------------------------------
# In the early days of the Web, the Common Gateway Interface (CGI) was
# designed for clients to make web servers run external programs and return
# the results. The setup didn't scale well. To avoid startup delays, they
# began merging the language interpreter into the web server. Apache ran PHP
# within its mod_php module, Perl in mod_perl, and Python in mod_python.
# Code in these languages could then be executed within the Apache process
# itself rather than in external programs.

# Python web development made a leap with the definition of Web Server Gateway
# Interface (WSGI), a universal API between Python web applications and web
# servers. All of the Python web frameworks and web servers in the following
# examples use WSGI.


# Frameworks
# -----------------------------------------------------------------------------
# Web servers handle the HTTP and WSGI details, but you use web frameworks to
# actually write the Python code that powers the site.

# If you want to write a website in Python, there are many Python web
# frameworks (ie Django – Full-stack framework, Flask – microframework).
# A web framework handles, at a minimum, client requests and server responses.
# It might provide some or all of these features:

# – Routes: interpret URLs and find the server files or Python server code
# – Templates: merge server-side data into pages of HTML
# – Authentication and authorization: handle usernames, passwords, permissions
# – Sessions: maintain transient data storage during a user's visit to the site


# Bottle (microframework, doesn't include direct support for databases)
# -----------------------------------------------------------------------------
# Bottle consists of a single Python file, so it's very easy to try out, and
# to deploy later.

# $ pip3 install bottle
# http://http://bottlepy.org/docs/dev/

# Save as bottle1.py:

from bottle import route, run

@route('/')
def home():
    return "Nothing fancy, just a test"

run(host='localhost', port=9999)

# Bottle uses the route decorator to associate a URL with the following
# function; in this case, / (the home page) is handled by the home() function.
# Make Python run this server script: $ python3 bottle1.py

# in your web browser go to http://localhost:9999/

# The run() function executes bottle's built-in Python test web server. You
# don't need to use this for bottle programs, but it's useful for initial
# development and testing.

# Try making bottle return the contents of an HTML page. Save the following
# script as bottle2.py and run: $ python3 bottle2.py

from bottle import route, run, static_file

@route('/')
def main():
    return static_file('index.html', root='bottletest/')

# This will serve any/all additional files in your directory,
# including but not limited to css:

@route('/<filename:path>')
def send_static(filename):
    return static_file(filename, root='bottletest/')

run(host='localhost', port=9999)


# Flask (microframework, doesn't include direct support for databases)
# -----------------------------------------------------------------------------
# Flask supports many useful web development extensions such as facebook
# authentication and database integration. The Flask package includes the
# werkzeug WSGI library and jinja2 template library. Flask was built to be
# extendened. There are tonnes of third party flask extensions that allow you
# use flask and choose whatever additional tools you want.

# Functions direct users to a page or 'endpoint' are often called 'view
# functions' or routes, and are decorated with @app.route.

# flask1.py:

from flask import Flask

app = Flask(__name__)

@app.route('/')  # http://127.0.0.1:5000/
def home():
    return 'Home - Content goes here'

@app.route('/about')  # http://127.0.0.1:5000/about
def about():
    return 'About - content goes here'

app.run(debug=True)

# Flask's default directory home for static files is static, and URLs for
# files there also begin with /static. For example, a linked stylesheet
# should be like this: /static/css/desktop.css instead of css/desktop.css
# If you don't want to use the static directory, change the folder to '.'
# (current directory) and the URL prefix to '' (empty) to allow the URL / to
# map to a loose index.html. To confirm, in the following example, index.html
# should be located in a folder called 'static'

# flask2.py:
# -----------------------------------------------------------------------------

from flask import Flask

app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route('/')
def home():
    return app.send_static_file('index.html')  # must be in the static folder

app.run(port=9999, debug=True)

# In the run() function, the setting debug=True does a couple of things.
# It reloads the page in the browser if you change any of the Python code.
# If an HTTP error or an exception occurs in the server code, Flask returns
# a specially formatted page with useful details about what went wrong, and
# where. Even better, you can type some commands to see the values of variables
# in the server program. DO NOT set debug=True in production web servers.
# It exposes too much information about your server to potential intruders.


# flask3.py:
# -----------------------------------------------------------------------------
# You have several ways to pass values to an endpoint: either as part of the
# path, in URL parameters (for GET requests), or the request body
# (for POST requests).

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home/<thing>')
def home(thing):
    # flask_test.html must be located in the templates directory
    return render_template('flask_test.html', thing=thing)

app.run(port=9999, debug=True)

# This example uses jinja2 templates. In order for it to work, you need to
# create a directory called 'templates' and put flask_test.html in there.
# The thing=thing argument means to pass a variable named thing to the
# template, with the value of the string entered as an arg in the URL:
# http://localhost:9999/home/lovely

# Somewhere in flask_test.html type {{ thing }} to receive the value.

# templates/flask_test.html:
'''
<!DOCTYPE HTML>
<html lang="en">

<head>
<meta charset="UTF-8">
<title>Flask Example</title>
</head>

<body>
<h1>Hello {{ thing }} </h1>

</body>
</html>
'''


# flask4.py:
# -----------------------------------------------------------------------------

# This example allows you to pass a second argument. You will need to add
# {{ other }} somewhere in flask_test.html to receive the additional value.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home/<thing>/<other>')
def home(thing, other):
    return render_template('flask_test.html', thing=thing, other=other)

app.run(port=9999, debug=True)

# The URL would be http://localhost:9999/home/lovely/something


# flask5.py:
# -----------------------------------------------------------------------------

# You can also provide arguments as 'GET' parameters:

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/home')
def home():
    thing = request.args.get('thing')
    other = request.args.get('other')
    return render_template('flask_test.html', thing=thing, other=other)

app.run(port=9999, debug=True)

# When a GET command is used for a URL, any arguments are passed like:
# &key1=val1&key2=val2&...
# So our URL would be: http://localhost:9999/home?thing=lovely&other=blah


# flask6.py:
# -----------------------------------------------------------------------------

# You can also use the dictionary operator ** to pass multiple arguments
# to a template from a single dictionary/

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/echo/')
def echo():
    kwargs = {}
    kwargs['thing'] = request.args.get('thing')
    kwargs['other'] = request.args.get('other')
    return render_template('flask_test.html', **kwargs)

app.run(port=9999, debug=True)

# The **kwargs acts like thing=thing, other=other. It saves some typing if
# there are a lot of input arguments. Use the same url pattern as above.


# Other Frameworks
# -----------------------------------------------------------------------------
# If you want to build a website backed by a relational database, you can use
# bottle and flask with relational database modules, or use SQLAlchemy. But if
# you're building larger database-backed websites, and the database design
# doesn't change very often, it might be worth working with one of the larger
# Python web frameworks like:

# Django - the most popular, especially for large sites. It includes ORM code
# to create automatic web pages for the typical database CRUD functions
# (create, replace, update, delete). You don't have to use django's ORM if you
# prefer another, such as SQLAlchemy, or direct SQL queries.

# web2py - same as django, with a different style

# pyramid - grew from the earlier pylons project, similar to django in scope.

# turbogears - supports an ORM, many databases, and multiple template
# languages.

# wheezy.web - This is a newer framework optimized for performance. It was
# faster than the others in a recent test.
