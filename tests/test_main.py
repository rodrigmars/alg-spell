from pytest import fixture

from os import system, path
from decouple import config

@fixture
def setup():
    return config("PATH_PROJECT"), config("NAME_PROJECT")


def test_create_folder(setup):
    
    path_project, name_project = setup

    system(f"mkdir {path_project}/{name_project}")

    assert path.isdir(f"{path_project}/{name_project}")
