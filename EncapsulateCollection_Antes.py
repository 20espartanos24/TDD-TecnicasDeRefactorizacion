class ShoppingCart:
    def __init__(self):
        self.items = []  # Lista de productos en el carrito

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        return self.items

cart = ShoppingCart()
cart.add_item("Laptop")
cart.add_item("Headphones")
print("Productos en el carrito:", cart.get_items())
cart.remove_item("Laptop")
print("Productos en el carrito:", cart.get_items())

