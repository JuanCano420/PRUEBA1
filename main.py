import sys
import os

# Agrega el directorio src al path de Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from inventory_manager import InventoryManager
from product import Product
from category import Category
from supplier import Supplier
from warehouse import Warehouse

def main():
    manager = InventoryManager()
    
    # Crear algunas instancias de ejemplo
    electronics = Category("Electronics", "Devices and gadgets")
    phone = Product("Phone", "Smartphone with 4G", 699.99, 50, electronics)
    
    # Añadir al gestor
    manager.add_category(electronics)
    manager.add_product(phone)
    
    # Imprimir detalles
    print(f"Product: {phone.name}, Stock: {phone.stock}")

if __name__ == "__main__":
    main()
