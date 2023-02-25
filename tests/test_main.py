from pytest import fixture

from os import system, path

from settings import NAME_PROJECT, PATH_PROJECT

@fixture
def setup():

    print("PATH_PROJECT:", PATH_PROJECT)

    if path.exists(path.join(PATH_PROJECT, NAME_PROJECT)):

        system(f"rm -r {PATH_PROJECT}/{NAME_PROJECT}")        

    return PATH_PROJECT, NAME_PROJECT


def test_create_folder(setup):

    pass
    
    # path_project, name_project = setup

    # system(f"mkdir {path_project}/{name_project}")

    # assert path.isdir(f"{path_project}/{name_project}")
