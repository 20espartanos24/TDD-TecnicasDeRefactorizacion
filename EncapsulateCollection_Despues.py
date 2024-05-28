class ShoppingCart:
    def __init__(self):
        self._items = [] 

    def add_item(self, item):
        self._items.append(item)

    def remove_item(self, item):
        self._items.remove(item)

    def get_items(self):
        return self._items.copy()

cart = ShoppingCart()
cart.add_item("Laptop")
cart.add_item("Headphones")
print("Productos en el carrito:", cart.get_items())
cart.remove_item("Laptop")
print("Productos en el carrito:", cart.get_items())

