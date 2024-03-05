from src.class_product import Product


class LawnGrass(Product):
    """Класс категории LawnGrass, наследник класса Product"""

    def __init__(self, name, description, color, price, quantity, manufacturer: str, germination_period: int):
        super().__init__(name, description, color, price, quantity)
        self.manufacturer = manufacturer
        self.germination_period = germination_period

    def __str__(self):
        return (f'Имя продукта: {self.name},\nОписание: {self.description},\n'
                f'Цвет: {self.color},\nЦена: {self.price} руб,\nКоличество: {self.quantity} шт,\n'
                f'Производитель: {self.manufacturer}\nПериод произрастания: {self.germination_period} дней')

    def __repr__(self):
        return (f'Class name: {self.__class__.__name__}, Name: {self.name}, Description: {self.description}, '
                f'Color: {self.color}, Price: {self.price}, Quantity: {self.quantity}, '
                f'Manufacturer: {self.manufacturer}, Germination period: {self.germination_period}')
