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
        r = Rectangle(self)
        r.plotShape()
        o = Oval(self)
        o.plotShape()

# the CoordinateShape system class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class CoordinateShape(object):
	def __init__(self):
		self.xCord = 0
		self.yCord = 0
		self.xCord2 = 0
		self.yCord2 = 0

		self.xCenter = 0
		self.yCenter = 0

		self.Area = 0
		self.length = 0
		self.width = 0

class KeyC(CoordinateShape):
	def __init__(self, parent):
		self.parent = parent
		self.canvas = parent.canvas
	def plotShape(self):
		self.canvas.create_rectangle(self.xCord, self.yCord, self.xCord2, self.yCord2, outline = "black", fill = "blue", width = 2)

class Square(CoordinateShape):
	def __init__(self, parent):
		self.parent = parent
		self.canvas = parent.canvas
	def plotShape(self):
		self.canvas.create_rectangle(self.xCord, self.yCord, self.xCord2, self.yCord2, outline = "black", fill = "yellow", width = 2)

class Oval(CoordinateShape):
	def __init__(self, parent):
		self.parent = parent
		self.canvas = parent.canvas
	def plotShape(self):
		self.canvas.create_oval(self.xCord, self.yCord, self.xCord2, self.yCord2, outline = "black", fill = "red", width = 2)

##########################################################
MainWindow()
