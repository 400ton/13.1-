import pytest
from src.class_category import Category
from src.class_product import Product


@pytest.fixture
def test_data():
    return [{"name": "Category 1",
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
                           "quantity": 3}]}]


def test_init_category(test_data):
    '''тестирование функции инициализации класса Category'''
    category = Category(test_data[0]["name"], test_data[0]["description"], test_data[0]["products"])

    assert category.name == "Category 1"
    assert category.description == "Description 1"
    assert category.goods == test_data[0]["products"]
    assert category.total_categories == 1
    assert category.total_products == 3


def test_repr_category(test_data):
    '''тестирование функции __repr__'''
    category = Category(test_data[0]["name"], test_data[0]["description"], test_data[0]["products"])
    assert repr(category) == f'{category.name}, {category.description}, {category.goods}'
    assert repr(category.description) == "'Description 1'"
    assert repr(category.name) == "'Category 1'"
    assert repr(category.goods) == [{'name': 'Product 1',
                                     'description': 'Description 1',
                                     'price': 100000.0,
                                     'quantity': 1},
                                    {'name': 'Product 2',
                                     'description': 'Description 2',
                                     'price': 200000.0,
                                     'quantity': 2},
                                    {'name': 'Product 3',
                                     'description': 'Description 3',
                                     'price': 300000.0,
                                     'quantity': 3
                                     }]


def test_init_product(test_data):
    '''тестирование функции инициализации класса Product'''
    category = test_data[0]
    products = category['products']

    for product in products:
        product_instance = Product(**product)
        assert product_instance.name == product['name']
        assert product_instance.description == product['description']
        assert product_instance.price == product['price']
        assert product_instance.quantity == product['quantity']


def test_repr_product(test_data):
    '''тестирование функции __repr__'''
    category = test_data[0]
    products = category['products']

    for product in products:
        product_instance = Product(**product)
        assert repr(product_instance) == f'{product_instance.name}, {product_instance.description}, {product_instance.price}, {product_instance.quantity}'