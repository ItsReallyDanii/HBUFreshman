###########################################################################################
# Name: Daniel Sleiman
# Date: 12/2/2019
# Description: Room Adventure 
###########################################################################################

###########################################################################################
# the blueprint for a room
class Room(object):
	# the constructor
  def __init__(self, name):
    self.items = []
    self.name = name
    self.grabbables = []
    self.exists = []
    self.existLocations = []
    self.itemDescription = []

  @property
  def name(self):
      return self._name 

  @name.setter
  def name (self, value):
      self._name = value
#
  @property
  def items(self):
      return self._items

  @items.setter
  def items(self, value):
      self._items = value
#
  @property
  def exists(self):
      return self._exists

  @exists.setter
  def exists(self, value):
      self._exists = value
#
  @property
  def grabbables(self):
      return self._grabbables

  @grabbables.setter
  def grabbables(self, value):
      self._grabbables = value
#
  @property
  def existLocations(self):
      return self._existLocations

  @existLocations.setter
  def existLocations(self, value):
      self._existLocations = value

  @property
  def itemDescription(self):
      return self.itemDescription

  @itemDescription.setter
  def itemDescription(self, value):
      self._itemDescription = value

  @property
  def addItem(self):
      return self.addItem

  @addItem.setter
  def addItem(self, value):
      self._addItem = value
      
    # adds an exit to the room
    # the exit is a string (e.g., north)
    # the room is an instance of a room

  def addExit(self, exit, location):

      # append the exit and room to the appropriate lists
          self._exists.append(exit)
          self._existLocations.append(location)

    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made of wood)

  def addItem(self, item, description):

      # append the item and description to the appropriate lists

          self._items.append(item)
          self._itemDescription.append(description)

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
      for item in self.items:
        s += item + " "
      s += "\n"

      s += "You also see these grabbable items: "
      for gB in self.grabbables:
        s += gB + " "
      s += "\n"

      # next, the exits from the room
      s += "Exits: "
      for exit in self.exists:
        s += exit + " "

      return s

###########################################################################################
# creates the rooms
def createRooms():
    global currentRoom

    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")
    

    r1.addItem("Chair" , "Desk Chair")
    r1.addItem("Table" , "An old oak table")
    r1.addItem("Globe" , "A world map")
    r1.addGrabbable("pen")
    r1.addExit("south", r3)
    r1.addExit("east", r2)
    r1.addGrabbable("key")

    
    r2.addExit("west", r1)
    r2.addExit("south", r4)
    r2.addGrabbable("log")
    r2.addItem("Painting" , "A very nice portait of Dr. Zaki is hanging from the fireplace")
    r2.addItem("Fireplace" , "A recently used fireplace with leftover embers")
    r2.addItem("Rug" , "A terrible design. Does not match the room.")


    r3.addExit("north", r1)
    r3.addExit("east", r4)
    r3.addGrabbable("book")
    r3.addGrabbable("violin")
    r3.addItem("Bookshevles" , "A dusty shelf. It does not look like someone does much reasing")
    r3.addItem("Statue" , "An odd looking Gargoyle. Should't it be on the roof?")
    r3.addItem("Desk" , "This desk is really cluttered! Someone needs to organize it")
    r3.addItem("Lamp" , "The Room is really dark! It might be used to light it up")


    r4.addExit("north", r2)
    r4.addExit("west", r3)
    r4.addExit("South", None)
    r4.addGrabbable("6-Pack")
    r4.addGrabbable("cups")
    r4.addItem("Brew Rig" , "Looks like this machine makes soda! Now is not the time.")
    r4.addItem("water cooler" , "Just in case you are thirsty on your journey!")    
    
    currentRoom = r1



# displays an appropriate "message" when the player dies
# yes, this is intentionally obfuscated!
def death():
	print " " * 17 + "u" * 7
	print " " * 13 + "u" * 2 + "$" * 11 + "u" * 2
	print " " * 10 + "u" * 2 + "$" * 17 + "u" * 2
	print " " * 9 + "u" + "$" * 21 + "u"
	print " " * 8 + "u" + "$" * 23 + "u"
	print " " * 7 + "u" + "$" * 25 + "u"
	print " " * 7 + "u" + "$" * 25 + "u"
	print " " * 7 + "u" + "$" * 6 + "\"" + " " * 3 + "\"" + "$" * 3 + "\"" + " " * 3 + "\"" + "$" * 6 + "u"
	print " " * 7 + "\"" + "$" * 4 + "\"" + " " * 6 + "u$u" + " " * 7 + "$" * 4 + "\""
	print " " * 8 + "$" * 3 + "u" + " " * 7 + "u$u" + " " * 7 + "u" + "$" * 3
	print " " * 8 + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3
	print " " * 9 + "\"" + "$" * 4 + "u" * 2 + "$" * 3 + " " * 3 + "$" * 3 + "u" * 2 + "$" * 4 + "\""
	print " " * 10 + "\"" + "$" * 7 + "\"" + " " * 3 + "\"" + "$" * 7 + "\""
	print " " * 12 + "u" + "$" * 7 + "u" + "$" * 7 + "u"
	print " " * 13 + "u$\"$\"$\"$\"$\"$\"$u"
	print " " * 2 + "u" * 3 + " " * 8 + "$" * 2 + "u$ $ $ $ $u" + "$" * 2 + " " * 7 + "u" * 3
	print " u" + "$" * 4 + " " * 8 + "$" * 5 + "u$u$u" + "$" * 3 + " " * 7 + "u" + "$" * 4
	print " " * 2 + "$" * 5 + "u" * 2 + " " * 6 + "\"" + "$" * 9 + "\"" + " " * 5 + "u" * 2 + "$" * 6
	print "u" + "$" * 11 + "u" * 2 + " " * 4 + "\"" * 5 + " " * 4 + "u" * 4 + "$" * 10
	print "$" * 4 + "\"" * 3 + "$" * 10 + "u" * 3 + " " * 3 + "u" * 2 + "$" * 9 + "\"" * 3 + "$" * 3 + "\""
	print " " + "\"" * 3 + " " * 6 + "\"" * 2 + "$" * 11 + "u" * 2 + " " + "\"" * 2 + "$" + "\"" * 3
	print " " * 11 + "u" * 4 + " \"\"" + "$" * 10 + "u" * 3
	print " " * 2 + "u" + "$" * 3 + "u" * 3 + "$" * 9 + "u" * 2 + " \"\"" + "$" * 11 + "u" * 3 + "$" * 3
	print " " * 2 + "$" * 10 + "\"" * 4 + " " * 11 + "\"\"" + "$" * 11 + "\""
	print " " * 3 + "\"" + "$" * 5 + "\"" + " " * 22 + "\"\"" + "$" * 4 + "\"\""
	print " " * 5 + "$" * 3 + "\"" + " " * 25 + "$" * 4 + "\""

###########################################################################################
# START THE GAME!!!

inventory = [] #creates empty inventory
createRooms()


while (True):
    status = "{}\n You are carrying: {}\n".format(currentRoom, inventory)

    if (currentRoom == None):
        status = "You are dead."

    print "================================================"
    print status

    if (currentRoom == None):
        death()
        break


    action = raw_input("What to do? ")
    action = action.lower()

    print action

    if (action == "quit" or action == "exit" or action == "bye"):
        print "inside if"
        break

    response = "I don't understand. Try a verb noun. Valid verbs are go, look, and take"
    words = action.split()

    if (len(words) == 2):
        verb = words[0]
        noun = words[1]

        if (verb == "go"):
            response = "Invalid exit"

            for i in range(len(currentRoom.exists)):
                if (noun == currentRoom.exists[i]):
                    response = "Room changed."
                    currentRoom = currentRoom.existLocations[i]
                    break
    
        elif (verb == "look"):
            response = "I do not see that item."

            for i in range (len(currentRoom.items)):
                if (noun == currentRoom.items[i]):
                    response = currentRoom.itemDescription[i]
                    break

        elif (verb == "take"):
            response = "I do not see that item."

            for grabbable in currentRoom.grabbables:
                if (noun == grabbable):
                    inventory.append(grabbable)

                    currentRoom.delGrabbable(grabbable)
                    response  = "Item grabbed."
                    break

    print "\n{}".format(response)

