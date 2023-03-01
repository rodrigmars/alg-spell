from re import sub
from time import process_time
from pytest import fixture
from typing import Iterator
from unicodedata import normalize


def only_alphabetic_characters(text: str) -> str:
    return sub("[^A-Za-z\\s]", "", text)


def normalize_text(text: str) -> str:
    return normalize('NFD', text)\
        .encode('ASCII', 'ignore')\
        .decode('UTF-8')


def letter_to_number(letter: str) -> Iterator[int]:
    _alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return (i for i, _letter in enumerate(_alphabet, 1) if _letter == letter)


@fixture()
def setup() -> list[str]:

    phrase_matrix = "Liberdade, verdade, paz ou talvez amor? São ilusões, \
        fantasias da percepção, sínteses temporárias de um débil intelecto \
            humano tentando desesperadamente explicar uma existência \
                sem significado ou propósito."

    return only_alphabetic_characters(normalize_text(phrase_matrix.lower())).split()


def test_letter_to_index_with_enumerate(setup) -> None:

    words = setup

    print("words:", words)

    start_time = process_time()

    letters: dict = {}

    for word in words:

        indexes = []

        for letter in [*word]:
            indexes.append(next(letter_to_number(letter), None))

        letters.update({word: indexes})

    end_time = process_time()

    res = end_time - start_time

    print(f'CPU Execution time:{res} seconds')
    print(f'\n{letters}\n')

    for k, v in letters.items():
        print(f'{k.rjust(16)}:{v}')
