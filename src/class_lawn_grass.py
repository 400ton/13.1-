from src.class_product import Product


class LawnGrass(Product):
    """
    Класс категории LawnGrass, наследник класса Product
    """

    def __init__(self, name, description, color, price, quantity, manufacturer: str, germination_period: int):
        """
        Конструктор класса
        :param name:
        :param description:
        :param color:
        :param price:
        :param quantity:
        :param manufacturer:
        :param germination_period:
        """
        self.manufacturer = manufacturer
        self.germination_period = germination_period
        super().__init__(name, description, color, price, quantity)

    def __str__(self):
        """
        Функция вывода строковой информации в консоль
        :return: string
        """
        return (f'Имя продукта: {self.name},\nОписание: {self.description},\n'
                f'Цвет: {self.color},\nЦена: {self.price} руб,\nКоличество: {self.quantity} шт,\n'
                f'Производитель: {self.manufacturer}\nПериод произрастания: {self.germination_period} дней')

    def __repr__(self):
        """
        Выводит отладочную информацию о классе
        :return: string
        """
        return super().__repr__()
