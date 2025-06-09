products = {
    "apple": {"price": 2.0, "discount": True},
    "banana": {"price": 1.5, "discount": False},
    "milk": {"price": 3.0, "discount": True},
    "bread": {"price": 2.5, "discount": False},
    "cheese": {"price": 4.0, "discount": True}
}

cart = {}  # item: quantity
total = 0.0

def display_products():
    print("\n AVAILABLE PRODUCTS")
    for item, info in products.items():
        discount = "Yes" if info["discount"] else "No"
        print(f"- {item.title()} | Price: ${info['price']:.2f} | Discount: {discount}")
    print("Type 'add', 'remove', or 'total' when you're ready.\n")

def display_cart():
    print("\n CURRENT CART:")
    if not cart:
        print("Cart is empty.")
    else:
        for item, qty in cart.items():
            price = products[item]["price"]
            print(f"- {item.title()} x{qty} = ${price * qty:.2f}")
        print(f"Subtotal so far: ${calculate_total():.2f}")

def calculate_total():
    return sum(products[item]["price"] * qty for item, qty in cart.items())