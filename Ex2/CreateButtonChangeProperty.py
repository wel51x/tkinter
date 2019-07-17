import tkinter as tk
from tkinter import ttk

win = tk.Tk()
#win.geometry("900x500")
win.title("First Python GUI")
#win.resizable(0, 0)
label1 = ttk.Label(win, text="Red Label")
label1.grid(column=0, row=0)
label2 = ttk.Label(win, text="Blue Label")
label2.grid(column=0, row=1)

def clickRed():
    action1.configure(text="Label now red!")
    label1.configure(foreground='red')
    label1.configure(text="Red Label")

def clickBlue():
    action2.configure(text="Label now blue!")
    label2.configure(foreground='blue')
    label2.configure(text="Blue Label")

action1 = ttk.Button(win, text="Click Red", command=clickRed)
action1.grid(column=1, row=0)

action2 = ttk.Button(win, text="Click Blue", command=clickBlue)
action2.grid(column=1, row=1)

win.mainloop()
