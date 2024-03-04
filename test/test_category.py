import pytest
from colorama import *
from src.class_category import Category
from src.class_product import Product
from src.class_lawn_grass import LawnGrass
from src.class_smartpfone import Smartphone


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
    category = Category(test_data["name"], test_data["description"], test_data["products"])
    assert category.name == "Category 1"
    assert category.description == "Description 1"
    assert category.total_categories == 1
    assert category.total_products == 3


def test_len(test_data):
    category = Category(test_data["name"], test_data["description"], test_data["products"])
    assert len(category) == 3


def test_str(test_data):
    category = Category(test_data["name"], test_data["description"], test_data["products"])
    assert str(category) == f'{Fore.CYAN}Category 1 {Fore.RESET},' \
                            f'{Fore.GREEN}Всего продуктов:{Fore.RESET}3 {Fore.GREEN}шт'


def test_goods(test_data):
    category = Category(test_data["name"], test_data["description"], test_data["products"])
    assert category.goods == test_data["products"]


def test_add_goods(test_data):
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
    category = Category(test_data["name"], test_data["description"], test_data["products"])
    assert repr(category) == f'Category, Category 1, Description 1, {test_data["products"]}'


# Тестируем класс Lawn_Grass

def test_init_lawn_grass(test_data):
    lg = LawnGrass('Трава', 'Трава зеленая', 'зеленый', 10000, 1, 'ru', 10)
    assert lg.name == 'Трава'
    assert lg.description == 'Трава зеленая'
    assert lg.color == 'зеленый'
    assert lg.price == 10000
    assert lg.quantity == 1
    assert lg.manufacturer == 'ru'
    assert lg.germination_period == 10


# Тестируем класс Smartphone

def test_init_smartphone(test_data):
    sm = Smartphone('Samsung', 'Samsung Galaxy S20', 'зеленый', 100000.0, 1, 10, 'Samsung Galaxy S20', 128)
    assert sm.name == 'Samsung'
    assert sm.color == 'зеленый'
    assert sm.price == 100000.0
    assert sm.quantity == 1
    assert sm.performance == 10
    assert sm.model == 'Samsung Galaxy S20'
    assert sm.amount_memory == 128
