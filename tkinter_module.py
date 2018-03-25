'''tkinter'''

# a graphic library, Tkinter is Python's standard GUI (Graphical User Interface)
# package. It is a thin object-oriented layer on top of Tcl/Tk.

# https://docs.python.org/3/library/tk.html
# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
# http://www.tkdocs.com/  <-- really good
# https://wiki.tcl.tk/37973
# http://effbot.org/tkinterbook/tkinter-widget-styling.htm

import tkinter as tk

# Note that everything in Tk is a window, and objects are placed in a hierarchy.
# In terms of how to display the applications widgets (the things you want to
# appear within the window), you would use one of three different 'geometry
# managers'. The most useful is the grid manager. The pack manager and place
# are the simplest.

print(tk.TkVersion)
print(tk.TclVersion)


# .pack()
# -----------------------------------------------------------------------------
# Start by creating the main window:

mainWindow = tk.Tk()
mainWindow.title('Window Title')
mainWindow.geometry('280x240+50+50')
mainWindow['pady'] = 15
mainWindow['padx'] = 15

# The numbers following the window size are the optional positioning from the
# top left. Negative numbers where rumored to go from the bottom right, but
# this doesn't appear to work.

leftFrame = tk.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', fill=tk.Y, expand=False)
# leftFrame.config(bg='red')

rightFrame = tk.Frame(mainWindow)
rightFrame.pack(side='left', anchor='n', fill=tk.BOTH, expand=True)
# rightFrame.config(bg='green')

label1 = tk.Label(leftFrame, text='kilograms (kg)')
label2 = tk.Label(leftFrame, text='grams (gm)')
label3 = tk.Label(leftFrame, text='pounds (lb)')
label4 = tk.Label(leftFrame, text='ounces (oz)')

label1.pack(side='top', anchor='w', pady=(7, 0))
label2.pack(side='top', anchor='e', pady=(3, 0))
label3.pack(side='top', anchor='e', pady=(3, 0))
label4.pack(side='top', anchor='e', pady=(3, 0))

e1=tk.Entry(rightFrame, width=14)
e1.pack(side='top', anchor='w')

t1=tk.Text(rightFrame, height=1, width=14, relief='solid', borderwidth=1)
t1.pack(side='top', anchor='w')

t2=tk.Text(rightFrame, height=1, width=14, relief='solid', borderwidth=1)
t2.pack(side='top', anchor='w')

t3=tk.Text(rightFrame, height=1, width=14, relief='solid', borderwidth=1)
t3.pack(side='top', anchor='w')

b1 = tk.Button(rightFrame, text='convert')
b1.pack(side='bottom', anchor='e')

mainWindow.mainloop()

# Use the fill argument to have an element (ie Frame) fit to the mainWindow.
# Acceptable values here are tk.X, tk.Y or tk.Both.

# The expand option tells the manager to assign additional space to the widget
# box. If the parent widget is made larger than necessary to hold all packed
# widgets, any exceeding space will be distributed among all widgets that have
# the expand option set to a non-zero value.

# When widgets share the same side, they're placed in the order they're
# "packed". You can use anchor to move things n, s, e, w but this will only
# work for the axis opposite to their side. (i.e. if you've aligned to the left
# you can only anchor n, s).


# .place()
# -----------------------------------------------------------------------------
# works by setting the absolute position for at least one window and placing
# other elements relative to it. Unless you know the single screen size you're
# programming for, its not super helpful.


# .grid()
# -----------------------------------------------------------------------------

def kg_to_other():
    grams = round((float(e1_value.get()) * 1000), 2)
    pounds = round((float(e1_value.get()) * 2.20462), 2)
    ounces = round((float(e1_value.get()) * 35.274), 2)
    t1.insert(tk.END, grams)
    t2.insert(tk.END, pounds)
    t3.insert(tk.END, ounces)

window = tk.Tk()
window.title('Unit Converter')
window.geometry('480x125-100-100')
window['padx'] = 15
window['pady'] = 15
font1 = ('Helvetica', 18, 'bold')
font2 = ('Helvetica', 11)

l1 = tk.Label(window, text='kilograms (kg)', font=font2)
l2 = tk.Label(window, text='grams (gm)', font=font2)
l3 = tk.Label(window, text='pounds (lb)', font=font2)
l4 = tk.Label(window, text='ounces (oz)', font=font2)
l1.grid(row=0, column=0, sticky='w')
l2.grid(row=0, column=1, sticky='w')
l3.grid(row=0, column=2, sticky='w')
l4.grid(row=0, column=3, sticky='w')

e1_value = tk.StringVar()
e1 = tk.Entry(window, width=12, textvariable=e1_value, font=font1, fg='azure4')
e1.grid(row=1, column=0, padx=(0, 20))

t1=tk.Text(window, height=1, width=13)
t1.grid(row=1, column=1, sticky='n')

t2=tk.Text(window, height=1, width=13)
t2.grid(row=1, column=2, sticky='n')

t3=tk.Text(window, height=1, width=13)
t3.grid(row=1, column=3, sticky='n')

b1 = tk.Button(window, text='convert', command=kg_to_other)
b1.grid(row=3, column=0, sticky='w')

window.mainloop()

# FYI relief types: flat, groove, raised, ridge, solid, or sunken


# sticky
# -----------------------------------------------------------------------------
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


# weight
# -----------------------------------------------------------------------------
# Every column and row has a "weight" grid option associated with it, which
# tells it how much it should grow if there is extra room to fill. By default,
# the weight of each column or row is 0, meaning don't expand to fill space.
# For the user interface to resize, you need to give a positive weight to the
# columns you'd like to expand. This is done using the "columnconfigure" and
# "rowconfigure" methods of grid. If two columns have the same weight, they'll
# expand at the same rate; if one has a weight of 1, another of 3, the latter
# one will expand three pixels for every one pixel added to the first.

# configure columns:
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)
# Window.columnconfigure(2, weight=3)


# tkinter.ttk
# -----------------------------------------------------------------------------
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
