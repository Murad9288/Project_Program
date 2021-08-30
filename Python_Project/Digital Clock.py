from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
#root.configure(background="black")
root.title("DIGITAL CLOCK")

def time():
    string = strftime("%I:%M:%S %p") # eitake Digital a convert korte hole "%I" er poriborte "%H" dite hobe..
    label.config(text = string)
    label.after(1000,time)
label = Label(root,font=("ds-digital",100,"bold"),background = "Black",foreground = "Red")
label.pack(anchor="center")
time()
mainloop()
