'''Polymorphism'''


# This is a fancy name describing a simple concept: different behaviors happen
# depending on which subclass is being used, without having to explicitly know
# what the subclass actually is. It's also the idea that one thing can 'be'
# many other things (see below).

# Let's imagine we want to create a program that plays audio files. We need to
# handle different file types that have different processes of extraction and
# decompression, but the media player doesn't need to know these details. It
# just calls a play() method and lets the object take care of the actual
# details of playing. We can use inheritance with polymorphism to simplify the
# design.

class AudioFile():
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception('Invalid file format')

        self.filename = filename

class Mp3File(AudioFile):
    ext = 'mp3'
    def play(self):
        print(f'playing mp3: {self.filename}')

class WavFile(AudioFile):
    ext = 'wav'
    def play(self):
        print(f'playing wav: {self.filename}')

class AacFile(AudioFile):
    ext = 'aac'
    def play(self):
        print(f'playing aac: {self.filename}')

a = Mp3File('sing.mp3')
b = WavFile('sang.wav')
c = AacFile('song.aac')
# d = AacFile('song.mp3')  # Exception: Invalid file format

a.play()
b.play()
c.play()
# playing mp3: sing.mp3
# playing wav: sang.wav
# playing aac: song.aac

# The __init__ method in the parent class is able to access the 'ext' class
# variable from different subclasses. That's polymorphism at work. In addition,
# each subclass of AudioFile implements play() in a different way (in theory).
# This is also polymorphism in action. The media player can use the same code
# to play a file, no matter what subclass of AudioFile it is looking at.
# The details of decompressing the audio are encapsulated.

# Instead of inheriting from AudioFile, we could also do this:

class FlacFile():
    def __init__(self, filename):
        if not filename.endswith('.flac'):
            raise Exception('Invalid file format')

        self.filename = filename

        def play(self):
            print(f'playing flac: {self.filename}')

# Duck typing in Python allows us to use any object that provides the required
# behavior (the play method) without forcing it to be a subclass. The dynamic
# nature of Python makes this trivial. Polymorphism is one of the most
# important reasons to use inheritance in many object-oriented contexts.
# Since any objects that supply the correct interface can be used
# interchangeably in Python, it reduces the need for polymorphic common
# superclasses. Inheritance can still be useful for sharing code but
# (by inheriting from AudioFile, we don't have to repeat the exception code),
# if all that is being shared is the public interface, duck typing is all that
# is required.


# Abstract base classes
# -----------------------------------------------------------------------------
# Abstract base classes, or ABCs define a set of methods and properties that a
# class must implement in order to be considered a duck-type instance of that
# class. The class can extend the abstract base class but it must supply all
# the appropriate methods. Most of the abstract base classes that exist in the
# Python Standard Library live in the collections module. One of the simplest
# ones is the Container class. __abstractmethods__ will tell us what this
# class requires:

from collections import Container

print(Container.__abstractmethods__)
# frozenset({'__contains__'})

# So, the Container class has exactly one abstract method that needs to be
# implemented, __contains__. As it turns out, this method is implemented by
# list, str, and dict to indicate whether or not a given value is in the data
# structure. Here we'll make our own:

class OddsContainer():
    def __contains__(self, x):
        if not isinstance(x, int) or not x % 2:
            return False
        return True

odds_container = OddsContainer()

print(isinstance(odds_container, Container))
# True

print(issubclass(OddsContainer, Container))
# True

# And that's why duck typing is more interesting than classical polymorphism.
# We can create 'is a' relationships without the overhead of using inheritance
# (or worse, multiple inheritance). The interesting thing about the Container
# ABC is that any class that implements it gets to use the 'in' keyword for
# free. In fact, 'in' is just syntax sugar that delegates to the __contains__
# method. Any class that has a __contains__ method is a Container and can
# therefore be queried by the 'in' keyword.

print(13 in odds_container)
# True

print(24 in odds_container)
# False


# Creating an abstract base class
# -----------------------------------------------------------------------------
# It's not necessary to have an abstract base class to enable duck typing.
# However, imagine we were creating a media player with third-party plugins.
# It is advisable to create an abstract base class in this case to document
# what API the third- party plugins should provide. The 'abc' module provides
# the tools you need to do this. A warning, this requires some of Python's
# most arcane concepts...

import abc

class MediaLoader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass

    @abc.abstractproperty
    def ext(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented

# The first weird thing is the metaclass keyword argument passed into the class
# where you would normally see the list of parent classes. This is a rarely
# used construct from the mystic art of metaclass programming. All you need
# to know is that by assigning the ABCMeta metaclass, you are giving your
# class superpowers. The two abstract decorators are stating that any subclass
# of this class must implement that method or supply that property in order
# to be considered a proper member of the class. See what happens if you
# implement subclasses that do or don't supply those properties:

class Flac(MediaLoader):
    # ext = 'flac'
    def play(self):
        print(f'playing flac: {self.filename}')

f = Flac()

# TypeError: Can't instantiate abstract class Flac with abstract methods ext
# If a subclass fails to implement the abstract attributes, it is not possible
# to instantiate that class.

# Going back to the ABC: the __subclasshook__. This special method is called
# by the Python interpreter to answer the question: Is the class 'C' a subclass
# of this class? The method is basically saying that any class that supplies
# concrete implementations of all the abstract attributes of this ABC should
# be considered a subclass of MediaLoader, even if it doesn't actually inherit
# from the MediaLoader class...

class Mpeg():
    ext = 'mpeg'
    def play(self):
        print(f'playing mpeg: {self.filename}')

print(issubclass(Mpeg, MediaLoader))
# True
