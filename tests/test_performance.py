from datetime import datetime
from re import sub
from time import process_time
from pytest import fixture
from typing import Iterator
from unicodedata import normalize


symbols = {"A": "Alfa",
           "B": "Bravo",
           "C": "Charlie",
           "D": "Delta",
           "E": "Echo",
           "F": "Foxtrot",
           "G": "Golf",
           "H": "Hotel",
           "I": "India",
           "J": "Juliett",
           "K": "Kilo",
           "L": "Lima",
           "M": "Mike",
           "N": "November",
           "O": "Oscar",
           "P": "Papa",
           "Q": "Quebec",
           "R": "Romeo",
           "S": "Sierra",
           "T": "Tango",
           "U": "Uniform",
           "V": "Victor",
           "W": "Whiskey",
           "X": "Xray",
           "Y": "Yankee",
           "Z": "Zulu",
           "0": "ZE-RO",
           "1": "WUN",
           "2": "TOO",
           "3": "TREE",
           "4": "FOW-er",
           "5": "FIFE",
           "6": "SIX",
           "7": "SEV-en",
           "8": "AIT",
           "9": "NIN-er"}


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

    print("words:>>>>>>>>>", words)

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


def test_get_time_execution():

    phrase = "The NATO phonetic alphabet is a Spelling Alphabet \
        a set of words used instead of letters in oral communication \
            over the phone or military radio The NATO phonetic alphabet is a Spelling Alphabet \
        a set of words used instead of letters in oral communication \
            over the phone or military radio The NATO phonetic alphabet is a Spelling Alphabet \
        a set of words used instead of letters in oral communication \
            over the phone or military radio The NATO phonetic alphabet is a Spelling Alphabet \
        a set of words used instead of letters in oral communication \
            over the phone or military radio The NATO phonetic alphabet is a Spelling Alphabet \
        a set of words used instead of letters in oral communication \
            over the phone or military radio The NATO phonetic alphabet is a Spelling Alphabet \
        a set of words used instead of letters in oral communication \
            over the phone or military radio The NATO phonetic alphabet is a Spelling Alphabet \
        a set of words used instead of letters in oral communication \
            over the phone or military radio The NATO phonetic alphabet is a Spelling Alphabet \
        a set of words used instead of letters in oral communication \
            over the phone or military radio The NATO phonetic alphabet is a Spelling Alphabet \
        a set of words used instead of letters in oral communication \
            over the phone or military radio"
    print()

    start_time = datetime.now()
    # list_ = []
    for word in phrase.split():
        # print(
        #     f"{word.rjust(13)}:{list(map(lambda x: symbols[x.upper()], [*word]))}")
        map(lambda x: symbols[x.upper()], [*word])

    end_time = datetime.now()

    print(f'TIME-01: {(end_time - start_time)}')

    start_time = datetime.now()

    code_words = [{word: [symbols[letter]
                          for letter in [*word.upper()]]}
                  for word in phrase.split()]

    # for coded in code_words:
    #     for k, v in coded.items():
    #         print(f"{k.rjust(15)}:{v}")

    end_time = datetime.now()

    print(f'TIME-02: {(end_time - start_time)}')

    # non_alphabet = "ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝŔÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿŕ";

    # non_alphabet = {"ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝŔÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿŕ"}

    non_alphabet = {"Á": "A",
                    "Â": "A",
                    "Ã": "A",
                    "Ä": "A",
                    "Å": "A",
                    "Æ": "A",
                    "Ç": "C",
                    "È": "E",
                    "É": "E",
                    "Ê": "E",
                    "Ë": "E",
                    "Ì": "I",
                    "Í": "I",
                    "Î": "I",
                    "Ï": "I",
                    "Ð": "D",
                    "Ñ": "N",
                    "Ò": "O",
                    "Ó": "O",
                    "Ô": "O",
                    "Õ": "O",
                    "Ö": "O",
                    "Ø": "O",
                    "Ù": "U",
                    "Ú": "U",
                    "Û": "U",
                    "Ü": "U",
                    "Ý": "Y",
                    "Ŕ": "R",
                    "Þ": "s",
                    "ß": "B",
                    "à": "a",
                    "á": "a",
                    "â": "a",
                    "ã": "a",
                    "ä": "a",
                    "å": "a",
                    "æ": "a",
                    "ç": "c",
                    "è": "e",
                    "é": "e",
                    "ê": "e",
                    "ë": "e",
                    "ì": "i",
                    "í": "i",
                    "î": "i",
                    "ï": "i",
                    "ð": "o",
                    "ñ": "n",
                    "ò": "o",
                    "ó": "o",
                    "ô": "o",
                    "õ": "o",
                    "ö": "o",
                    "ø": "o",
                    "ù": "u",
                    "ú": "u",
                    "û": "u",
                    "ü": "u",
                    "ý": "y",
                    "þ": "b",
                    "ÿ": "y",
                    "ŕ": "r"}

    def get_alphabet(letter: str) -> str:
        result = non_alphabet.get(letter)
        return result if result else sub("[^A-Za-z0-9]+", "", str(letter))

    phrase = "Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein...Fórmula 1: Pérez é o mais rápido no 1º treino livre do GP do Bahrein..."

    words = []

    start_time = datetime.now()

    for word in phrase.split():
        letters = []

        for letter in list(word):

            if (alpha := get_alphabet(letter)):
                letters.append(symbols[alpha.upper()])

        words.append([word, letters])

    end_time = datetime.now()

    for word in words:
        a, b = [*word]
        print(f"{a.rjust(10)}:{b}")

    print(f'TIME-03: {(end_time - start_time)}')
    print(len(phrase))
