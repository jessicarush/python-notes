'''sqlite3 Example'''

# This example contains several useful techniques for storing and retrieving
# datetime objects as well as displaying UTC time as local time when needed.
# There is also an example of performing a rollback, should an exception occur
# see lines 57-63.

import sqlite3
import datetime
import pytz

db = sqlite3.connect('accounts.sqlite')
db.execute('''CREATE TABLE IF NOT EXISTS accounts
              (name TEXT PRIMARY KEY NOT NULL,
              balance INTEGER NOT NULL)''')
db.execute('''CREATE TABLE IF NOT EXISTS history
              (time TIMESTAMP NOT NULL,
              account TEXT NOT NULL,
              amount INTEGER NOT NULL,
              PRIMARY KEY (time, account))''')

# A composite key is when you use more than one column as the primary key. In
# the transactions table above, time and account alone would not be enough to
# uniquely identify each transaction but together they work.

class Account():

    @staticmethod
    def _current_time():
        return pytz.utc.localize(datetime.datetime.utcnow())
        # We could choose to save local time like this:
        # local_time = pytz.utc.localize(datetime.datetime.utcnow())
        # return local_time.astimezone()
        # but time zones aren't converted back out very well. As always, work
        # with UTC and only convert to local time when you need to for the user.
        # There is another method that saves the zone in a separate column
        # but it requires quite a few changes. See sqlite3_example2.py

    def __init__(self, name: str, opening_balance: int=0):
        select_query = "SELECT name, balance FROM accounts WHERE name = ?"
        cursor = db.execute(select_query, (name,))
        row = cursor.fetchone()
        if row:
            self.name, self._balance = row # tuple unpacking
            print('Retrieved record for {}'.format(self.name))
        else:
            self.name = name
            self._balance = opening_balance
            insert_query = "INSERT INTO accounts VALUES(?, ?)",
            cursor.execute(insert_query, (name, opening_balance))
            cursor.connection.commit()
            print('Account created for {}'.format(self.name))
        self.show_balance()

    def _save_update(self, amount):
        # instead of self._balance += amount, we're assigning this to a new
        # variable because we don't want the self._balance to update if the
        # transaction fails for some reason.
        new_balance = self._balance + amount
        time = Account._current_time()

        try:
            db.execute("UPDATE accounts SET balance = ? WHERE name = ?",
              (new_balance, self.name))
            db.execute("INSERT INTO history VALUES(?, ?, ?)",
              (time, self.name, amount))
        except sqlite3.Error:
            db.rollback()
        else:
            db.commit()
            # The transaction has completed so now we can update self._balance
            self._balance = new_balance


    def deposit(self, amount: int):
        if amount > 0.0:
            self._save_update(amount)
            print('{:.2f} deposited'.format(amount/100))
        return self._balance/100

    def withdraw(self, amount: int):
        if 0 < amount <= self._balance:
            self._save_update(-amount)
            print('{:.2f} withdrawn'.format(amount/100))
            return amount/100
        else:
            print('Amount must be greater than 0 and not exceed balance')
            return 0.0

    def show_balance(self):
        print('Balance for {} is {:.2f}'.format(self.name, self._balance/100))

# -----------------------------------------------------------------------------
# Testing
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    rick = Account('Rick')
    morty = Account('Morty', 50000)
    pingpong = Account('Ping Pong', 10000)
    boktoktok = Account('Boktoktok', 2000)

    rick.deposit(10010)
    morty.withdraw(1000)

    db.close()

# -----------------------------------------------------------------------------
# Retrieve datetime objects
# -----------------------------------------------------------------------------

print('-' * 50)

# When writing datetime objects to a database, the object will be saved as a
# string. There are a number of ways to convert back to a datetime object if
# you needed to. One way would be to use the strptime() function to convert
# back to a structured time object. I this example, we can ask sqlite to do it
# for us with the parameter: detect_types=sqlite3.PARSE_DECLTYPES

# Note this method doesn't handle timezone aware dates, but you can convert
# the utc afterward as shown here:

db = sqlite3.connect('accounts.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)

for row in db.execute('SELECT * FROM history'):
    utc_time = row[0]
    print('UTC – {} \t {}'.format(utc_time, type(utc_time)))
    # UTC – 2017-11-30 20:03:05.131018   <class 'datetime.datetime'>
    # UTC – 2017-11-30 20:03:05.132068   <class 'datetime.datetime'>

db.close()

# -----------------------------------------------------------------------------
# Display stored UTC times as a users local time
# -----------------------------------------------------------------------------

print('-' * 50)

db = sqlite3.connect('accounts.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)

for row in db.execute('SELECT * FROM history'):
    local_time = pytz.utc.localize(row[0]).astimezone()
    print('Local – {} \t {}'.format(local_time, type(local_time)))
    # Local – 2017-11-30 12:03:05.131018-08:00   <class 'datetime.datetime'>
    # Local – 2017-11-30 12:03:05.132068-08:00   <class 'datetime.datetime'>

db.close()

# -----------------------------------------------------------------------------
# An alternate method to display as local time
# -----------------------------------------------------------------------------

print('-' * 50)

# sqlite3 has a way to convert UTC time strings into local time strings using
# its own strftime function. See the execute below. The first parameter should
# be a format string, then the time value then a modifier which causes the UTC
# time to be converted to local time.

db = sqlite3.connect('accounts.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)

for row in db.execute('''
  SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime')
  AS localtime, history.account, history.amount
  FROM history ORDER BY history.time'''):
    print(row) # prints local time now
    # ('2017-11-30 12:03:05.131', 'Rick', 10010)
    # ('2017-11-30 12:03:05.132', 'Morty', -1000)

db.close()

# -----------------------------------------------------------------------------
# Create a view using the above
# -----------------------------------------------------------------------------

print('-' * 50)

db = sqlite3.connect('accounts.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)

db.execute('''
  CREATE VIEW IF NOT EXISTS localhistory
  AS SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime')
  AS localtime, history.account, history.amount
  FROM history ORDER BY history.time
  ''')

for row in db.execute("SELECT * FROM localhistory"):
    print(row)
    # ('2017-11-30 12:07:34.624', 'Rick', 10010)
    # ('2017-11-30 12:07:34.625', 'Morty', -1000)
