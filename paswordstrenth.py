
from tkinter import *

window = Tk()
window.geometry("500x400")
window.title("Password Strength Calculator")

def calculate():
    num = 0
    for i in ent.get():
        num += 1

    lbl2 = Label(window, text=f"Your Password Strength is power: {num}")
    lbl2.pack()

lbl = Label(window, text="Enter Password:")
lbl.pack()

ent = Entry(window)
ent.pack()

btn = Button(window, text="Calculate", command=calculate)
btn.pack()

window.mainloop()
