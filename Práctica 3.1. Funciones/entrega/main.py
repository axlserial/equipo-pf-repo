from utils import all_registers
from pprint import pprint
import dict_comp as dc
import set_comp as sc
import list_comp as lc

def main():
    h, data = all_registers('./vgsales.csv')

    # List Comprehensions
    print("-------------------- List Comprehensions --------------------\n")
    print_list(h, data)
    print("\n-----------------------------------------------------------------")
    # Diccionary Comprehensions
    print("-------------------- Diccionary Comprehensions --------------------\n")
    print_dicts(h, data)
    print("\n-----------------------------------------------------------------")
    # Set Comprehensions
    print("\n-------------------- Set Comprehensions --------------------\n")
    print_sets(h, data)
    print("\n-----------------------------------------------------------------")
    print("\n-------------------- Set Operations ---------------------------\n")
    print_operation_sets(h, data)
    print("\n-----------------------------------------------------------------")


# ------------------ list Comps ----------------

def print_list(h: tuple[str, ...], data: tuple[tuple[str, ...], ...]) -> None:
    lista = lc.generarLista(h,data)

    print("\n #------1.- listas de tuplas con nombres con una letra inicial seleccionada------#\n")
    main_list = lc.lista_tupla(lista,1)
    main_list("w")
    print("\n #------2.- lista de tuplas con nombre y con un año seleccionado------#\n")
    main_list = lc.lista_tupla(lista,2)
    main_list("2006")
    print("\n #------3.- lista de tuplas con nombre, año y plataforma seleccionada------#\n")
    main_list = lc.lista_tupla(lista,3)
    main_list("pc","nombre")
    print("\n #------4.- lista de tuplas con nombre y promedio de las ventas, ordenadas asc o desc------#\n")
    main_list = lc.lista_tupla(lista,4)
    main_list("ascendentes")
    print("\n #------5.- lista con rango, nombre y género a partir del año dado y ordenado por rango ------#\n")
    main_list = lc.lista_tupla(lista,5)
    main_list("2012")




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

# ------------------ Set Operations ----------------

def print_operation_sets(h: tuple[str, ...], data: tuple[tuple[str, ...], ...]) -> None:
    
    # 1. Obtener el conjunto de las tuplas de los juegos donde su 'Platform' sea 3DS, su 'Publisher' sea Sega
    # y su nombre no contenga la palabra Sonic.

    A = sc.conjunto_p(data, h) - sc.fourth_set_comp(data, h)
    print((
        "\n1. Conjunto de las tuplas de los juegos donde su 'Platform' sea 3DS, "
        "su 'Publisher' sea Sega y su nombre no contenga la palabra Sonic."))
    pprint(set(list(A)[:5]))

    # 2. Obtener el conjunto de los 'Publisher' que poseen juegos del genero 'Platform' cuyo
    # lanzamiento esta entre los años 2013-2016 y los nombres de las plataformas.

    B = sc.fifth_set_comp(data, h).union(sc.first_set_comp(data, h))
    print((
        "\n2. Conjunto de los 'Publisher' que poseen juegos del genero 'Platform' "
        "cuyo lanzamiento esta entre los años 2013-2016 y los nombres de las plataformas."
    ))
    pprint(set(list(B)[:5]))
    
    # 3. Obtener el conjunto de tuplas que pertenezcan tanto al conjunto A y el resultado
    # de ejercicio 2 de la sección anterior.

    C = A.intersection(sc.second_set_comp(data, h))
    print(("\n3. Conjunto de tuplas que pertenezcan tanto al conjunto A "
           "y el resultado de ejercicio 2 de la sección anterior."))
    pprint(set(list(C)[:5]))

    # 4. Obtener el conjunto complemento de las plataformas que pertenecen a los resultados
    # del ejercicio 1 de la sección anterior y el conjunto de la llamada a la función
    # conjunto_q(f).

    D = sc.conjunto_q(data, h) ^ sc.first_set_comp(data, h)
    print((
        "\n4. Conjunto complemento de las plataformas que pertenecen a "
        "los resultados del ejercicio 1 de la sección anterior "
        "y el conjunto de la llamada a la función conjunto_q(f)."
    ))
    pprint(set(list(D)[:5]))

    # 5. Obtener el conjunto de tuplas donde las ventas de los juegos que se encuentren en el conjunto
    # del ejercicio 3 de la sección anterior y en el conjunto de la llamda a la función
    # conjunto_u(f).

    E = sc.third_set_comp(data, h) & sc.conjunto_u(data, h)
    print(
        ("\n5. Conjunto de tuplas donde las ventas de los juegos "
         "que se encuentren en el conjunto del ejercicio 3 de la sección "
         "anterior y en el conjunto de la llamda a la función conjunto_u(f)."))
    pprint(set(list(E)[:5]))

#---------------------------------------------------

if __name__ == '__main__':
    main()