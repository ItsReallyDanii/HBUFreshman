######################################################################################################################
# Name: Daniel Sleiman
# Date: 03/31/2020
# Description: Chaos Game
######################################################################################################################
from Tkinter import *
import math
from random import randint

# the 2D point class
class Point(object):
	# the constructor
	def __init__(self, x=0.0, y=0.0):
		self.X = x
		self.Y = y
	# accessors and mutators for x and y

	# calculates and returns the distance between two points
	def dist(self, other):
		dx = self.X - other.X
		dy = self.Y - other.Y
		return math.sqrt(dx**2 + dy**2)

	# calculates and returns the midpoint between two points

	def midpt(self, other):
		mx = ((other.X + self.X)/2)
		my = ((other.Y + self.Y)/2)

		if (mx < 0 or my < 0):
			return (abs(mx),abs(my))
		else:
			return (mx, my)

	# returns a string representation of the point: (x,y)
	def __str__(self):
		return "{}, {}".format(self.X, self.Y)


# the chaos game class
# inherits from the Canvas class of Tkinter
class ChaosGame(Canvas):
	# define your constants here

    # the constructor
	def __init__(self, parent):
		Canvas.__init__(self, parent, bg = "white")
		self.pack(fill = BOTH, expand = 1)

	# plays the chaos game
	def play(self, n):
		#self.plot(Point(50,30), 2, "blue")
		verticies = [Point(WIDTH  / 2, 5), Point(5, HEIGHT - 15), Point(WIDTH - 20, HEIGHT - 15)]

		for i in verticies:
			self.plot(i, "red", 50)

		for j in range(0, n):
			v = verticies[randint(0, len(verticies) - 1)]
			if (j == 0):
				p = verticies[randint(0, len(verticies) - 1)]
				while (p == v):
					p = verticies[randint(0, len(verticies) - 1)]

			mx, my = p.midpt(v)
			p = Point(mx, my)
			self.plot(p, 10, "red")

	# plot a single point with the radius specified and in the color specified
	def plot(self, point, radius, color):
        #MZ, you access the X and Y members variables of the point object by point.X and point.Y
		self.create_oval(point.X, point.Y, point.X+1, point.Y+1, outline = "black", fill = "blue", width = 1)

##########################################################
# the default size of the canvas is 600x520
# DO NOT CHANGE ANYTHING BELOW THIS
##########################################################

WIDTH = 600
HEIGHT = 520

# the number of midpoints to plot

NUM_POINTS = 50000

MINX = 10;
MAXX = WIDTH - 10;
MINY = 10;
MAXY = HEIGHT - 10 - (25 + 22 + 25 + 22 + 25);
MIDX = (MINX + MAXX) / 2;
MIDY = (MINY + MAXY) / 2;


# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("The Chaos Game")
# create the chaos game as a Tkinter canvas inside the window
s = ChaosGame(window)
# play the chaos game with at least 50000 points
s.play(NUM_POINTS)


# wait for the window to close
window.mainloop()
