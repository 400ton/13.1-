from src.class_abstract_and_mixin import MixinRepr


class Order(MixinRepr):
    """
    Класс заказа для продуктов
    """
    order_counter = 0

    def __init__(self, name: str, quantity: int, price: float):
        """
        Конструктор класса
        :param name:
        :param quantity:
        :param price:
        """
        self._name = name
        self.quantity = quantity
        self._price = price
        super().__init__()
        Order.order_counter += 1

    @property
    def name(self):
        """
        Возвращает имя продукта
        :return: str
        """
        if ',' in self._name:
            raise ValueError('В заказе может быть указан только один товар')
        return self._name

    @property
    def price(self):
        """
        Возвращает цену продукта
        :return: float
        """
        if self._price <= 0:
            raise ValueError('Цена не может быть < или = 0')
        return self._price * self.quantity

    def __str__(self):
        """
        Возвращает информацию о заказе
        :return: string
        """
        return (f'\nВсего заказов: {Order.order_counter}\nИмя продукта: {self.name},\nКоличество: {self.quantity},\n'
                f'Цена: {self.price},\n')

    def __repr__(self):
        """
        Возвращает отладочную информацию о заказе
        :return: string
        """
        return super().__repr__()

