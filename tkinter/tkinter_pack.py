#membuat program pack
from tkinter import *
import tkinter as tk
obj = tk.Tk()
obj.geometry("300x300")
label1 = Label(obj, text='label1', bg='red')
label2 = Label(obj, text='label2', bg='green')
label3 = Label(obj, text='label3', bg='blue')

label1.pack()
label2.pack()
label3.pack()  
obj.mainloop()
