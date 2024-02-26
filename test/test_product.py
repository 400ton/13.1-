import pytest
from src.class_product import Product


@pytest.fixture
def test_data():
    return {"name": "Category 1",
            "description": "Description 1",
            "products": [{"name": "Product 1",
                          "description": "Description 1",
                          "price": 100000.0,
                          "quantity": 1},
                         {"name": "Product 2",
                          "description": "Description 2",
                          "price": 200000.0,
                          "quantity": 2},
                         {"name": "Product 3",
                          "description": "Description 3",
                          "price": 300000.0,
                          "quantity": 3}]}


def test_init(test_data):
    products = test_data['products']
    for product in products:
        product_instance = Product(**product)
        assert product_instance.name == product['name']
        assert product_instance.description == product['description']
        assert product_instance.price == product['price']
        assert product_instance.quantity == product['quantity']


def test_create(test_data):
    product = Product.create_product('Category 1', 'Description 1', 100000.0, 1, test_data['products'])
    product_2 = Product.create_product('Product 1', 'Description 1', 10000.0, 1, test_data['products'])
    assert product == {'name': 'Category 1', 'description': 'Description 1', 'price': 100000.0, 'quantity': 1}
    assert product['name'] == 'Category 1'
    assert product_2 == {'name': 'Product 1', 'description': 'Description 1', 'price': 10000.0, 'quantity': 1}


def test_price(test_data):
    product = test_data['products']
    add_product = Product(product[0]['name'], product[0]['description'], product[0]['price'], product[0]['quantity'])

    assert add_product.price == 100000.0
    assert add_product.price != 0
    assert add_product.price != str


def test_price(test_data):
    product = Product.create_product("Product 1", "Description 1", 100000.0, 1, test_data['products'])
    assert product['price'] == 100000.0
    product['price'] = 200000.0
    assert product['price'] == 200000.0
    product['price'] = 90000.0
    assert product['price'] != 100000.0


def test_repr_product(test_data):
    products = test_data['products']
    for product in products:
        product_instance = Product(product['name'], product['description'], product['price'], product['quantity'])
        assert repr(
            product_instance) == f'{product_instance.name}, {product_instance.description}, {product_instance.price}, {product_instance.quantity}'
