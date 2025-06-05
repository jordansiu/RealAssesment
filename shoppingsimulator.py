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