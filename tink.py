from tkinter import *
import date_time
window=Tk()
window.title("demo")
window.geometry("400x300")
lb1=Label(text="hey there",fg="white",bg="blue",height=1,width=300)
lb2=Label(text="name",bg="blue")
nameen=Entry()
def display():
    name=nameen.get()
    global Message
    Message="welcome to the application \ntodays date is:"
    greet="hello",name,"\n"
    text_box.insert(END,greet)
    text_box.insert(END,Message)
    text_box.insert(END,date_time.today())
text_box=Text(height=3)
btn=Button(text="start",command=display,height=1,fg="white",bg="blue")
lb1.pack()
lb2.pack
nameen.pack()
btn.pack()
text_box.pack()
window.mainloop()