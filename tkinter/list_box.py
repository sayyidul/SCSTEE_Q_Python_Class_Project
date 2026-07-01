import tkinter
from tkinter import *
import tkinter as tk
top = Tk()
combo = Listbox(top, bd=1, height=10, width=35)
combo.insert(1, "Python")
combo.insert(2, "Java")
combo.insert(3, "HTML & CSS")
combo.insert(4, "JavaScript")
combo.insert(5, "PHP")
combo.insert(6, "Other")
combo.pack()
top.mainloop()