from colorama import *


class Product:
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
        result = (self._price * self.quantity) + (other.price * other.quantity)
        if not isinstance(other, type(self)):
            raise TypeError("Cannot add products of different types")
        return result

    @classmethod
    def create_product(cls, name: str, description: str, price: float, quantity: int, products: list):
        """
        Функция создания нового продукта
        """
        for value in products:
            if value['name'] == name:
                value['description'] = description
                if value['price'] <= price:
                    value['price'] = price
                    value['quantity'] += quantity
                    return cls(name=value['name'], description=value['description'], color=value[''],
                               price=value['price'], quantity=value['quantity'])
                else:
                    return cls(name=value['name'], description=value['description'], color=value[''],
                               price=value['price'], quantity=value['quantity'])

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
        return (f'{Fore.RED}Имя класса: {self.__class__.__name__},\n'
                f'Имя продукта, заданного при инициализации класса: {self.name},\n'
                f'Описание продукта: {self.description},\n'
                f'Цена: {self._price},\n'
                f'Количество:{self.quantity}{Fore.RESET}\n\n')
