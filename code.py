# Available products
products = {
    "apple": {"price": 2.0, "discount": True},
    "banana": {"price": 1.5, "discount": False},
    "milk": {"price": 3.0, "discount": True}
}

# Cart with quantities
cart = {}  # key: item name, value: quantity
total = 0.0

while True:
    print("\n--- Menu ---")
    print("Available items:")
    for name, data in products.items():
        print(f"- {name.title()} (${data['price']}) | Discount: {'Yes' if data['discount'] else 'No'}")

    item_name = input("Enter item name (or type 'total' to finish): ").lower()

    if item_name == "total":
        print("\nItems in your cart:")
        for item, qty in cart.items():
            print(f"- {item.title()} x{qty}")
        print(f"Subtotal: ${total:.2f}")

        # Check for any discounts
        discount_applied = any(products[item]["discount"] for item in cart)
        if discount_applied:
            print("Discount applied: -10%")
            total *= 0.9
        else:
            print("No discount available.")

        print(f"Final total: ${total:.2f}")
        confirm = input("Is that all the items? (yes/no): ").lower()
        if confirm == "yes":
            print("Proceeding to checkout...")
            break
        else:
            continue

    elif item_name in products:
        cart[item_name] = cart.get(item_name, 0) + 1
        total += products[item_name]["price"]
        print(f"{item_name.title()} added to cart. Current total: ${total:.2f}")
    else:
        print("Invalid item name.")