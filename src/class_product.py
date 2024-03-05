from colorama import *
from src.class_abstract_mixin import Abstract, MixinRepr


class Product(MixinRepr, Abstract):
    """Класс для продуктов"""

    def __init__(self, name: str, description: str, color: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.color = color
        self._price = price
        self.quantity = quantity

    def __str__(self):
        return f"{Fore.CYAN}{self.name}{Fore.RESET}, " \
               f"{self._price} {Fore.GREEN}руб. " \
               f"Остаток:{Fore.RESET} {self.quantity} {Fore.GREEN}шт"


    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError('Невозможно добавить товары разных типов')
        result = (self._price * self.quantity) + (other.price * other.quantity)
        return result

    @classmethod
    def create_product(cls, name: str, description: str, color: str, price: float, quantity: int, products: list):
        """Функция создания нового продукта"""
        for value in products:
            if value['name'] == name:
                value['color'] = color
                value['description'] = description
                if value['price'] <= price:
                    value['price'] = price
                    value['quantity'] += quantity
                    return cls(name=value['name'], description=value['description'], color=value['color'],
                               price=value['price'], quantity=value['quantity'])
            else:
                return cls(name=name, description=description, color=color, price=price, quantity=quantity)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        """Функция проверки и понижение цены продукта"""
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
        return (f'Class name: {self.__class__.__name__}, Name: {self.name}, Description: {self.description}, '
                f'Color: {self.color}, Price: {self.price}, Quantity: {self.quantity}')
