from flask import request, jsonify, Blueprint

products_route = Blueprint('products', __name__)

# Dummy product data 
products = [
    {
        "id": 1, 
        "name": "Product 1", 
        "price": 10.99, 
        "categoryId": 1,
        "category": "Category 1",
        "description": "This is the description for Product 1"
    },
    {
        "id": 2, 
        "name": "Product 2", 
        "price": 20.49, 
        "categoryId": 2,
        "category": "Category 2",
        "description": "This is the description for Product 2"
    }
]

@products_route.route('/products', methods=['GET'])
def get_products():
    """All products

    Returns:
        _type_: _description_
    """
    return jsonify(products), 200

@products_route.route('/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id: int):
    """Gets a product by its ID
    Args:
        product_id (int): product ID
    Returns:
        dict: the product
    """
    for product in products:
        if product.get('id') == product_id:
            return jsonify(product), 200
    return jsonify({"message": "Product not found"}), 404

