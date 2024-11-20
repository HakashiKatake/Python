#Create a digital clock GUI application with Python.

from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")
root.geometry("400x400")
root.resizable(0,0)

def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("ds-digital", 80), background = "black", foreground = "white")
label.pack(anchor='center')
time()

mainloop()

