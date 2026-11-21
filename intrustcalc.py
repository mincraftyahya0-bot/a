
import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        p = float(principal_entry.get())
        t = float(time_entry.get())
        r = float(rate_entry.get())

        if p < 0 or t < 0 or r < 0:
            messagebox.showerror("Error", "Enter positive values")
            return

        si = (p * t * r) / 100
        ci = p * ((1 + r / 100) ** t - 1)

        simple_result.set(f"Simple Interest: {si:.2f}")
        compound_result.set(f"Compound Interest: {ci:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")


root = tk.Tk()
root.title("Interest Calculator")
root.geometry("400x350")
root.configure(bg="lightblue")

tk.Label(
    root,
    text="Interest Calculator",
    font=("Arial", 20, "bold"),
    bg="lightblue"
).pack(pady=15)

tk.Label(
    root,
    text="Principal Amount:",
    bg="lightblue"
).pack()

principal_entry = tk.Entry(root)
principal_entry.pack(pady=5)

tk.Label(
    root,
    text="Time Period (Years):",
    bg="lightblue"
).pack()

time_entry = tk.Entry(root)
time_entry.pack(pady=5)

tk.Label(
    root,
    text="Rate of Interest (%):",
    bg="lightblue"
).pack()

rate_entry = tk.Entry(root)
rate_entry.pack(pady=5)

tk.Button(
    root,
    text="Calculate",
    command=calculate,
    bg="green",
    fg="white"
).pack(pady=15)

simple_result = tk.StringVar()
compound_result = tk.StringVar()

tk.Label(
    root,
    textvariable=simple_result,
    bg="lightblue",
    font=("Arial", 12)
).pack(pady=5)

tk.Label(
    root,
    textvariable=compound_result,
    bg="lightblue",
    font=("Arial", 12)
).pack(pady=5)

root.mainloop()
