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
