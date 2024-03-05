from colorama import *
from func import load_file
from src.class_category import Category
from src.class_product import Product
from src.class_smartpfone import Smartphone
from src.class_lawn_grass import LawnGrass

pr = Product('Nokia', 'клевый', 'черный', 10000, 1)
pr_2 = Product('Siemens', 'клевый', 'черный', 20000, 1)

sm = Smartphone('Nokia', 'клевый', 'черный', 10000, 1, 2.2, 'Nokia', 128)
sm_2 = Smartphone('Siemens', 'клевый', 'черный', 20000, 1,2.5, 'Siemens', 128)
lg = LawnGrass('Grass', 'green', 'green', 5000, 1, 'russian', 2)
lst = {"name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5}

print(pr)
print(pr_2)

print(sm)
print(sm_2)

print(lg)



# def main():
#     '''
#     Основная функция
#     '''
#     data = load_file('../data/products.json')
#     for unit in data:
#         category = Category(unit['name'], unit['description'], unit['products'])
#         print(Fore.GREEN + f'Имя категории: {Fore.RESET}{category.name}')
#         print(Fore.GREEN + f'Описание категории: {Fore.RESET}{category.description}')
#         print(Fore.GREEN + f'Список товаров: {Fore.RESET}')
#         print(category.goods)
#
#
#         user = input('Хотите добавить новый товар в категорию? Да/Нет ').lower()
#
#         if user != 'да':
#             print(Fore.GREEN + f'Всего категорий:{Fore.RESET} {Category.total_categories}')
#             print(Fore.GREEN + f'Всего товаров:{Fore.RESET} {Category.total_products}\n')
#             continue
#         else:
#             product_name = input('Введите название товара: ')
#             product_description = input('Введите описание товара: ')
#             try:
#                 product_price = float(input('Введите цену товара: '))
#             except ValueError:
#                 print('Цена должна быть числом\n')
#                 continue
#             try:
#                 product_count = int(input('Введите количество товара: '))
#             except ValueError:
#                 print('Количество должно быть числом\n')
#                 continue
#             product = Product(product_name, product_description, product_price, product_count)
#             get_product = Product.create_product(product_name, product_description, product_price, product_count,
#                                                  category.goods)
#
#             product.price = product_price
#             category.goods = get_product
#
#             print(f'\nСписок товаров: \n{category.goods}\n')
#             print(Fore.GREEN + f'Товар добавлен в категорию:{Fore.RESET} {category.name}\n')
#         print(Fore.GREEN + f'Всего категорий:{Fore.RESET} {Category.total_categories}')
#         print(Fore.GREEN + f'Всего товаров:{Fore.RESET} {Category.total_products}\n')
#
#
# if __name__ == '__main__':
#     main()
