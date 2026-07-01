#placement Tkinter
from tkinter import *
import tkinter as tk
obj = tk.Tk()

label1 = Label(obj, text="Label Widget 1", bg="red")
label2 = Label(obj, text="Label Widget 2", bg="Green")
label3 = Label(obj, text="Label Widget 3", bg="Blue")
label1.place(x=10, y=20)
label2.place(x=10, y=70)
label3.place(x=10, y=120)

obj.mainloop()
