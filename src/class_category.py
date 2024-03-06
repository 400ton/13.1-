from colorama import *
from src.class_product import Product
from src.class_abstract_and_mixin import MixinRepr


class Category(MixinRepr):
    """Класс категории для списка продуктов"""

    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, goods: list):
        self.name = name
        self.description = description
        self.__goods = goods
        super().__init__()

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
        """Функция добавления продукта в категорию
        :param объект класса:
        """
        if isinstance(product, Product):
            self.__goods.append(product)
            Category.total_products += 1
        else:
            raise ValueError("Продукт должен быть объектом класса Product")

    def __repr__(self):
        return (f'Создан класс: {self.__class__.__name__} с атрибутами (name: {self.name}, '
                f'description: {self.description}, goods: {self.__goods}\n')
