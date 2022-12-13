import csv
from pprint import pprint


# Conjunto de los nombres de las plataformas
def first_set_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=",")
        h = next(games)

        set_games = {game[h.index("Platform")] for game in games}

        return set_games


# Conjunto de todos los registros donde sus elementos
# sean la tupla 'Name' y 'Global_Sales' de los juegos
def second_set_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=",")
        h = next(games)

        set_games = {(game[h.index("Name")], game[h.index("Global_Sales")])
                     for game in games}

        return set_games


# Conjunto de todos los registros donde sus elementos
# sean la tupla 'Name' y 'NA_Sales' de los juegos
# que hayan vendido más de 5.0 millones en NA
def third_set_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=",")
        h = next(games)

        set_games = {(game[h.index("Name")], game[h.index("NA_Sales")])
                     for game in games
                     if float(game[h.index("NA_Sales")]) > 5.0}

        return set_games


# Conjunto de tuplas con las columnas: 'Name' y 'Global_Sales'
# de juegos donde su 'Publisher' sea Sega, su 'Platform' sea 3DS
# y que contengan la palabra Sonic.
def fourth_set_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=",")
        h = next(games)

        set_games = {(game[h.index("Name")], game[h.index("Global_Sales")])
                     for game in games if game[h.index("Publisher")] == "Sega"
                     and game[h.index("Platform")] == "3DS"
                     and game[h.index("Name")].find("Sonic") != -1}

        return set_games


# Conjunto de los nombres de los 'Publisher' que poseen juegos
# del genero 'Platform' cuyo lanzamiento esté entre los años 2013 y 2016.
def five_set_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=",")
        h = next(games)

        set_games = {
            game[h.index("Publisher")]
            for game in games
            if game[h.index("Year")] >= '2013' and game[h.index("Year")] <=
            '2016' and game[h.index("Genre")] == "Platform"
        }

        return set_games


# Conjunto de tuplas con las columnas: Name y Global_Sales
# de juegos que su plublisher sea Sega y su plataforma 3DS.
def conjunto_p(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=",")
        h = next(games)

        set_games = {(game[h.index("Name")], game[h.index("Global_Sales")])
                     for game in games if game[h.index("Publisher")] == "Sega"
                     and game[h.index("Platform")] == "3DS"}

        return set_games


# Conjunto de los nombres de las plataformas que tengan juegos del genero Action
def conjunto_q(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=",")
        h = next(games)

        set_games = {
            game[h.index("Platform")]
            for game in games if game[h.index("Genre")] == "Action"
        }

        return set_games


# Conjunto de todos los registros que sus elementos
# sean la tupla "Name" y "NA_Sales" de los juegos
# que hayan vendido menos de 2.0 millones en NA
def conjunto_u(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=",")
        h = next(games)

        set_games = {(game[h.index("Name")], game[h.index("NA_Sales")])
                     for game in games
                     if float(game[h.index("NA_Sales")]) > 4.0}

        return set_games


def run():
    f = './vgsales.csv'

    print("NOTA: Impresión limitada a los primeros 5 elementos del conjunto\n")

    print("--------------- Set comprenhensions:\n")

    print("1. Conjunto de los nombres de las plataformas")
    pprint(set(list(first_set_comp(f))[:5]))

    print(
        "\n2. Conjunto de todos los registros que sus elementos sean la tupla "
        "'Name' y 'Global_Sales' de los juegos")
    pprint(set(list(second_set_comp(f))[:5]))

    print(
        "\n3. Conjunto de todos los registros donde sus elementos sean la tupla "
        "'Name' y 'NA_Sales' de los juegos que hayan vendido más de 5.0 "
        "millones en NA")
    pprint(set(list(third_set_comp(f))[:5]))

    print(
        "\n4. Conjunto de tuplas con las columnas: 'Name' y 'Global_Sales' de juegos "
        "donde su 'Publisher' sea Sega, su 'Platform' sea 3DS y que contengan la palabra Sonic"
    )
    pprint(set(list(fourth_set_comp(f))[:5]))

    print(
        "\n5. Conjunto de los nombres de los 'Publisher' que poseen juegos del "
        "genero 'Platform' cuyo lanzamiento esté entre los años 2013 y "
        "2016")
    pprint(set(list(five_set_comp(f))[:5]))

    #Operaciones con conjuntos

    print("\n\n--------------- Operaciones con conjuntos:\n")

    # 1. Obtener el conjunto de las tuplas de los juegos donde su 'Platform' sea 3DS, su 'Publisher' sea Sega
    # y su nombre no contenga la palabra Sonic.
    A = conjunto_p(f) - fourth_set_comp(f)
    print((
        "\n1. Conjunto de las tuplas de los juegos donde su 'Platform' sea 3DS, "
        "su 'Publisher' sea Sega y su nombre no contenga la palabra Sonic."))
    pprint(set(list(A)[:5]))

    # 2. Obtener el conjunto de los 'Publisher' que poseen juegos del genero 'Platform' cuyo
    # lanzamiento esta entre los años 2013-2016 y los nombres de las plataformas.
    B = five_set_comp(f).union(first_set_comp(f))
    print((
        "\n2. Conjunto de los 'Publisher' que poseen juegos del genero 'Platform' "
        "cuyo lanzamiento esta entre los años 2013-2016 y los nombres de las plataformas."
    ))
    pprint(set(list(B)[:5]))

    # 3. Obtener el conjunto de tuplas que pertenezcan tanto al conjunto A y el resultado
    # de ejercicio 2 de la sección anterior.
    C = A.intersection(second_set_comp(f))
    print(("\n3. Conjunto de tuplas que pertenezcan tanto al conjunto A "
           "y el resultado de ejercicio 2 de la sección anterior."))
    pprint(set(list(C)[:5]))

    # 4. Obtener el conjunto complemento de las plataformas que pertenecen a los resultados
    # del ejercicio 1 de la sección anterior y el conjunto de la llamada a la función
    # conjunto_q(f).
    D = conjunto_q(f).symmetric_difference(first_set_comp(f))
    print((
        "\n4. Conjunto complemento de las plataformas que pertenecen a "
        "los resultados del ejercicio 1 de la sección anterior "
        "y el conjunto de la llamada a la función conjunto_q(f)."
    ))
    pprint(set(list(D)[:5]))

    # 5. Obtener el conjunto de tuplas donde las ventas de los juegos que se encuentren en el conjunto
    # del ejercicio 3 de la sección anterior y en el conjunto de la llamda a la función
    # conjunto_u(f).
    E = third_set_comp(f) & conjunto_u(f)
    print(
        ("\n5. Conjunto de tuplas donde las ventas de los juegos "
         "que se encuentren en el conjunto del ejercicio 3 de la sección "
         "anterior y en el conjunto de la llamda a la función conjunto_u(f)."))
    pprint(set(list(E)[:5]))


if __name__ == "__main__":
    run()