from tkinter import Tk, Canvas
from math import sin, cos, pi
size = 600


class Place:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Point:
    def __init__(self, place: Place) -> None:
        self.place = place


class Graph:
    def __init__(self, order: int) -> None:
        self.order = order
        self.points = [Place(((size/2)*sin(2*pi*i/order)+size/2+5,
                              (size/2)*cos(2*pi*i/order)+size/2+5)*2) for i in range(i)]

    def show(self):
        w = Tk()
        can = Canvas(w, width=size+10, height=size+10)
        can.pack()
        for i in range(steps):
            can.create_rectangle(((size/2)*sin(2*pi*i/steps)+size/2+5,
                                  (size/2)*cos(2*pi*i/steps)+size/2+5)*2)


w = Tk()
can = Canvas(w, width=size+10, height=size+10)
can.pack()
for i in range(steps):
    can.create_rectangle(((size/2)*sin(2*pi*i/steps)+size/2+5,
                         (size/2)*cos(2*pi*i/steps)+size/2+5)*2)
w.mainloop()
