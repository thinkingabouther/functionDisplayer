from tkinter import *
from function_displayer import Displayer, Handler
from expressions import Function


root = Tk()

frame1 = Frame(root)
displayer = Displayer(frame1)
handler = Handler(root, displayer)


frame1.grid(row=0, column=0)
handler.grid(row=0, column=1)
displayer.pack()

displayer.add_axis()

root.mainloop()
