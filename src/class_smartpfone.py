from src.class_product import Product


class Smartphone(Product):
    """Класс категории Smartphone, наследник класса Product"""
    def __init__(self, name, description, color, price, quantity, performance: float, model: str, amount_memory: int,):
        super().__init__(name, description, color, price, quantity)
        self.performance = performance
        self.model = model
        self.amount_memory = amount_memory

    def __str__(self):
        pass

    def __repr__(self):
        pass
