#activity1
from tkinter import *
root=Tk()
root.geometry("400x300")
root.title("Main")
def topwin():
    top=Toplevel()
    top.geometry("180x200")
    top.title("top")
    l2=Label(top,text="This is a top level window")
    l2.pack
l=Label(root,text="This is a root window")
btn=Button(l,text="Click to open top level window",command=topwin)
l.pack()
btn.pack()
root.mainloop()
from tkinter import messagebox
root=Tk()
root.configure(bg="light blue")
root.title("Demonination Calculator")
root.geometry("650x400")
l=Label(root, bg="light blue")
l.place(x=180,y=20)
l1=Label(root,text="Hey, welcome to the Demonination Calculator App")
l1.place(relx=0.5,y=340,anchor=CENTER)
def msg():
    msgbox=messagebox.showinfo("Alert","Do you want to show the demonination count?(ok/no thanks)")
    if msgbox =="ok":
        topwin()
btn=Button(root,text="Lets get started!",command=msg,bg="brown",fg="white")
btn.place(x=260,y=360)
root.mainloop()