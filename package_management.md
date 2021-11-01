# Package Management

## Table of contents

<!-- toc -->

- [pip](#pip)
- [Installing & upgrading packages](#installing--upgrading-packages)
- [pip help](#pip-help)
- [Listing all packages](#listing-all-packages)
- [Requirements files](#requirements-files)
  * [pipreqs](#pipreqs)
- [Dependencies](#dependencies)
  * [pipdeptree](#pipdeptree)

<!-- tocstop -->

## pip

*`pip`* - you can install most python packages this way  
*package managers* - (ie brew) work like pip but not restricted to python

NOTE: Depending on how your python3 is installed (or whether you're working in virtual environment), you may need to say 'pip3' instead of 'pip'. TBH, The whole thing is a bit of a mess. Here's what I see my machine:
```
$ which pip
/usr/local/bin/pip

$ which pip2
/usr/local/bin/pip2

$ which pip3
/usr/local/bin/pip3
```
```
$ pip --version
pip 10.0.1 from /usr/local/lib/python2.7/site-packages/pip (python 2.7)

$ pip2 --version
pip 10.0.1 from /usr/local/lib/python2.7/site-packages/pip (python 2.7)

$ pip3 --version
pip 10.0.1 from /usr/local/lib/python3.7/site-packages/pip (python 3.7)
```

to upgrade pip (the order matters):
```
$ pip3 install --upgrade pip
$ pip2 install --upgrade pip
$ pip install --upgrade pip
```
>Note: the pip command belongs to whichever Python installed pip last; this is unavoidable if python and python3 install scripts to the same prefix. See [pypa/pip#2973](https://github.com/pypa/pip/issues/2973). Run python -m pip -U --force-reinstall pip to force reinstalling pip on python2 which will rewrite the script again.

When using a virtual environment, you don't have to worry so much:

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install --upgrade pip
```


## Installing & upgrading packages

install the most recent version of something:
```
$ pip install flask
```
install a particular version:
```
$ pip install flask==0.12.0
```
install a minimum version:
```
$ pip install flask>==0.9.0
```
upgrade an already installed package:
```
$ pip install --upgrade flask
```
As of pip version 1.3 you can run the following command to check if any of
your packages can be updated. If you're in a virtual environment, add the `--local` option.
```
$ pip list --outdated
$ pip list --outdated --local
```
There's another library that actually format's this list even better:
```
$ pip install pip-check
$ pip-check
```
To see where a package is installed:
```
$ pip show flask
```

NOTE: Sometimes I've seen this recommended for installing modules:
```
$ python3 -m pip install PyYaml
```
One guy said the '-m' is an argument that allows python to locate modules
for execution as scripts. I get the sense that it's more of a Windows thing.


## pip help

To access pip's help documentation you can type `pip help` in the command line. You can also follow that with a specfic command you want help with, for example:

```bash
pip help install
```

This will give you all sorts of useful stuff including what all the various flags mean.


## Listing all packages

Yolk is a tool for obtaining information about installed Python packages and querying packages available on PyPI.
```
$ pip install yolk3k
```
List all installed Python packages using yolk:
```
$ yolk -l
```
Check to see if any installed Python packages have updates available:
```
$ yolk -U
```
If you want to see all versions available of something:
```
$ yolk -V flask
```
NOTE: Initially with the above two commands (which attempt to contact PyPi), I was getting the following error:
```
<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed...>
```
The solution was to run (double-click) the `Install Certificates.command`
found in: `Applications/Python 3.6/`


## Requirements files
<https://pip.pypa.io/en/latest/user_guide/#requirements-files>

Requirements files are files containing a list of items to be installed using pip install. Logically, a requirements file is just a list of pip install arguments placed in a file. Note that you should not rely on the items in the file being installed by pip in any particular order.

Requirements files are used to hold the result from pip freeze for the purpose of achieving repeatable installations. Your requirement file contains a pinned version of everything that was installed when pip freeze was run.

To list all the installed packages:
```
$ pip freeze
```
To output the list to a file:
```
$ pip freeze > requirements.txt
```
To install from the file:
```
$ pip install -r requirements.txt
```
NOTE: pip freeze saves all packages in the environment including those that you don't use in your current project.

NOTE: pip freeze only lists the packages that were installed using pip in your environment. If you installed other packages in a different way, or you need to add something that's required for the production server, just add in manually to the .txt file.

### pipreqs

pipreqs is a package used to generate a requirements.txt file for any project based on imports.
```
$ pip3 install pipreqs - https://github.com/bndr/pipreqs
```
Once pipreqs is installed:
```
$ pipreqs path/to/project/directory
```
That being said, the github page reports quite a few open issues. You're better off starting with a clean virtual environment and using pip to install everything you need as you go, thereby ensuring your pip freeze will be accurate and up-to-date.

## Dependencies

This will list all package dependencies:
```
$ pip show flask | grep Requires
Requires: click, Jinja2, Werkzeug, itsdangerous
```

### pipdeptree

This package pipdeptree will show the whole family tree of dependences in your environment.
```
$ pip install pipdeptree
```
Just run the command:
```
$ pipdeptree
```

Requirements files are used to force pip to properly resolve dependencies. As it is now, pip doesn't have true dependency resolution, but instead simply uses the first specification it finds for a project. For example, if pkg1 requires pkg3 >=1.0 and pkg2 requires pkg3 >=1.0, <=2.0, and if pkg1 is resolved first, pip will only use pkg3 >=1.0, and could easily end up installing a version of pkg3 that conflicts with the needs of pkg2. To solve this problem, you can place pkg3 >=1.0, <=2.0 (the correct specification) into your requirements file directly along with the other top level requirements. Like so:
```
pkg1
pkg2
pkg3>=1.0,<=2.0
```
More interesting tools for package management here:  
<http://tech.marksblogg.com/better-python-package-management.html>
