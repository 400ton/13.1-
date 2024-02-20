from colorama import *
from func import load_file
from src.class_category import Category
from src.class_product import Product

def main():
    '''
    Основная функция
    '''
    data = load_file('../data/products.json')

    for unit in data:
        category = Category(unit['name'], unit['description'], unit['products'])
        print(Fore.GREEN + f'Имя категории: {Fore.RESET}{category.name}')
        print(Fore.GREEN + f'Описание категории: {Fore.RESET}{category.description}')
        print(Fore.GREEN + f'Список товаров: {Fore.RESET}\n')

        for product in category.goods:
            element = Product(product['name'], product['description'], product['price'], product['quantity'])
            print(Fore.CYAN + f'{element.name}')
            print(Fore.GREEN + f'Описание: {Fore.RESET}{element.description}')
            print(Fore.GREEN + f'Цена: {Fore.RESET}{element.price} руб')
            print(Fore.GREEN + f'Количество: {Fore.RESET}{element.quantity} шт\n')

    print(Fore.GREEN + f'Всего категорий:{Fore.RESET} {Category.total_categories}')
    print(Fore.GREEN+ f'Всего товаров:{Fore.RESET} {Category.total_products}')


if __name__ == '__main__':
    main()
