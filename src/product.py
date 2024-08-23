class Product:
    def __init__(self, name, description, price, initial_stock, category):
        self.name = name
        self.description = description
        self.price = price
        self.stock = initial_stock
        self.category = category

    def add_stock(self, quantity):
        self.stock += quantity

    def remove_stock(self, quantity):
        if quantity > self.stock:
            raise ValueError("Not enough stock available")
        self.stock -= quantity

    def get_stock_value(self):
        return self.stock * self.price
