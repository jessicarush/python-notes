'''tkinter example - (NOT a functioning calculator)'''


import tkinter as tk
from tkinter import ttk


def click(key):
    '''dummy function for testing purposes only'''
    if (key == 'C') or (key == 'CE'):
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, key)


# Button text is stored as a list of row lists. The list items here are tuples,
# where the second value is being used as the colspan in the code below:
keys = [[('C', 2), ('CE', 2)],
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('0', 1), ('=', 2), ('/', 1)],]

# Using a variable for padding, since it's also used to calculate window size:
mainWindowPadding = 8

# Main window setup:
mainWindow = tk.Tk()
mainWindow.title("Calculator")
mainWindow.geometry('50x50-25-25')
mainWindow['padx'] = mainWindowPadding

# example style some ttk elements:
style = ttk.Style()

# A bug caused by the 'aqua' ttk style on Mac OSX makes it so that some
# elements won't drop the light gray background color. Classic should fix it:
style.theme_use('classic')
style.configure("test.TLabel", foreground="magenta", background="yellow")

# Example ttk window label:
label = ttk.Label(mainWindow, text='tkinter example', padding=(38,5,38,5),
                  style='test.TLabel')
label.grid(row=0, column=0)

# Result field:
# A "width" configuration option may be specified to provide the number of
# characters wide the entry should be.
entry = tk.Entry(mainWindow)
entry.grid(row=1, column=0, sticky='nsew')
entry.config(width=10)

# Key pad:
keyPad = tk.Frame(mainWindow)
keyPad.grid(row=2, column=0, sticky='nsew')

# padx and pady are intended to add external padding - the value can be a
# number or a tuple (5, 15) for separate left, right - top, bottom values.
# ipadx and ipady are intended to add internal padding - the value can only
# be a number, not a tuple. These don't appear to work consistently. In the
# example below both ipady and pady give the same result:

row = 0
for keyRow in keys:
    col = 0
    for key in keyRow:
        cmd = lambda x=key[0]: click(x)
        tk.Button(keyPad, text=key[0], command=cmd).grid(
            row=row, column=col, columnspan=key[1], sticky='nsew', ipadx=5)
        col += key[1]
    row += 1

# Set the minsize(), and a maxsize() of the window using the width and height
# of the keyPad element - .winfo_height() and winfo_width() methods.
# This won't work unless we force the window to draw the widgets first by
# calling its .update() method:

mainWindow.update()

mainWindow.minsize((keyPad.winfo_width() + mainWindowPadding * 2),
    (entry.winfo_height() + keyPad.winfo_height() + label.winfo_height()
    + mainWindowPadding))

mainWindow.maxsize((keyPad.winfo_width() + mainWindowPadding * 2),
    (entry.winfo_height() + keyPad.winfo_height() + label.winfo_height()
    + mainWindowPadding))

mainWindow.mainloop()
