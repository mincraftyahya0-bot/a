#activity1
from tkinter import *
window=Tk()
'''nums=[[9,8,7],[6,5,4],[3,2,1],["#",0,"*"]]
for i in range(4):
    window.columnconfigure(i,weight=1,minsize=75)
    window.rowconfigure(i,weight=1,minsize=50)
    for j in range(0,3):
        frame=Frame(master=window,relief=SUNKEN,borderwidth=1)
        frame.grid(row=i,column=j)
        label=Label(master=frame,text=nums[i][j],bg="black")
        label.pack(padx=3,pady=3)
window.mainloop()'''
frame=Frame(master=window,height=200,width=360,bg="black")
lb1=Label(master=frame,text="Enter Name",bg="black",fg="white")
lb2=Label(master=frame,text="Enter Email",bg="black",fg="white")
lb3=Label(master=frame,text="Enter Password",bg="black",fg="white")
nament=Entry(frame,show="•")
ement=Entry(frame)
ident=Entry(frame)
def display():
    name=ident.get()
    greet=f"hi {name}\n"
    messege="Welcome To Your New Account"
    textbox.insert(END,greet)
    textbox.insert(END,messege)
textbox=Text(bg="#BEBEBE",fg="black")
btn=Button(text="Create Account",command=display,bg="red")
frame.place(x=20,y=0)
lb1.place(x=20,y=20)
lb2.place(x=20,y=80)
lb3.place(x=20,y=140)
ident.place(x=150,y=20)
ement.place(x=150,y=80)
nament.place(x=150,y=140)
btn.place(x=130,y=210)
textbox.place(y=250)
window.mainloop()