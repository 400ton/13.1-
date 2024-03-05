import pytest
from unittest import mock
from src.class_product import Product


@pytest.fixture
def test_data():
    return {"name": "Category 1",
            "description": "Description 1",
            "products": [{"name": "Product 1",
                          "description": "Description 1",
                          "color": "Color 1",
                          "price": 100000.0,
                          "quantity": 1},
                         {"name": "Product 2",
                          "description": "Description 2",
                          "color": "Color 2",
                          "price": 200000.0,
                          "quantity": 2},
                         {"name": "Product 3",
                          "description": "Description 3",
                          "color": "Color 3",
                          "price": 300000.0,
                          "quantity": 3}]}


def test_init(test_data):
    products = test_data['products']
    for product in products:
        product_instance = Product(**product)
        assert product_instance.name == product['name']
        assert product_instance.description == product['description']
        assert product_instance.color == product['color']
        assert product_instance.price == product['price']
        assert product_instance.quantity == product['quantity']


def test_create_product(test_data):
    products = test_data['products']
    new_product = Product.create_product('Nokia', 'клевый', 'черный', 10000, 1, products)
    assert (new_product.name == 'Nokia' and new_product.description == 'клевый' and new_product.color == 'черный'
            and new_product.price == 10000 and new_product.quantity == 1)

    product_2 = Product.create_product('Siemens', 'клевый', 'черный', 20000, 1, products)
    assert (product_2.name == 'Siemens' and product_2.description == 'клевый' and product_2.color == 'черный'
            and product_2.price == 20000 and product_2.quantity == 1)


def test_price(test_data):
    products = test_data['products']
    product = Product.create_product("Product 1", "Description 1", "Color 1", 100000.0, 1, products)
    with mock.patch('builtins.input', return_value='y'):
        product.price = 200000.0
        assert product.price == 200000.0
        product.price = 1000.0
        assert product.price == 1000.0


def test_repr_product(test_data):
    products = test_data['products']
    test_product = Product(**products[0])
    assert repr(test_product) == test_product.__repr__()

    test_product_2 = Product(**products[1])
    assert repr(test_product_2) == ('Class name: Product, Name: Product 2, Description: Description 2, Color: Color 2, '
                                    'Price: 200000.0, Quantity: 2')

