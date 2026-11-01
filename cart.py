cart = []

def add_to_cart(product):
    cart.append(product)
    print(product, "added to cart")

def show_cart():
    print("Shopping Cart:")
    for item in cart:
        print(item)
