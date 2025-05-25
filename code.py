products = {
    "apple": {"price": 1.0, "discount": True},
    "banana":{"price": 1.5, "discount": False},
    "pineapple":{"price":3.0,"discount": True},
}
balance = 20.0
cart = {}

while True:
    print("\n--- Menu ---")
    item_name = input("Enter item name (or type 'total' to finish): ").lower()

    if item_name == "total":
        print("\nItems in your cart:")
        for item in cart:
            print(f"- {item}")
    print(f"Subtotal: ${total:.2f}")

    discount_applied = any(products[item]["discount"] for item in cart)
        if discount_applied:
            print("Discount applied: -10%")
            total *= 0.9  # apply 10% discount
        else:
            print("No discount available.")
            
        print(f"Final total: ${total:.2f}")
        confirm = input("Is that all the items? (yes/no): ").lower()
        if confirm == "yes":
            print("Proceeding to checkout...")
            break
        else:
            continue