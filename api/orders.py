import json
from flask import Blueprint, request, jsonify
from .products import get_product_by_id, products

orders_route = Blueprint('orders', __name__)

# Dummy order data
orders = [
    {
        "id": 1,
        "userId": 1,
        "details": {
            "productId": 1,
            "price": 10.99, 
            "quantity": 5
        },
        "total": 54.95
    },
    {
        "id": 2,
        "userId": 1,
        "details": {
            "productId": 2,
            "price": 20.49, 
            "quantity": 3
        },
        "total": 61.47
    },
    {
        "id": 3,
        "userId": 2,
        "details": {
            "productId": 2,
            "price": 20.49, 
            "quantity": 3
        },
        "total": 61.47
    }
]


@orders_route.route('/orders', methods=['GET'])
def get_orders_by_user():
    """Gets all existing orders
    Returns:
        list: a listof all existing orders of a user
    """
    user_id = request.args.get('user_id', None)
    if user_id is not None:
        print(user_id)
        user_orders = [order for order in orders if order.get("userId") == int(user_id)]
        return jsonify(user_orders), 200
    return jsonify(orders, 200)

@orders_route.route('/orders', methods=['POST'])
def place_order():
    """Place a new order
    Returns:
        dict: success message, created order ID
    """
    if not request.get_json():
        return jsonify("No request body")
    
    data = request.get_json()

    product_id = data.get("productId")
    quantity = data.get("quantity")
    user_id = data.get("userId")
    
    if not product_id or not quantity:
        return jsonify("Required fields: userId, productId, quantity"), 400 
    
    res, status_code = get_product_by_id(product_id)
    if (status_code) != 200:
        return jsonify({"message": "Product not found"}), 404

    product = json.loads(res.data)
    unit_price = product.get("price")
    order_total = unit_price * quantity
    
    order_details = {
        "productId": product_id,
        "price": unit_price, 
        "quantity": quantity
    }
    order_id = len(orders) + 1
    orders.append({"id": order_id, "userId": user_id, "details": order_details, "total": order_total})
    return jsonify({"message": "Order placed successfully", "order_id": order_id}), 201

@orders_route.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id: int):
    """Gets an order based on it's id
    Args:
        order_id (int): order ID
    Returns:
        dict: existing order || 404
    """
    for order in orders:
        if order.get('id') == order_id:
            return jsonify(order), 200
    return jsonify({"message": "Order not found"}), 404
