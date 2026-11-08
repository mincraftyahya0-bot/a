
import tkinter as tk

def convert():
    inches = float(entry.get())
    cm = inches * 2.54
    result.config(text=f"{cm:.2f} cm")

window = tk.Tk()
window.title("Inches to Centimeters")
window.geometry("350x220")

tk.Label(window, text="Inches to Centimeters Converter",
         font=("Arial", 14)).pack(pady=10)

tk.Label(window, text="Enter length in inches:").pack()

entry = tk.Entry(window)
entry.pack(pady=5)

tk.Button(window, text="Convert",
          command=convert).pack(pady=10)

result = tk.Label(window, text="Result will appear here")
result.pack()

window.mainloop()
