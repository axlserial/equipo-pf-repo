import csv

f = './vgsales.csv'


def all_registers(
        name_file: str) -> tuple[tuple[str], tuple[tuple[str, ...], ...]]:
    '''Devuelve una tupla que tiene una tupla con los headers del csv 
    y una tupla de tuplas con todos los registros y todas las columnas del archivo vgsales.csv'''

    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=',')
        h = tuple(next(games))

        tuple_games = tuple(tuple(game) for game in games)

        return (h, tuple_games)