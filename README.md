# Tinkoff образование: генерация текста, задача для прохождения вступительных испытаний

Утилита, которая на основе данного пользователем текста генерирует новый.
Используется только чистый python и встроенные библиотеки.

## Репозиторий содержит 4 файла и 2 папки 
1. model.py - основный скрипт, в котором описана вся логика модел:
fit и generate, загрузка и сохранение.
2. learning.py - скрипт, который запускает обучение модели.
3. generation.py - скрипт, который генерирует новый текст.
4. tokenizer.py - дополнительный скрипт для токенизации текста.
5. data - папка для данных для обучения. В которой хранится train.txt - "Война и Мир",
текст, на котором можно провести обучение модели.
6. models - папка для сохранения натренированных моделей.

## Обучение
Файл learning.py, имеет 3 аргумента:
1. *input_path* - местоположение файла с данными в формате .txt или папки, в которой данные хранятся.
2. *--folder_to_save_model* - в какую папку сохранить модель. По умолчанию ''.
3. *--name_to_save_model* - как назвать сохраненную модель. По умолчанию 'model'.

## Генерация
Файл generation.py, имеет 5 аргументов:
1. *file* - местоположение файла с натренированной моделью.
2. *--length* - длинна генерируемой строки. По умолчанию - 10.
3. *--is_rand* - является ли результат полностью случайным или выбор будет осущесвляться из самых
частотных слов. По умолчанию - false.
4. *--num_of_word_to_choose* - если is_rand равен false, то выбор следующего слова в последовательности осуществляется 
из рандомного слова из num_of_word_to_choose самых частотных слов после предыдущего члена последовательности. 
По умолчанию - 5.
5. *--seed* - сид. По умолчанию - 1.




