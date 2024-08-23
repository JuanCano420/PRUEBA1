class Warehouse:
    def __init__(self, name, location, max_capacity):
        self.name = name
        self.location = location
        self.max_capacity = max_capacity
        self.products = {}

    def add_product(self, product, quantity):
        if product in self.products:
            if self.products[product] + quantity > self.max_capacity:
                raise ValueError("Not enough space in the warehouse")
            self.products[product] += quantity
        else:
            if quantity > self.max_capacity:
                raise ValueError("Not enough space in the warehouse")
            self.products[product] = quantity

    def remove_product(self, product, quantity):
        if product not in self.products or self.products[product] < quantity:
            raise ValueError("Not enough stock available in the warehouse")
        self.products[product] -= quantity
        if self.products[product] == 0:
            del self.products[product]

    def check_availability(self, product):
        return self.products.get(product, 0)
