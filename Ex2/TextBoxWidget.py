import tkinter as tk
from tkinter import ttk

win = tk.Tk()
#win.geometry("900x500")
win.title("First Python GUI")
#win.resizable(0, 0)
label = ttk.Label(win)
label.grid(column=0, row=1)

def clickMe():
    label.configure(text="Hello, " + name.get() + '!')

ttk.Label(win, text="Enter your name: ").grid(column=0, row=0)

name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=1, row=0)

action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=1, row=1)

win.mainloop()
