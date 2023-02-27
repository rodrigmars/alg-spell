from pytest import fixture

from os import system

from settings import NAME_PROJECT, PATH_PROJECT


@fixture
def setup() -> tuple[str, str]:

    root = f"{PATH_PROJECT}/{NAME_PROJECT}"

    system(f"rm -r {root}") \
        if 0 == system(f"[ -d {root} ];") else None

    return root, NAME_PROJECT


def test_creating_repo_folder(setup: tuple[str, str]) -> None:

    root, _ = setup

    assert 0 == system(f"mkdir {root}")


def test_creating_application_folder(setup: tuple[str, str]) -> None:

    root, name_project = setup

    assert 0 == system(f'mkdir {root} && mkdir {root}/{name_project}')
