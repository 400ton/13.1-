from src.class_product import Product


class LawnGrass(Product):
    """Класс категории LawnGrass, наследник класса Product"""

    def __init__(self, name, description, color, price, quantity, manufacturer: str, germination_period: int):
        self.manufacturer = manufacturer
        self.germination_period = germination_period
        super().__init__(name, description, color, price, quantity)

    def __str__(self):
        return (f'Имя продукта: {self.name},\nОписание: {self.description},\n'
                f'Цвет: {self.color},\nЦена: {self.price} руб,\nКоличество: {self.quantity} шт,\n'
                f'Производитель: {self.manufacturer}\nПериод произрастания: {self.germination_period} дней')

    def __repr__(self):
        return super().__repr__()
