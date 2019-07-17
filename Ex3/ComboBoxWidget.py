import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("SetFocusDisableWidget Python GUI")
label = ttk.Label(win)
label.grid(column=0, row=1)

def clickMe():
    label.configure(text="Hello, " + name.get() + ' #' + numberChosen.get() +'!')
    label.configure(foreground='purple')
    actionButton.configure(state="disabled")
    actionButton.configure(text="Disabled!")

ttk.Label(win, text="Enter your name: ").grid(column=0, row=0)

name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=1, row=0)

actionButton = ttk.Button(win, text="Click Me!", command=clickMe)
actionButton.grid(column=1, row=1)
nameEntered.focus()

ttk.Label(win, text="Select a number: ").grid(column=0, row=2)
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number)
numberChosen["values"] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=2)
numberChosen.current(0)

win.mainloop()
