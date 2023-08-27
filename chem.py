from tkinter import *

with open("prescription.txt", "r") as op:
    x = op.read()

root1 = Tk()
root1.geometry("500x700")
l1 = Label(root1, text=x)
l1.pack()

root1.mainloop()
