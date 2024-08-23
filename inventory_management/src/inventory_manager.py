from product import Product
from category import Category
from supplier import Supplier
from warehouse import Warehouse

class InventoryManager:
    def __init__(self):
        self.products = []
        self.categories = []
        self.suppliers = []
        self.warehouses = []

    def add_product(self, product):
        self.products.append(product)

    def add_category(self, category):
        self.categories.append(category)

    def add_supplier(self, supplier):
        self.suppliers.append(supplier)

    def add_warehouse(self, warehouse):
        self.warehouses.append(warehouse)
