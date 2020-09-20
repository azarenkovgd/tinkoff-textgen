import random
import pickle
import sys


class TextGenModel:
    """Модель генерирует тексты заданной пользователем длины. Для генерации используются биграммы."""

    def __init__(self):
        # Словарь из слова в качестве ключа и массива кортежей из слов, идущих после первого слова и частоты,
        # с которой они шли
        self.model = {}

    def save(self, path):
        pickle.dump(self.model, open(path, 'wb'))

    def load(self, path):
        self.model = pickle.load(open(path, 'rb'))

    def fit(self, tokens):
        """Обучение модели

        Args:
            tokens: Массив токенов, предварительно извлеченных из выбранного текста
        """

        if len(tokens) < 2:
            sys.exit(f'Слишком маленький датасет')

        bigramms = get_bigramms(tokens)  # Получим все биграммы
        bigramms_counter = {}  # Создадим словарь для сохранения частотности всех биграмм

        for bigramm in bigramms:
            bigramms_counter[bigramm] = bigramms_counter.setdefault(bigramm, 0) + 1

        for (w1, w2), freq in bigramms_counter.items():  # Занесем данные в модель
            self.model[w1] = self.model.setdefault(w1, [])
            self.model[w1].append((w2, freq))

    def generate(self, length, is_rand, seed, num_of_word_to_choose):
        """Генерация текста

        Args:
            length: Количество слов в генерируемой строке
            is_rand: Использовать ли любое рандомное слово,
                     встречающееся после исходного, или наиболее часто встречающееся
            seed: Сид для random
            num_of_word_to_choose: Если генерация не полностью рандомная, то эта переменная используется для определения
                                   топовых N слов, из которых уже рандомно выбирается одно
        """

        random.seed(seed)
        w1 = random.choice(list(self.model.keys()))
        gen_str = w1[0].upper() + w1[1:]

        for i in range(length - 1):
            if w1 in self.model:
                if is_rand:
                    # Рандомное слово из всех когда либо появлявшихся после слова w1
                    w2 = random.choice(self.model[w1])[0]
                else:
                    # Для избежания бесконечных самоповторов при большой длинне итоговой строки берется не просто
                    # слово с самой высокой частотой появления после w1, а рандомное слово из первых
                    # num_of_word_to_choose с самой высокой частотой появления после w1
                    w2 = random.choice(sorted(self.model[w1], key=lambda x: x[1], reverse=True)[:num_of_word_to_choose])[0]
            else:
                # Если после слова w1 не шло ни одно другое слово, то выбирается рандомное слово из всех имеющихся в
                # тренировочной выборке
                w2 = random.choice(tuple(self.model.keys()))

            gen_str += ' ' + w2
            w1 = w2

        return gen_str


def get_bigramms(tokens):
    """Возвращает биграммы из массива токенов"""

    return [(tokens[i], tokens[i + 1]) for i in range(0, len(tokens) - 1)]
