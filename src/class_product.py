from colorama import *
from src.class_abstract_and_mixin import Abstract, MixinRepr


class Product(MixinRepr, Abstract):
    """
    Класс для продуктов
    """

    def __init__(self, name: str, description: str, color: str, price: float, quantity: int):
        """
        Конструктор класса
        :param name:
        :param description:
        :param color:
        :param price:
        :param quantity:
        """
        self.name = name
        self.description = description
        self.color = color
        self._price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        """
        Функция вывода строковой информации о продукте
        :return: string
        """
        return f"{Fore.CYAN}{self.name}{Fore.RESET}, " \
               f"{self._price} {Fore.GREEN}руб. " \
               f"Остаток:{Fore.RESET} {self.quantity} {Fore.GREEN}шт{Fore.RESET}"

    def __add__(self, other):
        """
        Функция сложения обьектов одного класса
        :param other:
        :return: float
        """
        if type(other) is not type(self):
            raise TypeError('Невозможно добавить товары разных типов')
        result = (self._price * self.quantity) + (other.price * other.quantity)
        return result

    @classmethod
    def create_product(cls, products, **kwargs, ):
        """
        Функция создания нового продукта
        :param products:
        :param kwargs:
        :return: dictionary
        """
        name = kwargs.get('name')
        description = kwargs.get('description')
        color = kwargs.get('color')
        price = kwargs.get('price')
        quantity = kwargs.get('quantity')

        if products is None:
            raise ValueError('Список продуктов не может быть пустым')

        for value in products:
            if value['name'] != name:
                value['color'] = color
                value['description'] = description
                if value['price'] <= price:
                    value['price'] = price
                    value['quantity'] += quantity
                    return cls(name=value['name'], description=value['description'], color=value['color'],
                               price=value['price'], quantity=value['quantity'])
            else:
                return cls(**value)

    @property
    def price(self):
        """
        Функция возвращения цены продукта
        :return: float
        """
        return self._price

    @price.setter
    def price(self, value: float):
        """
        Функция проверки и понижение цены продукта"
        :param value:
        :return: float
        """
        if value <= 0:
            print(Fore.RED + f'\nНедопустимое значение цены{Fore.RESET}{Fore.GREEN}\n')
        elif value < self._price:
            confirm = input("Вы действительно хотите понизить цену? (y/n): ").lower()
            if confirm == "y":
                self._price = value
            else:
                print(Fore.RED + "Понижение цены отменено." + Fore.RESET)
        else:
            self._price = value

    def __repr__(self):
        """
        Функция вывода отладочной информации о продукте
        :return: string
        """
        return super().__repr__()
