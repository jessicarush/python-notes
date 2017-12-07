# -----------------------------------------------------------------------------
# Jupyter Notebook
# -----------------------------------------------------------------------------
# Jupyter Notebook is a hybrid editor and interactive shell that runs in the
# browser. It works really well for exploring large sets of data. It does not
# replace your regular editor or IDE (which is more useful for working with
# multiple files and projects) but definitely worth considering if you need to
# explore your datasets and test your code before implementing.

# $ pip3 install jupyter

# If you intend on working with excel files, you should also install:

# $ pip3 install xlrd

# Once installed, start a jupyter session by navigating to your working
# directory in the command line, then launch:

# $ jupyter notebook

# This will launch a jupyter session in a new browser window. You will see
# all your files listed from your current working directory.

# From the dropdown in the top right corner, choose to create a new python
# notebook. Python is listed as the only type of notebook because we installed
# jupyter via python with pip. This opens a new untitled tab. When you give it
# a name and you'll see a new .ipynb file and folder show up in your working
# directory. The .ipynb file allows you to return to your previous saved
# session (follow the same steps to launch jupyter, but instead of creating a
# new session, select the .ipynb file).

# The editable field here is the shell. You can enter in as many lines of code
# as you want. Hitting the return key will not execute the code. When you are
# ready to execute hit ctrl + return.

# At this point you can continue to edit the code in the first shell 'cell',
# or you can create a new 'cell' by hitting option/alt + return. You can
# execute your code and immediately create a new 'cell' with shift + return.

# To remove a 'cell', press esc, then dd
# To add a cell without executing press esc, then b

# You can find more shortcuts under the help menu

# To view data try this:
# – In a new jupyter 'cell':
#   import pandas

# – In a second cell:
#   df = pandas.read_csv('data/supermarkets.csv')
#   df

# When you execute the second cell, you should see the data displayed in a
# friendly, easy-to-read table. Note the header rows in CSV files are shown
# in bold text. Try setting the header arg to None as demonstrated earlier to
# see the difference.

# Another nice feature of jupyter is the ability to get help on methods or
# classes by typing a question mark:

# df.set_index?

# Will open a window with detailed help... really nice.

# When you are finished working, logout of the browser windows. Back in the
# command line window, CTRL C, then enter 'y' to quit:

# The Jupyter Notebook is running at:
# http://localhost:8888/?token=d1ac3...
# Shutdown this notebook server (y/[n])? y
# [C 10:16:08.918 NotebookApp] Shutdown confirmed
