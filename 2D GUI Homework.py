from Tkinter import *
from random import randint

WIDTH = 400
HEIGHT = 400
POINT_COLORS = ["red", "orange", "green", "blue", "yellow", "purple", "pink"]
POINT_RADIUS = 2
NUM_POINTS = 2500


class Points(Canvas):
    def __init__(self, master):
        Canvas.__init__(self, master, bg = "white")
        self.pack(fill = BOTH, expand = 1)


    def plotPoints(self, n):
        for i in range (n):
            x = randint(0, WIDTH - 1)
            y = randint(0, HEIGHT - 1)
            self.plot(x,y)

    def plot(self, x, y):
        color = POINT_COLORS[randint(0, len(POINT_COLORS) - 1)]
        color2 = POINT_COLORS[randint(0, len(POINT_COLORS) - 1)]
        self.create_rectangle(x, y, x + POINT_RADIUS *2, y + POINT_RADIUS*2, outline = color, fill = color2)


window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("Check out these points!")
p = Points(window)
p.plotPoints(NUM_POINTS)
window.mainloop()