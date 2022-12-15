import csv
from typing import Callable


f = './vgsales.csv'


def all_registers(
        name_file: str) -> tuple[tuple[str, ...], tuple[tuple[str, ...], ...]]:
    '''Devuelve una tupla que tiene una tupla con los headers del csv 
    y una tupla de tuplas con todos los registros y todas las columnas del archivo vgsales.csv'''

    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=',')
        h = tuple(next(games))

        tuple_games = tuple(tuple(game) for game in games)

        return (h, tuple_games)


# Closure para seleccionar una columna de una tupla.
def select_column(column: str, h: tuple[str, ...]) -> Callable:

    def inner(data: tuple):
        return data[h.index(column)]

    return inner


# Closure para filtrar una tupla de tuplas por una columna y un valor.
def filter_column(column: str, value, h: tuple[str, ...]) -> Callable:

    def inner(data: tuple) -> tuple:
        return tuple([d for d in data if d[h.index(column)] == value])

    return inner