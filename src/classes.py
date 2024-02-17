
class Category:
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


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity





