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
    product = Product('Nokia', 'клевый', 'черный', 10000, 1)
    product_2 = Product('Siemens', 'клевый', 'черный', 20000, 1)

    lst = [product, product_2]
    date = {"name": "Nokia",
            "description": "клевый",
            "color": "черный",
            "price": 180000.0,
            "quantity": 5}

    new_product = Product.create_product(lst, **date)
    assert (new_product.name == 'Nokia' and new_product.description == 'клевый' and new_product.color == 'черный'
            and new_product.price == 180000.0 and new_product.quantity == 5)

    data_2 = {"name": "Product 1",
              "description": "Description 1",
              "color": "Color 1",
              "price": 1000.0,
              "quantity": 1}

    new_product_2 = Product.create_product(lst, **data_2)
    assert new_product_2.name == 'Product 1'
    assert new_product_2.price == 10000.0
    assert new_product_2.quantity == 1


def test_price(test_data):
    """
    Тест функции изменения цены товара
    :param test_data:
    """
    product = {"name": "Product 1",
               "description": "Description 1",
               "color": "Color 1",
               "price": 100000.0,
               "quantity": 1}

    new_product = Product.create_product(test_data, **product)
    with mock.patch('builtins.input', return_value='y'):
        new_product.price = 200000.0
        assert new_product.price == 200000.0
        new_product.price = 1000.0
        assert new_product.price == 1000.0


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
                                    "'_price': 200000.0, 'quantity': 2}\n")
