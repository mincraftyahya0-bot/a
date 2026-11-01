from tkinter import *
from datetime import date

window=Tk()
window.title("demo")
window.geometry("400x300")
lb1=Label(text="hey there",fg="white",bg="blue",height=1,width=300)
lb2=Label(text="name",bg="blue")
nameen=Entry()
def display():
    name=nameen.get()
    text_box.insert(END, f"hello {name}\n")
    text_box.insert(END, "welcome to the application\ntodays date is:")
    text_box.insert(END, str(date.today()))
text_box=Text(height=3)
btn=Button(text="start",command=display,height=1,fg="white",bg="blue")
lb1.pack()
lb2.pack()
nameen.pack()
btn.pack()
text_box.pack()
window.mainloop()