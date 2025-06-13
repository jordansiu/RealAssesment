import tkinter as tk
from tkinter import messagebox

# This is a simple shopping cart system made with tkinter GUI.
# You can add or remove products, see the total, check for discounts, and choose a payment method.
# This version is now made longer and includes more explanations and options.

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

# Set up the main window
root = tk.Tk()
root.title("Shopping Cart System")
root.geometry("600x700")  # Made bigger since we have more features

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
        total += price
        lines.append(f"{item} x{qty} = ${price:.2f}")
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