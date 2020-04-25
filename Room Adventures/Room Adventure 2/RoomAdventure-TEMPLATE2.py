###########################################################################################
# Name:
# Date:
# Description:
###########################################################################################
from Tkinter import *

""" import one
import two
import three

result = one.func()
instance = two.YourClass()
something = three.func() """
# the room class
# note that this class is fully implemented with dictionaries as illustrated in the lesson "More on Data Structures"
class Room(object):
	# the constructor
	def __init__(self, name, image):
		# rooms have a name, an image (the name of a file), exits (e.g., south), exit locations
		# (e.g., to the south is room n), items (e.g., table), item descriptions (for each item),
		# and grabbables (things that can be taken into inventory)
		self.name = name
		self.image = image
		self.exits = {}
		self.items = {}
		self.grabbables = []

	# getters and setters for the instance variables
	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, value):
		self._name = value

	@property
	def image(self):
		return self._image

	@image.setter
	def image(self, value):
		self._image = value

	@property
	def exits(self):
		return self._exits

	@exits.setter
	def exits(self, value):
		self._exits = value

	@property
	def items(self):
		return self._items

	@items.setter
	def items(self, value):
		self._items = value

	@property
	def grabbables(self):
		return self._grabbables

	@grabbables.setter
	def grabbables(self, value):
		self._grabbables = value

	# adds an exit to the room
	# the exit is a string (e.g., north)
	# the room is an instance of a room
	def addExit(self, exit, room):
		# append the exit and room to the appropriate dictionary
		self._exits[exit] = room

	# adds an item to the room
	# the item is a string (e.g., table)
	# the desc is a string that describes the item (e.g., it is made of wood)
	def addItem(self, item, desc):
		# append the item and description to the appropriate dictionary
		self._items[item] = desc

	# adds a grabbable item to the room
	# the item is a string (e.g., key)
	def addGrabbable(self, item):
		# append the item to the list
		self._grabbables.append(item)

	# removes a grabbable item from the room
	# the item is a string (e.g., key)
	def delGrabbable(self, item):
		# remove the item from the list
		self._grabbables.remove(item)

	# returns a string description of the room
	def __str__(self):
		# first, the room name
		s = "You are in {}.\n".format(self.name)

		# next, the items in the room
		s += "You see: "
		for item in self.items.keys():
			s += item + " "
		s += "\n"

		# next, the exits from the room
		s += "Exits: "
		for exit in self.exits.keys():
			s += exit + " "

		return s

# the game class
# inherits from the Frame class of Tkinter
class Game(Frame):
	# the constructor
	def __init__(self, parent):
		# call the constructor in the superclass
		Frame.__init__(self, parent)

	# creates the rooms
	def createRooms(self):
#Room 1
		r1 = Room("Room 1", "room1.gif")
		r2 = Room("Room 2", "room2.gif")
		r3 = Room("Room 3", "room3.gif")
		r4 = Room("Room 4", "room4.gif")

		r1.addExit("east",r2)
		r1.addExit("south",r3)

		r1.addGrabbable("key")

		r1.addItem("chair","Insert desc here")
		r1.addItem("table","Insert desc here")

#Room 2
		r2.addExit("west",r1)
		r2.addExit("south",r4)

		r2.addItem("rug","Insert desc here")
		r2.addItem("fireplace","Insert desc here")

#Room 3
		r3.addExit("north",r2)
		r3.addExit("east", r3)

		r3.addGrabbable("book")

		r3.addItem("bookshelves","Insert desc here")
		r3.addItem("desk","Insert desc here")
		r3.addItem("statue","Insert desc here")

#Room 4
		r4.addExit("north", r2)
		r4.addExit("west", r3)
		r4.addExit("south", None) #Death

		r4.addGrabbable("6-pack")
		r4.addItem("brew_rig","Insert desc here")

		#Set room 1 as current room in the beginning of the Game
		Game.currentRoom = r1
		Game.inventory = []

	# sets up the GUI
	def setupGUI(self):
		self.pack(fill=BOTH, expand = 1)

#Sets up player input at the bottom of the GUI
#Gives it focus so player does not have to click on it
		Game.player_input = Entry(self, bg = "white")
		Game.player_input.bind("<Return>", self.process)
		Game.player_input.pack(side = BOTTOM, fill = X)
		Game.player_input.focus()

#Sets up images to left of screen
		img = None
		Game.image = Label(self, width=WIDTH / 2, image = img)
		Game.image.image = img
		Game.image.pack(side=LEFT, fill = Y)
		Game.image.pack_propagate(False)

#Starts up the text to the right of the GUI
		text_frame = Frame(self, width = WIDTH / 2)
		Game.text = Text(text_frame, bg = "lightgrey", state = DISABLED)
		Game.text.pack(fill = Y, expand = 1)
		text_frame.pack(side = RIGHT, fill = Y)
		text_frame.pack_propagate(False)

	# sets the current room image
	def setRoomImage(self):
		if (Game.currentRoom == None):
			Game.img = PhotoImage(file = "skull.gif")
		else:
			Game.img = PhotoImage(file = Game.currentRoom.image)

		Game.image.config(image=Game.img)
		Game.image.image = Game.img
	# sets the status displayed on the right of the GUI
	def setStatus(self, status):
		Game.text.config(state=NORMAL)
		Game.text.delete("1.0", END)

		if (Game.currentRoom == None):
			Game.text.insert(END, "You are dead. The only thing you can do now is quit. \n")

		else:
			Game.text.insert(END, str(Game.currentRoom) + "\n You are carrying:" + str(Game.inventory) + "\n \n" + status)

			Game.text.config(state = DISABLED)
	# plays the game
	def play(self):
		# add the rooms to the game
		self.createRooms()

		# configure the GUI
		self.setupGUI()

		# set the current room
		self.setRoomImage()
		# set the current status
		self.setStatus("")

	# processes the player's input
	def process(self, event):
		action = Game.player_input.get()
		action = action.lower()

		response = "I don't understand. Try a verb or noun. Valid verbs are 'go', 'look' and 'take'."

		if (action == "quit" or action == "exit" or action == "bye"):
			exit(0)

		if (Game.currentRoom == None):
			Game.player_input.delete(0, END)
			return

		words = action.split()

		if (len(words) == 2):
			verb = words[0]
			noun = words[1]

			if (verb == "go"):
				response = "Invalid Exit."

				if (noun in Game.currentRoom.exits):
					Game.currentRoom = Game.currentRoom.exits[noun]
					response = "Room changed."

			elif (verb == "look"):
				response = "I do not see that item."

				if (noun in Game.currentRoom.items):
					response = Game.currentRoom.items[noun]

			elif (verb == "take"):
				response = "I do not see that item."

				for grabbable in Game.currentRoom.grabbables:
					if (noun == grabbable):
						Game.inventory.append(grabbable)
						Game.currentRoom.delGrabbable(grabbable)
						response = "Item Grabbed"
						break
			self.setStatus(response)
			self.setRoomImage()
			Game.player_input.delete(0, END)

##########################################################
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

# create the window
window = Tk()
window.title("Room Adventure")

# create the GUI as a Tkinter canvas inside the window
g = Game(window)
# play the game
g.play()

# wait for the window to close
window.mainloop()
