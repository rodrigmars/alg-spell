from decouple import config

NAME_PROJECT = config("NAME_PROJECT", "").__str__()

PATH_PROJECT = config("PATH_PROJECT", "").__str__()
