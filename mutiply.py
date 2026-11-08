
import tkinter as tk

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        product = num1 * num2

        result.config(text=f"Product = {product:g}")
    except ValueError:
        result.config(text="Please enter valid numbers!")

window = tk.Tk()
window.title("Multiplication Calculator")
window.geometry("350x250")

tk.Label(window, text="Multiplication Calculator",
         font=("Arial", 16)).pack(pady=10)

tk.Label(window, text="Enter First Number:").pack()
entry1 = tk.Entry(window)
entry1.pack(pady=5)

tk.Label(window, text="Enter Second Number:").pack()
entry2 = tk.Entry(window)
entry2.pack(pady=5)

tk.Button(window, text="Multiply",
          command=multiply).pack(pady=10)

result = tk.Label(window, text="Result will appear here")
result.pack()

window.mainloop()
