from tkinter import Button, Label, Tk, Canvas, Toplevel
from tkinter.simpledialog import askstring, askinteger
from math import sin, cos, pi


def Graph(expr: str, order: int = 0, canvassize: int = 0):
    if not canvassize:
        canvassize = 1000
    if not order:
        order = 500

    def link(a: int, b: int):
        can.create_line(points[a][0], points[a][1], points[b][0], points[b][1])

    points = [
        (
            (canvassize / 2) * sin(2 * pi * i / order) + canvassize / 2 + 5,
            (canvassize / 2) * cos(2 * pi * i / order) + canvassize / 2 + 5,
        )
        for i in range(order)
    ]
    w = Toplevel()
    w.title("(a,b) in V if " + expr)
    can = Canvas(w, width=canvassize + 10, height=canvassize + 10)
    can.pack()
    result = a = b = None
    for a in range(order):
        can.create_rectangle(
            (
                (canvassize / 2) * sin(2 * pi * a / order) + canvassize / 2 + 5,
                (canvassize / 2) * cos(2 * pi * a / order) + canvassize / 2 + 5,
            )
            * 2
        )
        for b in range(order):
            result = eval(expr)
            if result:
                link(a, b)


if __name__ == "__main__":

    def showexamples():
        for expr in ["(a+1) % (b+1) == 0", "a==b*2", "a==b**2"]:
            Graph(expr)

    w = Tk()
    w.resizable(False, False)
    w.title("Expression defined graph generator")
    lb = Label(w, text="Welcome to my graph generator!\nPlease choose an option:")
    ex = Button(w, text="See examples", command=showexamples)
    us = Button(
        w,
        text="Enter expression",
        command=lambda: Graph(
            askstring(
                "Expression input",
                "Enter boolean expression using (a,b) as the two points (from 0):",
                initialvalue="a==b*2",
            ),
            askinteger("Order input", "Enter the number of points:", initialvalue=500),
        ),
    )
    lb.pack(padx=2)
    ex.pack(side="left")
    us.pack()
    w.mainloop()
