import re
import os
import sys


def check_path(path):
    """Выводит ошибку если файл не существует"""

    if not os.path.exists(path):
        sys.exit(f'{path} не существует')


def extract_tokens_from_file(path):
    """Извлекает токены файла"""

    if not path.endswith('.txt'):
        return []

    output = []

    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            for word in re.findall(u'[а-я]+', line.lower()):
                output.append(word)

    return output


def get_tokens(input_path):
    """Возвращает токены из файла или группы файлов"""

    check_path(input_path)
    output = []

    if os.path.isfile(input_path):
        output = extract_tokens_from_file(input_path)
    else:
        for local_path in os.listdir(input_path):
            output += extract_tokens_from_file(os.path.join(input_path, local_path))

    if len(output) < 2:
        sys.exit('Слишком маленький датасет')

    return output
