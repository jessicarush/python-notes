'''A study of inheritance'''


# see first: classes.py, composition.py

# This is a demonstration of multiple inheritance through a simple real estate
# application that allows an agent to manage properties for purchase or rent.
# The classes are not intended to represent complete, production-ready code.

class Property():
    '''A superclass from which all property types can extend.'''
    def __init__(self, sqft='', beds='', baths='', **kwargs):
        super().__init__(**kwargs)
        self.sqft = sqft
        self.beds = beds
        self.baths = baths

    def display(self):
        print("property details".title())
        print("–" * 16)
        print(f"square footage: {self.sqft}")
        print(f"bedrooms: {self.beds}")
        print(f"bathrooms: {self.baths}\n")

    @staticmethod
    def prompt_init():
        return dict(sqft=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))

# We've included a call to super().__init__ in case we are not the last call
# in the multiple inheritance chain. In this case, we're consuming the keyword
# arguments because we know they won't be needed at other levels of the
# inheritance hierarchy.


class Apartment(Property):
    '''A representation of a apartment property.'''
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print("apartment details".title())
        print(f"laundry: {self.laundry}")
        print(f"balcony: {self.balcony}")

    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = get_valid_input("What kind of laundry facilities... ",
            Apartment.valid_laundries)
        balcony = get_valid_input("Does it have a balcony... ",
            Apartment.valid_balconies)
        parent_init.update({'laundry': laundry, 'balcony': balcony})
        return parent_init

# The display() and __init__() methods call their respective parent class
# methods using super() to ensure the Property class is properly initialized.


class House(Property):
    '''A representation of a house property.'''
    valid_garage = ("attached", "detached", "none")
    valid_fence = ("yes", "no")

    def __init__(self, floors='', garage='', fence='', **kwargs):
        super().__init__(**kwargs)
        self.floors = floors
        self.garage = garage
        self.fence = fence

    def display(self):
        super().display()
        print("house details".title())
        print(f"floors: {self.floors}")
        print(f"garage: {self.garage}")
        print(f"fence: {self.fence}")

    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        floors = input("How many floors? ")
        garage = get_valid_input("Does it have a garage... ",
            House.valid_garage)
        fence = get_valid_input("Is there a fenced yard... ",
            House.valid_fence)
        parent_init.update({'floors': floors, 'garage': garage, 'fence': fence})
        return parent_init


def get_valid_input(input_string, valid_options):
    '''A helper function: get user input and check against valid options'''
    input_string += f"{', '.join(valid_options)}? "
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class Purchase():
    '''A representation of a property for sale.'''
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print("purchase details".title())
        print(f"selling price: {self.price}")
        print(f"estimated taxes: {self.taxes}")

    @staticmethod
    def prompt_init():
        return dict(price=input("Selling price? "),
                    taxes=input("Estimated taxes? "))

# These two classes don't have a superclass (other than object), but we still
# call super().__init__ because they are going to be combined with the other
# classes, and we don't know what order the super calls will be made in.


class Rental():
    '''A representation of a property for rent.'''
    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        super().display()
        print("rental details".title())
        print(f"rent: {self.rent}")
        print(f"estimated utilities: {self.utilities}")
        print(f"furnished: {self.furnished}")

    @staticmethod
    def prompt_init():
        return dict(rent=input("Monthly rent? "),
                    utilities=input("Estimated utilities? "),
                    furnished = get_valid_input("Furnished? ", ("yes", "no")))

# The interface of Rental and Purchase is similar to that used for House and
# Apartment, which is very useful when we combine the functionality of these
# four classes in separate subclasses. For example:

class HouseRental(Rental, House):
    '''A representation of a house for rent.'''
    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init


class HousePurchase(Purchase, House):
    '''A representation of a house for sale.'''
    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init


class AptRental(Rental, Apartment):
    '''A representation of a apartment for rent.'''
    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init


class AptPurchase(Purchase, Apartment):
    '''A representation of a apartment for sale.'''
    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

# This is slightly surprising, as the class on its own has neither an __init__
# nor display method. Because both parent classes appropriately call super in
# these methods, we only have to extend those classes and the classes will
# behave in the correct order. This is not the case with prompt_init, of
# course, since it is a static method that does not call super, so we
# implement this one explicitly.

# NOTE: the order of the inherited classes here (Rental, House) is important.
# When display() is called on HouseRental, it goes to the Rental version of
# the method first, which then calls super.display() to get the House version,
# which again calls super.display() to get the property version. If we switched
# the order, display would refer to the House class's display(). When super
# is called there it goes directly to the method on the Property parent class.
# This means Rental class's display method never gets called! You might think
# we could have added a super call to Property.display(), but that will fail
# because the next superclass of Property is Object, and Object doesn't have
# a display method. Given this logic, I'm not sure how the super().display()
# in Rental routes over to House and not Object but there you have it. If you
# are uncomfortable with this, you could always resolve this be having Rental
# and Purchase extend the Property class as well instead of deriving directly
# from object.

# The moral of the story: Methods on parent classes can be called using super
# and argument lists must be formatted safely for these calls to work when
# using multiple inheritance!


# How it works so far:
# -----------------------------------------------------------------------------
# The idea is first you would run the prompt_init static method to collect
# the information via input and return a dictionary of all the key/values
# (attributes) for the property. Then, you pass that dictionary to the actual
# new object:

info = HouseRental.prompt_init()

house1 = HouseRental(**info)

house1.display()

# Instead though, we'll put this in an Agent class which will be responsible
# for creating new listings and displaying existing ones.


class Agent():
    '''An interface for creating and storing property listings.'''
    def __init__(self):
        self.property_list = []

    def display_properties(self):
        for p in self.property_list:
            p.display()

    type_map = {
        ('house', 'rental'): HouseRental,
        ('house', 'purchase'): HousePurchase,
        ('apartment', 'rental'): AptRental,
        ('apartment', 'purchase'): AptPurchase,
        }

    def add_property(self):
        property_type = get_valid_input(
            "What type of property... ", ("house", "apartment")).lower()
        payment_type = get_valid_input(
            "Payment... ", ("purchase", "rental")).lower()
        PropertyClass = self.type_map[(property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))


# To test:
agent = Agent()
agent.add_property()
agent.add_property()
agent.display_properties()
