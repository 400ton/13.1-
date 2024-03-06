import pytest
from colorama import Fore
from unittest import mock
from src.class_product import Product


@pytest.fixture
def test_data():
    """
    Тестовые данные для класса Product
    :return: dict
    """
    list_products = {"name": "Category 1",
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
    products = list_products['products']
    return products


def test_init_product(test_data):
    """
    Тест конструктора
    :param test_data:
    """
    for product in test_data:
        product_instance = Product(**product)
        assert product_instance.name == product['name']
        assert product_instance.description == product['description']
        assert product_instance.color == product['color']
        assert product_instance.price == product['price']
        assert product_instance.quantity == product['quantity']


def test_str_product(test_data):
    """
    Тест функции вывода в консоль
    :param test_data:
    """
    test_product = Product(**test_data[0])
    assert str(test_product) == test_product.__str__()
    assert str(test_product) == (f'{Fore.CYAN}Product 1{Fore.RESET}, '
                                 f'100000.0 {Fore.GREEN}руб. '
                                 f'Остаток:{Fore.RESET} 1 {Fore.GREEN}шт{Fore.RESET}')


def test_add_product(test_data):
    """
    Тест функции сложения товара и тест на ошибку Type
    :param test_data:
    """
    test_product = Product(**test_data[0])
    test_product_2 = Product(**test_data[1])

    assert test_product + test_product_2 == 500000.0
    with pytest.raises(TypeError) as excinfo:
        test_product + [*test_data]
    assert 'Невозможно добавить товары разных типов' in str(excinfo.value)


def test_create_product(test_data):
    """
    Тест функции создания товара
    :param test_data:
    """
    new_product = Product.create_product('Nokia', 'клевый', 'черный', 10000, 1, test_data)
    assert (new_product.name == 'Nokia' and new_product.description == 'клевый' and new_product.color == 'черный'
            and new_product.price == 10000 and new_product.quantity == 1)

    product_2 = Product.create_product('Siemens', 'клевый', 'черный', 20000, 1, test_data)
    assert (product_2.name == 'Siemens' and product_2.description == 'клевый' and product_2.color == 'черный'
            and product_2.price == 20000 and product_2.quantity == 1)


def test_price(test_data):
    """
    Тест функции изменения цены товара
    :param test_data:
    """
    product = Product.create_product("Product 1", "Description 1", "Color 1", 100000.0, 1, test_data)
    with mock.patch('builtins.input', return_value='y'):
        product.price = 200000.0
        assert product.price == 200000.0
        product.price = 1000.0
        assert product.price == 1000.0


def test_repr_product(test_data):
    """
    Тест функции вывода отладочной информации в консоль
    :param test_data:
    """
    test_product = Product(**test_data[0])
    assert repr(test_product) == test_product.__repr__()

    test_product_2 = Product(**test_data[1])
    assert repr(test_product_2) == ("\nСоздан класс: Product с атрибутами {'name': 'Product 2', "
                                    "'description': 'Description 2', 'color': 'Color 2', "
                                    "'_price': 200000.0, 'quantity': 2}")
