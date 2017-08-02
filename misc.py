# Python philosophy
import this 

# Continuing lines with \
long_text = 'A long time ago' + \
    ' in a galaxy far, far away' + \
    ' blah blah bla'

# None
"""
None is not the same as False. Though it may look false when evaluated as a boolean,
None is technically none as seen here:
"""
    
thing = None 

def is_none(thing):
    if thing is None:
        print("it's none")
    elif thing:
        print("it's True")
    else:
        print("it must be False")

is_none(thing)
