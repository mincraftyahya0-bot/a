
import tkinter as tk
from datetime import date

def calculate_age():
    day = int(day_entry.get())
    month = int(month_entry.get())
    year = int(year_entry.get())

    today = date.today()
    birth_date = date(year, month, day)

    age = today.year - birth_date.year

    if (today.month, today.day) < (month, day):
        age -= 1

    result.config(text=f"Your age is {age} years")

window = tk.Tk()
window.title("Age Calculator")
window.geometry("350x350")

tk.Label(window, text="Age Calculator",
         font=("Arial", 16)).pack(pady=10)

tk.Label(window, text="Enter Day:").pack()
day_entry = tk.Entry(window)
day_entry.pack()

tk.Label(window, text="Enter Month:").pack()
month_entry = tk.Entry(window)
month_entry.pack()

tk.Label(window, text="Enter Year:").pack()
year_entry = tk.Entry(window)
year_entry.pack()

tk.Button(window, text="Calculate Age",
          command=calculate_age).pack(pady=15)

result = tk.Label(window, text="Your age will appear here")
result.pack()

window.mainloop()