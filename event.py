from tkinter import *
window=Tk()
window.geometry("100x100")
window.title("Event Handler")

def hndlekyprs(event):
    print(event.char)
window.bind("<Key>",hndlekyprs)
def hndleclk(event=None):
    print("test")
btn=Button(text="start",command=hndleclk,height=1,fg="white",bg="black")
btn.bind("<Button-1>",hndleclk)
btn.pack()
window.mainloop()