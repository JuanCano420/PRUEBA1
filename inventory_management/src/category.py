class Category:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []

    def add_product(self, product):
        if product not in self.products:
            self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
