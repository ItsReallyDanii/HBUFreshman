from Tkinter import *

#App class is a subclass of the Tkinter Frame class. 
#Initializes Tkinter Frame which serves as holder for other GUI componenets
class App(Frame):
    def __init__(self,master):#master 
        Frame.__init__(self, master)
        #quit is already defined in a Tkinter library
        self.button1 = Button(master, text = "BYE!", fg = "red", command = self.quit)
        #places the button the furthest to the left as possible. default is TOP, which places
        #the compenent as far top as possible 
        self.button1.pack(side = LEFT)
        #say is declared in the function below
        self.button2 = Button(master, text = "Say Something!", command = self.say)
        #places button furthest to the right as possible
        self.button2.pack(side = LEFT)

    def say(self):
        print "Froot Loops"


window = Tk()
#creates new instance of App class passing the main window as the parameter (becomes a parent of any GUI components created in the App class)
#this launches constructor as the App class in line 5
app = App(window)
window.mainloop()