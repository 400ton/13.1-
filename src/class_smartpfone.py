from src.class_product import Product


class Smartphone(Product):
    """Класс категории Smartphone, наследник класса Product"""

    def __init__(self, name, description, color, price, quantity, performance: float, model: str, amount_memory: int):
        super().__init__(name, description, color, price, quantity)
        self.performance = performance
        self.model = model
        self.amount_memory = amount_memory

    def __str__(self):
        return (f'\nИмя продукта: {self.name},\nОписание: {self.description},\n'
                f'Цвет: {self.color},\nЦена: {self.price},\nКоличество: {self.quantity},\n'
                f'Производительность: {self.performance}\nМодель: {self.model},\nОбьем памяти: {self.amount_memory}\n')

    def __repr__(self):
        return (f'Class name: {self.__class__.__name__}, Name: {self.name}, Description: {self.description}, '
                f'Color: {self.color}, Price: {self.price}, Quantity: {self.quantity}, Performance: {self.performance}'
                f'Model: {self.model}, Amount memory: {self.amount_memory}')
