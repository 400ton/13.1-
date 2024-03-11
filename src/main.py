from colorama import *
from func import load_file
from src.class_category import Category
from src.class_product import Product
from src.class_smartpfone import Smartphone
from src.class_lawn_grass import LawnGrass


def main():
    lst = {"name": "Nokia",
           "description": "клевый",
           "color": "черный",
           "price": 100,
           "quantity": 1}

    product = Product('Nokia', 'клевый', 'черный', 10000, 1)
    product_2 = Product('Siemens', 'клевый', 'черный', 20000, 1)

    lst_2 = [product, product_2]
    #
    # smartphone = Smartphone('Nokia', 'клевый', 'черный', 10000, 1, 2.2, 'Nokia', 128)
    # smartphone_2 = Smartphone('Siemens', 'клевый', 'черный', 20000, 1, 2.5, 'Siemens', 128)
    # lawn_grass = LawnGrass('Grass', 'green', 'green', 5000, 1, 'russian', 2)
    # category = Category('Смартфоны', 'Смартфоны, как средство не только коммуникации, '
    #                                  'но и получение дополнительных функций для удобства жизни', [])
    print(product.create_product(lst_2, **lst))
    # print(Fore.RED + f'{category.average_price_goods}' + Fore.RESET)


if __name__ == '__main__':
    main()
