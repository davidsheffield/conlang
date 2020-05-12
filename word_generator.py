import random

import pandas as pd


def word_generator(frequencies, syllables, words):
    frequencies = pd.read_csv(frequencies)

    for i in range(words):
        word = ''.join([f'{C}{V}' for (C, V) in zip(
            random.choices(frequencies['Phoneme'].values,
                           frequencies['C'].values,
                           k=syllables),
            random.choices(frequencies['Phoneme'].values,
                           frequencies['V'].values,
                           k=syllables))])
        print(word)


if __name__ == '__main__':
    word_generator('frequencies.csv', 2, 20)
