from abc import ABC, abstractmethod


class Abstract(ABC):
    """Шаблон для создания классов"""

    @abstractmethod
    def __init__(self, *args, **kwargs):
        """
        Конструктор класса
        """
        pass

    @abstractmethod
    def create_product(self, *args, **kwargs):
        """
        Создание продукта
        :param args:
        :param kwargs:
        :return:
        """
        pass

    @abstractmethod
    def __str__(self):
        """
        Выводит информацию о продукте
        :return: string
        """
        pass

    @abstractmethod
    def __repr__(self):
        """
        Возвращает отладочную информацию о продукте
        :return: string
        """
        pass


class MixinRepr:
    """
    Класс для расширения функциональности основных классов.
    Выводит отладочную информацию о классе для разработчика.
    """
    def __init__(self, *args, **kwargs):
        print(repr(self))

    def __repr__(self):
        return f'\nСоздан класс: {self.__class__.__name__} с атрибутами {self.__dict__}\n'

