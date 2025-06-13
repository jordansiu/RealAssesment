import tkinter as tk
from tkinter import messagebox

# This is a simple shopping cart system made with tkinter GUI.
# You can add or remove products, see the total, check for discounts, and choose a payment method.
# This version includes a fix so discounts apply only to products that actually have them.

# List of available items with prices and discount flags
products = {
    "Apple": {"price": 2.0, "discount": True},
    "Banana": {"price": 1.5, "discount": False},
    "Milk": {"price": 3.0, "discount": True},
    "Bread": {"price": 2.5, "discount": False},
    "Cheese": {"price": 4.0, "discount": True},
    "Eggs": {"price": 3.5, "discount": False},
    "Yogurt": {"price": 2.2, "discount": True},
    "Juice": {"price": 3.0, "discount": True},
    "Cereal": {"price": 3.8, "discount": False},
    "Butter": {"price": 2.9, "discount": True}
}

# This is the cart where items will be added
cart = {}

# Set up the main window (smaller to fit most screens)
root = tk.Tk()
root.title("Shopping Cart System")
root.geometry("500x480")  # Smaller window size to fit smaller screens

# Variables that update the GUI content
cart_text = tk.StringVar()
total_text = tk.StringVar()
message_text = tk.StringVar()

# Update cart display with current items and prices
def update_cart_display():
    lines = []
    total = 0.0
    for item, qty in cart.items():
        price = products[item]["price"] * qty
        lines.append(f"{item} x{qty} = ${price:.2f}")
        total += price
    if lines:
        cart_text.set("\n".join(lines))
    else:
        cart_text.set("Cart is empty.")
    total_text.set(f"Subtotal: ${total:.2f}")

# Add item to cart
def add_item(item):
    cart[item] = cart.get(item, 0) + 1
    message_text.set(f"Added {item}")
    update_cart_display()

# Remove item from cart
def remove_item(item):
    if item in cart:
        if cart[item] > 1:
            cart[item] -= 1
        else:
            del cart[item]
        message_text.set(f"Removed {item}")
    else:
        message_text.set(f"{item} not in cart")
    update_cart_display()

# Clear cart contents
def clear_cart():
    cart.clear()
    update_cart_display()
    message_text.set("Cart cleared")

# Reset everything
def reset_all():
    cart.clear()
    payment_var.set("Cash")
    cart_text.set("")
    total_text.set("")
    message_text.set("System reset")

# Checkout and calculate individual discounts
def checkout():
    if not cart:
        messagebox.showinfo("Checkout", "Your cart is empty!")
        return

    subtotal = 0.0
    discount_total = 0.0
    summary_lines = []

    for item, qty in cart.items():
        item_price = products[item]["price"]
        if products[item]["discount"]:
            item_total = item_price * qty * 0.9
            discount_total += (item_price * qty) - item_total
        else:
            item_total = item_price * qty
        subtotal += item_total
        summary_lines.append(f"- {item} x{qty} = ${item_total:.2f}")

    summary = "Checkout Summary\n"
    summary += f"Total Savings: ${discount_total:.2f}\n"
    summary += f"Final Total: ${subtotal:.2f}\n"
    summary += f"Payment Method: {payment_var.get()}\n"
    summary += "\nItems:\n"
    summary += "\n".join(summary_lines)

    messagebox.showinfo("Order Complete", summary)
    clear_cart()

# Help instructions
def show_help():
    help_msg = (
        "Instructions:\n"
        "1. Click Add to put an item in the cart.\n"
        "2. Click Remove to take it out.\n"
        "3. Pick how you want to pay.\n"
        "4. Use Checkout to finish.\n"
        "5. Clear Cart to empty it.\n"
        "6. Reset All to start fresh."
    )
    messagebox.showinfo("Help", help_msg)

# Create product list and buttons
frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="Product List", font=("Arial", 12)).pack()
for item in products:
    btn_frame = tk.Frame(frame)
    btn_frame.pack(fill='x', padx=5, pady=1)
    label_text = f"{item} - ${products[item]['price']:.2f} ({'10 percent off' if products[item]['discount'] else 'No discount'})"
    tk.Label(btn_frame, text=label_text, width=40, anchor='w', font=("Arial", 9)).pack(side='left')
    tk.Button(btn_frame, text="Add", width=5, command=lambda i=item: add_item(i)).pack(side='left')
    tk.Button(btn_frame, text="Remove", width=6, command=lambda i=item: remove_item(i)).pack(side='left')

# Cart display and total
tk.Label(root, text="\nYour Cart", font=("Arial", 11)).pack()
tk.Label(root, textvariable=cart_text, justify='left', bg="white", relief="solid", width=50, height=6, font=("Arial", 9)).pack(pady=5)
tk.Label(root, textvariable=total_text, font=('Arial', 10, 'bold')).pack(pady=3)
tk.Label(root, textvariable=message_text, fg='green', font=("Arial", 9)).pack()

# Payment method dropdown
tk.Label(root, text="Payment Method:", font=('Arial', 10)).pack()
payment_var = tk.StringVar(value="Cash")
payment_menu = tk.OptionMenu(root, payment_var, "Cash", "Credit", "EFTPOS", "Online Banking")
payment_menu.config(font=("Arial", 9))
payment_menu.pack(pady=4)

# Action buttons
btns = tk.Frame(root)
btns.pack(pady=5)
tk.Button(btns, text="Checkout", width=10, bg="green", fg="white", command=checkout, font=("Arial", 9)).pack(side='left', padx=3)
tk.Button(btns, text="Clear Cart", width=10, command=clear_cart, font=("Arial", 9)).pack(side='left', padx=3)
tk.Button(btns, text="Reset All", width=10, command=reset_all, font=("Arial", 9)).pack(side='left', padx=3)
tk.Button(btns, text="Help", width=8, command=show_help, font=("Arial", 9)).pack(side='left', padx=3)

# Launch the app
update_cart_display()
root.mainloop()