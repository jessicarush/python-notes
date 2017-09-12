'''Package Management'''

# Installing packages ----------------------------------------------------------

# pip - you can install most packages this way
# package managers (ie brew) - work like pip but not restricted to python

# install the most recent version: pip3 install flask
# install a particular version: pip3 install flask==0.12.0
# install a minimum version: pip3 install flask>==0.9.0

# Yolk is a tool for obtaining information about installed Python packages and
# querying packages available on PyPI

# $ pip3 install yolk3k (just yolk for Python 2)

# List all installed Python packages
# yolk -l

# Checks to see if any installed Python packages have updates available.
# $ yolk -U

# If you want to see all versions available of something:
# $ yolk -V flask

# Requirements files -----------------------------------------------------------

# https://pip.pypa.io/en/latest/user_guide/#requirements-files

# Requirements files are files containing a list of items to be installed using
# pip install. Logically, a requirements file is just a list of pip install
# arguments placed in a file. Note that you should not rely on the items in the
# file being installed by pip in any particular order.

# Requirements files are used to hold the result from pip freeze for the
# purpose of achieving repeatable installations. In this case, your requirement
# file contains a pinned version of everything that was installed when pip
# freeze was run.

# To list all the packages:
# $ pip3 freeze

# To output the list to a file:
# $ pip3 freeze > requirements.txt

# To install from the list:
# $ pip3 install -r requirements.txt

# NOTE: pip freeze saves all packages in the environment including those that
# you don't use in your current project. (if you don't have virtualenv)

# NOTE: pip freeze only saves the packages that are installed with pip install
# in your environment.

# pipreqs

# pipreqs is used to generate a requirements.txt file for any project based on
# imports: $ pip3 install pipreqs - https://github.com/bndr/pipreqs

# Once pipreqs is installed:
# $ pipreqs path/to/project/directory

# That being said, the github page reports quite a few open issues.

# Dependencies -----------------------------------------------------------------

# This will list package dependencies:
# pip3 show flask | grep Requires

# There is a tool called pipdeptree that will show the whole family tree of
# dependences in your environment: $ pip3 install pipdeptree

# $ pipdeptree

# Requirements files are used to force pip to properly resolve dependencies. As
# it is now, pip doesn't have true dependency resolution, but instead simply
# uses the first specification it finds for a project. E.g. if pkg1 requires
# pkg3>=1.0 and pkg2 requires pkg3>=1.0,<=2.0, and if pkg1 is resolved first,
# pip will only use pkg3>=1.0, and could easily end up installing a version of
# pkg3 that conflicts with the needs of pkg2. To solve this problem, you can
# place pkg3>=1.0,<=2.0 (i.e. the correct specification) into your requirements
# file directly along with the other top level requirements. Like so:

# pkg1
# pkg2
# pkg3>=1.0,<=2.0

# More interesting tools for package management here:
# http://tech.marksblogg.com/better-python-package-management.html
