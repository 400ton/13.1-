import pytest
from colorama import Fore
from src.class_category import Category

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

    category = Category(test_data["name"], test_data["description"], test_data["products"])
    assert category.name == "Category 1"
    assert category.description == "Description 1"
    assert category.total_categories == 1
    assert category.total_products == 3


# def test_goods(test_data):
#     category = Category(test_data['name'], test_data['description'], test_data['products'])
#     expected_result = '\n'.join((f'{Fore.CYAN}Product 1{Fore.RESET}, {Fore.GREEN}Цена{Fore.RESET} 100000.0{Fore.GREEN} руб. {Fore.GREEN}Остаток:{Fore.RESET} 1 {Fore.GREEN}шт,\n '
#                        f'{Fore.CYAN}Product 2{Fore.RESET}, {Fore.GREEN}Цена{Fore.RESET} 200000.0{Fore.GREEN} руб. {Fore.GREEN}Остаток:{Fore.RESET} 2 {Fore.GREEN}шт,\n '
#                        f'{Fore.CYAN}Product 3{Fore.RESET}, {Fore.GREEN}Цена{Fore.RESET} 300000.0{Fore.GREEN} руб. {Fore.GREEN}Остаток:{Fore.RESET} 3 {Fore.GREEN}шт,'))
#     assert category.goods == expected_result

def test_repr_category(test_data):
    '''тестирование функции __repr__'''
    category = Category(test_data["name"], test_data["description"], test_data["products"])
    assert repr(category.description) == "'Description 1'"
    assert repr(category.name) == "'Category 1'"

