from colorama import *
from class_product import Product


class Category:
    '''
    Класс для категорий
    '''

    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, goods: list):
        self.name = name
        self.description = description
        self.__goods = goods

        Category.total_categories += 1
        Category.total_products += len(self.__goods)

    @property
    def goods(self):
        '''
        Функция вывода списка товаров в определенном формате
        '''
        return '\n'.join(f"{Fore.CYAN}{product.name}{Fore.RESET}, "
                         f"{Fore.GREEN}Цена{Fore.RESET} {product.price}{Fore.GREEN} руб. "
                         f"{Fore.GREEN}Остаток:{Fore.RESET} {product.price} {Fore.GREEN}шт"
                         for product in self.__goods)

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

