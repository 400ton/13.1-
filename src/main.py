from colorama import *
from func import load_file
from src.class_category import Category
from src.class_product import Product


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
