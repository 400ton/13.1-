
class Category:
    '''
    Класс для категорий
    '''

    name: str
    description: str
    goods: list

    total_categories = 0
    total_products = []

    def __init__(self, name: str, description: str, goods: list):
        self.name = name
        self.description = description
        self.goods = goods

        Category.total_categories += 1
        Category.total_products.append(len(goods))

    def __repr__(self):
        return f'{self.name}, {self.description}, {self.goods}'


class Product:
    '''
    Класс для продуктов
    '''
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f'{self.name}, {self.description}, {self.price}, {self.quantity})'





