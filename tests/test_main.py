from pytest import fixture

from os import system, path

from settings import NAME_PROJECT, PATH_PROJECT


@fixture
def setup():

    if path.exists(path.join(PATH_PROJECT, NAME_PROJECT)):

        system(f"rm -r {PATH_PROJECT}/{NAME_PROJECT}")

    return PATH_PROJECT, NAME_PROJECT


def test_creating_root_folder(setup):

    path_project, name_project = setup

    system(f"mkdir {path_project}/{name_project}")

    assert path.exists(f"{path_project}/{name_project}")

def test_creating_root_sub_folder(setup):

    path_project, name_project = setup

    system(f"mkdir {path_project}/{name_project}/{name_project}")

    assert path.exists(f"{path_project}/{name_project}/{name_project}")

