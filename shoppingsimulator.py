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