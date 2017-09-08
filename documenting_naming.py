# Documenting and Naming

# docstrings -----------------------------------------------------------------

# For obvious reasons, it helps to document your code. Documentation can
# include comments and docstrings, but it can also incorporate informative
# naming of variables, functions, modules, and classes. Don't be obsessive, say
# why you assigned the value. Point out why you called the variable whatever.
# If you were writing a Fahrenheit to Celsius converter:

def ftoc(f_temp):
    '''Convert Fahrenheit temperature <f_temp> to Celsius and return it.'''
    f_boil_temp = 212.0
    f_freeze_temp = 32.0
    c_boil_temp = 100.0
    c_freeze_temp = 0.0
    f_range = f_boil_temp - f_freeze_temp
    c_range = c_boil_temp - c_freeze_temp
    f_c_ratio = c_range / f_range
    c_temp = (f_temp - f_freeze_temp) * f_c_ratio + c_freeze_temp
    return c_temp

# And a little test code wouldn't hurt:

if __name__ == '__main__':
    for f_temp in [-40.0, 0.0, 32.0, 100.0, 212.0]:
        c_temp = ftoc(f_temp)
        print('%f F => %f C' % (f_temp, c_temp))

# Constants ------------------------------------------------------------------

# Python doesn't have constants, but the PEP8 stylesheet recommends using
# capital letters and underscores (e.g., ALL_CAPS) when naming variables that
# should be considered constants.

# Because we precompute values based on constant values, move them to the top
# level of the module. Then, they'll only be calculated once rather than in
# every call to the ftoc() function:

F_BOIL_TEMP = 212.0
F_FREEZE_TEMP = 32.0
C_BOIL_TEMP = 100.0
C_FREEZE_TEMP = 0.0
F_RANGE = F_BOIL_TEMP - F_FREEZE_TEMP
C_RANGE = C_BOIL_TEMP - C_FREEZE_TEMP
F_C_RATIO = C_RANGE / F_RANGE

def ftoc(f_temp):
    "Convert Fahrenheit temperature <f_temp> to Celsius and return it."
    c_temp = (f_temp - F_FREEZE_TEMP) * F_C_RATIO + C_FREEZE_TEMP
    return c_temp

# Private functions ----------------------------------------------------------

# If you're building a module that will be imported, you can identity functions
# that aren't intended to be called on their own by naming them with a leading
# underscore.

def _guts():
    pass

# Throwaway values -----------------------------------------------------------

# in the event that you need to give something a name but you have no intention
# of using it, it's acceptable to use the name '-'. The perfect example of this
# is with tuple unpacking. In the example below, I don't want the age
# information, but I need to give it a name in order to unpack the rest:

person = ('Kali', '50', 'Peru')

name, _, country = person

print(name, country)
