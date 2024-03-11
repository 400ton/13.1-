from colorama import *
from exception.custom_exceptions import QuantityError
from src.class_product import Product
from src.class_abstract_and_mixin import MixinRepr


class Category(MixinRepr):
    """
    Класс категорий для списка продуктов
    """

    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, goods: list):
        """
        Конструктор класса
        :param name:
        :param description:
        :param goods:
        """
        self.name = name
        self.description = description
        self.__goods = goods
        super().__init__()

        Category.total_categories += 1
        Category.total_products += len(self.__goods)

    def __len__(self):
        """
        Функция возвращает количество продуктов в категории
        :return: длину списка
        """
        return len(self.__goods)

    def __str__(self):
        """
        Функция вывода информации о категории
        :return: string
        """
        return f'{Fore.CYAN}{self.name} {Fore.RESET},' \
               f'{Fore.GREEN}Всего продуктов:{Fore.RESET}{len(self.__goods)} {Fore.GREEN}шт'

    @property
    def goods(self):
        """Функция геттера для списка продуктов
        :return: list of products
        """
        return self.__goods

    @goods.setter
    def goods(self, product):
        """Функция добавления продукта в список,
        продукт должен быть обьектом класса Product.
        :param product:
        :return: list of products
        """
        if not isinstance(product, Product):
            raise ValueError('The product must be an object of class Product')

        try:
            if product.quantity <= 0:
                raise QuantityError
        except QuantityError:
            print(Fore.RED + 'Product quantity cannot be zero or negative' + Fore.RESET)

        else:
            self.__goods.append(product)
            Category.total_products += 1
            print(Fore.GREEN + '\nТовар добавлен' + Fore.RESET)
        finally:
            print(Fore.GREEN + '*Oбработка добавления товара завершена' + Fore.RESET)

    @property
    def average_price_goods(self):
        """
        Функция возвращает среднюю цену всех продуктов в категории
        :return: float
        """

        try:
            total_price = sum(product.price * product.quantity for product in self.__goods)
            total_products = len(self.__goods)
            return round(total_price / total_products, 1)
        except ZeroDivisionError:
            return 0

    def __repr__(self):
        """
        Функция вывода отладочной информации о классе
        :return: string
        """
        return super().__repr__()
