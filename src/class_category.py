from colorama import *
from class_product import Product


class Category:
    '''
    Класс категории для списка продуктов
    '''

    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, goods: list):
        self.name = name
        self.description = description
        self.__goods = goods

        Category.total_categories += 1
        Category.total_products += len(self.__goods)

    def __len__(self):
        return len(self.__goods)

    def __str__(self):
        return '\n'.join(f'{Fore.CYAN}{self.name} {Fore.RESET},'
                         f'{Fore.GREEN}Всего продуктов:{Fore.RESET}{self.__len__} {Fore.GREEN}шт')

    @property
    def goods(self):
        return self.__goods

    @goods.setter
    def goods(self, product):
        '''
        Функция добавления товара в категорию
        '''
        get_product = Product(name=product['name'], description=product['description'], price=product['price'],
                              quantity=product['quantity'])
        self.__goods.append(get_product)
        Category.total_products += 1

    def __repr__(self):
        return f'{self.name}, {self.description}, {self.__goods}'

