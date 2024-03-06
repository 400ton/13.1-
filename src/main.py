from colorama import *
from func import load_file
from src.class_category import Category
from src.class_product import Product
from src.class_smartpfone import Smartphone
from src.class_lawn_grass import LawnGrass


def main():
    product = Product('Nokia', 'клевый', 'черный', 10000, 1)
    product_2 = Product('Siemens', 'клевый', 'черный', 20000, 1)

    smartphone = Smartphone('Nokia', 'клевый', 'черный', 10000, 1, 2.2, 'Nokia', 128)
    smartphone_2 = Smartphone('Siemens', 'клевый', 'черный', 20000, 1, 2.5, 'Siemens', 128)

    lawn_grass = LawnGrass('Grass', 'green', 'green', 5000, 1, 'russian', 2)
    lst = {"name": "Samsung Galaxy C23 Ultra",
           "description": "256GB, Серый цвет, 200MP камера",
           "price": 180000.0,
           "quantity": 5}

    print(product + product_2)
    print(product + smartphone)
    # print(smartphone + lawn_grass)


if __name__ == '__main__':
    main()
