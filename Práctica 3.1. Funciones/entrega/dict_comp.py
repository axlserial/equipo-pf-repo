from typing import Callable
from statistics import mean

# ------------------ Closures ------------------


# Closure para seleccionar una columna de una tupla.
def select_column(column: str, h: tuple[str]) -> Callable:

    def inner(data: tuple):
        return data[h.index(column)]

    return inner


# Closure para obtener ciertas columnas de una tupla.
def select_columns(columns: list[str], h: tuple[str]) -> Callable:

    def inner(data: tuple) -> tuple:
        return tuple([data[h.index(c)] for c in columns])

    return inner


# Closure para filtrar una tupla de tuplas por una columna y un valor.
def filter_column(column: str, value, h: tuple[str]) -> Callable:

    def inner(data: tuple) -> tuple:
        return tuple([d for d in data if d[h.index(column)] == value])

    return inner


# Closure para ordenar una tupla de tuplas por una columna.
def sort_column(column: str, h: tuple[str], asc=True) -> Callable:

    def inner(data: tuple) -> tuple:
        return tuple(
            sorted(data, key=lambda x: x[h.index(column)], reverse=not asc))

    return inner


# ----------------------------------------------

# ------------------ Dict Comps ----------------


# Diccionario con el 'Name' del juego como clave y la 'Platform'
# del juego como valor.
def first_dict_comp(data: tuple[tuple[str, ...], ...], h: tuple[str]) -> dict:
    get_name = select_column("Name", h)
    get_platform = select_column("Platform", h)

    dict_games = {get_name(game): get_platform(game) for game in data}

    return dict_games


# Diccionario con el 'Name' del juego como clave y la 'Platform'
# del juego como valor, que sean del año 2009.
def second_dict_comp(data: tuple[tuple[str, ...], ...], h: tuple[str]) -> dict:
    filter_year = filter_column("Year", "2009", h)
    get_name = select_column("Name", h)
    get_platform = select_column("Platform", h)

    dict_games = {
        get_name(game): get_platform(game)
        for game in filter_year(data)
    }

    return dict_games


# Diccionario con todos los registros que su 'Publisher' sea Sega
def third_dict_comp(data: tuple[tuple[str, ...], ...], h: tuple[str]) -> dict:
    filter_publisher = filter_column("Publisher", "Sega", h)
    get_name = select_column("Name", h)
    get_platform = select_column("Platform", h)
    get_year = select_column("Year", h)
    get_genre = select_column("Genre", h)
    get_publisher = select_column("Publisher", h)

    dict_games = {
        get_name(game): {
            "Platform": get_platform(game),
            "Year": get_year(game),
            "Genre": get_genre(game),
            "Publisher": get_publisher(game),
        }
        for game in filter_publisher(data)
    }

    return dict_games


# Diccionario que tiene el 'Name' del juego como clave
# y sus datos como valor y que 'Rank' sea mayor a 10 y menor a 20
def fourth_dict_comp(data: tuple[tuple[str, ...], ...], h: tuple[str]) -> dict:
    get_name = select_column("Name", h)
    get_rank = select_column("Rank", h)
    get_platform = select_column("Platform", h)
    get_year = select_column("Year", h)
    get_genre = select_column("Genre", h)
    get_publisher = select_column("Publisher", h)

    sort_func = sort_column("Rank", h)

    dict_games = {
        get_name(game): {
            "Rank": get_rank(game),
            "Platform": get_platform(game),
            "Year": get_year(game),
            "Genre": get_genre(game),
            "Publisher": get_publisher(game),
        }
        for game in sort_func([
            d for d in data if int(get_rank(d)) > 10 and int(get_rank(d)) < 20
        ])
    }

    return dict_games


# Diccioanrio con el 'Name' del juego como clave
# y un promedio de sus Sales como valor
def fifth_dict_comp(data: tuple, h: tuple[str]) -> dict:
    sales_selected = select_columns(
        ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"], h)
    get_name = select_column("Name", h)

    dict_games = {
        get_name(game): mean(map(lambda x: float(x), sales_selected(game)))
        for game in data
    }

    return dict_games


# ----------------------------------------------