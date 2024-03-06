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
    """Класс для расширения функциональности основных классов"""
    def __init__(self, *args, **kwargs):
        print(repr(self))

    def __repr__(self):
        for key in self.__dict__:
            return f'Создан обьект: {self.__class__.__name__} ({key} = {self.__dict__[key]})'

