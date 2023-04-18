from tkinter import Tk, Canvas
from math import sin
w = Tk()
can = Canvas(w,width=600,height=600)
can.pack()
a=300
for i in range(10):
    can.create_rectangle((sin(i),3)*2)
w.mainloop()
