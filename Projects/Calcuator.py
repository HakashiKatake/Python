#Simple GUI calculator using Tkinter

import tkinter
from tkinter import *

root = Tk() #creating a window
root.title("Calculator")
root.geometry("400x400")
root.resizable(0,0)
root.configure(bg = "powder blue")

e = Entry(root, width = 50, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

def button_click(number):   
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():   
    first_number = e.get()
    global f_num    
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))

def button_subtract():   
    first_number = e.get()
    global f_num    
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)    

def button_multiply():   
    first_number = e.get()
    global f_num    
    global math
    math = "multiplication"
    f_num = int(first_number)   
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num    
    global math
    math = "division"
    f_num = int(first_number)   
    e.delete(0, END)

button_1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click(1))

