######################################################################################################################
# Name:
# Date:
# Description:
######################################################################################################################
from Tkinter import *
import math

# the CoordinateShape system class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class CoordinateShape(Canvas):

	# the constructor
	def __init__(self, parent):
		# call the constructor in the superclass
		Canvas.__init__(self, parent, bg="white")
		# organize the canvas
		self.pack(fill=BOTH, expand=1)

		self.xCord = 0
		self.yCord = 0
		self.xCord2 = 0
		self.yCord2 = 0

		self.xCenter = 0
		self.yCenter = 0

		self.Area = 0
		self.pi = math.pi
		self.length = 0
		self.width = 0


	#ToDo: provide the remaining methods for this class
	def Center(self):
		#self.xCenter = ((self.xCord + self.xCord2)/2)
		#self.yCenter = ((self.yCord + self.yCord2)/2)
		#cLabel = Label(window, text = "{},{}".format(self.xCenter, self.yCenter))
		#cLabel = Label(window, text = "Yes")
		print

	def AreaCalc(self):
		print

class Rectangle(CoordinateShape):
	def __init__(self, parent):
		CoordinateShape.__init__(self, parent)
		self.xCord = 10
		self.yCord = 10
		self.xCord2 = 100
		self.yCord2 = 260
	# ToDo: provide the remaining methods for this class
	def plotShape(self):
		self.create_rectangle(self.xCord, self.yCord, self.xCord2, self.yCord2, outline = "black", fill = "blue", width = 2)

	def Center(self):
		self.xCenter = ((self.xCord + self.xCord2)/2)
		self.yCenter = ((self.yCord + self.yCord2)/2)

		cLabel = Label(window, text = "{},{}".format(self.xCenter, self.yCenter), fg = "black", bg = "blue")
		cLabel.place(x = self.xCenter, y = self.yCenter)


	def AreaCalc(self):
		self.width = (self.xCord - self.xCord2)
		self.length = (self.yCord - self.yCord2)
		self.Area = (self.length * self.width)
		print "Area of the rectangle is {}".format(self.Area)

class Square(CoordinateShape):
	def __init__(self, parent):
		CoordinateShape.__init__(self, parent)
		self.xCord = 50
		self.yCord = 50
		self.xCord2 = 125
		self.yCord2 = 125
	# ToDo: provide the remaining methods for this class
	def plotShape(self):
		self.create_rectangle(self.xCord, self.yCord, self.xCord2, self.yCord2, outline = "black", fill = "yellow", width = 2)

	def Center(self):
		self.xCenter = ((self.xCord + self.xCord2)/2)
		self.yCenter = ((self.yCord + self.yCord2)/2)

		cLabel = Label(window, text = "{},{}".format(self.xCenter, self.yCenter), fg = "black", bg = "blue")
		cLabel.place(x = self.xCenter, y = self.yCenter)


	def AreaCalc(self):
		self.width = (self.xCord - self.xCord2)
		self.length = (self.yCord - self.yCord2)
		self.Area = (self.length * self.width)
		print "Area of the square is {}".format(self.Area)

class Oval(CoordinateShape):
	def __init__(self, parent):
		CoordinateShape.__init__(self, parent)
		#add member variables to this class "if needed"
		self.xCord = 10
		self.yCord = 10
		self.xCord2 = 60
		self.yCord2 = 60

	# ToDo: provide the remaining methods for this class
	def plotShape(self):
		self.create_oval(self.xCord, self.yCord, self.xCord2, self.yCord2, outline = "black", fill = "red", width = 2)

	def Center(self):
		self.xCenter = ((self.xCord + self.xCord2)/2)
		self.yCenter = ((self.yCord + self.yCord2)/2)

		cLabel = Label(window, text = "{},{}".format(self.xCenter, self.yCenter), fg = "black", bg = "blue")
		cLabel.place(x = self.xCenter, y = self.yCenter)

	def AreaCalc(self):
		self.width = (self.xCord - self.xCord2)
		self.length = (self.yCord - self.yCord2)
		self.Area = (self.length * self.width * self.pi)
		print "Area of the oval is {}".format(self.Area)
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
r1 = Rectangle(window)
r1.plotShape()
r1.Center()
r1.AreaCalc()
# create your own shapes and plot them to the canvas


o1 = Oval(window)
o1.plotShape()
o1.Center()
o1.AreaCalc()


s1 = Square(window)
s1.plotShape()
s1.Center()
s1.AreaCalc()
# wait for the window to close
window.mainloop()
