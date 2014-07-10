#! /usr/bin/env python

from Tkinter import *


def func():
    print "Salut!"

root = Tk()
b2 = Button(root, text="afisare", command=func)
b2.pack()
b = Button(root, text="quit", command=root.destroy)
b.pack()
root.mainloop()
