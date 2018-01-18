'''Relational Databases'''

# In relational databases, data is stored in table rows and columns, with a row
# corresponding to a single record and the columns representing the fields that
# make up a the record such as name, address, phone number, date of birth.
# Traditional databases typically use Structured Query Language (SQL) to query
# and update the data. FYI there are plenty of NoSQL databases as well (often
# used for "Big Data") - see noSQL_datastores.py

# -----------------------------------------------------------------------------
# Terminology:
# -----------------------------------------------------------------------------
# Database Dictionary
#    – a comprehensive list of the structure and types of data in the database.
# Table
#    – a collection of related data held in a database
# Field
#    – the basic unit of data in a table. Fields have names and a type (int,
#      string, etc). The type indicates what kind of data should be stored in
#      that field. Some fields can even hold images and audio files. These
#      fields are often called Blobs (binary large objects). Note that SQLite
#      field types don't actually restrict what kind of data can go in.
# Column
#    – another name for a field. The difference between a spreadsheet column &
#      a database column, is that the database column refers to a single entry.
# Row (record)
#    – a single set of data containing all the columns in the table
# Key
#    – a key in a table is indexed, so searches (and joins) are much faster.
# Primary key
#    – a column whose values must be unique in the table. If you try to insert
#      a primary key that's already being used in the table, you will get an
#      error: UNIQUE constraint failed: table.column. Another interesting bit:
#      If you set your primary key type to integer (an ID number), you
#      don't need to enter the integer when inserting a new record, it will
#      automatically use the next number. That being said... it has to be
#      INTEGER and not INT. See https://www.sqlite.org/datatype3.html 
# Unique
#    – A unique constraint is similar to a primary key constraint, except that
#      a single table may have any number of unique columns. For each unique
#      constraint on the table, each row must contain a unique combination of
#      values in the columns.
# Flat File database
#    – stored all data in a single table (not so great)
# Normalization
#    – the process of organizing tables and columns to remove redundant, or
#      irrelevant information and improve data integrity. The idea is to use
#      one or more columns to link tables together.
# View
#    – a way of looking at the data in a format similar to a table. The data
#      can be a selection of rows and columns from more than one joined table.
#      In some databases you can actually modify data in the view and it will
#      update the corresponding tables, but not in SQLite.
# Not Null
#    – an option that says a particular field is required. Note that Integer
#      Primary Key columns automatically have a not null.

# What makes a database relational, is that you can have many tables that are
# linked together. For example, a business might have a table of vendors thats
# linked to a table of invoices.

# -----------------------------------------------------------------------------
# DB-API
# -----------------------------------------------------------------------------
# DB-API is Python's standard API (application programming interface) for
# accessing relational databases. It's main functions:

# connect()
#   – make a connection to the database. can include args like username,
#     password, server address etc.
# cursor()
#   – create a cursor object to manage queries
# execute(), executemany()
#   – run one or more SQL commands against the database
# fetchone(), fetchmany(), fetchall()
#   – get the result from execute()

# -----------------------------------------------------------------------------
# SQLite
# -----------------------------------------------------------------------------
# A good, light, open source relational database. It's implemented as a
# standard Python library, and stores databases in normal files. It isn't as
# full-featured as MySQL, but it does support SQL, and manages multiple
# simultaneous users. Web browsers, smart phones, and other apps use SQLite as
# an embedded database. It's completely self contained and doesn't need a
# separate server to run on.

# https://sqlite.org/mostdeployed.html

# This example creates a table called inventory in a file called practice.db.
# things - is a variable length string and the primary key
# count - is an integer count of each thing
# cost - is a dollar amount of each thing
# the ALL CAPS sections are the SQL commands

import sqlite3

conn = sqlite3.connect('practice.db') # creates the file if it doesn't exist
curs = conn.cursor()

curs.execute('''CREATE TABLE IF NOT EXISTS inventory
                (things VARCHAR(20) PRIMARY KEY,
                count INTEGER,
                cost FLOAT)''')

# add things to inventory:

curs.execute('INSERT INTO inventory VALUES("pencils", 100, 0.5)')

# a safer way to insert data, using placeholders... This is a common method
# for protecting against SQL injection:

ins = 'INSERT INTO inventory(things, count, cost) VALUES(?, ?, ?)'
curs.execute(ins, ('erasers', 85, 0.25))
curs.execute(ins, ('widgets', 2, 10.0))

# retrieve items (as a list) from the database:

curs.execute('SELECT * FROM inventory')
rows = curs.fetchall()
print(rows)
# [('pencils', 100, 0.5), ('erasers', 85, 0.25), ('widgets', 2, 10.0)]

# retrieve items from the database and order them by their cost:

curs.execute('SELECT * FROM inventory ORDER BY cost')
rows = curs.fetchall()
print(rows)
# [('erasers', 85, 0.25), ('pencils', 100, 0.5), ('widgets', 2, 10.0)]

# by their cost descending order:

curs.execute('SELECT * FROM inventory ORDER BY cost DESC')
rows = curs.fetchall()
print(rows)
# [('widgets', 2, 10.0), ('pencils', 100, 0.5), ('erasers', 85, 0.25)]

# retrieve item with the highest count:

curs.execute('''SELECT * FROM inventory WHERE
  count = (SELECT MAX(count) FROM inventory)''')
rows = curs.fetchall()
print(rows)  # [('pencils', 100, 0.5)]

# when finished, you need to commit any changes and close any connections
# and cursors:

conn.commit()
curs.close()
conn.close()

# NOTE when selecting columns from a table, they will automatically be sorted
# by their primary key. That being said, the *actual* order of the records in
# the database is undefined. You can use the ORDER BY clause to order it by
# another column as demonstrated above.

# -----------------------------------------------------------------------------
# SQLite Datatypes
# -----------------------------------------------------------------------------
# https://www.sqlite.org/datatype3.html

# Note there are 5 main data types in sqlite3:
# NULL, INTEGER, REAL, TEXT, BLOB

# The link above also lists the other acceptable names for these data types.
# For example FLOAT is actual REAL.

# -----------------------------------------------------------------------------
# SQLite Commands
# -----------------------------------------------------------------------------
# $ sqlite3 contacts.db (creates the database if it doesn't exist)
# $ .help
# $ .headers on
# $ .tables
# $ .schema
# $ .dump (dump the entire database or table into a text file)
# $ .backup contacts_backup.db
# $ .restore contacts_backup.db
# $ .quit
# CREATE TABLE contacts (name text, phone integer, email text);
# CREATE TABLE IF NOT EXISTS ...
# INSERT INTO contacts (name, email) VALUES('Bob', 'mail@me.com');
# INSERT INTO contacts VALUES('Rick', 3425, 'rick@me.com');
#    – with this method you must provide all three values
# SELECT * FROM contacts;
# SELECT name, email FROM contacts;
# SELECT * FROM contacts WHERE name='Rick';
# SELECT * FROM contacts WHERE name LIKE 'Ri%';
#    – WHERE wildcards can be written like '%abc', 'abc%', or '%abc%'
# SELECT * FROM contacts ORDER BY name;
# SELECT * FROM contacts ORDER BY name COLLATE NOCASE;
#    – ignores case when sorting
# SELECT * FROM contacts ORDER BY name COLLATE NOCASE DESC
#    – DESC for descending, ASC for ascending
# SELECT * FROM albums ORDER BY artist, name;
#    – order first by one column, then by another
# SELECT email FROM contacts WHERE name='Morty';
# SELECT count(*) FROM contacts;
#    – returns the number of records
# SELECT count(title) FROM artist_list WHERE artist = 'Aerosmith';
# SELECT DISTINCT title FROM artist_list WHERE artist='Pixies' ORDER BY title;
#    – DISTINCT omits any duplicates from the resulting output
# SELECT count(DISTINCT title) FROM artist_list WHERE artist='Pixies';
# UPDATE contacts SET email='Danger! this will replace ALL email fields'
# UPDATE contacts SET email='updates the one record' WHERE name='Bob';
# DELETE FROM contacts WHERE name='Bob';
# DELETE FROM inventory WHERE quantity < 5
#    – note, all operators work here
# DROP VIEW artist_list;
#    – deletes the view (views explained below)
# DROP TABLE artists;
#    – deletes a table (be careful!)
# ALTER TABLE contacts RENAME TO customers;
# ALTER TABLE contacts ADD COLUMN newcol TEXT;

# -----------------------------------------------------------------------------
# JOIN (a column in one table corresponds to a column in another)
# -----------------------------------------------------------------------------
# For the following examples imagine this schema:

'''
CREATE TABLE songs
  (_id INTEGER PRIMARY KEY, track INTEGER, title TEXT NOT NULL, album INTEGER);
CREATE TABLE albums
  (_id INTEGER PRIMARY KEY, name TEXT NOT NULL, artist INTEGER);
CREATE TABLE artists (_id INTEGER PRIMARY KEY, name TEXT NOT NULL);
'''

# SELECT songs.title, albums.name
# FROM songs JOIN albums ON songs.album = albums._id;

#    displays the title column from the songs table and the name column from
#    the albums table by linking the songs album column to the album _id
#    column. JOIN is actually an INNER JOIN. The following is the same:

# SELECT songs.title, albums.name
# FROM songs INNER JOIN albums ON songs.album = albums._id;

# SELECT albums.name, songs.track, songs.title
# FROM songs INNER JOIN albums ON songs.album = albums._id
# ORDER BY albums.name, songs.track;

# SELECT artists.name, albums.name
# FROM artists INNER JOIN albums ON artists._id = albums.artist
# ORDER BY artists.name, albums.name;

# SELECT artists.name, albums.name, songs.track, songs.title
# FROM songs INNER JOIN albums ON songs.album = albums._id
# INNER JOIN artists ON albums.artist = artists._id
# ORDER BY artists.name, albums.name, songs.track;

# NOTE the ordering of the keyword commands must go like this:

# SELECT artists.name, albums.name, songs.track, songs.title
# FROM songs INNER JOIN albums ON songs.album = albums._id
# INNER JOIN artists ON albums.artist = artists._id
# WHERE artists.name = 'Rolling Stones'
# ORDER BY artists.name, albums.name, songs.track;

# WHERE wildcards: (Where a name contains something)

# SELECT artists.name, albums.name, songs.track, songs.title
# FROM songs INNER JOIN albums ON songs.album = albums._id
# INNER JOIN artists ON albums.artist = artists._id
# WHERE albums.name LIKE '%Live%'
# ORDER BY artists.name, albums.name, songs.track;

# Select the duplicate album names:

# SELECT albums.name, COUNT(albums.name) AS num_albums
# FROM albums GROUP BY albums.name HAVING num_albums > 1

# Select all the details of the duplicate album names:

# SELECT artists._id, artists.name, albums.name FROM artists
# INNER JOIN albums ON albums.artist = artists._id
# WHERE albums.name IN (SELECT albums.name FROM albums
# GROUP BY albums.name HAVING COUNT(albums.name) > 1)
# ORDER BY albums.name, artists.name

# -----------------------------------------------------------------------------
# VIEWS: (save a SELECT query)
# -----------------------------------------------------------------------------
# CREATE VIEW artist_list AS
# SELECT artists.name, albums.name, songs.track, songs.title
# FROM songs INNER JOIN albums ON songs.album = albums._id
# INNER JOIN artists ON albums.artist = artists._id
# ORDER BY artists.name, albums.name, songs.track;

# If you check the .schema, you will see this view is now stored in the db
# The view can now be queried like a table (reminder: you can't change any of
# the data in SQLite views)

# SELECT * FROM artist_list;

# If you try to SELECT a name though, you'll have difficulty as two columns are
# now called name (actually one has been renamed name:1). Since we are not
# actually pointing to the original table, album.name will no longer work
# because the is actually the view artist_list. What you should do is rename
# the columns where needed so there's no conflict (like import random as ran).

# SELECT songs.title FROM artist_list WHERE albums.name = 'Forbidden';
#    – Will NOT work

# Recreate the view like this:

# CREATE VIEW artist_list AS
# SELECT artists.name AS artist, albums.name AS album, songs.track, songs.title
# FROM songs INNER JOIN albums ON songs.album = albums._id
# INNER JOIN artists ON albums.artist = artists._id
# ORDER BY artists.name, albums.name, songs.track;

# SELECT title FROM artist_list WHERE album = 'Forbidden';
#    – Now this works

# -----------------------------------------------------------------------------
# SQLite Review 1
# -----------------------------------------------------------------------------
import sqlite3


conn = sqlite3.connect('contacts.sqlite')
curs = conn.cursor()

conn.execute('''CREATE TABLE IF NOT EXISTS contacts
                (name TEXT, phone INTEGER, email TEXT)''')
conn.execute('''INSERT INTO contacts(name, phone, email)
                VALUES("Rick", 4362, "rick@email.com")''')
conn.execute('INSERT INTO contacts VALUES("Morty", 7395, "morty@email.com")')

# database cursors are generators and they are iterable!
curs.execute('SELECT * FROM contacts')
for row in cursor:
    print(row)

# unpack the tuples if you want:
curs.execute('SELECT * FROM contacts')
for name, phone, email in cursor:
    print(name, '–', phone, '–', email)
    print('-' * 20)

# You can dump into a variable to use (not so good with a big db)
curs.execute('SELECT * FROM contacts')
stuff = cursor.fetchall()

print(stuff)
for name, phone, email in stuff:
    print(name, '\n', phone, '\n', email)
    print('-' * 20)

# You can also fetch one at a time:
curs.execute('SELECT * FROM contacts')
one = curs.fetchone()
two = curs.fetchone()
three = curs.fetchone()

print(one)
print(two)
print(three)

curs.close()
conn.commit()
conn.close()

# -----------------------------------------------------------------------------
# SQLite Review 2
# -----------------------------------------------------------------------------
import sqlite3

# Note: INTEGER PRIMARY KEYS do not need to be given a value. See (NULL, ?, ?).
# Note: Feed multiple tuples into a query with executemany()

conn = sqlite3.connect('data.db')
curs = conn.cursor()

table = '''CREATE TABLE IF NOT EXISTS users
           (id INTEGER PRIMARY KEY,
           username TEXT,
           password TEXT)'''
curs.execute(table)

user = ('bob', 'password')
insert_query = 'INSERT INTO users VALUES(NULL, ?, ?)'
curs.execute(insert_query, user)

users =[('rick', 'password'), ('morty', 'password')]
curs.executemany(insert_query, users)

select_query = 'SELECT * FROM users'
for row in curs.execute(select_query):
    print(row)

conn.commit()
curs.close()
conn.close()

# -----------------------------------------------------------------------------
# Cursor or no cursor
# -----------------------------------------------------------------------------
# shortcut: you actually don't need a cursor if you just want to run a query
# The execute method creates a cursor behind the scenes when used with SELECT

import sqlite3

conn = sqlite3.connect('contacts.sqlite')

for row in conn.execute('SELECT * FROM contacts'):
    print(row)

# tuple unpacking again
for name, phone, email in conn.execute('SELECT * FROM contacts'):
    print(name)
    print(phone)
    print(email)
    print('-' * 20)

# cursors can be helpful though. For example they have a row count property so
# we can see how many rows were affected by the previous SQL statement.

update_sql = 'UPDATE contacts SET email = "blerk" WHERE name = "Rick"'
update_cursor = conn.cursor()
update_cursor.execute(update_sql)

print('{} rows updated'.format(update_cursor.rowcount))

# In addition, when you use cursors, you can commit based on that cursor.
# This method of committing can be helpful when you're doing all this in a
# function. This ensures a commit, but doesn't affect any other open
# connections. This potential bug would be hard to find otherwise.

update_cursor.connection.commit()

# -----------------------------------------------------------------------------
# Placeholders and parameter substitution
# -----------------------------------------------------------------------------
# As a somewhat obvious side note, you would probably never wan't to hard code
# values in like above, you would likely use variables. There a couple ways:

update_name = 'Rick'
update_email = input('Enter your email ')

# update_sql = "UPDATE contacts SET email = '{}' WHERE name = '{}'".format(
#               update_email, update_name)

# update_cursor = db.cursor()
# update_cursor.execute(update_sql)

# OR using placeholders and parameter substitution:

update_sql = "UPDATE contacts SET email = ? WHERE name = ?"

update_cursor = conn.cursor()
update_cursor.execute(update_sql, (update_email, update_name))

# This allows the python sqlite library to "sanitize the input". This process
# is somewhat complicated but just know that this is the safest way to do it
# if you're using user input or parameters passed from external code.

# -----------------------------------------------------------------------------
# executescript()
# -----------------------------------------------------------------------------
# Is used for running more than one SQL statement in a single call. Individual
# statements are separated by a semi-colon and will run one after the other.
# If the above code used this line instead:

# update_cursor.executescript(update_sql)

# Then it would allow for an SQL injection attack. If the user typed something
# like this into the input - anything; DROP TABLE contacts
# The table would be deleted. You might think that not knowing the table name
# would prevent this from happening but it's actually easy to get that info:

for row in conn.execute("SELECT * FROM sqlite_master"):
    print(row)
# ('table', 'contacts', 'contacts', 2, 'CREATE TABLE contacts
# (name TEXT, phone INTEGER, email TEXT)')

update_cursor.close()
conn.close()

# -----------------------------------------------------------------------------
# Placeholders Review
# -----------------------------------------------------------------------------
import sqlite3


conn = sqlite3.connect('contacts.sqlite')
name = input('enter a name: ')

# Method 1

for row in conn.execute("SELECT * FROM contacts WHERE name='{}'".format(name)):
    print(row)

# Method 2

for row in conn.execute('SELECT * FROM contacts WHERE name=?', (name,)):
    print(row)

# Method 3

lookup = 'SELECT * FROM contacts WHERE name=?'
for row in conn.execute(lookup,(name,)):
    print(row)

# The big lesson in the last to situations where we're using parameter
# substitution is the comma after input_name. In both cases it's that comma
# at the end that tells python you want a tuple when providing only one item.
# And as it turns out, a tuple is REQUIRED when you're doing this kind of
# parameter substitution.

conn.close()

# -----------------------------------------------------------------------------
# Detect types
# -----------------------------------------------------------------------------
# When writing datetime objects to a database, the object will be saved as a
# string. You could use the strptime() function to convert back to a structured
# time object, or you could ask sqlite to do it for you with the following
# parameter: detect_types=sqlite3.PARSE_DECLTYPES

conn = sqlite3.connect('accounts.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)

# There are also a couple of ways to convert the UTC string to local time.
# see sqlite3_example1.py & sqlite3_example2.py

# -----------------------------------------------------------------------------
# Sqlite links
# -----------------------------------------------------------------------------
# https://docs.python.org/3.5/library/sqlite3.html
# https://www.sqlite.org/lang_corefunc.html
# https://sqlite.org/lang_datefunc.html

# -----------------------------------------------------------------------------
# MySQL
# -----------------------------------------------------------------------------
# Unlike SQLite, it's an actual server, so clients can access it from different
# devices across the network. MysqlDB is the most popular driver, but hasn't
# yet been ported to Python 3. You can use these to access MySQL from Python:

# MySQL Connector - http://bit.ly/mysql-cpdg
# PYMySQL - https://github.com/petehunt/PyMySQL/
# oursql - http://pythonhosted.org/oursql/

# -----------------------------------------------------------------------------
# PostgreSQL
# -----------------------------------------------------------------------------
# Is a full-featured open source relational database, in many ways more
# advanced than MySQL. Python drivers for PostgreSQL:

# psycopg2 - http://initd.org/psycopg/
# py-postgresql - http://python.projects.pgfoundry.org/

# see postgresSQL_example.py

# -----------------------------------------------------------------------------
# SQLAlchemy
# -----------------------------------------------------------------------------
# DB-API takes you only so far. Each database implements a particular dialect
# reflecting its features and philosophy. Many libraries try to bridge these
# differences. The most popular cross-database Python library is SQLAlchemy.

# You don't need to import the driver; the initial connection string you
# provide to SQLAlchemy will determine it:

# dialect + driver :// user : password @ host : port / dbname

# dialect - the database type
# driver - the particular driver you want to use for that database
# user and password - our database authentication strings
# host and port - the database server's location
# (: port is only needed if it's not the standard one for this server)
# dbname - the database to initially connect to on the server

# SQLite skips the host, port, user, and password.

# The dbname informs SQLite as to what file to use to store your database.
# If you omit the dbname, SQLite builds a database in memory. If the dbname
# starts with a slash (/), it's an absolute filename on your computer
# Otherwise, it's relative to your current directory.

# -----------------------------------------------------------------------------
# SQLAlchemy – The Engine Layer
# -----------------------------------------------------------------------------

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
print(rows) # <sqlalchemy.engine.result.ResultProxy object at 0x1037119e8>
for row in rows:
    print(row)  # ('balls', 20, 0.5)  ('spoons', 62, 1.5)  ('rocks', 454, 0.1)

# This was pretty much the same as DB-API except we have the added benefit of
# being able to change the connection string to port this code to another type
# of database. The next level up would be...

# -----------------------------------------------------------------------------
# SQLAlchemy – SQL Expression Language
# -----------------------------------------------------------------------------
# SQLAlchemy's SQL Expression Language introduces functions to create the SQL
# for various operations. The Expression Language handles more of the SQL
# dialect differences. Here's how to create and populate the a table using
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

# Note: the inventory object is the connection between SQL and Python

conn.execute(inventory.insert(('socks', 2, 10.0)))
conn.execute(inventory.insert(('paperclips', 1000, 0.05)))
conn.execute(inventory.insert(('snow globes', 50, 5.0)))

# inventory.select() selects everything from the table (represented by the
# inventory object), as SELECT * FROM would do in plain SQL:

result = conn.execute(inventory.select())

rows = result.fetchall()
print(rows)
# [('socks', 2, 10.0), ('paperclips', 1000, 0.05), ('snow globes', 50, 5.0)]

# The highest level is...

# -----------------------------------------------------------------------------
# SQLAlchemy – Object-Relational Mapper
# -----------------------------------------------------------------------------
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

# You can use sqlite in the command line to check it:
# $ sqlite3 inventory2.db
# .tables
# select * from inventory;
# .quit

# -----------------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------------
# This was a brief overview to help decide which of the following levels would
# best fit your needs:

# – Plain DB-API, as in the earlier SQLite section
# – The SQLAlchemy engine room
# – The SQLAlchemy Expression Language
# – The SQLAlchemy ORM
