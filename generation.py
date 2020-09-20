import argparse
import model

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Использование модели TextGen для генерации текста')
    parser.add_argument('file', type=str, help='Путь к местоположению модели')
    parser.add_argument('--length', '-l', type=int, default=10, help='Длинна фразы для генерации')
    parser.add_argument('--is_rand', '-r', type=str, default='false', help='Метод генерации')
    parser.add_argument('--num_of_word_to_choose', '-n', type=int, default=7,
                        help='Если генерация не полностью рандомная, то эта переменная используется для определения '
                             'топовых N слов, из которых уже рандомно выбирается одно')
    parser.add_argument('--seed', '-s', type=int, default=0, help='Seed')
    args = parser.parse_args()

    gen_model = model.TextGenModel()
    gen_model.load(args.file)
    result_string = gen_model.generate(length=args.length, is_rand=(args.is_rand.lower() == 'true'), seed=args.seed,
                                       num_of_word_to_choose=args.num_of_word_to_choose)

    print(result_string)
