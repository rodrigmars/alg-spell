from time import process_time
from pytest import fixture
from typing import Iterator


def letter_to_index(letter: str) -> Iterator[int]:
    _alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return (i for i, _letter in enumerate(_alphabet, 1) if _letter == letter)


@fixture()
def setup() -> list[str]:

    phrase_matrix = "Liberdade, verdade, paz ou talvez amor? São ilusões, \
        fantasias da percepção, sínteses temporárias de um débil intelecto \
            humano tentando desesperadamente explicar uma existência \
                sem significado ou propósito."

    words = phrase_matrix.lower().split()

    return words


def test_letter_to_index_with_enumerate(setup) -> None:

    words = setup

    print("words:", words)

    start_time = process_time()

    letters: list = []
    
    for letter in words:

        chars = []

        for char in [*letter]:
            chars.append(next(letter_to_index(char), None))

        letters.append({letter: chars})




    end_time = process_time()

    res = end_time - start_time

    print(f'CPU Execution time:{res} seconds')
    print(f'\n{letters}')