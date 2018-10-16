'''Serializing with pickle'''


# Serialization is the process that allows objects to be saved to a file so
# that they can be restored from the file later. Formats such as JSON might
# require some custom converters to serialize all the data types from a Python
# program. Python's pickle module can save and restore any object in a
# special binary format.


import pickle
import datetime

now1 = datetime.datetime.utcnow()
pickled = pickle.dumps(now1)
now2 = pickle.loads(pickled)

assert now1 == now2

# Use dump() to pickle to a file, and load() to unpickle from one.

import pickle

unkle = ('The Road, Pt. 1', 'UNKLE', '2017', (
         (1, 'Inter 1'),
         (2, 'Farewell'),
         (3, 'Looking for the Rain'),
         (4, 'Cowboys or Indians')))

with open('data/music.pickle', 'wb') as pickle_file:
    pickle.dump(unkle, pickle_file)

with open('data/music.pickle', 'rb') as unpickle_file:
    unkle2 = pickle.load(unpickle_file)

assert unkle == unkle2

# You can pickle as many objects as you want to one file, you just have to
# remember to load them back in the same order:

queens = ('Villians', 'QOTSA', '2017', (
         (1, "Feet Don't Fail Me"),
         (2, 'The Way You Used to Do'),
         (3, 'Domesticated Animals'),
         (4, 'Fortess')))

arcade = ('Everything Now', 'Arcade Fire', '2017', (
         (1, 'Everything Now'),
         (2, 'Signs of Life'),
         (3, 'Creature Comfort'),
         (4, 'Peter Pan')))

with open('data/music.pickle', 'wb') as pickle_file:
    pickle.dump(unkle, pickle_file)
    pickle.dump(queens, pickle_file)
    pickle.dump(arcade, pickle_file)
    pickle.dump(2348990008, pickle_file)

with open('data/music.pickle', 'rb') as unpickle_file:
    unkle2 = pickle.load(unpickle_file)
    queens2 = pickle.load(unpickle_file)
    arcade2 = pickle.load(unpickle_file)
    x = pickle.load(unpickle_file)

# pickle can use different protocols when serializing data. These protocols are
# released with new versions of Python and will include better support for more
# complex data objects. That being said, the protocols aren't backwards
# compatible. If you pickle something with the latest version you may not be
# able to load back in with an older version. Keep in mind too that some of the
# older versions have major security issues. To specify a protocol:

with open('data/music.pickle', 'wb') as pickle_file:
    pickle.dump(unkle, pickle_file, protocol=3) # default released with Python 3
    pickle.dump(unkle, pickle_file, protocol=2) # for python 2
    pickle.dump(unkle, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(unkle, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)

# Final Note: as with PyYAML load(), pickle can create Python objects.
# Don't unpickle something that you don't trust. Here's an example of code
# that would delete a file called text.txt if run:

pickle.loads(b"cos\nsystem\n(S'rm text.txt'\ntR.")      # mac/linux
pickle.loads(b"cos\nsystem\n(S'del text.txt'\ntR.")     # windows



# Customizing pickles
# -----------------------------------------------------------------------------
# With most common Python objects, pickling just works. Basic primitives such
# as integers, floats, strings, lists, dictionaries and even object are all
# picklable, provided their contents (or attibutes) are also picklable. Some
# examples of things that are not picklable are open file objects, network
# connections, or database connections.

# https://docs.python.org/2/library/pickle.html#what-can-be-pickled-and-unpickled

# In many cases it would not make sense to pickle these objects, but
# in other cases we may want to customize how such transient data is stored
# and restored. For example, let's say we have a class that loads contents of
# a web page and then uses the threading.Timer class to schedule an hourly
# update. If you try to pickle this class as is, it'll raise a TypeError:
# can't pickle _thread.lock objects

import datetime
import pickle
from threading import Timer
from urllib.request import urlopen


class UpdatedURL():
    def __init__(self, url):
        self.url = url
        self.contents = ''
        self.last_updated = None
        self.update()

    def update(self):
        self.contents = urlopen(self.url).read()
        self.last_updated = datetime.datetime.now()
        self.schedule()

    def schedule(self):
        self.timer = Timer(3600, self.update)
        self.timer.setDaemon(True)
        self.timer.start()

u = UpdatedURL('https://news.ycombinator.com/')
# serialized = pickle.dumps(u)

# When pickle tries to serialize an object, it simply tries to store the
# object's __dict__ attribute; __dict__ is a dictionary mapping all the
# attribute names on the object to their values. Luckily, before checking
# __dict__, pickle checks to see whether a __getstate__ method exists. If it
# does, it will store the return value of that method instead of the __dict__.

# Basically, Ww can use, __getstate__ and __setstate__, to give pickle special
# instructions to do before pickling and after pickling. In the __getstate__
# we delete the offending timer attribute. In the __setstate__, which is called
# when the pickled object is restored, we can reset the __dict__ object and
# re-run the method that adds the timer.

class UpdatedURL():
    def __init__(self, url):
        self.url = url
        self.contents = ''
        self.last_updated = None
        self.update()

    def update(self):
        self.contents = urlopen(self.url).read()
        self.last_updated = datetime.datetime.now()
        self.schedule()

    def schedule(self):
        self.timer = Timer(3600, self.update)
        self.timer.setDaemon(True)
        self.timer.start()

    def __getstate__(self):
        new_state = self.__dict__.copy()
        if 'timer' in new_state:
            del new_state['timer']
        return new_state

    def __setstate__(self, data):
        self.__dict__ = data
        self.schedule()


u = UpdatedURL('https://news.ycombinator.com/')
serialized = pickle.dumps(u)
# Now it works!
