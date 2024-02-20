
class Category:
    '''
    Класс для категорий
    '''

    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, goods: list):
        self.name = name
        self.description = description
        self.goods = goods

        Category.total_categories += 1
        Category.total_products += len(goods)

    def __repr__(self):
        return f'{self.name}, {self.description}, {self.goods}'






