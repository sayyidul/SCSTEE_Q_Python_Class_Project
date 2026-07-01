import tkinter
from tkinter import *
import tkinter as tk

x = tk.Tk()
penghitung = 0

def hitung(teks):
    def count():    
        global penghitung
        penghitung += 1
        teks.config(text=str(penghitung))
        teks.after(1000, count)

    count()
teks = tk.Label(x, font = "Verdana 16 bold")
teks.pack()
hitung(teks)
x.geometry('300x300')
x.title('Button Stop Preview')
button=tk.Button(x, text='Stop', width=75, command=x.destroy)
button.pack()
x.mainloop()