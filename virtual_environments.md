# Virtual Environments

A Virtual Environment, put simply, is an isolated working copy of Python that allows you to work on a specific project without affecting any other projects. It creates a directory which contains all the necessary executables to use the packages that a Python project would need.

The basic problem being addressed is one of dependencies and versions, and indirectly permissions. Imagine you have an application that needs version 1 of LibFoo, but another application requires version 2. How can you use both these applications? It’s easy to end up in a situation where you unintentionally upgrade an application that shouldn’t be.

More generally, what if you want to install an application and leave it be? If an application works, any change in its libraries or the versions of those libraries can break the application. Also, what if you can’t install packages into the global site-packages directory? For instance, on a shared host.

In these cases, venv (standard library) or virtualenv (independent library) can help. Both create an environment that has its own installation directories, that don’t share libraries with other virtual environments (and optionally don’t access the globally installed libraries either).

<https://docs.python.org/3/tutorial/venv.html>


## Create a virtual environment

To create a virtual environment, navigate to your project directory in the command line and enter the following. Note: the *first* 'venv' is the name of the module (I'm choosing to use the one from Python's standard library), the *second* 'venv' is the directory name for all the environment files... call it whatever you want):

```
$ python3 -m venv test_venv
```

Next, install packages in the virtual environment. There are two ways to do this. One, from the same project directory where venv lives:

```
$ venv/bin/pip3 install flask
```

Alternatively, you can *activate* your virtual environment first, then pip install as you would normally:

```
$ source venv/bin/activate
(venv) $ pip install flask
```

You should see the name of your environment (venv) at the start of the command line prompt. While in the activated state, you can pip install as you normally would (without the preceding venv/bin/ as above). We don't to specify pip3 as our environment only contains pip3 and python3 anyways.

## Run your program in the virtual environment

Again, you can do one of two things. First, the long way:

```
$ venv/bin/python3 myscript.py
```

or, you can activate your environment as above:

```
$ source venv/bin/activate
(venv) $ python myscript.py
```

When you're finished working in the project, deactivate the environment:

```
(venv) $ deactivate
```

## Keep track of requirements

see package_management.py

# Depending on which method you prefer, do one of the following:

```
$ venv/bin/pip3 freeze > requirements.txt
(venv) $ pip freeze > requirements.txt
```
