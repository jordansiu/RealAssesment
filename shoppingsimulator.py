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

def check_discount():
    return any(products[item]["discount"] for item in cart)
while True:
    display_products()
    display_cart()
    action = input("\nWhat would you like to do? (add/remove/total): ").strip().lower()

    if action == "total":
        break

    elif action == "add":
        item_name = input("Enter the product name to add: ").strip().lower()
        if item_name in products:
            qty_input = input(f"How many {item_name}s would you like to add? ").strip()
            if qty_input.isdigit():
                qty = int(qty_input)
                cart[item_name] = cart.get(item_name, 0) + qty
                print(f" Added {qty} x {item_name.title()} to cart.")
            else:
                print(" Invalid quantity. Must be a number.")
        else:
            print(" That item doesn't exist.")
            
    elif action == "remove":
        item_name = input("Enter the product name to remove: ").strip().lower()
        if item_name in cart:
            qty_input = input(f"How many {item_name}s would you like to remove? ").strip()
            if qty_input.isdigit():
                qty = int(qty_input)
                if qty >= cart[item_name]:
                    del cart[item_name]
                    print(f" Removed all {item_name.title()}s from cart.")
                else:
                    cart[item_name] -= qty
                    print(f" Removed {qty} x {item_name.title()}.")
            else:
                print(" Invalid quantity.")
        else:
            print(" That item is not in your cart.")

    else:
        print(" Unknown action. Please type 'add', 'remove', or 'total'.")
