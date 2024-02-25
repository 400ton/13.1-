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
        print(Fore.GREEN + f'Список товаров: {Fore.RESET}')
        print(f'{category.goods}\n')

        user = input('Хотите добавить новый товар в категорию? Да/Нет ').lower()

        if user != 'да':
            continue
        else:
            product_name = input('Введите название товара: ')
            product_description = input('Введите описание товара: ')
            try:
                product_price = float(input('Введите цену товара: '))
            except ValueError:
                print('Цена должна быть числом')
                continue
            try:
                product_count = int(input('Введите количество товара: '))
            except ValueError:
                print('Количество должно быть числом')
                continue

            get_product = Product.create_product(product_name, product_description, product_price, product_count,
                                                 category.goods)
            print(get_product)
            category.goods = get_product

            print(f'Список товаров: \n{category.goods}\n')
            print(Fore.GREEN + f'Товар добавлен в категорию:{Fore.RESET} {category.name}')
            print(Fore.GREEN + f'Всего товаров:{Fore.RESET} {len(category.goods)}\n')




if __name__ == '__main__':
    main()
