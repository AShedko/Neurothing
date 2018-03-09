"NeuroThing"
from tkinter import *
from time import sleep
import numpy as np
import random
from functools import *

# various props
W=600
H=900
SZ=20
LEN = 36
X0s = [10 for i in range(LEN)] + [W-10-SZ for i in range(LEN)]
Y0s = [10+SZ*1.2*i for i in range(LEN)] + [10+SZ*1.2*i for i in range(LEN)]
cols = ['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange','pink', 'purple', 'red','yellow', 'violet', 'indigo', 'chartreuse', 'lime', "#f55c4b"]

# render diodes
def draw(cv,ary=cols):
    cv.delete("all")
    for (X0,Y0) in zip(X0s,Y0s):
        cv.create_oval(X0, Y0, X0+SZ, Y0+SZ, fill=random.choice(ary))
    return 1

# Update fun
def update():
    while 1:
        # ary = eval(input())
        draw(cv)
        root.update()
        sleep(0.1)

root=Tk()
reading = StringVar()

w = Label(root, textvariable = reading)
w.pack()
cv = Canvas(root, width=W, height=H)
cv.pack()

root.after(0,update)
root.mainloop()
