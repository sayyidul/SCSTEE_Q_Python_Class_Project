#membuat frame awal
from tkinter import *
import tkinter as tk
obj = tk.Tk()
TopFrame = Frame(obj)
TopFrame.pack(side=TOP, fill=X)

#pembuatan frame kedua
BottomFrame = Frame(obj)
BottomFrame.pack(side=BOTTOM, fill=X)

#labeling TopFrame
label1 = Label(TopFrame, text="Label Widget 1", bg="red")
label2 = Label(TopFrame, text="Label Widget 2", bg="Green")
label3 = Label(TopFrame, text="Label Widget 3", bg="Blue")
label1.pack(side=LEFT)
label2.pack(side=LEFT)
label3.pack(side=LEFT)

#labeling BottomFrame
label4 = Label(BottomFrame, text="Label Widget 4", bg="Yellow")
label5 = Label(BottomFrame, text="Label Widget 5", bg="magenta")
label4.pack()
label5.pack()

obj.mainloop()