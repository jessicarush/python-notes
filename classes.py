# A string and an integer are examples of built-in Python classes. 
# A class is logical grouping of data and functions. The "integer" class 
# is like an instruction manual for constructing "integer" objects.

# to make your own custom object, you'll need to first define a class by using the class keyword.

class Person():
    pass

# you can create an object from a class by calling it as if it were a function:

henry = Person()

# in this case, Person() creates an individual object from the Person class and assigns it the name henry.

class Person():
    def __init__(self):
        pass

# The __init__ is a special method that initializes an individual object from its class definition. 
# The self argument specifies that it refers to the individual object itself. 
# When you define __init__() in a class definition, its firs parameter should always be self. 
# Although self is not a reserved word in Python, it's common usage.

class Person():
    def __init__(self, name):
        self.name = name

astronaut = Person('Roberta Bondar')

# note the name value passed in is saved with the object as an attribute. You can read and write it directly:

print(astronaut.name)

# it is NOT necessary to have an __init__ method in every class definition. 
# It's used to do anything that's needed to distinguish this object from others created from the same class

# Inheritance
# Creating a new class from an existing class but with some additions or changes. 
# When you use inheritance, the new class can automatically use all the code from the old class 
# without copying any of it. You only define what you need to add or change in the new class 
# and this overrides the behaviour of the old class. 
# The original class is the parent, superclass or base class. 
# The new one is the child, subclass or derived class.

class Car():
    pass

class Honda(Car):
    pass

a_car = Car()
a_honda = Honda()

# the object called a_honda is an instance of the class Honda, but it also inherits whatever Car can do.
# unless there is an override of a parents function in the child's:

class Person():
    def __init__(self, name):
        self.name = name

class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name

person = Person('Fudd')
doctor = MDPerson('Fudd')

print(person.name)
print(doctor.name)

# super()
# If you override a method like __init__ , you can retrieve attributes back from the parent using super():

class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

# The above could be written like this:

class EmailPerson(Person):
    def __init__(self, name, email):
        self.name = name 
        self.email = email

# But then we would loose our inheritance. If the definition of the parent class changes, 
# using super() ensures the child will inherit the changes.

# some object oriented languages support private object attributes that can't be accessed from the outside. 
# They have to write getter and setter methods to read and write the values on these private attributes. 
# Python doesn't need these because all attributes and methods are public. 
# A good way to hide attributes is to use property(). The naming convention for hidden attributes is __whatever

class Person():
    def __init__(self, input_name):
        self.__name = input_name
    def get_name(self):                     # the getter
        print('inside the getter')
        return self.__name
    def set_name(self, input_name):         # the setter
        print('inside the setter')
        self.__name = input_name
    name = property(get_name, set_name)

# similar too:

class Person():
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name

someone = Person('howard')
someone.name = 'harry'
print(someone.__name)    # This will raise an exception


# @property
# making a method behave like an attribute. This essentially makes a read-only attribute.

class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

c = Circle(5)
print(c.diameter)
c.radius = 7
print(c.diameter)
c.diameter = 4      # This will raise an exception

# Set a setter for the method too:

class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius
    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2.0    # remember to specify floats when dividing 

c.diameter = 20     # now this will work

# instance methods
# Some data(attributes) and functions(methods) are part of the class itself and some are part of the 
# objects that are created from that class. When you see an initial self argument in methods within a 
# class def, it's an instance method. These are the types of methods you normally write. 
# The first parameter of an instance method is self.

# class methods
# A class method affects the class as a whole. Any change you make to the class affects all of its objects. 
# Use a @classmethod decorator to indicate the following function is a class method. 
# The first parameter to the method is the class itself, cls (which is used because class is already taken).

# this class method will count how many objects have been made from it:

class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A")
    @classmethod
    def children(cls):
        print("A has", A.count, "objects made from it.")

# testing:

test1 = A()
test2 = A()
test3 = A()
test4 = A()
A.children()

# static methods
# The third type of method in a class definition is a static method. If affects neither the class nor its objects.
# It's just there for convenience. begin with an @static method decorator with no initial self or class parameter:

class A():
    @staticmethod
    def note():
        print('This is a static method')

A.note()
