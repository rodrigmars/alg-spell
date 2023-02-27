from pytest import fixture


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

# @mark.skip
def test_menu_option_one() -> None:

    assert [1, 2, 3] == create_menu()
