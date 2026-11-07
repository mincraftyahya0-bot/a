from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("200x200")
window.title("non-virus link")
def virus():
    messagebox.showwarning("ALERT: Virus Detected")
btn=Button(text="Scan",command=virus,height=1,fg="white",bg="black")
btn.place(x=40,y=80)
window.mainloop()