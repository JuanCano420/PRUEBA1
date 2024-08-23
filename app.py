# app.py

from flask import Flask, render_template
from src.inventory_manager import InventoryManager
from src.product import Product
from src.category import Category

app = Flask(__name__)

# Crear una instancia del gestor de inventario y añadir algunos datos
manager = InventoryManager()
electronics = Category("Electronics", "Devices and gadgets")
phone = Product("Phone", "Smartphone with 4G", 699.99, 50, electronics)
manager.add_category(electronics)
manager.add_product(phone)

@app.route('/')
def index():
    # Consultar el producto y pasarlo a la plantilla
    product = manager.get_product("Phone")
    return render_template('index.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
