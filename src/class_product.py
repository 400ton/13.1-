
class Product:
    '''
    Класс для продуктов
    '''
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f'{self.name}, {self.description}, {self.price}, {self.quantity}'

