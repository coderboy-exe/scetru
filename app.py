from flask import Flask
from api.products import products_route
from api.orders import orders_route

app = Flask(__name__)

app.register_blueprint(products_route)
app.register_blueprint(orders_route)


if __name__ == '__main__':
    app.run(debug=True)
