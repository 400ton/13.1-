from src.class_product import Product


class LawnGrass(Product):
    """Класс категории Smartphone, наследник класса Product"""

    def __init__(self, name, description, color, price, quantity, manufacturer: str, germination_period: int):
        super().__init__(name, description, color, price, quantity)
        self.manufacturer = manufacturer
        self.germination_period = germination_period

    def __str__(self):
        pass 

    def __repr__(self) :
        pass
