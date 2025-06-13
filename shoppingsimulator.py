import tkinter as tk
from tkinter import messagebox

# This is a simple shopping cart system made with tkinter GUI.
# You can add or remove products, see the total, check for discounts, and choose a payment method.
# This version includes a fix so discounts apply only to products that actually have them.

# This is the list of items you can buy. Each item has a price and some have discounts.
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

# This keeps track of what you've added to your cart.
cart = {}

# Set up the main window (made smaller so it fits on smaller screens)
root = tk.Tk()
root.title("Shopping Cart System")
root.geometry("520x640")  # Smaller window size

# Variables that will update the cart and messages on screen
cart_text = tk.StringVar()
total_text = tk.StringVar()
message_text = tk.StringVar()

# This function updates the cart view and the total
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

# When you click Add, it adds the item to the cart
def add_item(item):
    cart[item] = cart.get(item, 0) + 1
    message_text.set(f"Added {item}")
    update_cart_display()

# When you click Remove, it takes one of that item out of the cart
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

# This clears everything from the cart
def clear_cart():
    cart.clear()
    update_cart_display()
    message_text.set("Cart cleared")

# A reset button to clear everything and reset payment option
def reset_all():
    cart.clear()
    payment_var.set("Cash")
    cart_text.set("")
    total_text.set("")
    message_text.set("System reset")

# When you click Checkout, this shows the final total and the payment type
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
            item_total = item_price * qty * 0.9  # apply 10% discount
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

# Shows a help popup with instructions
def show_help():
    help_msg = (
        "Instructions:\n"
        "1. Use Add to put something in your cart.\n"
        "2. Use Remove to take something out.\n"
        "3. Choose how you want to pay (like cash or card).\n"
        "4. Click Checkout to see your total.\n"
        "5. Clear Cart removes all items.\n"
        "6. Reset will restart the whole thing."
    )
    messagebox.showinfo("Help", help_msg)

# This part makes the list of products and buttons
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Product List", font=("Arial", 14)).pack()
for item in products:
    btn_frame = tk.Frame(frame)
    btn_frame.pack(fill='x', padx=5, pady=2)
    label_text = f"{item} - ${products[item]['price']:.2f} ({'10 percent off' if products[item]['discount'] else 'No discount'})"
    tk.Label(btn_frame, text=label_text, width=40, anchor='w').pack(side='left')
    tk.Button(btn_frame, text="Add", width=6, command=lambda i=item: add_item(i)).pack(side='left')
    tk.Button(btn_frame, text="Remove", width=8, command=lambda i=item: remove_item(i)).pack(side='left')

# This shows your cart and totals
tk.Label(root, text="\nYour Cart", font=("Arial", 13)).pack()
tk.Label(root, textvariable=cart_text, justify='left', bg="white", relief="solid", width=50, height=8).pack(pady=5)
tk.Label(root, textvariable=total_text, font=('Arial', 12, 'bold')).pack(pady=5)
tk.Label(root, textvariable=message_text, fg='green').pack()

# Dropdown to pick how you want to pay
tk.Label(root, text="Payment Method:", font=('Arial', 11)).pack()
payment_var = tk.StringVar(value="Cash")
payment_menu = tk.OptionMenu(root, payment_var, "Cash", "Credit", "EFTPOS", "Online Banking")
payment_menu.pack(pady=5)

# These are the action buttons at the bottom
btns = tk.Frame(root)
btns.pack(pady=10)
tk.Button(btns, text="Checkout", width=12, bg="green", fg="white", command=checkout).pack(side='left', padx=5)
tk.Button(btns, text="Clear Cart", width=12, command=clear_cart).pack(side='left', padx=5)
tk.Button(btns, text="Reset All", width=12, command=reset_all).pack(side='left', padx=5)
tk.Button(btns, text="Help", width=10, command=show_help).pack(side='left', padx=5)

# Start the app
update_cart_display()
root.mainloop()
