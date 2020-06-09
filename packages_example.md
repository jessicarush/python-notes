# Packages Example

This example demonstrates how to organize modules into file hierarchies. Note that a *package* is a collection of Python *modules*. While a module is a single Python file, a package is a directory of Python modules containing an additional `__init__.py` file, which distinguishes a package from a directory that just happens to contain a bunch of Python scripts.

Our directory structure for this example will look like so:

```
packages_example
├─ sources
│ ├─ __init__.py
│ ├─ daily.py
│ └─ weekly.py
└─ weather.py
```

## package: sources/\__init__.py

In the sources directory you'll need to create a file named `__init__.py`. This file can be empty. Python needs it to treat the directory containing it as a package.

Note that this `__init__.py` file runs as soon as you import anything from the package. It can be used to set some shared variables or execute some "initialization" code. That being said, programmers do not expect actual logic to happen in this file so keep it at that.

## module 1: sources/daily.py

```python
def forecast():
    '''Daily forecast'''
    return 'Like yesterday'
```


## module 2: sources/weekly.py

```python
def forecast():
    '''Weekly forecast'''
    return['snow', 'clear', 'sleet', 'rain', 'freezing rain', 'fog', 'hail']
```


## main program: weather.py

```python
from sources import daily, weekly

print('daily forecast:', daily.forecast())
print('weekly forecast:')

for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)
```

The enumerate function above takes apart a list and feeds each item to the for loop, adding a number to each item starting from 1. The expected output would be:

```pytb
daily forecast: Like yesterday
weekly forecast:
1 snow
2 clear
3 sleet
4 rain
5 freezing rain
6 fog
7 hail
```

## Importing specific function/classes

If you wanted to import a function or class from a module that's within a package you'd say:

```python
from sources.daily import forecast
```

## Importing between packages

For this example let's add to our directory structure:

```
packages_example
├─ sources
│ ├─ __init__.py
│ ├─ daily.py
│ └─ weekly.py
├─ testing
│ ├─ __init__.py
│ ├─ demo.py
└─ weather.py
```

I can import packages into other packages using the same syntax as above, provided the final call happens in the main program. For example:

testing/demo.py
```python
from sources.daily import forecast

def myfunction():
    print('Testing myfunction:', forecast())
```

weather.py
```python
from testing.demo import myfunction

myfunction()
```

This works great. Provided your program is always being invoked from your main script, this is all you'll ever need to do, however, if you try to run demo.py directly, it will NOT work. You'll get a traceback that the sources module could not be found. Note this:

**When running a script directly, it is impossible to import anything from its parent directory.**

To be clear, the python `import` statement searches through the list of paths contained in the variable `sys.path`. The very first item in the `sys.path` list happens to be the path to the script currently invoked on the command line (`sys.path[0]`). For example:

If I print out the value of `sys.path[0]` from *weather.py*:
```python
import sys

print ('path to weather.py:', sys.path[0])
```

I'll get this:

```pytb
path to weather.py: /Users/jessicarush/Documents/Coding/Python/programs/packages_example
```

If I print out the value of `sys.path[0]` from *testing/demo.py*:
```python
import sys

print ('path to demo.py:', sys.path[0])
```

I'll get this:

```pytb
path to demo.py: /Users/jessicarush/Documents/Coding/Python/programs/packages_example/testing
```

As it turns out, after initialization, Python programs can modify `sys.path`. So the following would allow us to run *testing/demo.py* without errors:

```python
import sys

sys.path.insert(1, sys.path[0] + '/../')
# inserts the following path:
# /Users/jessicarush/Documents/Coding/Python/programs/packages_example/testing/../

from sources.daily import forecast


def myfunction():
    print('Testing myfunction:', forecast())

myfunction()
```

This allows me to run both *weather.py* and *testing/demo.py*. I would think the situations where you would need to do this would be pretty slim.


## More on sys.path and PYTHONPATH

So we know python imports search through the directories in `sys.path`.

Python’s documentation for sys.path describes it as…

> A list of strings that specifies the search path for modules. Initialized from the environment variable PYTHONPATH, plus an installation-dependent default.
>
> As initialized upon program startup, the first item of this list, path[0], is the directory containing the script that was used to invoke the Python interpreter. If the script directory is not available (e.g. if the interpreter is invoked interactively or if the script is read from standard input), path[0] is the empty string, which directs Python to search modules in the current directory first. Notice that the script directory is inserted before the entries inserted as a result of PYTHONPATH.

In short `sys.path` is initialized from these locations:

- The directory containing the input script (or the current directory when no file is specified). In other words: If the Python interpreter is run interactively, sys.path[0] is an empty string ''. This tells Python to search the current working directory from which you launched the interpreter, i.e., the output of `pwd`. If we run a script with `python <script>.py`, sys.path[0] is the path to `<script>.py.`
- PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).
- The installation-dependent defaults.

We know we can modify `sys.path` in our scripts using the `insert()` method as demonstrated above, but what about PYTHONPATH?

PYTHONPATH is an environment variable which you can set to add additional directories where python will look for modules and packages. For most installations, you shouldn't need to touch these variables. Python knows where to find its standard library. To learn more see the [python documentation](https://docs.python.org/3/using/cmdline.html#environment-variables).
