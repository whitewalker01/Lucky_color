from tkinter import *
import time 
mw=Tk()
mw.title("Find Your Lucky - Color!")
mw.geometry("400x200")

global entry
global colour


# mw.configure({"background": colour[x]})  
def surya(*args):
    new = e1.get().lower()
    if new != "":
        letter = new[-1]
        mw.configure({"background":clr[letter]})

            
            
var = StringVar()

"""butt=Button(mw,text="click me!?",command=surya)
butt.pack(side = RIGHT , anchor = CENTER , padx =8 , pady=8)"""


e1 = Entry(mw, width=30, textvariable=var) 
e1.pack(side=RIGHT, anchor=CENTER, padx=5, pady=5)



test = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
colour = ["turquoise2", "hot pink", "SteelBlue1", "green2", "red3", "DarkOrchid3", "dark orange", "wheat3", "maroon3", "thistle3", "yellow", "gold3",
"blue", "dark green", "aquamarine2", "sienna3", "brown4", "misty rose", "gray54", "peach puff", "VioletRed2", "SeaGreen3", "coral", "forest green",
"light slate blue", "gray10"]
clr=dict(zip(test,colour))
var.trace(mode="w", callback=surya)
label= Label(mw,text="Enter Your Name", font="Helvetica 16 bold", justify=LEFT)
label.pack(side=LEFT, anchor=CENTER, padx=5, pady=5)



e1.pack()



mw.mainloop()