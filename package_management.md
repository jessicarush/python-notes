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

NOTE: Usually, pip is automatically installed if you installed Python from python.org or you're working in virtual environment. You can see where the pip command is looking, for example: 

A Python installation on mac os might look like:

```bash
$ which pip
/usr/local/bin/pip
```

If using [pyenv](https://github.com/pyenv/pyenv), the path may look like this:

```bash
$ which pip
/Users/jessicarush/.pyenv/shims/pip
```

If activating a virtual environment, it should point to the `venv` directory in our project folder:

```bash
$ source venv/bin/activate
$ which pip
/Users/jessicarush/Documents/Coding/Python/github_python/venv/bin/pip
```

You can check the path and the version with `pip --version`:

```bash
$ pip --version
pip 21.2.4 from /Users/jessicarush/.pyenv/versions/3.10.2/lib/python3.10/site-packages/pip (python 3.10)
```

to upgrade pip (the order matters):

```bash
$ pip install --upgrade pip
```


## Installing & upgrading packages

Install the most recent version of something:

```bash
$ pip install flask
```

Upgrade an already installed package:

```bash
$ pip install --upgrade flask
```

Install a particular version:

```bash
$ pip install flask==2.0.3
```

Install a minimum version:

```bash
$ pip install flask>==0.9.0
```

To see where a package is installed:

```bash
$ pip show flask
```

Run the following command to check if any of your packages can be updated.

```bash
$ pip list --outdated
```

There's another library that does this way better. It shows which packages have a minor vs major updates and formats the output really nice:

```bash
$ pip install pip-check
$ pip-check
```


## pip help

To access pip's help documentation you can type `pip help` in the command line. You can also follow that with a specific command you want help with, for example:

```bash
pip help install
```

This will give you all sorts of useful stuff including what all the various flags mean.


## Requirements files

[Requirements files](https://pip.pypa.io/en/latest/user_guide/#requirements-files) are files containing a list of packages to be installed using pip install. Logically, a requirements file is just a list of pip install arguments placed in a file. Note that you should not rely on the items in the file being installed by pip in any particular order.

Requirements files are used to hold the result from `pip freeze` for the purpose of achieving repeatable installations. Your requirement file contains a pinned version of everything that was installed when pip freeze was run.

To list all the installed packages:

```bash
$ pip freeze
```

To output the list to a file:

```bash
$ pip freeze > requirements.txt
```

To install from the file:

```bash
$ pip install -r requirements.txt
```

NOTE: `pip freeze` saves all packages that are currently installed in the environment.

NOTE: `pip freeze` only lists the packages that were installed using pip in your environment. If you installed other packages in a different way, or you need to add something that's required for the production server, just add it manually to the `requirements.txt` file.

### pipreqs

[pipreqs](https://github.com/bndr/pipreqs) is a package used to generate a `requirements.txt` file for any project based on imports.

```bash
$ pip install pipreqs
```

Once pipreqs is installed:

```bash
$ pipreqs path/to/project/directory
```

That being said, the github page reports quite a few open issues. You're better off starting with a clean virtual environment and using pip to install everything you need as you go, thereby ensuring your pip freeze will be accurate and up-to-date.


## Dependencies

This will list all package dependencies:

```bash
$ pip show flask | grep Requires
Requires: click, Jinja2, Werkzeug, itsdangerous
```

### pipdeptree

The [pipdeptree](https://github.com/naiquevin/pipdeptree) package will show the whole family tree of dependencies in your environment.

```bash
$ pip install pipdeptree
```

Just run the command:

```bash
$ pipdeptree
```

Requirements files are used to force pip to properly resolve dependencies. As it is now, pip doesn't have true dependency resolution, but instead simply uses the first specification it finds for a project. For example, if pkg1 requires pkg3 >=1.0 and pkg2 requires pkg3 >=1.0, <=2.0, and if pkg1 is resolved first, pip will only use pkg3 >=1.0, and could easily end up installing a version of pkg3 that conflicts with the needs of pkg2. To solve this problem, you can place pkg3 >=1.0, <=2.0 (the correct specification) into your requirements file directly along with the other top level requirements. Like so:

```text
pkg1
pkg2
pkg3>=1.0,<=2.0
```
