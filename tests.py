import json
import unittest
from unittest.mock import patch
from app import app
from api import products, orders


class TestProductInformationAPI(unittest.TestCase):
    @patch('api.products.products', [{"id": 1, "name": "Product 1", "price": 10.99, "description": "Description of Product 1"}])
    def test_get_products(self):
        with app.test_client() as client:
            response = client.get('/products')
            self.assertEqual(response.status_code, 200)

    @patch('api.products.products', [{"id": 1, "name": "Product 1", "price": 10.99, "description": "Description of Product 1"}])
    def test_get_product_by_id(self):
        with app.test_client() as client:
            product_id = 1
            response = client.get(f'/products/{product_id}')
            self.assertEqual(response.status_code, 200)
            

class TestOrderProcessingAPI(unittest.TestCase):
    @patch('api.orders.orders', [])
    def test_place_order(self):
        with app.test_client() as client:
            order_data = {"productId": 1, "quantity": 2}
            response = client.post('/orders', json=order_data)
            self.assertEqual(response.status_code, 200)
            self.assertIn("order_id", json.loads(response.data))

    @patch('api.orders.orders', [{"id": 1, "userId": 1, "details": {"productId": 1, "price": 10.99, "quantity": 2}, "total": 10.99}, {"id": 1, "userId": 2, "details": {"productId": 1, "price": 10.99, "quantity": 2}, "total": 10.99}])
    def test_get_order(self):
        with app.test_client() as client:
            order_id = 1
            response = client.get(f'/orders/{order_id}')
            self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()
