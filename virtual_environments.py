'''Creating Virtual Environments'''

# A Virtual Environment, put simply, is an isolated working copy of Python that
# allows you to work on a specific project without worry of affecting other
# projects. It creates a folder which contains all the necessary executables to
# use the packages that a Python project would need.
#
# The basic problem being addressed is one of dependencies and versions, and
# indirectly permissions. Imagine you have an application that needs version 1
# of LibFoo, but another application requires version 2. How can you use both
# these applications? It’s easy to end up in a situation where you
# unintentionally upgrade an application that shouldn’t be.
#
# Or more generally, what if you want to install an application and leave it be?
# If an application works, any change in its libraries or the versions of those
# libraries can break the application. Also, what if you can’t install packages
# into the global site-packages directory? For instance, on a shared host.
#
# In these cases, venv (standard library) or virtualenv (independent library)
# can help. It creates an environment that has its own installation directories,
# that doesn’t share libraries with other virtual environments
# (and optionally doesn’t access the globally installed libraries either).

# https://docs.python.org/3/tutorial/venv.html

# -----------------------------------------------------------------------------
# Create a virtual environment
# -----------------------------------------------------------------------------
# To create a virtual environment, navigate to your project directory in the
# command line and enter (note 'test_env' is the folder name for the
# environment files, call it whatever you want):

# $ python3 -m venv test_env

# -----------------------------------------------------------------------------
# Install packages in the virtual environment
# -----------------------------------------------------------------------------
# from your same project directory where test_env lives:

# $ test_env/bin/pip3 install flask

# Alternatively, you can activate your virtual environment first, then pip3
# install as you would normally... see below

# -----------------------------------------------------------------------------
# Run your program in the virtual environment
# -----------------------------------------------------------------------------
# You can do one of two things. First, the long way:

# $ test_env/bin/python3 myscript.py

# Or, you can activate and deactivate your environment like:

# $ source test_env/bin/activate

# You should see the name of your environment (test_env) as the first item of
# the command line prompt. While in the activated state, you can pip3 install
# as you normally would (without the preceding test_env/bin/ as above).
# When you're done:

# $ deactivate

# -----------------------------------------------------------------------------
# Keep track of dequirements
# -----------------------------------------------------------------------------
# see package_management.py

# Depending on which method above you choose to run your environment,
# do one of the following:

# $ pip3 freeze > requirements.txt
# $ est_env/bin/pip3 freeze > requirements.txt
