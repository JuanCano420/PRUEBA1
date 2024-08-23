class Supplier:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.products = []

    def add_product(self, product):
        if product not in self.products:
            self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
