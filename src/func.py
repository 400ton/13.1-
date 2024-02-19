import json
import os

def load_file(filename) -> list:
    '''
    Функция загрузки информации из файла
    '''
    file_path = os.path.join(filename)
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

