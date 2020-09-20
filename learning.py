import argparse
import tokenizer
import model

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Обучение модели TextGen')
    parser.add_argument('input_path', type=str, help=('Расположение файла для обучения в формате .txt '
                                                      'или расположение папки с файлами для обучения в '
                                                      'формате .txt'))
    parser.add_argument('--path_to_save_model', '-s', type=str, default='textgen_model', help='Путь для сохранения '
                                                                                              'модели')
    args = parser.parse_args()
    tokens = tokenizer.get_tokens(args.input_path)

    print('Обучение начато.')

    gen_model = model.TextGenModel()
    gen_model.fit(tokens)
    gen_model.save(args.path_to_save_model)

    print(f'Обучение прошло успешно. Модель сохранена в {args.path_to_save_model}')
