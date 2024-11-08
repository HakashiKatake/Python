import tkinter as tk

def add_numbers():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result.set(num1 + num2)

root = tk.Tk()
root.title("Add Numbers")

entry1 = tk.Entry(root)
entry1.pack()
entry2 = tk.Entry(root)
entry2.pack()
result = tk.StringVar()
label_result = tk.Label(root, textvariable=result)
label_result.pack()

button_add = tk.Button(root, text="Add", command=add_numbers)
button_add.pack()

root.mainloop()



