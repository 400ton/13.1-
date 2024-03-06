from src.class_product import Product


class Smartphone(Product):
    """Класс категории Smartphone, наследник класса Product"""

    def __init__(self, name, description, color, price, quantity, performance: float, model: str, amount_memory: int):
        self.performance = performance
        self.model = model
        self.amount_memory = amount_memory
        super().__init__(name, description, color, price, quantity)

    def __str__(self):
        return (f'\nИмя продукта: {self.name},\nОписание: {self.description},\n'
                f'Цвет: {self.color},\nЦена: {self.price},\nКоличество: {self.quantity},\n'
                f'Производительность: {self.performance}\nМодель: {self.model},\nОбьем памяти: {self.amount_memory}\n')

    def __repr__(self):
        return (f'Создан класс: {self.__class__.__name__} с атрибутами (name: {self.name}, '
                f'description: {self.description}, color: {self.color}, price: {self.price}, '
                f'quantity: {self.quantity}, performance: {self.performance}, '
                f'model: {self.model}, amount memory: {self.amount_memory})\n')
