######################################################################################################################
# Name: Daniel Sleiman
# Date: 03/05/2020
# Description: Plotting shapes through class inheritance
######################################################################################################################
from Tkinter import *

# the CoordinateShape system class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class CoordinateShape(Canvas):

	# the constructor
	def __init__(self, parent):
		# call the constructor in the superclass
		Canvas.__init__(self, parent, bg="white")
		# organize the canvas
		self.pack(fill=BOTH, expand=1)
		self.parent = parent
		#self.canvas = Canvas(self.parent)
		self.xCord = 0
		self.yCord = 0
		self.xCord2 = 0
		self.yCord2 = 0

	def Center(self):
		return "{},{}".format(((self.xCord + self.xCord2)/2), ((self.yCord + self.yCord2)/2))
		cLabel = Label(window, "{},{}".format(((self.xCord + self.xCord2)/2), ((self.yCord + self.yCord2)/2)) )
		cLabel.pack(LEFT)

	def AreaCalc():

		print 5
	#ToDo: provide the remaining methods for this class


class Rectangle(CoordinateShape):
	def __init__(self, parent):
		CoordinateShape.__init__(self, parent)
		#self.canvas = Canvas(self.parent)
		self.xCord = 10
		self.yCord = 10
		self.xCord2 = 100
		self.yCord2 = 260


	def Center(self):
		cLabel = Label(window, "{},{}".format(((self.xCord + self.xCord2)/2), ((self.yCord + self.yCord2)/2)), color = "red" )
		cLabel.pack(LEFT)	# ToDo: provide the remaining methods for this class

	def plotShape(self):
		self.create_rectangle(self.xCord, self.yCord, self.xCord2, self.yCord2, outline = "black", fill = "blue", width = 2)

class Square(CoordinateShape):
	def __init__(self, parent):
		CoordinateShape.__init__(self, parent)
		self.canvas = Canvas(self.parent)
		self.xCord = 10
		self.yCord = 5
		self.xCord2 = 60
		self.yCord2 = 60
	# ToDo: provide the remaining methods for this class


class Oval(CoordinateShape):
	def __init__(self, parent):
		CoordinateShape.__init__(self, parent)
		self.canvas = Canvas(self.parent)
		self.xCord = 10
		self.yCord = 10
		self.xCord2 = 60
		self.yCord2 = 60


	def Center(self):
		cLabel = Label(window, "{},{}".format(((self.xCord + self.xCord2)/2), ((self.yCord + self.yCord2)/2)), color = "red" )
		cLabel.pack(LEFT)	# ToDo: provide the remaining methods for this class

	def plotShape(self):
			self.create_oval(self.xCord, self.yCord, self.xCord2, self.yCord2, outline = "black", fill = "red", width = 10)

""" create_oval(x1, y1, x2, y2, fill)
create_oval(x1, y1, x2, y2)
create_oval(x1, y1, x2, y2, fill, outline)
create_oval(x1, y1, x2, y2, outline, width, fill)
create_oval(x1, y1, x2, y2, width, fill) """

	# ToDo: provide the remaining methods for this class

##########################################################
# Main Program
# the default size of the canvas is 800x800
WIDTH = 800
HEIGHT = 800

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("Shapes...Plotted")



# create the coordinate system as a Tkinter canvas inside the window
#p1 = CoordinateShape(window)


#r1 = Rectangle(window)
#r1.plotShape()


o2 = Oval(window)
o2.plotShape()
#plot the rectangle

# create your own shapes and plot them to the canvas



# wait for the window to close
window.mainloop()
