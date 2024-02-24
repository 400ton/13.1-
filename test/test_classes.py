import pytest
from src.class_category import Category
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


def test_init_category(test_data):
    '''тестирование функции инициализации класса Category'''

    category = Category(test_data[0]["name"], test_data[0]["description"], test_data[0]["products"])
    assert category.name == "Category 1"
    assert category.description == "Description 1"
    assert category.total_categories == 1
    assert category.total_products == 3


def test_get_goods(test_data):
    '''Тестирование функции get_goods'''
    category = Category(test_data[0]["name"], test_data[0]["description"], test_data[0]["products"])
    products = test_data[0]["products"]
    print(products)

    for product in products:
        category.get_goods(Product(**product))

    assert category.total_categories == 1
    assert category.total_products == len(products)
    assert category.goods == products


def test_repr_category(test_data):
    '''тестирование функции __repr__'''
    category = Category(test_data[0]["name"], test_data[0]["description"])
    assert repr(category) == f'{category.name}, {category.description}, []'
    assert repr(category.description) == "'Description 1'"
    assert repr(category.name) == "'Category 1'"


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


def test_create_product(test_data):
    '''Тестирование функции create_product'''
    category = Category(test_data[0]["name"], test_data[0]["description"])
    products = test_data[0]["products"]

    for product in products:
        category.create_product(Product(**product))

    assert category.total_categories == 1
    assert category.total_products == len(products)
    assert category.goods == products


def test_price_product(test_data):
    category = test_data[0]
    product = category['products']
    add_product = Product(product[0]['name'], product[0]['description'], product[0]['price'], product[0]['quantity'])

    assert add_product.price == 100000.0


def test_price(test_data):
    product = Product.create_product("Product 1", "Description 1", 100000.0, 1)
    assert product.price == 100000.0

    product.price = 200000.0
    assert product.price == 200000.0

    product.price = 90000.0
    assert product.price == 100000.0

    product.price = 100000.0
    assert product.price == 100000.0


def test_repr_product(test_data):
    '''тестирование функции __repr__'''
    category = test_data[0]
    products = category['products']

    for product in products:
        product_instance = Product(**product)
        assert repr(
            product_instance) == f'{product_instance.name}, {product_instance.description}, {product_instance.price}, {product_instance.quantity}'
