from abc import ABC, abstractmethod


class Abstract(ABC):
    """Шаблон для создания классов"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class MixinRepr:
    """
    Класс для расширения функциональности основных классов.
    Выводит отладочную информацию о классе для разработчика.
    """
    def __init__(self, *args, **kwargs):
        print(repr(self))

    def __repr__(self):
        return f'\nСоздан класс: {self.__class__.__name__} с атрибутами {self.__dict__}'

