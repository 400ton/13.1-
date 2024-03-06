from src.class_product import Product


class Smartphone(Product):
    """
    Класс категории Smartphone, наследник класса Product
    """

    def __init__(self, name, description, color, price, quantity, performance: float, model: str, amount_memory: int):
        """
        Конструктор класса
        :param name:
        :param description:
        :param color:
        :param price:
        :param quantity:
        :param performance:
        :param model:
        :param amount_memory:
        """
        self.performance = performance
        self.model = model
        self.amount_memory = amount_memory
        super().__init__(name, description, color, price, quantity)

    def __str__(self):
        """
        Функция вывода строковой информации в консоль
        :return: string
        """
        return (f'\nИмя продукта: {self.name},\nОписание: {self.description},\n'
                f'Цвет: {self.color},\nЦена: {self.price},\nКоличество: {self.quantity},\n'
                f'Производительность: {self.performance}\nМодель: {self.model},\nОбьем памяти: {self.amount_memory}\n')

    def __repr__(self):
        """
        Функция вывода отладочной информации о классе
        :return: string
        """
        return super().__repr__()
