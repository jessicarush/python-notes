'''tkinter'''

# a graphic library, Tkinter is Python's standard GUI (Graphical User Interface) package. It is a thin object-oriented layer on top of Tcl/Tk.

# https://docs.python.org/3/library/tk.html
# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
# http://www.tkdocs.com/ - looks really good
# https://wiki.tcl.tk/37973

import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# Note that everything in Tk is a window, and objects are places in a hierarchy.
# In terms of how to display the applications widgets (the things you want to
# appear within the window), you would use one of three different 'geometry
# managers'. The most useful is the grid manager. The pack manager is the
# simplest as is place.

mainWindow = tkinter.Tk()
mainWindow.title('Top Hats & Bees')
mainWindow.geometry('640x480+100+20')

# The numbers following the window size are the optional positioning from the
# top left. You can use negative numbers to go from the bottom right.

# .pack()---------------------------------------------------------------------

# use fill in canvas.pack() to have the canvas fit to the mainWindow.
# Acceptable values here are tkinter.X, tkinter.Y or tkinter.Both
# canvas.pack(side='top', fill=tkinter.BOTH, expand=True)

# when widgets share the same side, they're placed in the order they're
# "packed". You can use anchor to move things n, s, e, w but this will only
# work for the axis opposite to their side. (i.e. if you've aligned to the left
# you can only anchor n, s).

label = tkinter.Label(mainWindow, text="Something")
label.pack(side='top')

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.pack(side='left', anchor='n')

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', fill=tkinter.Y, expand=True)

button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')

mainWindow.mainloop()

# .place() -------------------------------------------------------------------

# works by setting the absolute position for at least one window and placing
# other elements relative to it. Unless you know the single screen size you're
# programming for, its not super helpful.

# .grid() --------------------------------------------------------------------

label = tkinter.Label(mainWindow, text="Something")
label.grid(row=0, column=0)

leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)

# possible relief types: flat, groove, raised, ridge, solid, or sunken

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.grid(row=1, column=0)

rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2, sticky='n')

button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

# configure columns:
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)

# configure frames:
leftFrame.config(relief='sunken', borderwidth=1)
rightFrame.config(relief='sunken', borderwidth=1)
leftFrame.grid(sticky='ns')
rightFrame.grid(sticky='new')
rightFrame.columnconfigure(0, weight=1)

# configure buttons:
button3.grid(sticky='ew')

# this function always at the end:
mainWindow.mainloop()

# sticky ---------------------------------------------------------------------

# By default, if a cell is larger than the widget contained in it, the widget
# will be centered within it, both horizontally and vertically, with the
# master's background showing in the empty space around it. The "sticky" option
# can be used to change this default behavior.

# The value of the "sticky" option is a string of 0 or more of the compass
# directions "nsew", specifying which edges of the cell the widget should be
# "stuck" to. So for example, a value of "n" (north) will jam the widget up
# against the top side, with any extra vertical space on the bottom; the widget
# will still be centered horizontally. A value of "nw" (north-west) means the
# widget will be stuck to the top left corner.

# weight ---------------------------------------------------------------------

# Every column and row has a "weight" grid option associated with it, which
# tells it how much it should grow if there is extra room to fill. By default,
# the weight of each column or row is 0, meaning don't expand to fill space.
# For the user interface to resize, you need to give a positive weight to the
# columns you'd like to expand. This is done using the "columnconfigure" and
# "rowconfigure" methods of grid. If two columns have the same weight, they'll
# expand at the same rate; if one has a weight of 1, another of 3, the latter
# one will expand three pixels for every one pixel added to the first.

# tkinter.ttk ----------------------------------------------------------------

# The tkinter.ttk module provides access to the Tk themed widget set,
# introduced in Tk 8.5. The basic idea for tkinter.ttk is to separate, to the
# extent possible, the code implementing a widget’s behavior from the code
# implementing its appearance. Using the Ttk widgets gives the application an
# improved look and feel. Seems way better than the methods above.

# example Tk code:

# l1 = tkinter.Label(text="Test", fg="black", bg="white")
# l2 = tkinter.Label(text="Test", fg="black", bg="white")

# example Ttk code:

# style = ttk.Style()
# style.configure("BW.TLabel", foreground="black", background="white")

# l1 = ttk.Label(text="Test", style="BW.TLabel")
# l2 = ttk.Label(text="Test", style="BW.TLabel")

# https://docs.python.org/3/library/tkinter.ttk.html
# http://www.tkdocs.com/tutorial/grid.html
