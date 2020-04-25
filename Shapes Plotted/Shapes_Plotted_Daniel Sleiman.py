######################################################################################################################
# Name: Daniel Sleiman
# Date: 03.05.2020
# Description: Plotting shapes on a canvas
######################################################################################################################
import Tkinter as tk
import math
from Tkinter import *


class MainWindow(object):
    def __init__(self):
        self.window = tk.Tk()

        self.canvas = tk.Canvas(self.window, height = 800, width = 800, bg="white")
        self.canvas.pack()

        self.drawShapes()
        self.window.mainloop()

    def drawShapes(self):


        s = Square(self)
        s.plotShape()
        s.Center()
        s.AreaCalc()

        r = Rectangle(self)
        r.plotShape()
        r.Center()
        r.AreaCalc()

        o = Oval(self)
        o.plotShape()
        o.Center()
        o.AreaCalc()
"""
        t = Triangle(self)
        t.plotShape()
"""

# the CoordinateShape system class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class CoordinateShape(object):
	# the constructor
	def __init__(self):
		# call the constructor in the superclass
		# organize the canvas
		self.xCord = 0
		self.yCord = 0
		self.xCord2 = 0
		self.yCord2 = 0

		self.xCenter = 0
		self.yCenter = 0

		self.Area = 0
		self.length = 0
		self.width = 0


class Rectangle(CoordinateShape):
	def __init__(self, parent):
		self.parent = parent
		self.canvas = parent.canvas
		self.xCord = 360
		self.yCord = 600
		self.xCord2 = 450
		self.yCord2 = 800
	# ToDo: provide the remaining methods for this class
	def plotShape(self):
		self.canvas.create_rectangle(self.xCord, self.yCord, self.xCord2, self.yCord2, outline = "black", fill = "blue", width = 2)

	def Center(self):
		self.xCenter = ((self.xCord + self.xCord2)/2)
		self.yCenter = ((self.yCord + self.yCord2)/2)

		#cLabel = Label(self.canvas, text = "{},{}".format(self.xCenter, self.yCenter), fg = "black")
		#cLabel.place(x = self.xCenter, y = self.yCenter)
		print "Center of the Rectangle is {},{}".format(self.xCenter, self.yCenter)


	def AreaCalc(self):
		self.width = (self.xCord - self.xCord2)
		self.length = (self.yCord - self.yCord2)
		self.Area = (self.length * self.width)
		cLabel = Label(self.canvas, text = "{}".format(self.Area), fg = "black")
		cLabel.place(x = self.xCenter, y = self.yCenter)
		print "Area of the Rectangle is {}".format(self.Area)
		print

class Square(CoordinateShape):
	def __init__(self, parent):
		self.parent = parent
		self.canvas = parent.canvas
		self.xCord = 200
		self.yCord = 400
		self.xCord2 = 600
		self.yCord2 = 800
	# ToDo: provide the remaining methods for this class
	def plotShape(self):
		self.canvas.create_rectangle(self.xCord, self.yCord, self.xCord2, self.yCord2, outline = "black", fill = "yellow", width = 2)

	def Center(self):
		self.xCenter = ((self.xCord + self.xCord2)/2)
		self.yCenter = ((self.yCord + self.yCord2)/2)
		print "Center of the Square is {},{}".format(self.xCenter, self.yCenter)
		#cLabel = Label(self.canvas, text = "{},{}".format(self.xCenter, self.yCenter, self), fg = "black")
		#cLabel.place(x = self.xCenter, y = self.yCenter)


	def AreaCalc(self):
		self.width = (self.xCord - self.xCord2)
		self.length = (self.yCord - self.yCord2)
		self.Area = (self.length * self.width)
		cLabel = Label(self.canvas, text = "{}".format(self.Area), fg = "black")
		cLabel.place(x = self.xCenter, y = self.yCenter)
		print "Area of the Square is {}".format(self.Area)
		print

class Oval(CoordinateShape):
	def __init__(self, parent):
		self.parent = parent
		self.canvas = parent.canvas
		#add member variables to this class "if needed"
		self.xCord = 425
		self.yCord = 700
		self.xCord2 = 450
		self.yCord2 = 725

	# ToDo: provide the remaining methods for this class
	def plotShape(self):
		self.canvas.create_oval(self.xCord, self.yCord, self.xCord2, self.yCord2, outline = "black", fill = "red", width = 2)

	def Center(self):
		self.xCenter = ((self.xCord + self.xCord2)/2)
		self.yCenter = ((self.yCord + self.yCord2)/2)
		print "Center of the Oval is {},{}".format(self.xCenter, self.yCenter)
		#cLabel = Label(self.canvas, text = "{},{}".format(self.xCenter, self.yCenter), fg = "black")
		#cLabel.place(x = self.xCenter, y = self.yCenter)

	def AreaCalc(self):
		self.width = (self.xCord - self.xCord2)
		self.length = (self.yCord - self.yCord2)
		self.Area = (self.length * self.width * math.pi)
		cLabel = Label(self.canvas, text = "{}".format(self.Area), fg = "black")
		cLabel.place(x = self.xCenter, y = self.yCenter)
		print "Area of the Oval is {}".format(self.Area)
		print

"""

class Triangle(CoordinateShape):
	def __init__(self, parent):
		self.parent = parent
		self.canvas = parent.canvas
		#add member variables to this class "if needed"

	# ToDo: provide the remaining methods for this class
	def plotShape(self):
		self.canvas.create_line(200,400,400,200)
        self.canvas.create_line(400,200,600,200)
"""
##########################################################
MainWindow()
