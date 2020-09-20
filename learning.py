import argparse
import tokenizer
import model

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Обучение модели TextGen')
    parser.add_argument('input_path', type=str, help=('Расположение файла для обучения в формате .txt '
                                                      'или расположение папки с файлами для обучения в '
                                                      'формате .txt'))
    parser.add_argument('--folder_to_save_model', '-f', type=str, default='models', help='Папка для сохранения модели')
    parser.add_argument('--name_to_save_model', '-n', type=str, default='model', help='Имя модели для сохранения')
    args = parser.parse_args()

    tokenizer.check_path(args.folder_to_save_model)
    tokens = tokenizer.get_tokens(args.input_path)
    path_to_save_model = f'{args.folder_to_save_model}/{args.name_to_save_model}'

    print('Обучение начато.')
    gen_model = model.TextGenModel()
    gen_model.fit(tokens)
    gen_model.save(path_to_save_model)
    print(f'Обучение прошло успешно. Модель сохранена в {path_to_save_model}')
