from src.class_category import Category


class Iterator:
    """
    Класс, который принимает на вход категорию и дает возможность использовать цикл
    for для прохода по всем товарам данной категории
    """

    def __init__(self, category: Category):
        self.category = category

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.category.goods):
            return self.category.goods[self.index]
        else:
            raise StopIteration
