from utils import all_registers
from pprint import pprint
import list_comp as lc
import dict_transform as dt
import set_transform as st


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
    
    # Set
    print("\n------------------------ Set -------------------------------\n")
    print_sets(h, data)
    print(
        "\n-------------------------------------------------------------------"
    )

    # Set Operations
    print("\n------------------------ Set Opetarions -------------------------------\n")
    print_operation_sets(h, data)
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

# ------------------ Sets ----------------------

def print_sets(h: tuple[str, ...], data: tuple[tuple[str, ...], ...]) -> None:
    print(
        "1. Conjunto de los nombres de las plataformas."
    )
    set_one = st.first_set(data, h)
    pprint(set(list(set_one)[:5]))
    
    print(
        "\n2. Conjunto de todos los registros que sus elementos sean la tupla "
        "'Name' y 'Global_Sales' de los juegos."
    )
    set_two = st.second_set(data, h)
    pprint(set(list(set_two)[:5]))

    print(
        "\n3. Conjunto de todos los registros donde sus elementos sean la tupla "
        "'Name' y 'NA_Sales' de los juegos que hayan vendido más de 5.0 "
        "millones en NA"
    )
    set_three = st.third_set(data, h)
    pprint(set(list(set_three)[:5]))

    print(
        "\n4. Conjunto de tuplas con las columnas: 'Name' y 'Global_Sales' de juegos "
        "donde su 'Publisher' sea Sega, su 'Platform' sea 3DS y que contengan la palabra Sonic"
    )
    set_four = st.fourth_set(data, h)
    pprint(set(list(set_four)[:5]))

    print(
        "\n5. Conjunto de los nombres de los 'Publisher' que poseen juegos del "
        "genero 'Platform' cuyo lanzamiento esté entre los años 2013 y "
        "2016"
    )
    set_five = st.fifth_set(data, h)
    pprint(set(list(set_five)[:5]))

#-----------------------------------------------


# ------------------ Sets Operations ----------------------
def print_operation_sets(h: tuple[str, ...], data: tuple[tuple[str, ...],...]) -> None:

    A = st.conjunto_p(data, h) - st.fourth_set(data, h)
    print(
        "\n1. Conjunto de las tuplas de los juegos donde su 'Platform' sea 3DS, "
        "su 'Publisher' sea Sega y su nombre no contenga la palabra Sonic."
    )
    pprint(set(list(A)[:5]))

    B = st.fifth_set(data, h).union(st.first_set(data, h))
    print(
        "\n2. Conjunto de los 'Publisher' que poseen juegos del genero 'Platform' "
        "cuyo lanzamiento esta entre los años 2013-2016 y los nombres de las plataformas."
    )
    pprint(set(list(B)[:5]))

    C = A.intersection(st.second_set(data, h))
    print(
        "\n3. Conjunto de tuplas que pertenezcan tanto al conjunto A "
           "y el resultado de ejercicio 2 de la sección anterior."
    )
    pprint(set(list(C)[:5]))

    D = st.conjunto_q(data, h) ^ st.first_set(data, h)
    print(
        "\n4. Conjunto complemento de las plataformas que pertenecen a "
           "los resultados del ejercicio 1 de la sección anterior "
           "y el conjunto de la llamada a la función conjunto_q()."
    )
    pprint(set(list(D)[:5]))

    E = st.third_set(data, h) & st.conjunto_u(data, h)
    print(
        "\n5. Conjunto de tuplas donde las ventas de los juegos "
         "que se encuentren en el conjunto del ejercicio 3 de la sección "
         "anterior y en el conjunto de la llamda a la función conjunto_u()."
    )
    pprint(set(list(E)[:5]))


if __name__ == '__main__':
    main()