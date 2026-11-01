from tkinter import *
window=Tk()
window.title("multiply")
window.geometry("400x300")
lb1=Label(text="Number 1",fg="white",bg="black",height=1,width=300)
num1=Entry()
lb2=Label(text="Number 2",fg="white",bg="black",height=1,width=300)
num2=Entry()
def dis():
    try:
        first = int(num1.get())
        second = int(num2.get())
    except ValueError:
        text_box.insert(END, "Please enter valid integers.")
        return
    result = first * second
    text_box.insert(END, f"{first} * {second} = {result}")
text_box=Text(height=3)
btn=Button(text="Multiply",command=dis)
lb1.pack()
num1.pack()
lb2.pack()
num2.pack()
btn.pack()
text_box.pack()
window.mainloop()