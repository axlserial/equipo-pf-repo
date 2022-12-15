from utils import all_registers
from pprint import pprint
import dict_comp as dc
import set_comp as sc


def main():
    h, data = all_registers('./vgsales.csv')


    # Diccionary Comprehensions
    print("-------------------- Diccionary Comprehensions --------------------\n")
    print_dicts(h, data)
    print("\n-----------------------------------------------------------------")
    # Set Comprehensions
    print("\n-------------------- Set Comprehensions --------------------\n")
    print_sets(h, data)
    print("\n-----------------------------------------------------------------")


# ------------------ Dict Comps ----------------


def print_dicts(h: tuple[str, ...], data: tuple[tuple[str, ...], ...]) -> None:
    print(
        "1. Diccionario con el 'Name' del juego como clave y la 'Platform' del juego como valor."
    )
    dict_one = dc.first_dict_comp(data, h)
    pprint(dict(list(dict_one.items())[:3]))

    print(
        "\n2. Diccionario con el 'Name' del juego como clave y la 'Platform' del juego como valor que sean del año 2009."
    )
    dict_two = dc.second_dict_comp(data, h)
    pprint(dict(list(dict_two.items())[:3]))

    print(
        "\n3. Diccionario con todos los registros que su 'Publisher' sea Sega")
    dict_three = dc.third_dict_comp(data, h)
    pprint(dict(list(dict_three.items())[:3]))

    print(
        "\n4. Diccionario que tiene el 'Name' del juego como clave y sus datos como valor y que 'Rank' sea mayor a 10 y menor a 20"
    )
    dict_four = dc.fourth_dict_comp(data, h)
    pprint(dict(list(dict_four.items())[:3]))

    print(
        "\n5. Diccionario con el 'Name' del juego como clave y un promedio de sus Sales como valor"
    )
    dict_five = dc.fifth_dict_comp(data, h)
    pprint(dict(list(dict_five.items())[:3]))


# ----------------------------------------------

# ------------------ Set Comps ----------------

def print_sets(h: tuple[str, ...], data: tuple[tuple[str, ...], ...]) -> None:
    print(
        "1. Conjunto de los nombres de las plataformas."
    )
    set_one = sc.first_set_comp(data, h)
    pprint(set(list(set_one)[:5]))

    print(
        "\n2. Conjunto de todos los registros que sus elementos sean la tupla "
        "'Name' y 'Global_Sales' de los juegos."
    )
    set_two = sc.second_set_comp(data, h)
    pprint(set(list(set_two)[:5]))

    print(
        "\n3. Conjunto de todos los registros donde sus elementos sean la tupla "
        "'Name' y 'NA_Sales' de los juegos que hayan vendido más de 5.0 "
        "millones en NA")
    set_three = sc.third_set_comp(data, h)
    pprint(set(list(set_three)[:5]))

    print(
        "\n4. Conjunto de tuplas con las columnas: 'Name' y 'Global_Sales' de juegos "
        "donde su 'Publisher' sea Sega, su 'Platform' sea 3DS y que contengan la palabra Sonic"
    )
    set_four = sc.fourth_set_comp(data, h)
    pprint(set(list(set_four)[:5]))

    print(
        "\n5. Conjunto de los nombres de los 'Publisher' que poseen juegos del "
        "genero 'Platform' cuyo lanzamiento esté entre los años 2013 y "
        "2016")
    set_five = sc.fifth_set_comp(data, h)
    pprint(set(list(set_five)[:5]))

if __name__ == '__main__':
    main()