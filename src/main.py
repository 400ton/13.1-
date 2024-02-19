from func import load_file
from src.classes import Category, Product


def main():
    '''
    Основная функция
    '''
    data = load_file('../data/products.json')

    for unit in data:
        category = Category(unit['name'], unit['description'], unit['products'])
        print(f'Имя категории: {category.name}')
        print(f'Описание категории: {category.description}')
        print(f'Список товаров:\n')

        for product in category.goods:
            element = Product(product['name'], product['description'], product['price'], product['quantity'])
            print(f'{element.name}\nОписание:{element.description}\nЦена: {element.price} руб\nКоличество: {element.quantity} шт\n')

    print(f'Всего категорий: {Category.total_categories}')
    print(f'Всего товаров: {sum(Category.total_products)}')


if __name__ == '__main__':
    main()
