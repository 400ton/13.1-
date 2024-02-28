from colorama import *
from src.class_product import Product


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
        return f'{Fore.CYAN}{self.name} {Fore.RESET},' \
               f'{Fore.GREEN}Всего продуктов:{Fore.RESET}{len(self)} {Fore.GREEN}шт'

    @property
    def goods(self):
        return self.__goods

    @goods.setter
    def goods(self, product):
        '''
        Функция добавления продукта в категорию
        :param объект класса Product:
        '''
        if isinstance(product, Product):
            self.__goods.append(product)
            Category.total_products += 1
        else:
            raise ValueError("Продукт должен быть объектом класса Product")

    def __repr__(self):
        return (f'{Fore.RED}Имя класса: {self.__class__.__name__},\n'
                f'Название категории, заданной при инициализации класса: {self.name},\n'
                f'Описание категории: {self.description},\n'
                f'Список продуктов: {self.__goods}{Fore.RESET}')

