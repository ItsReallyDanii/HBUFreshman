from Tkinter import *

class GUITest(Frame):
    #constructor 
    def __init__ (self, master):
        #calls constructor of the super class (Frame)
        Frame.__init__(self, master)
        #declares an instance variable master that is stored in the main window and is necessary to set up 
        #the setupGUI function can add widgets as children to the main window
        self.master = master

#instanciates and and posisitons the widgets in bulk
    def setupGUI(self):
    #instanciates a new label as a child of the main window (from master in the GUITest class)
        l1 = Label(self.master, text = "A label", font = ("Arial Bold" , 50))
    #defines the properties of the label
        l1.grid(row = 0, column = 0, sticky = W)

        l2 = Label(self.master, text = "Another label")
        l2.grid(row = 1, column = 0, sticky = W)

        l3 = Label(self.master, text = "A third label, centered")
        l3.grid(row = 2, column = 0, columnspan = 2, sticky = E + W)

#PhotoImage is a class from the Tkinter library
        #img = PhotoImage(file = "smile.gif")

    #assigns the variable img as the label's image, but in the PhotoImage class, the
    #image dissapears from GUI when setUpGUI function terminates, so we have an extra 
    #reference for the image
        #l4 = Label(self.master, image = img)
        #l4.image = img
        #l4.grid(row = 0, column = 2, columnspan = 2, rowspan = 2, sticky = N+S+E+W)

        e1 = Entry(self.master)
        e1.grid(row = 0, column = 1)

        e2 = Entry(self.master)
        e2.insert(END, "user input")
        e2.grid(row = 1, column = 1)

        c1 = Checkbutton(self.master, text = "Some checknutton option")
        c1.grid(row = 3, column = 0, columnspan = 2, sticky = W)

        b1 = Button(self.master, text = "A button")
        b1.grid(row = 3, column = 2)

        b2 = Button(self. master, text = "Another button")
        b2.grid(row = 3, column = 2)


#creates main window
window = Tk()
#creates the instance of the GUITest class (which is a Frame (built in Tkinter class))
test = GUITest(window)
test.setupGUI()
window.geometry('350x200')
window.mainloop()