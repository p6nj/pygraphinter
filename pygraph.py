from tkinter import (
    END,
    Button,
    Entry,
    Label,
    Tk,
    Spinbox,
)
from math import sin, cos, pi
from PIL import Image, ImageDraw


def Graph(save: bool, expr: str, order: int, size: int):
    if not order:
        order = 6
    if not size:
        size = 1000

    im = Image.new("1", (size + 1,) * 2, 1)
    draw = ImageDraw.Draw(im)

    def link(a: int, b: int):
        draw.line(points[a] + points[b], fill=0)

    points = [
        (
            int((size / 2) * sin(2 * pi * i / order) + size / 2),
            int((size / 2) * cos(2 * pi * i / order) + size / 2),
        )
        for i in range(order)
    ]
    result = a = b = None
    for a in range(order):
        try:
            im.putpixel(points[a], 0)
        except IndexError as e:
            print(f"{e}: {points[a]}/{im.size}")
        for b in range(order):
            result = eval(expr)
            if result:
                link(a, b)
    if save:
        im.save("output.bmp")
    im.show()


def save():
    Graph(True, eExp.get(), int(eOrder.get()), int(eSize.get()))


def show():
    Graph(False, eExp.get(), int(eOrder.get()), int(eSize.get()))


initialexpr = "(a+1)%(b+1)==0"
w = Tk()
lExp = Label(w, text="Expression:")
eExp = Entry(w)
eExp.insert(END, initialexpr)
lOrder = Label(w, text="Order:")
eOrder = Spinbox(w, from_=1, to=10000)
eOrder.insert(0, "1")
lSize = Label(w, text="Size:")
eSize = Spinbox(w, from_=2, to=10000)
eSize.insert(0, "100")
bShow = Button(w, text="Show", command=show)
bSave = Button(w, text="Save", command=save)
lExp.grid(column=1, row=1)
lOrder.grid(column=1, row=2)
lSize.grid(column=1, row=3)
bShow.grid(column=1, row=4)
bSave.grid(column=2, row=4)
eExp.grid(column=2, row=1)
eOrder.grid(column=2, row=2)
eSize.grid(column=2, row=3)
w.mainloop()
