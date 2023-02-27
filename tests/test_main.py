from pytest import fixture

from os import system, path

from settings import NAME_PROJECT, PATH_PROJECT

@fixture
def setup() -> tuple[str, str]:
    
    root_project = f"{PATH_PROJECT}/{NAME_PROJECT}"

    system(f"rm -r {root_project}") \
        if 0 == system(f"[ -d {root_project} ];") else None

    return PATH_PROJECT, NAME_PROJECT

def test_creating_root_folder(setup: tuple[str, str]) -> None:

    path_project, name_project = setup

    assert 0 == system(f"mkdir {path.join(path_project, name_project)}")

def test_creating_root_sub_folder(setup: tuple[str, str]) -> None:

    path_project, name_project = setup

    root: str = path.join(path_project, name_project)

    assert 0 == system(f"mkdir {root} && cd {root} && mkdir {name_project}")
