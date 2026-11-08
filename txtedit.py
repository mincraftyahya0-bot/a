from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
window=Tk()
window.title("Text Editor")
window.geometry("600x500")
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

def opnfle():
    filepath=askopenfilename(filetypes=[("Text File","*.txt"),("All Files","*.*")])
    if not filepath:
        return
    txt_edit.delete(1.0,END)

    with open(filepath,"r") as input_file:
        text=input_file.read()
        txt_edit.insert(END,text)
        input_file.close
def svefle():
    filepath=asksaveasfilename(defaultextension="txt",filetypes=[("Text File","*.txt"),("All Files","*.*")])
    if not filepath:
        return
    with open(filepath,"w") as output_file:
        text=txt_edit.get(1.0,END)
        output_file.write(text)
    window.title(f"Txt Editr-{filepath}")

txt_edit=Text(window)
fr_buttons=Frame(window,relief=RAISED,bd=2)
btn_open=Button(fr_buttons,text="Open",command=opnfle)
btn_save=Button(fr_buttons,text="Save As...",command=svefle)
btn_open.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
btn_save.grid(row=1,column=0,sticky="ew",padx=5)

fr_buttons.grid(row=0,column=0,sticky="ns")
txt_edit.grid(row=0,column=1,sticky="nsew")

window.mainloop()