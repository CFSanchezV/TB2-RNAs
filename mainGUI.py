import pandas as pd
import numpy as np
import tkinter as tk

def printtext():
    global e1
    string = e1.get()
    print(string)


root = tk.Tk()
label = tk.Label(root, text="First Name")
# tk.Label(root, text="Last Name").grid(row=1)
label.pack()

b = tk.Button(root, text='okay', command=printtext)
b.pack(side='bottom')

content = tk.StringVar()
e1 = tk.Entry(root, textvariable=content)
e1.pack()
# e2 = tk.Entry(master)

# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)

root.mainloop()


# root = Tk()

# root.title('Name')

# e = Entry(root)
# e.pack()
# e.focus_set()

# b = Button(root, text='okay', command=cliked)
# b.pack(side='bottom')
# root.mainloop()


# # if __name__ == "__main__":
# #     printtext()
