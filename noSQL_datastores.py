'''NoSQL Data Stores'''

# Some databases are not relational and don't support SQL. These were written to
# handle very large data sets, allow more flexible data definitions, or support
# custom data operations.

# -----------------------------------------------------------------------------
# dbm Family
# -----------------------------------------------------------------------------
# key-value stores often embedded in apps such as web browsers to maintain
# settings. A dbm database is like a Python dictionary. Example:

import dbm

db = dbm.open('definitions', 'c')

# The second argument to the following open() method is 'r' to read, 'w' to
# write, and 'c' for both, creating the file if it doesn't exist. To create
# key-value pairs, just assign a value to a key just as you would a dictionary:

db['jaune'] = 'yellow'
db['rouge'] = 'red'
db['vert'] = 'green'

# testing:
print(len(db))
print(db['vert'])

# close the database:
db.close()

# reopen and read:
db = dbm.open('definitions', 'r')
print(db['jaune'])

# Keys and values are stored as bytes. You cannot iterate over the database
# object db, but you can get the number of keys by using len(). Note that get()
# and setdefault() work as they do for dictionaries.

# -----------------------------------------------------------------------------
# Memcached
# -----------------------------------------------------------------------------
# memcached is a fast in-memory key-value cache server. It's often put in front
# of a database, or used to store web server session data. To try it out, you
# need a memcached server and Python driver. There are many drivers; one that
# works with Python 3 is python3-memcached, which you can install by using the
# command: $ pip install python-memcached

# Once you connect to a memcached server, you can do the following:

# Set and get values for keys
# Increment or decrement a value
# Delete a key

# Data is not persistent, and data that you wrote earlier might disappear. This
# is inherent in memcached, being that it's a cache server. It avoids running
# out of memory by discarding old data.

# -----------------------------------------------------------------------------
# Redis
# -----------------------------------------------------------------------------
# Redis is a data structure server. Like memcached, all of the data in a Redis
# server should fit in memory (though there is now an option to save to disk).

# Unlike memcached, Redis can do the following:
#  – Save data to disk for reliability and restarts
#  – Keep old data
#  – Provide more data structures than simple strings

# The Redis data types are a close match to Python's, and a Redis server can
# be a useful intermediary for one or more Python applications to share data.
#  – install the Python driver redis-py: pip3 install redis
#  – install the Server: brew install redis
#  – launch Redis server: redis-server
#  – test that the server is running: redis-cli ping (respose PONG)
#  – shutdown server: redis-cli shutdown

import redis
conn = redis.Redis('localhost', 6379)

# -----------------------------------------------------------------------------
# Redis Strings
# -----------------------------------------------------------------------------
# A key with a single value is a Redis string. Python data types are
# automatically converted.

# set a string, integer and float
conn.set('item', 'octopus')
conn.set('quantity', '2')
conn.set('cost', '175.00')

# List all keys
conn.keys('*')

# get values by key:
conn.get('item')

# setnx() method sets a value only if the key does not exist:
conn.setnx('item', 'seahorse')

# getset() method returns the old value and sets it to a new one:
conn.getset('item', 'seahorse')
conn.get('item')

# getrange() to get a substring , 0=start, -1=end
conn.getrange('item', -5, -1 )

# setrange() to replace a substring, using 0 based offset
conn.setrange('item', 3, 'monkey')
conn.get('item')

# mset() to set multiple keys at once:
conn.mset({'colour': 'purple', 'size:': 'large'})

# mget() to get more than one value at once:
conn.mget(['colour', 'cost'])

# delete() to delete a key:
conn.delete('size')

# incr(), incrbyfloat(), decr() to increment or decrement:
conn.incr('quantity')
conn.incr('quantity', 12)
conn.decr('quantity', 5)
conn.incrbyfloat('cost')
conn.incrbyfloat('cost', 2.50)

# There is no decrement for incrbyfloat(), just use a negative value:
conn.incrbyfloat('cost', -2.50)

# -----------------------------------------------------------------------------
# Redis Lists
# -----------------------------------------------------------------------------
# lpush() to insert at the beginning. The list (zoo in the examples below) is
# created when you do your first insertion. Lists can contain only strings.
conn.lpush('zoo', 'bear', 'marmoset')

# linsert() to insert before or after
conn.linsert('zoo', 'before', 'marmoset', 'beaver')
conn.linsert('zoo', 'after', 'marmoset', 'yak')

# rpush() to insert at the end
conn.rpush('zoo', 'zebra')

# lset() to insert at an offset
conn.lset('zoo', 2, 'iguana')

# lindex() to get the value at an offset
conn.lindex('zoo', 3)

# lrange() to get the values of an offset range (0 to -1 for all)
conn.lrange('zoo', 0, -1)

# ltrim() to trim a list and keep only those in a range
conn.ltrim('zoo', 0, 5)

# see also : networks.py where Redis lists and publish-subscribe is used to
# implement job queues.

# -----------------------------------------------------------------------------
# Redis Hashes
# -----------------------------------------------------------------------------
# are similar to python dictionaries but can only contain strings.

# hset() to set a single key value
conn.hset('colours', 'red', 'rouge')

# hmset() to set multiple key values
conn.hmset('colours', {'yellow': 'jaune', 'green': 'vert'})

# hget() to get one keys value
conn.hget('colours', 'red')

# hmget() to get multiple values
conn.hmget('colours', 'red', 'green')

# hkeys() to get all keys
conn.hkeys('colours')

# hvals() to get all the values
conn.hvals('colours')

# hlen() to get the number of fields
conn.hlen('colours')

# hgetall() to get all keys and values
conn.hgetall('colours')

# hsetnx() to create a a field if its key doesn't exist already
conn.hsetnx('colours', 'red', 'blabla')

# -----------------------------------------------------------------------------
# Redis sets
# -----------------------------------------------------------------------------
# sadd() to add one or more values to a sets
conn.sadd('a', 'red', 'orange', 'yellow', 'purple', 'bla')

# scard() to get the number of values from a sets
conn.scard('a')

# smembers() to get all the values
conn.smembers('a')

# srem() to remove a value
conn.srem('a', 'bla')

# sinter() to get the common values (intersection) of two sets
conn.sadd('b', 'blue', 'orange', 'green', 'purple')
conn.sinter('a', 'b')

# sinterstore() to get the common values and store the result in a new set:
conn.sinterstore('c', 'a', 'b')

# sunion() to get all values of both sets
conn.sunion('a', 'b')

# sunionstore() to get all values ot both sets and store the result:
conn.sunionstore('c', 'a', 'b')

# sdiff() the difference between set1 and set2
conn.sdiff('a', 'b')

# sdiffstore() ... and store the difference
conn.sdiffstore('c', 'a', 'b')
conn.smembers('c')

# -----------------------------------------------------------------------------
# Redis Sorted Sets (zset)
# -----------------------------------------------------------------------------
# Is a set of unique values, each with an associated floating point 'score'.
# You can access each item by its value or score. This example tracks user
# logins via timestamps using the Unix epoch value that's returned by the
# Python time() function:

import time
now = time.time()

# add the first user:
conn.zadd('logins', 'sansa', now)

# add another 5 minutes later:
conn.zadd('logins', 'jon', now+(5*60))

# add another 2 hours later:
conn.zadd('logins', 'bran', now+(2*60*60))

# add anothr the next day:
conn.zadd('logins', 'aria', now+(24*60*60))

# get the order off a value:
conn.zrank('logins', 'bran')

# get the timestamp (score):
conn.zscore('logins', 'bran')

# view all values in order:
conn.zrange('logins', 0, -1)

# view all values in order, with the scores:
print(conn.zrange('logins', 0, -1, withscores=True))

# -----------------------------------------------------------------------------
# Redis Bits
# -----------------------------------------------------------------------------
# a space efficient way to deal with large sets of numbers. Example along the
# same line as above would be tracking increasing numeric user IDS. Bits are
# more compact and faster:

days = ['2017-08-14', '2017-08-15', '2017-08-16']
aria = 1022
sansa = 40569
jon = 6603762

# Each date is a separate key. Set the bit for a user ID for that date.
# For example, on the first date two users logged in:
conn.setbit(days[0], aria, 1)
conn.setbit(days[0], jon, 1)

# the next day:
conn.setbit(days[1], jon, 1)
conn.setbit(days[1], sansa, 1)

# the last day:
conn.setbit(days[2], jon, 1)

# get the daily visitor count for each day:
for day in days:
    print(conn.bitcount(day))

# check if a particular user visited on a particular day:
conn.getbit(days[1], aria)

# how many users visited everyday:
conn.bitop('and', 'everyday', *days)
conn.bitcount('everyday')

# check if a particular user visited everyday:
conn.getbit('everyday', jon)

# what was the total number of unique users across all days:
conn.bitop('or', 'alldays', *days)
conn.bitcount('alldays')

# -----------------------------------------------------------------------------
# Redis Caches and Expiration:
# -----------------------------------------------------------------------------
# Redis keys have a time-to-live, or expiration date. By default it's forever.
# Use the expire() function to instruct Redis how long to keep the key. The
# value is a number of seconds:

import time
key = 'ned'
conn.set(key, 'ned_will_expire')
conn.expire(key, 5)
conn.ttl(key)
conn.get(key)   # returns ned_will_expire
time.sleep(6)
conn.get(key)   # returns None

# The expireat() command expires a key at a given epoch time. Key expiration
# is useful to keep caches fresh and to limit login sessions.

# -----------------------------------------------------------------------------
# Other NoSQL databases
# -----------------------------------------------------------------------------
# These handle data larger than memory, and many of them use multiple computers:

# Cassanda      http://cassandra.apache.org/        Python API: pycassa
# CouchDB       http://couchdb.apache.org/          Python API: couchdb-python
# HBase         http://hbase.apache.org/            Python API: happybase
# Kyoto Cabinet http://fallabs.com/kyotocabinet/    Python API: kyotocabinet
# MongoDB       https://www.mongodb.com/            Python API: mongodb
# Riak          http://basho.com/riak/              Python API: riak-python-client

# -----------------------------------------------------------------------------
# Full-Text Databases
# -----------------------------------------------------------------------------
# There's a special category of databases for full-text search. They index
# everything, so you can search for anything. Some popular open source
# examples, and their Python APIs:

# Lucene        http://lucene.apache.org/       Python API: pylucene
# Solr          http://lucene.apache.org/solr/  Python API: SolPython
# ElasticSearch https://www.elastic.co/         Python API: pyes
# Sphinx        http://sphinxsearch.com/        Python API: sphinxapi
# Xapian        https://xapian.org/             Python API: xappy
# Whoosh        https://bitbucket.org/mchaput/whoosh/wiki/Home
