from utils import all_registers
from pprint import pprint
import dict_comp as dc


def main():
    h, data = all_registers('./vgsales.csv')

    # Diccionary Comprehensions
    print_dicts(h, data)


# ------------------ Dict Comps ----------------


def print_dicts(h: tuple[str], data: tuple[tuple[str, ...], ...]) -> None:
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

if __name__ == '__main__':
    main()