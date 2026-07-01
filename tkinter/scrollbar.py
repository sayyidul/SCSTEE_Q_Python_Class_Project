import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.resizable(False, False)
root.title("Scrollbar Widget Example")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

text = tk.Text(root, height=10)
text.grid(row=0, column=0, sticky=tk.EW)

scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=text.yview)
scrollbar.grid(row=0, column=1, sticky=tk.NS)

text['yscrollcommand']=scrollbar.set

for i in range(1,50):
    position = f'{i}.0'
    text.insert(position,f'Line{i}\n');
root.mainloop()