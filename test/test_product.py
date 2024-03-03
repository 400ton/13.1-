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
    product = Product('Product 1', 'Description 1', 100000.0, 1)
    new_product = Product.create_product('Product 2', 'Description 2', 200000.0, 2, test_data['products'])
    product_2 = Product.create_product('Product 2', 'Description 2', 10000.0, 1, test_data['products'])


def test_price(test_data):
    product = Product.create_product("Product 1", "Description 1", 100000.0, 1, test_data['products'])
    assert product.price == 100000.0
    product.price = 200000.0
    assert product.price == 200000.0
    product.price = 1000.0
    assert product.price == 1000.0


def test_repr_product(test_data):
    products = test_data['products']
    product_in = Product(products[0]['name'], products[0]['description'], products[0]['price'],
                         products[0]['quantity'])

    product_in_1 = Product(products[1]['name'], products[1]['description'], products[1]['price'],
                           products[0]['quantity'])

    product_in_2 = Product(products[2]['name'], products[2]['description'], products[2]['price'],
                           products[0]['quantity'])

    assert repr(product_in) == 'Product, Product 1, Description 1, 100000.0, 1'
    assert repr(product_in_1) == 'Product, Product 2, Description 2, 200000.0, 1'
    assert repr(product_in_2) == 'Product, Product 3, Description 3, 300000.0, 1'
