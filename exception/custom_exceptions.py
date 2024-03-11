class QuantityError(Exception):
    """
    Пользовательский класс исключений
    """

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Number of products 0'

    def __str__(self):
        return self.message
