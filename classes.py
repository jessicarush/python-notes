'''Classes'''


# A string and an integer are examples of built-in Python classes.
# A class is logical grouping of data and functions. The "integer" class is
# like an instruction manual for making integer objects. To make your own
# objects, you'll need to first define a class:

class Person():
    pass

# You can create an instance of a class (instantiating) by calling it as if it
# were a function:

henry = Person()

# In this case, Person() creates an individual object from the Person class and
# assigns it the name henry.

class Person():
    def __init__(self):
        pass

# The __init__ (initialize) is a special method. Python runs it automatically
# whenever we create a new instance from the class. Everything defined in the
# __init__ method will be applied to this new instance when it is created
# (instantiated). The self argument specifies that it refers to the
# individual object itself. When you define __init__() in a class definition,
# its first parameter should always be self. Although self is not a reserved
# word in Python, it's common usage.

# NOTE: While it's not required to have an __init__ method in every class
# definition, it's used to do define attributes that will distinguish this
# object from others created from the same class.

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

astronaut = Person('Roberta Bondar', 40)
baker = Person('Mrs. Lovett', 35)

# The name and age variables have the prefix self. Any variable prefixed with
# self is available to every method in the class and we'll also be able to
# access these variables through any instance of the class.

# The name and age passed in is saved with the object as an attribute.
# When a variable is bound to an instance of a class, it's called a data
# attribute. You can read and write this attribute directly by using dot
# notation:

print(astronaut.name)
astronaut.age = 20

# You aren't limited to the attributes set in the class. You can still assign
# new instance variables not present in the class:

baker.friend = 'Todd'

# Data attributes can be obtained in several ways when it comes to working with
# replacement fields. The last example (f-strings) is available as of v3.6.

print('Name {} age {}, name {} age {}'.format(
    astronaut.name, astronaut.age, baker.name, baker.age))

print('Name {0.name} age {0.age}, name {1.name} age {1.age}'.format(
    astronaut, baker))

print(f'Name {astronaut.name} age {astronaut.age}, name {baker.name} age {baker.age}')


# Class attributes (class variables)
# -----------------------------------------------------------------------------

class Contact():

    all_contacts = []  # class variable

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


# The all_contacts list above is shared by all instances of the class. This
# means that there is only one all_contacts contacts list which we can access
# by Contact.all_contacts or self.all_contacts on any object instantiated from
# Contact. If you use the second method, it will check first in the object for
# the value then, if it doesn't find it there it will look in the class... and
# thus refer to the same single list. Note that if you do an assignment via the
# Class, then the variable is changed, but if you do it via an instance, you're
# not reassigning the original variable, you are creating a new local instance
# variable with the same name:

a = Contact('rick', 'rick@email.com')
b = Contact('morty', 'morty@email.com')
c = Contact('summer', 'summer@email.com')

print(Contact.all_contacts == c.all_contacts)  # True

Contact.all_contacts = set(Contact.all_contacts)

c.all_contacts = tuple(Contact.all_contacts)   # new local instance variable

print(Contact.all_contacts == c.all_contacts)  # False

Contact.all_contacts = list(Contact.all_contacts)


# Default values
# -----------------------------------------------------------------------------
# Looking at the example above, we could imagine using class variables like a
# default value. If the value isn't found in the object, it will look in the
# class. In these cases, it makes more sense to specify this initial value in
# the body of the __init__ method. If the intention is for instances to have
# their own value, we should see this instantiated with self. Note that if you
# specify a default value for an attribute like this, you don't need to include
# it as a mandatory parameter in the __init__ methods parenthesis.

class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.nationality = 'Canadian'

# When you set a default value this way, if you want to change the value for an
# instance, you would do that the same way as above: instance.attribute = 'xyz'
# That being said, you can also set default values this way:

class Person():

    def __init__(self, name, age, nationality='Canadian'):
        self.name = name
        self.age = age
        self.nationality = nationality

# The main difference here is that we can change the nationality when the
# instance is created, if we want to. In the previous example we'd have to
# write separate assignment line. There's also a good example below showing
# how default values set in the parameters can be helpful when creating
# subclasses whose defaults should be different.


# __dict__
# -----------------------------------------------------------------------------
# A dictionary or other mapping object is used to store an object’s (writable)
# attributes. Use __dict__ to see all the attributes:

print(baker.__dict__)
print(astronaut.__dict__)
print(Person.__dict__)

# {'name': 'Mrs. Lovett', 'age': 35, 'friend': 'Todd', 'nationality': 'British'}
# {'name': 'Roberta Bondar', 'age': 20}
# {'__module__': '__main__', '__init__': <function Person.__init__ at 0x101bb6d90>,
#  '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__':
#  <attribute '__weakref__' of 'Person' objects>, '__doc__': None}


# Calling methods from a class
# -----------------------------------------------------------------------------
# There are a couple of ways to call a method from a class:

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.alive = True

    def deceased(self):
        self.alive = False

snape = Person('Severus Snape', 38)

# call the method (function) like this:
snape.deceased()
print(snape.alive)

# or like this:
Person.deceased(snape)
print(snape.alive)


# Inheritance
# -----------------------------------------------------------------------------
# Creating a new class from an existing class, with some additions or changes.
# When you use inheritance, the new class can automatically use all the code
# from the old class without copying any of it. You only define what you need
# to add or change in the new class and this overrides the behavior of the
# original class. The original class is the parent, superclass or base class.
# The new one is the child, subclass or derived class.

# In the examples below, the Child classes inherit from the Parent in some way.
# The Child will do their thing, but also the parents thing, unless there is an
# override of a parents function in the child's:

class Parent():
    def __init__(self):
        print('Parent')
    def method(self):
        print('Parent method')

class Child1():                # Child1 will use the Parents __init__,
    def __init__(self):        # as well as it's own,
        Parent.__init__(self)  # but will have no access to the parents method
        print('Child 1')

class Child2(Parent):          # Child2 will use its own __init__,
    def __init__(self):        # and will have access to the parents method
        print('Child 2')

class Child3(Parent):          # Child3 will use the Parents __init__,
    def __init__(self):        # as well as it's own,
        Parent.__init__(self)  # and will have access to the parents method
        print('Child 3')

class Child4(Parent):          # Child4 will use the Parents __init__,
    def __init__(self):        # as well as it's own,
        super().__init__()     # and will have access to the parents method
        print('Child 4')

class Child5(Parent):          # Child5 will use the Parents __init__,
    def __init__(self):        # as well as it's own,
        super().__init__()     # and will use its own method
        print('Child 5')
    def method(self):          # Note: using super allows you to specify which
        print('Child method')  # parts of the parent __init__ to inherit

child1 = Child1()
# Parent
# Child 1

child2 = Child2()
child2.method()
# Child 2
# Parent method

child3 = Child3()
child3.method()
# Parent
# Child 3
# Parent method

child4 = Child4()
child4.method()
# Parent
# Child 4
# Parent method

child5 = Child5()
child5.method()
# Parent
# Child 5
# Child method


# super()
# -----------------------------------------------------------------------------
# If you override a method like __init__ , you can retrieve attributes back
# from the parent using super():

class Person():
    def __init__(self, name, age, email, status):
        self.name = name
        self.email = email
        self.age = age
        self.email = email
        self.satus = status

class Doctor(Person):
    def __init__(self, name, age, email, status):
        self.name = "Doctor " + name
        super().__init__(age, email, status)

# The above could be written like this:

class Doctor(Person):
    def __init__(self, name, age, email, status):
        self.name = "Doctor " + name
        self.email = email
        self.age = age
        self.email = email
        self.satus = status

# But then not only are we duplicating a bunch of code, but we are also loosing
# our inheritance. By using super(), if the definition of the parent class
# changes, the child will inherit the changes.


# .super() with default values
# -----------------------------------------------------------------------------

class Enemy():
    def __init__(self, name='Enemy', hp=0, lives=1):
        self.name = name
        self.hp = hp
        self.lives = lives

    def __str__(self):
        return "{0.name} – Lives: {0.lives}, Hit points: {0.hp}".format(self)

class Vampire(Enemy):
        def __init__(self, name):
            super().__init__(name=name, hp=12, lives=3)

# In the above example, we are able to change the default values that were set
# for the base class. Note when creating a vampire object, we will only be able
# to pass in an argument for name. But it will automatically get 12 hit points
# and 3 lives.

bat = Enemy('Batty')
spider = Enemy('Crawly', 10, 1)
spike = Vampire('Spike')

print(bat)      # Batty – Lives: 1, Hit points: 0
print(spider)   # Crawly – Lives: 1, Hit points: 10
print(spike)    # Spike – Lives: 3, Hit points: 12


# Multiple Inheritance
# -----------------------------------------------------------------------------
# In principle, it's very simple: a subclass that inherits from more than one
# parent class is able to access functionality from both of them. In practice,
# this is less useful than it sounds and many expert programmers recommend
# against using it. This example is not very practical but demonstrates the
# idea. The simplest and most useful form of multiple inheritance is called a
# mixin and is described below.

class Animal:
  def __init__(self, name):
    print(name, 'is an animal.');

class Mammal(Animal):
  def __init__(self, name):
    print(name, 'is a warm-blooded animal.')
    super().__init__(name)

class NonWingedMammal(Mammal):
  def __init__(self, name):
    print(name, "can't fly.")
    super().__init__(name)

class NonMarineMammal(Mammal):
  def __init__(self, name):
    print(name, "can't breathe underwater.")
    super().__init__(name)

class Dog(NonMarineMammal, NonWingedMammal):
  def __init__(self, name):
    print(name, 'has 4 legs.');
    super().__init__(name)

chihuahua = Dog('Chihuahua')
bat = NonMarineMammal('Bat')

# Chihuahua has 4 legs.
# Chihuahua can't breathe underwater.
# Chihuahua can't fly.
# Chihuahua is a warm-blooded animal.
# Chihuahua is an animal.
# Bat can't breathe underwater.
# Bat is a warm-blooded animal.
# Bat is an animal.


# MRO (Method resolution order)
# -----------------------------------------------------------------------------
# Python has a class method that can be applied to any class object that will
# reveal the order in which the inheritance executes. For example:

from pprint import pprint

pprint(Dog.mro())
# [<class '__main__.Dog'>,
#  <class '__main__.NonMarineMammal'>,
#  <class '__main__.NonWingedMammal'>,
#  <class '__main__.Mammal'>,
#  <class '__main__.Animal'>,
#  <class 'object'>]

# Note that this order can be modified, but that's some pretty expert stuff.
# http://www.python.org/download/releases/2.3/mro/.


# Diamond inheritance
# -----------------------------------------------------------------------------
# One thing that .super() does is resolve a problem with diamond inheritance.
# Diamond inheritance happens when you have a subclass that inherits from two
# superclasses, and those two superclasses inherit from the same base class.
# If you draw this out, it creates a diamond shape.

#    base class
#        /\
#       /  \
#      /    \
#   super  super
#      \    /
#       \  /
#        \/
#     subclass

# Technically, all classes inherit from the Object base class so it's a thing.
# What ends up happening here is the base class' __init__ method is called
# twice. That's relatively harmless with the Object class, but in some
# situations, it could be bad... imagine trying to connect to a database twice
# for every request.


class Base():
    def __init__(self):
        print("Base initializing")

class Left(Base):
    def __init__(self):
        Base.__init__(self)
        print("Left initializing")

class Right(Base):
    def __init__(self):
        Base.__init__(self)
        print("Right initializing")

class Subclass(Left, Right):
    def __init__(self):
        Left.__init__(self)
        Right.__init__(self)
        print("Subclass initializing")

s = Subclass()
# Base initializing
# Left initializing
# Base initializing
# Right initializing
# Subclass initializing

# We can resolve this issue simply bt using .super():

class Base():
    def __init__(self):
        print("Base initializing")

class Left(Base):
    def __init__(self):
        super().__init__()
        print("Left initializing")

class Right(Base):
    def __init__(self):
        super().__init__()
        print("Right initializing")

class Subclass(Left, Right):
    def __init__(self):
        super().__init__()
        print("Subclass initializing")

s = Subclass()
# Base initializing
# Right initializing
# Left initializing
# Subclass initializing

# Use **kwargs to handle multiple parameters:

class Base():
    def __init__(self):
        print("Base initializing")

class Left(Base):
    def __init__(self, name='', email='', **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        print("Left initializing")

class Right(Base):
    def __init__(self, address='', street='', **kwargs):
        super().__init__(**kwargs)
        self.address = address
        self.street = street
        print("Right initializing")

class Subclass(Left, Right):
    def __init__(self, phone='', **kwargs):
        super().__init__(**kwargs)
        self.phone = phone
        print("Subclass initializing")


s = Subclass(name='bob', phone=6041234567, street=1234, email='test@test.com')
# Base initializing
# Right initializing
# Left initializing
# Subclass initializing

print(s.__dict__)
# {'address': '', 'street': 1234, 'name': 'bob', 'email': '', 'phone': 6041234567}
exit()
# Basic multiple inheritance can be handy but, in many cases, we may want to
# choose a more transparent way of combining two disparate classes, usually
# using composition or another design pattern.


# Mixins
# -----------------------------------------------------------------------------
# A mixin is generally a superclass that is not meant to exist on its own, but
# is meant to be inherited by some other class to provide extra functionality.
# For example, lets say we wanted to add emailing functionality to a class.
# Since sending email is a common task that we might want to use on many other
# classes, a mixin is a good solution.

class Emailer():
    def send_email(self, message):
        print('Sending mail to ' + self.email)
        print('Message: ' + message)
        # email logic goes here

class Subscriber(Contact, Emailer):
    pass

s = Subscriber('bob', 'bob@email.com')

s.send_email('Hello, this is a test.')
# Sending mail to bob@email.com
# Message: Hello, this is a test.


# Extending built-in classes with inheritance
# -----------------------------------------------------------------------------
# Referring back to the Contact class from above. Imagine that we wanted to
# include a search function. We could add this to the Contact class, but it
# feels like this belongs to the list itself. We can do this with inheritance:

class ContactList(list):

    def search(self, search_name):
        '''Return all contacts that contain the search value in the name.'''
        matching_contacts = []
        for contact in self:
            if search_name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact():

    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


a = Contact('rick', 'rick@email.com')
b = Contact('morty', 'morty@email.com')
c = Contact('summer', 'summer@email.com')

search = Contact.all_contacts.search('sum')

print(search)
# [<__main__.Contact object at 0x101ce1860>]

print(search[0].email)
# summer@email.com

print(search[0].name)
# summer


# Getter and Setter methods with property()
# -----------------------------------------------------------------------------
# Some object oriented languages support private object attributes that can't
# be accessed from the outside. They have to write getter and setter methods
# to read and write the values on these private attributes. Python doesn't
# need these because all attributes and methods are public. A good way to hide
# attributes is to use property(). The naming convention for hidden attributes
# is _whatever (see documenting_naming.py).

# The property() method returns a property attribute. It makes a method
# (a function in a class) behave like an attribute. This allows us to create
# a read-only attribute of _name.

# The property method takes four optional parameters:
# – fget : function for getting the attribute value
# – fset : function for setting the attribute value
# – fdel : function for deleting the attribute value
# – doc : string that contains the docstring for the attribute

# property(fget=None, fset=None, fdel=None, doc=None)

class Person():
    def __init__(self, value):
        self._name = value

    def getName(self):
        print('Getting name: ' + self._name)
        return self._name

    def setName(self, value):
        print('Setting name to: ' + value)
        self._name = value

    def delName(self):
        print('Deleting name')
        del self._name

    # Set a property called name to use getName, setName and delName methods
    name = property(getName, setName, delName, 'Name property')


p = Person('Adam')

print(p.name)
# Getting name: Adam

p.name = 'John'
# Setting name to: John

del p.name
# Deleting name

# NOTE: The big question here though is why would you want to go to all the
# trouble. The simple answer is that using methods, you could run additional
# code in the getting and setting of the property (say checking a database)
# but from the outside it still looks and acts like a plain old property.

# NOTE: The deletion function is often left empty because object attributes
# are rarely deleted. If a coder does try to delete a property that doesn't
# have a delete function specified, it will raise an exception. Therefore,
# if there is a legitimate reason to delete our property, we should supply
# that function.


# Getter and Setter methods using @decorators
# -----------------------------------------------------------------------------

class Person():
    def __init__(self, value):
        self._name = value

    @property
    def name(self):
        print('Getting name: ' + self._name)
        return self._name

    @name.setter
    def name(self, value):
        print('Setting name to: ' + value)
        self._name = value

    @name.deleter
    def name(self):
        print('Deleting name')
        del self._name


p = Person('Tim')

print(p.name)
# Getting name: Tim

p.name = 'Paul'
# Setting name to: Paul

del p.name
# Deleting name


# Uses for Getters and Setters
# -----------------------------------------------------------------------------
# While you shouldn't necessarily worry about private attributes in Python,
# getter and setter methods can be useful in situations where you want to set
# up some sort of validation for the values that the data attributes can be set
# to. In the following example, lives is not allowed to be a negative number.

# NOTE: In the previous examples, the data attributes have a slightly different
# name from the property (__name, name) because we were trying to hide the,
# attribute, but it should be pointed out that these names have to be different.

class Player():
    def __init__(self, name):
        self.name = name
        self._lives = 3
        self.level = 1
        self.score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives can't be negative")
            # could also raise an exception here.
            self._lives = 0

    lives = property(_get_lives, _set_lives)


# Uses for property()
# -----------------------------------------------------------------------------

class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius


c = Circle(5)
print(c.diameter)  # 10

c.radius = 7
print(c.diameter)  # 14

# c.diameter = 4  # this will raise an AttributeError

# Create a setter to make the diameter method also accept new values:

class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2.0  # best to specify floats when dividing

c = Circle(5)
print(c.diameter) # 10

c.diameter = 20  # now this will work
print(c.radius)  # 10.0


# Another common need for this custom property/getter/setter stuff is simply
# caching a value that is difficult to calculate or expensive to lookup
# (for example, requiring a network request or database query). The goal is to
# store the value locally to avoid repeated calls to the expensive calculation.
# We do this with a custom getter @property. The first time the value is
# retrieved, we perform the lookup or calculation. The next time the value is
# requested, we return the stored data. Here's an example:

from time import time, sleep
from urllib.request import urlopen


class Website():
    def __init__(self, url):
        self.url = url
        self._content = None

    @property
    def content(self):
        if not self._content:
            print('Getting webpage...')
            sleep(2)  # pretend it's a big website
            self._content = urlopen(self.url).read()
        return self._content


w = Website("https://www.python.org/")

start = time()
c1 = w.content
print('{:.5f}'.format(time() - start))

start = time()
c2 = w.content
print('{:.5f}'.format(time() - start))

# Getting webpage...
# 2.14882
# 0.00001


# Instance methods
# -----------------------------------------------------------------------------
# Some data(attributes) and functions(methods) are part of the class itself and
# some are part of the objects that are created from that class. When you see
# an initial self argument in methods within a class def, it's an instance
# method. These are the types of methods you normally write. The first
# parameter of an instance method is self. Any change made to the class
# affects all of its objects.


# Class methods
# -----------------------------------------------------------------------------
# A class method is essentially a method can be called on a class instead of
# an instantiated object. Use the @classmethod decorator to indicate the
# following function is a class method. The first parameter to the method is
# the class itself: cls (because the word 'class' is already taken).

# This class method will count how many objects have been made from it:

class A():
    count = 0
    def __init__(self):
        A.count += 1

    def exclaim(self):
        print("I'm an A")

    @classmethod
    def children(cls):
        print(f'Class {cls.__name__} has {A.count} instances.')

# testing:
test1 = A()
test2 = A()
test3 = A()
test4 = A()

A.children()
# Class A has 4 instances.

# Here's another example that compares a regular method to a class method
# in terms of inheritance.

# Example A (no class method)
# ---------------------------

class Parent():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def friend(self, friend_name, age):
        return Parent(friend_name, age)

class Child(Parent):
    def __init__(self, name, age, other):
        super().__init__(name, age)
        self.other = other

child = Child('Loki', 1048, 'something else')
friend = child.friend('Thor', 1049)

print(child.name)   # Loki
print(child.age)    # 1048
print(child.other)  # something else
print(friend.name)  # Thor
print(friend.age)   # 1049
print(child)        # <__main__.Child object at 0x10150e668>
print(friend)       # <__main__.Parent object at 0x10150e6a0>


# Example B (class method)
# ------------------------

class Parent():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def friend(cls, friend_name, *args):
        return cls(friend_name, *args)

class Child(Parent):
    def __init__(self, name, age, other):
        super().__init__(name, age)
        self.other = other

child = Child('Loki', 1048, 'something else')
friend = child.friend('Thor', 1049, 'another thing')

print(child.name)    # Loki
print(child.age)     # 1048
print(child.other)   # something else
print(friend.name)   # Thor
print(friend.age)    # 1049
print(friend.other)  # another thing
print(child)         # <__main__.Child object at 0x10150e748>
print(friend)        # <__main__.Child object at 0x10150e780>

# The first example is pretty much what we expect. In the next example,
# the class method and the use of cls instead of self basically maps the
# method to whatever class is calling it, therefor friend is now an instance
# of the Child class, even though its been defined in the Parent class.

# NOTE: you can also write class methods outside of classes. You might do this
# if you wanted to create a class method that you could call on many classes.

# TODO: example of class method outside of class


# Static methods
# -----------------------------------------------------------------------------
# The third type of method in a class def is a static method. Static methods
# are associated only with a class (something like class variables), rather
# than a specific object instance. Hence, they have no self argument. They know
# nothing about the class or instance they were called on and behave like plain
# functions except that you can call them from an instance or the class.

class A():
    @staticmethod
    def note():
        print('This is a static method')

A.note()

# Note also that if you want to use the static method within the class istelf,
# you can call it in the very same way:

class A():
    @staticmethod
    def note():
        print('This static method can be used throughout the class')

    def do_something(self):
        # do something
        A.note()


# Review: an interesting example
# -----------------------------------------------------------------------------

class Coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "Coordinates: " + str(self.__dict__)

def add(a, b):
    return Coordinate(a.x + b.x, a.y + b.y)

def sub(a, b):
    return Coordinate(a.x - b.x, a.y - b.y)

one = Coordinate(100, 200)
two = Coordinate(300, 200)

print(add(one, two))  # Coordinates: {'x': 400, 'y': 400}


# Summary of Terms
# -----------------------------------------------------------------------------
# Class:
#     template for creating objects. All objects created using
#     the same class will have the same characteristics.
# Object:
#    an instance of a class.
# Instantiate:
#    create an instance of a class.
# Method:
#    a function defined in a class.
# Attribute:
#    a variable bound to an instance of a class, however...

# Technically, in Python, data, properties, and methods are all attributes on
# a class. The fact that a method is callable does not distinguish it from
# other types of attributes. Methods are just callable attributes, and
# properties are just customizable attributes. Methods should typically
# represent actions; things that can be done to, or performed by, the object.
# When you call a method, even with only one argument, it should do something.
# Method names are generally verbs.

# If we determine that an attribute is not an action, we need to decide between
# standard data attributes and properties. In general, always use a standard
# attribute until you need to control access to that property in some way.
# In either case, your attribute is usually a noun. The only difference between
# an attribute and a property is that we can invoke custom actions
# automatically when a property is retrieved, set, or deleted.


# Classes and Objects versus Modules
# -----------------------------------------------------------------------------
# Objects are most useful when you need a number of individual instances that
# have similar behavior (methods), but differ in their internal attributes.
# Classes support inheritance, modules don't. If you want only one of
# something, a module might be best. No matter how many times a Python module
# is referenced in a program, only one copy is loaded. If you have a number of
# variables that contain multiple values and can be passed as arguments to
# multiple functions, it might be better to define them as classes.
# For example, you might use a dictionary with keys size and color to represent
# an image. You could create a different dictionary for each image in your
# program, and pass them as arguments to functions such as scale() or
# transform(). This can get messy as you add more keys and functions.
# It's simpler to define an Image class with attributes size or color and
# methods scale() and transform(). Then, all the data and methods for a color
# image are defined in one place. Use the simplest solution to the problem.
# A dict, list, or tuple is simpler, smaller, and faster than a module, which
# is usually simpler than a class.


# see also:
# - polymorphism.py
# - inheritance.py
# - composition.py
# - data_classes.py
