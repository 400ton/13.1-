import pytest
from colorama import *
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
    assert str(category) == f'{Fore.CYAN}Category 1 {Fore.RESET},'\
                            f'{Fore.GREEN}Всего продуктов:{Fore.RESET}3 {Fore.GREEN}шт'


def test_goods(test_data):
    category = Category(test_data["name"], test_data["description"], test_data["products"])
    assert category.goods == test_data["products"]


def test_add_goods(test_data):
    category = Category(test_data["name"], test_data["description"], test_data["products"])
    new_product = Product('Product 4', 'Description 1', 100000.0,  4)
    assert category.goods == test_data["products"]
    category.goods = new_product
    assert category.goods == test_data["products"]

    new_product_2 = ('Product 5', 'Description 1', 200000.)
    with pytest.raises(ValueError) as excinfo:
        category.goods = new_product_2
    assert str(excinfo.value) == "Продукт должен быть объектом класса Product"


def test_repr(test_data):
    category = Category(test_data["name"], test_data["description"], test_data["products"])
    assert repr(category) == f'{Fore.RED}Имя класса: Category,\nНазвание категории, заданной при инициализации класса: Category 1,\n\
Описание категории: Description 1,\n\
Список продуктов: {test_data["products"]}{Fore.RESET}'

