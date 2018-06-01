'''Structured Text Files'''

# In simple text files, the only level of organization is the line. Sometimes,
# you need more structure than that. You might want to save data for your
# program to use later, or send data to another program. There are many
# formats. Each of these can be read and written by at least one Python module:

# – A separator (or delimiter) character like tab '\t', comma ',', or vertical
#   bar '|'. This is an example of the comma-separated values (CSV) format.
# – < and > around tags. Examples include XML and HTML.
# – Punctuation. An example is JavaScript Object Notation (JSON).
# – Indentation. An example is YAML (.yaml, .yml)
# – Miscellaneous, such as configuration files for programs.


# CSV
# -----------------------------------------------------------------------------
# Delimited files are often used as an exchange format for spreadsheets and
# databases. You could read CSV files manually, a line at a time, splitting
# each line into fields at comma separators, and adding the results to data
# structures such as lists and dictionaries. But it's better to use the
# standard csv module, because parsing these files can be more complicated.

# Some have alternate delimiters besides a comma like '|' and '\t' (tab)
# Some have escape sequences. If the delimiter character can occur within a
# field, the entire field might be surrounded by quote characters or preceded
# by some escape character. Files have different line-ending characters. Unix
# uses '\n', Microsoft uses '\r \n', and Apple used to use '\r' but now '\n'.
# There can be column names in the first line.

import csv

singers = [
    ['Maynard', 'James Keenan'],
    ['Thom', 'York'],
    ['Alison', 'Mosshart'],
    ['Win', 'Butler'],
    ['Etta', 'James'],
    ]

with open('data/singers.csv', 'w') as fout:
    csv_out = csv.writer(fout)
    csv_out.writerows(singers)

# This creates a file 'singers.csv'. Try reading it back in:

with open('data/singers.csv', 'r') as fin:
    csv_in = csv.reader(fin)
    singers = [row for row in csv_in]  # list comprehension

# Using reader() and writer() with their default options, columns are
# separated by commas and rows by line feeds.

# DictReader()

# The data can be a list of dictionaries instead of a list of lists

with open('data/singers.csv', 'r') as fin:
    csv_in = csv.DictReader(fin, fieldnames=['first', 'last'])
    singers = [row for row in csv_in]

# DictWriter() will use a list of dictionaries to write the CSV file.

# writeheader() will write an initial line of column names to the CSV file.

singers = [
    {'first': 'Jack', 'last': 'White'},
    {'first': 'Eddie', 'last': 'Vedder'},
    {'first': 'David', 'last': 'Bowie'},
    {'first': 'Josh', 'last': 'Homme'},
    {'first': 'Annie', 'last': 'Lennox'},
    ]

with open('data/singers.csv', 'w') as fout:
    csv_out = csv.DictWriter(fout, ['first', 'last'])
    csv_out.writeheader()
    csv_out.writerows(singers)

# This time when reading back in with DictReader(), we'll omit the fieldnames
# argument. It will then use the values it finds on the first line instead.

with open('data/singers.csv', 'r') as fin:
    csv_in = csv.DictReader(fin)
    singers = [row for row in csv_in]


# XML
# -----------------------------------------------------------------------------
# practice.xml code for example below:

"""
<?xml version="1.0"?>
    <menu>
      <breakfast hours="7-11">
        <item price="$6.00">breakfast burritos</item>
        <item price="$4.00">pancakes</item>
      </breakfast>
      <lunch hours="11-3">
        <item price="$5.00">hamburger</item>
      </lunch>
      <dinner hours="3-10">
        <item price="8.00">spaghetti</item>
      </dinner>
    </menu>
"""

# A few things to keep in mind when working with XML: though much like HTML,
# the choice of where to put attributes, values and nested tags-is somewhat
# arbitrary. For instance, we could see the following:
# <item price="8.00">spaghetti</item>
# <item price="$8.00" food="spaghetti"/>

# XML is often used for data feeds and messages. It's flexibility has
# inspired multiple Python libraries that differ in approach and
# capabilities. The simplest way to parse XML in Python is by using:

# ElementTree:

# This will parse the menu.xml file and print some tags and attributes:

import xml.etree.ElementTree as et

tree = et.ElementTree(file='data/practice.xml')
root = tree.getroot()

print(root.tag)

for child in root:
    print('tag:', child.tag, 'attributes:', child.attrib)
    for grandchild in child:
        print('\ttag:', grandchild.tag, 'attributes:', grandchild.attrib)

print(len(root))    # number of menu sections
print(len(root[0])) # number of breakfast items

# ElementTree has many other ways of searching XML-derived data, modifying
# it, and even writing XML files. The ElementTree documentation can be found:
# https://docs.python.org/3.3/library/xml.etree.elementtree.html

# Other standard Python XML libraries include:
# xml.dom - This module loads the entire XML file into memory and lets you
#           access all the pieces equally.
# xml.sax - simple API for XML, parses XML on the fly, so it does not have
#           to load everything into memory at once. A good choice if you need
#           to process very large streams of XML.


# HTML
# -----------------------------------------------------------------------------
# The problem here is so much of it doesn't follow the HTML rules, which can
# make it difficult to parse. Also, much of HTML is intended more to format
# output than interchange data. More to come...


# JSON
# -----------------------------------------------------------------------------
# Has become a very popular data interchange format. The JSON format is a
# subset of JavaScript, and often legal Python syntax as well. Its close fit
# to Python makes it a good choice for data interchange among programs.

# The JSON module encodes (dumps) data to a JSON string and decodes (loads)
# a JSON string back to data.

# Here's a pythonic data structure to use:

menu = {
'breakfast': {
    'hours': '7-11',
    'items': {
        'breakfast burritos': '$6.00',
        'pancakes': '$4.00',
        'bagel': '$2.50',
        }
    },
'lunch': {
    'hours': '11-3',
    'items': {'sandwich': '$8.00'}
    },
'dinner': {
    'hours': '3-10',
    'items': {'spaghetti': '$9.00'}
    }
}

# Encode the data structure (menu) to a JSON string (menu_json) by using:
# dumps()

import json
menu_json = json.dumps(menu)

print(menu_json)

# Decode the JSON string back into a python data structure using:
# loads()

menu2 = json.loads(menu_json)

print(menu2)

# Note that the order of the keys may be different from when we started.

# You might get an exception while trying to encode or decode some objects,
# such as datetime. This can happen because the JSON standard does not define
# date or time types; it expects you to define how to handle them. You could
# convert the datetime to something JSON understands, such as a string or an
# epoch value. More to come...

# If the datetime value could occur in the middle of normally converted data
# types, it might be annoying to make these special conversions. You can
# modify how JSON is encoded by using inheritance. Python's JSON
# documentation gives an example of this for complex numbers, which can be
# modified for datetime:

import datetime
from time import mktime

now = datetime.datetime.utcnow()

class DTEncoder(json.JSONEncoder):
    def default(self, obj):
        # isinstance() checks the type of object:
        if isinstance(obj, datetime.datetime):
            return int(mktime(obj.timetuple()))
        # else we'll assume it's something the decoder knows:
        return json.JSONEncoder.default(self, obj)

json.dumps(now, cls=DTEncoder)

# The new class DTEncoder is a subclass, or child class, of JSONEncoder.
# We only need to override its default() method to add datetime handling.
# Inheritance ensures that everything else will be handled by the parent
# class. The isinstance() function checks whether the object obj is of the
# class datetime.datetime.

# For JSON and other structured text formats, you can load from a file into
# data structures without knowing anything about the structures ahead of
# time. Then, you can walk through the structures by using isinstance() and
# type-appropriate methods to examine their values. For example, if one of
# the items is a dictionary, you can extract contents through keys(),
# values(), and items().


# YAML
# -----------------------------------------------------------------------------
# practice.yaml code for example below:

"""
name:
  first: James
  last: McIntyre
dates:
  birth: 1828-05-25
  death: 1906-03-31
details:
  bearded: true
  themes: [cheese, Canada]
books:
  url: http://www.gutenberg.org/files/36068/36068-h/36068-h.htm
poems:
  - title: 'Motto'
    text: |
      Politeness, perseverance and pluck,
      To their possessor will bring good luck.
  - title: 'Canadian Charms'
    text: |
      Here industry is not in vain,
      For we have bounteous crops of grain,
      And you behold on every field
      Of grass and roots abundant yield,
      But after all the greatest charm
      Is the snug home upon the farm,
      And stone walls now keep cattle warm.
"""

# Similar to JSON, YAML has keys and values, but handles more data types
# such as dates and times. The standard Python library does not yet include
# YAML handling, so you need to install a third-party library named yaml to
# manipulate it. safe_load() converts a YAML string to Python data, whereas
# dump() does the opposite.

# Values such as true, false, on, and off are converted to Python Booleans.
# Integers and strings are converted to their Python equivalents. Other
# syntax creates lists and dictionaries:

import yaml

with open('data/practice.yaml', 'r') as fin:
    text = fin.read()
data = yaml.safe_load(text)

print(data['details'])
print(len(data['poems']))
print(data['poems'][1]['title'])

# PyYAML can load() Python objects from strings, and this is dangerous.
# Always Use safe_load() instead of load(), especially if you're importing
# YAML that you don't trust.


# Configuration files
# -----------------------------------------------------------------------------
# The standard configparser module handles Windows-style .ini files.
# Such files have sections of key = value definitions.

# practice.cfg code for example below:

"""
[english]
    greeting = Hello
[french]
    greeting = Bonjour
[files]
home = /usr/local
# simple interpolation:
bin = %(home)s/bin
"""

import configparser

cfg = configparser.ConfigParser()
cfg.read('data/practice.cfg')

print(cfg['french']['greeting'])


# Serialize with pickle
# -----------------------------------------------------------------------------
# see pickling.py


# Shelve module
# -----------------------------------------------------------------------------
# see shelve_module.py


# Spreadsheets
# -----------------------------------------------------------------------------
# Spreadsheets, notably Microsoft Excel, are widespread binary data formats.
# If you can save your spreadsheet to a CSV file, you can read it by using
# the standard csv module that was described earlier. If you have a binary
# xls file, xlrd is a third-party package for reading and writing.


# HDF5
# -----------------------------------------------------------------------------
# is a binary data format for multidimensional or hierarchical numeric data.
# It's used mainly in science, where fast random access to large datasets
# (gigabytes to terabytes) is a common requirement. It's best suited to WORM
# (write once/read many) applications for which database protection against
# conflicting writes is not needed. Consider HDF5 when you need to store and
# retrieve large amounts of data and are willing to consider something
# outside the box (as well as the usual database solutions). HDF5 modules:

# h5py is a full-featured low-level interface
# PyTables is a bit higher-level, with database-like features
