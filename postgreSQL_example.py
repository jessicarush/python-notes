'''PostgreSQL'''

# To work with this database server, first you'll need to download the
# installer: https://www.postgresql.org/

# Launch the installer and it will take you into the 'setup wizard'.
# Choose your installation directory, data directory, (by default these are
# /Library/PostgreSQL/10/data). Then you'll need to create a superuser
# password. The superuser is 'postgres' by default but you select the password.
# It's a good idea to record all this in a credentials file including the
# next item which is port. By default is: 5432.

# The next question 'Set the locale to be used by the new database cluster'.
# There's a good description of database clusters here:
# https://www.postgresql.org/docs/current/static/creating-cluster.html
# Locale refers to an application respecting cultural preferences regarding
# alphabets, sorting, number formatting, etc. If your system is already set to
# use the locale that you want in your database cluster then there is nothing
# else you need to do. If you want to use a different locale you can select
# something else from the list. Note, you can't change this afterwards.

# After the main install completes, it will ask you if you want some additional
# tools (Stack Builder). There's bunch of add-ons available here. You can
# access this current list of add-ons at any time by launching stackbuilder:
# /Library/PostgreSQL/10/stackbuilder

# Next, you'll need to use the pgAdmin tool to create a database. Once the
# dashboard tool opens, right click on the PostgreSQL server in the left
# panel and choose 'Connect Server'. Type your password. Once connected,
# pop open the Databases group and you'll see one default database called
# 'postgres'. To create a new one, right click on the 'Databases' group and
# choose 'Create' > database.

# You could use the included tools in this directory to interact with the
# PostgreSQL database, or you could use python with the help of an external
# library psycopg2: http://initd.org/psycopg/

# NOTE: once you've created the database, you can check out the table in
# the pgAdmin tool. Navigate to your database > Schemas > Public > Tables
# There's also a query tool that allows you to query your database.

# NOTE: for some reason PostgreSQL doesn't like the syntax of using ? as
# placeholder values. It prefers %s instead!

# NOTE: do not use the name 'user' for a table name as is is a reserved word
# in postgresql. 'users' seems to work fine.

import psycopg2


db = ("dbname='test1'"
      "user='postgres'"
      "password='your-password'"
      "host='localhost'"
      "port='5432'")

def create():
    conn = psycopg2.connect(db)
    curs = conn.cursor()
    curs.execute('''CREATE TABLE IF NOT EXISTS inventory
      (item TEXT, quantity INT, cost FLOAT)''')
    conn.commit()
    curs.close()
    conn.close()


def insert(item, quantity, cost):
    conn = psycopg2.connect(db)
    curs = conn.cursor()
    curs.execute("INSERT INTO inventory VALUES (%s, %s, %s)",
      (item, quantity, cost))
    curs.connection.commit()
    curs.close()
    conn.close()


def display():
    conn = psycopg2.connect(db)
    curs = conn.cursor()
    curs.execute('SELECT * FROM inventory')
    rows = curs.fetchall()
    curs.close()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect(db)
    curs = conn.cursor()
    curs.execute('DELETE FROM inventory WHERE item=%s', (item,))
    curs.connection.commit()
    curs.close()
    conn.close()


def update(quantity, cost, item):
    conn = psycopg2.connect(db)
    curs = conn.cursor()
    curs.execute('UPDATE inventory SET quantity=%s, cost=%s WHERE item=%s',
      (quantity, cost, item))
    curs.connection.commit()
    curs.close()
    conn.close()


create()
insert('Dolphin', 5, 1000)
# insert('Rocks', 5, 2)
# insert('Dice', 100, 0.5)
# delete('Dice')
update(5000, 0.5, 'Giraffe')
print(display())



# To compare: sqlite3
# -----------------------------------------------------------------------------
# The following is the same code but written for sqlite3:

import sqlite3

db = 'test.db'

def create():
    conn = sqlite3.connect(db)
    curs = conn.cursor()
    curs.execute('''CREATE TABLE IF NOT EXISTS inventory
      (item TEXT, quantity INT, cost FLOAT)''')
    conn.commit()
    curs.close()
    conn.close()


def insert(item, quantity, cost):
    conn = sqlite3.connect(db)
    curs = conn.cursor()
    curs.execute('INSERT INTO inventory VALUES (?, ?, ? )',
      (item, quantity, cost))
    curs.connection.commit()
    curs.close()
    conn.close()


def display():
    conn = sqlite3.connect(db)
    curs = conn.cursor()
    curs.execute('SELECT * FROM inventory')
    rows = curs.fetchall()
    curs.close()
    conn.close()
    return rows


def delete(item):
    conn = sqlite3.connect(db)
    curs = conn.cursor()
    curs.execute('DELETE FROM inventory WHERE item=?', (item,))
    curs.connection.commit()
    curs.close()
    conn.close()


def update(quantity, cost, item):
    conn = sqlite3.connect(db)
    curs = conn.cursor()
    curs.execute('UPDATE inventory SET quantity=?, cost=? WHERE item=?',
      (quantity, cost, item))
    curs.connection.commit()
    curs.close()
    conn.close()


create()
# insert('Coffee', 25, 10.5)
# insert('Rocks', 5, 2)
# insert('Dice', 100, 0.5)
# delete('Rocks')
update(100, 0.5, 'Dice')
print(display())
