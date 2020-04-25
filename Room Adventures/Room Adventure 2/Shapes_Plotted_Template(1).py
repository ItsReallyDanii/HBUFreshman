######################################################################################################################
# Name:
# Date:
# Description:
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

	#ToDo: provide the remaining methods for this class


class Rectangle(CoordinateShape):
	def __init__(self, parent):
		CoordinateShape.__init__(self, parent)

	# ToDo: provide the remaining methods for this class

class Square(CoordinateShape):
	def __init__(self, parent):
		CoordinateShape.__init__(self, parent)

	# ToDo: provide the remaining methods for this class


class Oval(CoordinateShape):
	def __init__(self, parent):
		CoordinateShape.__init__(self, parent)
		#add member variables to this class "if needed"

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
r1 = Rectangle(window)
#plot the rectangle

# create your own shapes and plot them to the canvas

# wait for the window to close
window.mainloop()
