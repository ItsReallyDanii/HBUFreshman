######################################################################################################################
# Name:
# Date:
# Description:
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
		mx = ((other.X - self.X)/2)
		my = ((other.Y - self.Y)/2)

		if (mx < 0 and my < 0):
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
		verticies = [Point(WIDTH  / 2.0 + 1 * 2 - 1), Point(0 + 1 * 2 - 1), Point(WIDTH - 1 - 1, HEIGHT - 1 - 1), Point(WIDTH - 1 - 1, HEIGHT - 1 - 1)]
		for v in verticies:
			self.plot(v, "red", 1)

		for i in range(n):
			v = verticies[randint(0, len(verticies) - 1)]
			if (i ==0):
				p = verticies[randint(0, len(verticies) - 1)]
				while (p == v):
					p = verticies[randint(0, len(verticies) - 1)]
			p = Point.midpt(v)
			self.plot(p, "blue", 0.5)

	# plot a single point with the radius specified and in the color specified
	def plot(self, point, radius, color):
		self.create_oval(point.x, self.Y, self.X, self.Y, outline = "black", fill = "blue", width = 1)

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


c1 = Point(4,3)
c2 = Point(0,0)
print c1.__str__()
print c1.dist(c2)
print c1.midpt(c2)



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
