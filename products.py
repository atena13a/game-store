products = [
    {
        "name": "God of War",
        "price": 50,
        "platform": "PS5",
        "genre": "Action"
    },
    {
        "name": "Minecraft",
        "price": 30,
        "platform": "PC",
        "genre": "Adventure"
    }
]

def show_products():
    for product in products:
        print(product["name"], "-", product["price"])
