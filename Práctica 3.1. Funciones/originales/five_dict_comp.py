import csv
from pprint import pprint
from statistics import mean


# Diccionario con el 'Name' del juego como clave y la 'Platform'
# del juego como valor.
def first_dict_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=',')
        h = next(games)

        dict_games = {
            game[h.index("Name")]: game[h.index("Platform")]
            for game in games
        }

        return dict_games


# Diccionario con el 'Name' del juego como clave y la 'Platform'
# del juego como valor que sean del año 2009.
def second_dict_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=',')
        h = next(games)

        dict_games = {
            game[h.index("Name")]: game[h.index("Platform")]
            for game in games if game[h.index("Year")] == "2009"
        }

        return dict_games


# Diccionario con todos los registros que su 'Publisher' sea Sega
def third_dict_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=',')
        h = next(games)

        dict_games = {
            game[h.index("Name")]: {
                "Platform": game[h.index("Platform")],
                "Year": game[h.index("Year")],
                "Genre": game[h.index("Genre")],
                "Publisher": game[h.index("Publisher")]
            }
            for game in games if game[h.index("Publisher")] == "Sega"
        }

        return dict_games


# Diccionario que tiene el 'Name' del juego como clave
# y sus datos como valor y que 'Rank' sea mayor a 10 y menor a 20
def fourth_dict_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=',')
        h = next(games)

        dict_games = {
            game[h.index("Name")]: {
                "Rank": game[h.index("Rank")],
                "Platform": game[h.index("Platform")],
                "Year": game[h.index("Year")],
                "Genre": game[h.index("Genre")],
                "Publisher": game[h.index("Publisher")]
            }
            for game in games if int(game[h.index("Rank")]) > 10
            and int(game[h.index("Rank")]) < 20
        }

        return dict_games


# Diccioanrio con el 'Name' del juego como clave
# y un promedio de sus Sales como valor
def fifth_dict_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=',')
        h = next(games)

        dict_games = {
            game[h.index("Name")]: mean([
                float(game[h.index("NA_Sales")]),
                float(game[h.index("EU_Sales")]),
                float(game[h.index("JP_Sales")]),
                float(game[h.index("Other_Sales")])
            ])
            for game in games
        }

        return dict_games


def run():
    f = './vgsales.csv'

    print("Impresión limitada a los primeros 3 elementos del diccionario\n")

    print(
        "1. Diccionario con el 'Name' del juego como clave y la 'Platform' del juego como valor."
    )
    first = first_dict_comp(f)
    pprint(dict(list(first.items())[:3]))

    print(
        "\n2. Diccionario con el 'Name' del juego como clave y la 'Platform' del juego como valor que sean del año 2009."
    )
    second = second_dict_comp(f)
    pprint(dict(list(second.items())[:3]))

    print(
        "\n3. Diccionario con todos los registros que su 'Publisher' sea Sega")
    third = third_dict_comp(f)
    pprint(dict(list(third.items())[:3]))

    print(
        "\n4. Diccionario que tiene el 'Name' del juego como clave y sus datos como valor y que 'Rank' sea mayor a 10 y menor a 20"
    )
    fourth = fourth_dict_comp(f)
    pprint(dict(list(fourth.items())[:3]))

    print(
        "\n5. Diccionario con el 'Name' del juego como clave y un promedio de sus Sales como valor"
    )
    fifth = fifth_dict_comp(f)
    pprint(dict(list(fifth.items())[:3]))


if __name__ == "__main__":
    run()