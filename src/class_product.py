from colorama import *
class Product:
    '''
    Класс для продуктов
    '''

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @classmethod
    def create_product(cls, name: str, description: str, price: float, quantity: int, products: list):
        '''Функция создания нового продукта'''
        for value in products:
            if value['name'] == name:
                if value['price'] <= price:
                    value['price'] = price
                value['quantity'] += quantity
                return value
        else:
            return dict(name=name, description=description, price=price, quantity=quantity)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        '''Функция изменения цены продукта'''
        if value <= 0:
            print(Fore.RED + f'\nНедопустимое значение цены{Fore.RESET}{Fore.GREEN}\n')
        elif value < self._price:
            confirm = input("Вы действительно хотите понизить цену? (y/n): ").lower()
            if confirm == "y":
                self._price = value
            else:
                print("Понижение цены отменено.")
        else:
            self._price = value

    def __repr__(self):
        return f'{self.name}, {self.description}, {self._price}, {self.quantity}'


