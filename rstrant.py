import tkinter as tk
from tkinter import ttk, messagebox


class Restaurant:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Order")

        self.menu_items = {
            "FRIES MEAL": 2,
            "LUNCH MEAL": 2,
            "BURGER MEAL": 3,
            "PIZZA MEAL": 4,
            "CHEESE BURGER": 2.5,
            "DRINKS": 1,
        }
        self.exchange_rate = 82

        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ttk.Label(frame, text="Restaurant Order Management",
                  font=("Arial", 20, "bold")).grid(row=0, columnspan=3, padx=10, pady=10)

        self.menu_labels = {}
        self.menu_quantities = {}

        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            lbl = ttk.Label(frame, text=f"{item} (${price:.2f}):", font=("Arial", 12))
            lbl.grid(row=i, column=0, padx=10, pady=5)
            self.menu_labels[item] = lbl

            entry = ttk.Entry(frame, width=5)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = entry

        row = len(self.menu_items) + 1
        self.currency_var = tk.StringVar()
        ttk.Label(frame, text="Currency:", font=("Arial", 12)).grid(row=row, column=0, padx=10, pady=5)

        dropdown = ttk.Combobox(frame, textvariable=self.currency_var,
                                state="readonly", width=18, values=("USD", "INR"))
        dropdown.grid(row=row, column=1, padx=10, pady=5)
        dropdown.current(0)
        self.currency_var.trace_add("write", self.update_menu_prices)

        ttk.Button(frame, text="Place Order", command=self.place_order).grid(
            row=row + 1, columnspan=3, padx=10, pady=10)

    def get_currency(self):
        if self.currency_var.get() == "INR":
            return "₹", self.exchange_rate
        return "$", 1

    def update_menu_prices(self, *args):
        symbol, rate = self.get_currency()
        for item, label in self.menu_labels.items():
            price = self.menu_items[item] * rate
            label.config(text=f"{item} ({symbol}{price:.2f}):")

    def place_order(self):
        symbol, rate = self.get_currency()
        total_cost = 0
        order_summary = "Order Summary:\n"

        for item, entry in self.menu_quantities.items():
            quantity = entry.get().strip()
            if quantity.isdigit() and int(quantity) > 0:
                quantity = int(quantity)
                price = self.menu_items[item] * rate
                cost = quantity * price
                total_cost += cost
                order_summary += f"{item}: {quantity} x {symbol}{price:.2f} = {symbol}{cost:.2f}\n"

        if total_cost > 0:
            order_summary += f"\nTotal Cost: {symbol}{total_cost:.2f}"
            messagebox.showinfo("Order Placed", order_summary)
        else:
            messagebox.showerror("Error", "Please order at least one item.")


if __name__ == "__main__":
    root = tk.Tk()
    app = Restaurant(root)
    root.geometry("800x600")
    root.mainloop()