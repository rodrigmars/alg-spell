from unicodedata import normalize

from pytest import fixture

from time import sleep


def create_menu() -> list[int]:

    actions: list = []

    while True:

        print("menu\n1-Cadastro\n2-Consulta\n3-Sair")

        option: str = input("Informe uma opção:_")

        if "1" == option:
            actions.append(1)

        if "2" == option:
            actions.append(2)

        if "3" == option:
            actions.append(3)
            break

    return actions

@fixture()
def setup() -> None:
    pass


def create_engine_data_set():
    pass

def create_data_set():
    pass


def convert_char_to_int_HOF(chars: list) -> list[int]:
    return [*map(ord, chars)]

# @mark.skip
def test_menu_option_one() -> None:
    original = "já que possui metrificação, É isto é, ç todos os versos apresentam dez sílabas poéticas (decassílabos)"

    original = "O que é real? Como você define o 'real'? \
        Se você está falando sobre o que você pode sentir, o que você pode cheirar, \
            o que você pode saborear e ver, o real são simplesmente sinais elétricos \
                interpretados pelo seu cérebro."


    def letter_to_int(letter):
        alphabet = list('abcdefghijklmnopqrstuvwxyz')
        return alphabet.index(letter) + 1

    chars_list = []
    for letter in [*"falando"]:
        chars_list.append(letter_to_int(letter))

    print("chars_list:", chars_list)



    # print(">>>>>>>>>>>", letter_to_int('A'))


    # print(f"\n>>>>>>>>>>>>>>>> {original}")

    def NFD_normalized(text: str) -> str:
        # NFKD - Normalization Form Compatibility Decomposition
        # D = Decomposition 
        # C = Composition
        # K = Compatibility
        return normalize('NFKD', text).encode('ASCII', 'ignore').decode('UTF-8')

    def remove_char(text: str) -> str:
        return re.sub('[^a-zA-Z0-9 ]+', '', text)

    import re
    char_array = [*remove_char(NFD_normalized(original))]

    # char_array = [
    #     *filter(str.isalnum and str.isspace, )]

    print("normalized:", char_array)

    print(convert_char_to_int_HOF(char_array))

    assert [1, 2, 3] == create_menu()
