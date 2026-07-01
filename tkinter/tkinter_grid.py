#membuat program grid
from tkinter import *
import tkinter as tk
obj = tk.Tk()

#membuat widget label dan memasukkan ke grid
Header = Label(obj, text="Login Here")
Header.grid(columnspan = 2)

#membuat widget label dan label entry
label1 = Label(obj, text="Username")
label2 = Label(obj, text="Password")
Entry1 = Entry(obj)
Entry2 = Entry(obj)

#memasukkan widget label dan label entry username
label1.grid(row=2, column=0, sticky=E)
label2.grid(row=3, column=0, sticky=E)
Entry1.grid(row=2, column=1)
Entry2.grid(row=3, column=1)

#creating check button
check = Checkbutton(obj, text="Remember me")
check.grid(row=4, columnspan=2)

button = Button(obj, text="Login")
button.grid(row=5, columnspan=2)

obj.mainloop()