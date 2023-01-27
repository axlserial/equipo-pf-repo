from typing import Callable
from statistics import mean
from functools import reduce

# ------------------ Closures ------------------


# Closure para obtener ciertas columnas de una tupla.
def select_columns(columns: list[str], h: tuple[str, ...]) -> Callable:

    def inner(data: tuple[str, ...]):
        return (data[h.index(c)] for c in columns)

    return inner


# ----------------------------------------------


# Diccionario con el 'Name' del juego como clave y la 'Platform'
# del juego como valor.
def first_dict(data: tuple[tuple[str, ...], ...], h: tuple[str, ...]) -> dict:

    # Map que recorre la lista y genera una tupla con el 'Name' y la 'Platform'
    # del juego para luego convertirlo en un diccionario.
    return dict(
        map(lambda game: (game[h.index("Name")], game[h.index("Platform")]),
            data))


# Diccionario con el 'Name' del juego como clave y la 'Platform'
# del juego como valor, que sean del año 2009.
def second_dict(data: tuple[tuple[str, ...], ...], h: tuple[str, ...]) -> dict:

    # Map que recorre la lista y genera una tupla con el 'Name' y la 'Platform'
    # del juego de aquellos que son del año 2009 para luego convertirlo en un diccionario.
    return dict(
        map(lambda game: (game[h.index("Name")], game[h.index("Platform")]),
            filter(lambda game: game[h.index("Year")] == "2009", data)))


# Diccionario con todos los registros que su 'Publisher' sea Sega
def third_dict(data: tuple[tuple[str, ...], ...], h: tuple[str, ...]) -> dict:

    # filter que filtra a los juegos que su 'Publisher' sea Sega
    filtered_games = filter(lambda game: game[h.index("Publisher")] == "Sega",
                            data)

    # Map que recorre la lista y genera una tupla con el 'Name' y un diccionario
    # con los datos del juego para luego convertirlo en un diccionario.
    return dict(
        map(
            lambda game: (game[h.index("Name")], {
                "Platform": game[h.index("Platform")],
                "Year": game[h.index("Year")],
                "Genre": game[h.index("Genre")],
                "Plublisher": game[h.index("Publisher")],
            }), filtered_games))


# Diccionario que tiene el 'Name' del juego como clave
# y sus datos como valor y que 'Rank' sea mayor a 10 y menor a 20
def fourth_dict(data: tuple[tuple[str, ...], ...], h: tuple[str, ...]) -> dict:

    # filter que filtra a los juegos que su 'Rank' sea mayor a 10 y menor a 20
    filtered_games = filter(
        lambda game: int(game[h.index("Rank")]) > 10 and int(game[h.index(
            "Rank")]) < 20, data)

    # Map que recorre la lista y genera una tupla con el 'Name' y un diccionario
    # con los datos del juego para luego convertirlo en un diccionario.
    data = map(
        lambda game: (game[h.index("Name")], {
            "Rank": game[h.index("Rank")],
            "Platform": game[h.index("Platform")],
            "Year": game[h.index("Year")],
            "Genre": game[h.index("Genre")],
            "Plublisher": game[h.index("Publisher")],
        }), filtered_games)

    return dict(sorted(data, key=lambda game: game[1]["Rank"]))


# Diccionario con el 'Name' del juego como clave
# y un promedio de sus Sales como valor
def fifth_dict(data: tuple[tuple[str, ...], ...], h: tuple[str, ...]) -> dict:

    # Closure para obtener las columnas de ventas en diferentes territorios.
    sales_selected = select_columns(
        ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"], h)

    # Reduce que recorre la lista y genera un diccionario con el 'Name' del juego
    # como clave y un promedio de sus Sales como valor.
    return reduce(
        lambda dictionary, game: {
            **dictionary, game[h.index("Name")]:
            mean(map(float, sales_selected(game)))
        }, data, {})
