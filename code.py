products = {
    "apple": {"price": 1.0, "discount": True},
    "banana":{"price": 1.5, "discount": False},
    "pineapple":{"price":3.0,"discount": True}
}
balance = 20.0
cart = {}

def show_products():
    print("\nAvailable Products:")
    for item, details in products.items():
        discount_msg = "Yes" if details["discount"] else "No"
        print(f"{item.title()} - ${details['price']} | Discount: {discount_msg}")

def show_cart():
    print("\nYour Cart:")
    total = 0
    for item, qty in cart.items():
        price = products[item]["price"]