# Classes
# A string and an integer are examples of built-in Python classes. 
# A class is logical grouping of data and functions. 
# The "integer" class is like an instruction manual for constructing "integer" objects.
# To make your own custom object, you'll need to first define a class by using the class keyword.

class Person():
    pass

# You can create an object from a class by calling it as if it were a function:

henry = Person()

# In this case, Person() creates an individual object from the Person class and assigns it the name henry.

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

# Note the name value passed in is saved with the object as an attribute. You can read and write it directly:

print(astronaut.name)

# It is NOT necessary to have an __init__ method in every class definition. 
# It is used to do anything that's needed to distinguish this object from others created from the same class

# Inheritance
# Creating a new class from an existing class but with some additions or changes. 
# When you use inheritance, the new class can automatically use all the code from the old class 
# without copying any of it. You only define what you need to add or change in the new class and
# this overrides the behaviour of the old class. 
# The original class is the parent, superclass or base class. 
# The new one is the child, subclass or derived class.

class Car():
    pass

class Honda(Car):
    pass

a_car = Car()
a_honda = Honda()

# The object called a_honda is an instance of the class Honda, but it also inherits whatever Car can do.
# Unless there is an override of a parents function in the child's:

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

# Some object oriented languages support private object attributes that can't be accessed from the outside. 
# They have to write getter and setter methods to read and write the values on these private attributes. 
# Python doesn't need these because all attributes and methods are public. 
# A good way to hide attributes is to use property(). The naming convention for hidden attributes is __whatever.

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
# Makes a method behave like an attribute. This essentially creates a read-only attribute.

class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

# testing:

c = Circle(5)
print(c.diameter)
c.radius = 7
print(c.diameter)
c.diameter = 4      # This will raise an exception

# Create a setter to make the method also accept new values:

class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius
    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2.0    # remember to specify floats when dividing 

# testing:

c.diameter = 20     # now this will work

# Instance methods
# Some data(attributes) and functions(methods) are part of the class itself and some are part of the 
# objects that are created from that class. When you see an initial self argument in methods within a 
# class def, it's an instance method. These are the types of methods you normally write. 
# The first parameter of an instance method is self.

# Class methods
# A class method affects the class as a whole. Any change made to the class affects all of its objects. 
# Use the @classmethod decorator to indicate the following function is a class method. 
# The first parameter to the method is the class itself: cls (is used because class is already taken).

# This class method will count how many objects have been made from it:

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

# Static methods
# The third type of method in a class def is a static method. If affects neither the class nor its objects.
# It's just there for convenience. Begin with the @static method decorator, no initial self or class parameter:

class A():
    @staticmethod
    def note():
        print('This is a static method')

A.note()

# In this example note how the subclasses are using the parents __init__ method. 
# Because of this we can use the variable self.words in the subclasses.

class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'

class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'

class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'

person1 = Quote('Bob', 'Hello')
person2 = QuestionQuote('Bill', 'What')
person3 = ExclamationQuote('Bruce', 'OK')

# testing:

print(person1.who(), ': ', person1.says())
print(person2.who(), ': ', person2.says())
print(person3.who(), ': ', person3.says())

# Here's another class that has no relation to the previous classes (descendants of Quote), 
# but will use the same method names:

class BabblingBrook():
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'

brook = BabblingBrook()

# Now a function that runs the who() and says() methods of any object:

def who_says(obj):
    print(obj.who(), ': ', obj.says())

# testing:

who_says(person1)
who_says(person2)
who_says(person3)
who_says(brook)

#When to Use Classes and Objects versus Modules
# Objects are most useful when you need a number of individual instances that have 
# similar behavior (methods), but differ in their internal states (attributes).
# Classes support inheritance, modules don’t.
# If you want only one of something, a module might be best. No matter how many times a 
# Python module is referenced in a program, only one copy is loaded. 
# If you have a number of variables that contain multiple values and can be passed as 
# arguments to multiple functions, it might be better to define them as classes. 
# For example, you might use a dictionary with keys size and color to represent an image. 
# You could create a different dictionary for each image in your program, and pass them as 
# arguments to functions such as scale() or transform(). 
# This can get messy as you add more keys and functions. 
# It’s simpler to define an Image class with attributes size or color and methods scale() and transform(). 
# Then, all the data and methods for a color image are defined in one place.
# Use the simplest solution to the problem. 
# A dict, list, or tuple is simpler, smaller, and faster than a module, which is usually simpler than a class.
