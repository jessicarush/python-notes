# Relational Databases

# DB-API is Python's standard API (application programming interface) for
# accessing relational databases. It's main functions:

# connect() - make a connection to the database.
# can include args like username, password, server address etc.

# cursor() - create a cursor object to manage queries

# execute(), executemany() - run one or more SQL command against the database

# fetchone(), fetchmany(), fetchall() - get the result from execute()

# SQLite

# A good, light, open source relational database. It’s implemented as a standard
# Python library, and stores databases in normal files. It isn’t as full-featured
# as MySQL, but it does support SQL, and manages multiple simultaneous users. Web
# browsers, smart phones, and other apps use SQLite as an embedded database.

# This example creates a table called inventory in a file called practice.db
# things is a variable length string and the primary key (a column or group of
# columns whose data values must be unique in the table).
# count is an integer count of each thing
# cost is a dollar amount of each thing
# the ALL CAPS sections are the SQL commands

import sqlite3

conn = sqlite3.connect('practice.db') # creates the file if it doesn't exist
curs = conn.cursor()
#curs.execute('''CREATE TABLE inventory
#(things VARCHAR(20) PRIMARY KEY,
# count INT,
# cost FLOAT)''')

# add things to inventory:

curs.execute('INSERT INTO inventory VALUES("pencils", 100, 0.5)')

# a safer way to insert data , using a placeholder:

ins = 'INSERT INTO inventory (things, count, cost) VALUES(?, ?, ?)'
curs.execute(ins, ('erasers', 85, 0.25))
curs.execute(ins, ('widgets', 2, 10.0))

# retrieve items (as a list) from the database:

curs.execute('SELECT * FROM inventory')
rows = curs.fetchall()
print(rows)

# retrieve items from the database and order them by their cost:

curs.execute('SELECT * FROM inventory ORDER BY cost')
rows = curs.fetchall()
print(rows)

# by their cost descending order:

curs.execute('SELECT * FROM inventory ORDER BY cost DESC')
rows = curs.fetchall()
print(rows)

# retrieve item with the highest count:

curs.execute('''SELECT * FROM inventory WHERE
count = (SELECT MAX(count) FROM inventory)''')
rows = curs.fetchall()
print(rows)

# when finished, you need to close any connections and cursors:

curs.close()
conn.close()

# MySQL

# Unlike SQLite, it’s an actual server, so clients can access it from different
# devices across the network. MysqlDB is the most popular driver, but hasn't
# yet been ported to Python 3. You can use these to access MySQL from Python:

# MySQL Connector - http://bit.ly/mysql-cpdg
# PYMySQL - https://github.com/petehunt/ PyMySQL/
# oursql - http://pythonhosted.org/oursql/

# PostgreSQL

# is a full-featured open source relational database, in many ways more
# advanced than MySQL. Pyhton drivers for PostgreSQL:

# psycopg2 - http://initd.org/psycopg/
# py-postgresql - http://python.projects.pgfoundry.org/

# SQLAlchemy

# DB-API takes you only so far. Each database implements a particular dialect
# reflecting its features and philosophy. Many libraries try to bridge these
# differences. The most popular cross-database Python library is SQLAlchemy.

# you don’t need to import the driver; the initial connection string you
# provide to SQLAlchemy will determine it:

# dialect + driver :// user : password @ host : port / dbname

# dialect - the database type
# driver - the particular driver you want to use for that database
# user and password - our database authentication strings
# host and port - the database server’s location
# (: port is only needed if it’s not the standard one for this server)
# dbname - the database to initially connect to on the server

# SQLite skips the host, port, user, and password.

# The dbname informs SQLite as to what file to use to store your database.
# If you omit the dbname, SQLite builds a database in memory. If the dbname
# starts with a slash (/), it’s an absolute filename on your computer
# Otherwise, it’s relative to your current directory.

# The Engine Layer

import sqlalchemy as sa

# Connect to the database and create the storage for it in memory:

conn = sa.create_engine('sqlite://')

# Create a database called inventory with three columns:

conn.execute('''CREATE TABLE inventory
(things VARCHAR(20) PRIMARY KEY,
 count INT,
 cost FLOAT)''')

# Running conn.execute() returns a SQLAlchemy object called a ResultProxy

# Insert data into the empty table:

ins = 'INSERT INTO inventory (things, count, cost) VALUES (?, ?, ?)'
conn.execute(ins, 'balls', 20, 0.50)
conn.execute(ins, 'spoons', 62, 1.50)
conn.execute(ins, 'rocks', 454, 0.10)

# Ask the database for everything:

rows = conn.execute('SELECT * FROM inventory')
print(rows)
for row in rows:
    print(row)

# This was pretty much the same as DB-API except we have the added benefit of
# being able to change the connection string to port this code to another type
# of database.

# SQL Expression Language

# SQLAlchemy’s SQL Expression Language introduces functions to create the SQL
# for various operations. The Expression Language handles more of the SQL
# dialect differences. Here’s how to create and populate the a table using
# some of the Expression Language instead of SQL:

import sqlalchemy as sa
conn = sa.create_engine('sqlite://')

meta = sa.MetaData()
inventory = sa.Table('inventory', meta,
    sa.Column('things', sa.String, primary_key=True),
    sa.Column('count', sa.Integer),
    sa.Column('cost', sa.Float)
    )
meta.create_all(conn)

# Note: the inventory object is connection between SQL and Python

conn.execute(inventory.insert(('socks', 2, 10.0)))
conn.execute(inventory.insert(('paperclips', 1000, 0.05)))
conn.execute(inventory.insert(('snow globes', 50, 5.0)))

# inventory.select() selects everything from the table (represented by the
# inventory object), as SELECT * FROM would do in plain SQL:

result = conn.execute(inventory.select())

rows = result.fetchall()
print(rows)

# Object-Relational Mapper

# At the top layer of SQLAlchemy, the Object-Relational Mapper (ORM) uses the
# SQL Expression Language but tries to make the actual database mechanisms
# invisible. You define classes, and the ORM handles how to get their data in
# and out of the database.

# This time we'll define an inventory class and hook it into the ORM. The
# initial import is the same, but we add something extra after it:

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

# make the connection:

conn = sa.create_engine('sqlite:///inventory2.db')

# define the class and associate its attributes with table columns:

Base = declarative_base()

class Inventory(Base):
    __tablename__ = 'inventory'
    things = sa.Column('things', sa.String, primary_key=True)
    count = sa.Column('count', sa.Integer)
    cost = sa.Column('cost', sa.Float)
    def __init__(self, things, count, cost):
        self.things = things
        self.count = count
        self.cost = cost
    def __repr__(self):
        return "<Inventory({}, {}, {})>".format(self.things, self.count, self.cost)

# the following line creates the database and table:

Base.metadata.create_all(conn)

# insert data by creating Python objects. The ORM manages these internally:

first = Inventory('shoe laces', 12, 1.0)
second = Inventory('mascara', 24, 12.0)
third = Inventory('peanuts', 1200, 6.99)

# get the ORM to take us to SQL. create a session to talk to the database:

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=conn)
session = Session()

# within the session, write the three objects to the database.
# The add() function adds one object, and add_all() adds a list:

session.add(first)
session.add_all([second, third])

# force everything to complete:

session.commit()

# You can use the command line to check it:
# $ sqlite3 inventory2.db
# .tables
# select * from inventory;

# Summary

# This was a brief overview to help decide which of the following levels would
# best fit your needs:

# • Plain DB-API, as in the earlier SQLite section
# • The SQLAlchemy engine room
# • The SQLAlchemy Expression Language
# • The SQLAlchemy ORM
