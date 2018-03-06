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
            raise Exception("Invalid file format")

        self.filename = filename

class Mp3File(AudioFile):
    ext = 'mp3'
    def play(self):
        print(f"playing mp3: {self.filename}")

class WavFile(AudioFile):
    ext = 'wav'
    def play(self):
        print(f"playing wav: {self.filename}")

class AacFile(AudioFile):
    ext = 'aac'
    def play(self):
        print(f"playing aac: {self.filename}")

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
        if not filename.endswith(".flac"):
            raise Exception("Invalid file format")

        self.filename = filename

        def play(self):
            print(f"playing flac: {self.filename}")

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
# Abstract base classes, or ABCs define set of methods and properties that a
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

# And that is why duck typing is way more interesting than classical
# polymorphism. We can create 'is a' relationships without the overhead of using
# inheritance (or worse, multiple inheritance). The interesting thing about the
# Container ABC is that any class that implements it gets to use the in keyword
# for free. In fact, in is just syntax sugar that delegates to the __contains__
# method. Any class that has a __contains__ method is a Container and can
# therefore be queried by the in keyword.

print(1 in odds_container)
# True

print(24 in odds_container)
# False
