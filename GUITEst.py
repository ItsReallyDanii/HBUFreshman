from Tkinter import *

window = Tk()

text = Label(window, text= "GUIs in Python are pretty easy!")
text1 = Label(window, text= "GUIs in Python are pretty easy!")
#label is a componenent that is used to display text, an icon or an image on a GUI
#creates a Label under the variable text and is bound (attached) to the window as a child



text.pack()
text1.pack()
#pack is used on all widgests by default
#instructs the label to size itself to sepcified text to make it visible


window.mainloop()
#displays GUI on desktop. Will remain until user closes it