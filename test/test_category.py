import pytest
from colorama import *
from src.class_category import Category
from src.class_product import Product
from src.class_lawn_grass import LawnGrass
from src.class_smartpfone import Smartphone


@pytest.fixture
def test_data():
    """
    Тестовые данные для класса Катогорий
    :return: dict
    """
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
    """
    Тест инициализацию класса Category
    :param test_data:
    """
    category = Category(test_data["name"], test_data["description"], test_data["products"])
    assert category.name == "Category 1"
    assert category.description == "Description 1"
    assert category.total_categories == 1
    assert category.total_products == 3


def test_len(test_data):
    """
    Тест длины списка продуктов в категории
    :param test_data:
    """
    category = Category(test_data["name"], test_data["description"], test_data["products"])
    assert len(category) == 3


def test_str(test_data):
    """
    Тест вывода информации в консоль
    :param test_data:
    """
    category = Category(test_data["name"], test_data["description"], test_data["products"])
    assert str(category) == f'{Fore.CYAN}Category 1 {Fore.RESET},' \
                            f'{Fore.GREEN}Всего продуктов:{Fore.RESET}3 {Fore.GREEN}шт'


def test_goods(test_data):
    """
    Тест геттера категории
    :param test_data:
    """
    category = Category(test_data["name"], test_data["description"], test_data["products"])
    assert category.goods == test_data["products"]


def test_add_goods(test_data):
    """
    Тест добавления продукта в категорию
    :param test_data:
    """
    category = Category(test_data["name"], test_data["description"], test_data["products"])
    new_product = Product('Product 4', 'Description 1', 'red', 100000.0, 4)
    assert category.goods == test_data["products"]
    category.goods = new_product
    assert category.goods == test_data["products"]

    new_product_2 = ('Product 5', 'Description 1', 200000.)
    with pytest.raises(ValueError) as excinfo:
        category.goods = new_product_2
    assert str(excinfo.value) == "Продукт должен быть объектом класса Product"


def test_repr(test_data):
    """
    Тест вывода отладочной информации в консоль
    :param test_data:
    """
    category = Category(test_data["name"], test_data["description"], test_data["products"])
    assert repr(category) == category.__repr__()


# Тестируем класс Lawn_Grass
@pytest.fixture
def test_grass():
    """
    Тестовые данные для класса Lawn_Grass
    :return: Обьект класса
    """
    grass = LawnGrass('Трава', 'Трава зеленая', 'зеленый', 10000, 1, 'ru', 10)
    return grass


def test_init_lawn_grass(test_grass):
    """
    Тест инициализации класса Lawn_Grass
    :param test_grass:
    """

    assert test_grass.name == 'Трава'
    assert test_grass.description == 'Трава зеленая'
    assert test_grass.color == 'зеленый'
    assert test_grass.price == 10000
    assert test_grass.quantity == 1
    assert test_grass.manufacturer == 'ru'
    assert test_grass.germination_period == 10


def test_create_lawn_grass(test_grass):
    """
    Тест создания продукта класса Lawn_Grass
    :param test_grass:
    """
    date = [{'name': 'Трава ',
             'description': 'Трава зеленая',
             'color': 'зеленый',
             'price': 10000,
             'quantity': 1,
             'manufacturer': 'ru',
             'germination_period': 10}]

    grass = {'name': 'Трава 1',
             'description': 'Трава зеленая 1',
             'color': 'зеленый',
             'price': 10000,
             'quantity': 1,
             'manufacturer': 'ru',
             'germination_period': 10}

    new_grass = LawnGrass.create_product(date, **grass)
    assert (new_grass.name == 'Трава 1' and new_grass.description == 'Трава зеленая 1', new_grass.color == 'зеленый',
            new_grass.price == 10000, new_grass.quantity == 1, new_grass.manufacturer == 'ru',
            new_grass.germination_period == 10)


def test_str_lawn_Grass(test_grass):
    """
    Тест вывода строковой информации в консоль
    :param test_grass:
    """

    assert str(test_grass) == test_grass.__str__()


def test_repr_lawn_grass(test_grass):
    """
    Тест вывода отладочной информации в консоль
    :param test_grass:
    """

    assert repr(test_grass) == test_grass.__repr__()


# Тестируем класс Smartphone
@pytest.fixture
def test_smartphone():
    """
    Тестовые данные для класса Smartphone
    :return: Обьект класса
    """

    smart = Smartphone('Samsung', 'Samsung Galaxy S20', 'зеленый', 100000.0, 1, 10, 'Samsung Galaxy S20', 128)
    return smart


def test_init_smartphone(test_smartphone):
    """
    Тест инициализации класса Smartphone
    :param test_smartphone:
    """

    assert test_smartphone.name == 'Samsung'
    assert test_smartphone.color == 'зеленый'
    assert test_smartphone.price == 100000.0
    assert test_smartphone.quantity == 1
    assert test_smartphone.performance == 10
    assert test_smartphone.model == 'Samsung Galaxy S20'
    assert test_smartphone.amount_memory == 128


def teat_create_smartphone(test_smartphone):
    """
    Тест создания продукта класса Smartphone
    :param test_smartphone:
    :return:
    """
    lst = [{"name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5}]

    new_smartphone = Smartphone.create_product(lst, **test_smartphone)
    assert (new_smartphone.name == 'Samsung Galaxy C23 Ultra', new_smartphone.color == 'зеленый',
            new_smartphone.price == 180000.0, new_smartphone.quantity == 5, new_smartphone.performance == 10,
            new_smartphone.model == 'Samsung Galaxy S20')


def test_str_smartphone(test_smartphone):
    """
    Тест вывода строковой информации в консоль
    :param test_smartphone:
    """

    assert str(test_smartphone) == test_smartphone.__str__()


def test_repr_smartphone(test_smartphone):
    """
    Тест вывода отладочной информации в консоль
    :param test_smartphone:
    """

    assert repr(test_smartphone) == test_smartphone.__repr__()
