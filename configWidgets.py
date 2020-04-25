from Tkinter import *

window = Tk()

text = Button()
text.config(text= "GUIs in Python are pretty easy!", fg = "blue", bg = "yellow", command = trying)
#label is a componenent that is used to display text, an icon or an image on a GUI
#creates a Label under the variable text     and is bound (attached) to the window as a child

def (trying):
    

text.pack()
#pack is used on all widgests by default
#instructs the label to size itself to sepcified text to make it visible


window.mainloop()
#displays GUI on desktop. Will remain until user closes it