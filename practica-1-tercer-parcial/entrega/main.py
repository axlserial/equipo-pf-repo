from utils import all_registers
from pprint import pprint
import list_comp as lc
import dict_transform as dt


def main():
    h, data = all_registers('./vgsales.csv')

    # List
    print("----------------------------- List  -------------------------------\n")
    print_list()
    print(
        "\n-------------------------------------------------------------------"
    )

    # Dict
    print("\n------------------------ Dictionary -------------------------------\n")
    print_dicts(h, data)
    print(
        "\n-------------------------------------------------------------------"
    )


# ------------------ list Comps ----------------


def print_list() -> None:
    dir_csv = "./vgsales.csv"

    #Ciclo que sirve como iteradores encadenados y nos muestra las 5 actividades, genera una lista del CSV y musestra las 5 actividades puestas en el modulo List_comp.py
    for i in lc.actividades(dir_csv):

        #Comprueba que sea un iterador (Object)
        if (isinstance(i, object)):
            for j, k in enumerate(i):
                #Usando enumerate vamos a verificar que solo 3 se impriman, esto para no imprimir muchos juegos y puedan diferenciarse las actividades
                if j == 3:
                    print(k)
                    break
                print(k)

        # si no es un iterador es un iterable o lista
        else:
            print(i[:4])


# ------------------ Dicts ----------------


def print_dicts(h: tuple[str, ...], data: tuple[tuple[str, ...], ...]) -> None:
    print(
        "1. Diccionario con el 'Name' del juego como clave y la 'Platform' del juego como valor."
    )
    dict_one = dt.first_dict(data, h)
    pprint(dict(list(dict_one.items())[:3]))

    print(
        "\n2. Diccionario con el 'Name' del juego como clave y la 'Platform' del juego como valor que sean del año 2009."
    )
    dict_two = dt.second_dict(data, h)
    pprint(dict(list(dict_two.items())[:3]))

    print(
        "\n3. Diccionario con todos los registros que su 'Publisher' sea Sega")
    dict_three = dt.third_dict(data, h)
    pprint(dict(list(dict_three.items())[:3]))

    print(
        "\n4. Diccionario que tiene el 'Name' del juego como clave y sus datos como valor y que 'Rank' sea mayor a 10 y menor a 20"
    )
    dict_four = dt.fourth_dict(data, h)
    pprint(dict(list(dict_four.items())[:3]))

    print(
        "\n5. Diccionario con el 'Name' del juego como clave y un promedio de sus Sales como valor"
    )
    dict_five = dt.fifth_dict(data, h)
    pprint(dict(list(dict_five.items())[:3]))


# ----------------------------------------------

if __name__ == '__main__':
    main()