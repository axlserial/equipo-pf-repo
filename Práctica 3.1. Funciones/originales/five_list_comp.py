import csv
from statistics import mean


# Lista con los nombres de los juegos
def first_list_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=',')
        h = next(games)

        list_games = [game[h.index("Name")] for game in games]

        return list_games


# Lista de tuplas con el nombre y el año de los juegos
def second_list_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=',')
        h = next(games)

        list_games = [(game[h.index("Name")], game[h.index("Year")])
                      for game in games]

        return list_games


# Lista de tuplas con el nombre, el año y la plataforma de los juegos
def third_list_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=',')
        h = next(games)

        list_games = [(game[h.index("Name")], game[h.index("Year")],
                       game[h.index("Platform")]) for game in games]

        return list_games


# Lista de tuplas que esten compuestas por
# las columnas Name y Avg_Sales la cual se obtiene
# del promedio de las columnas NA_Sales, EU_Sales, JP_Sales, Other_Sales y Global_Sales
def fourth_list_comp(name_file: str):
    sales = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']

    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=',')
        h = list(next(games))

        list_games = [(game[h.index("Name")],
                       mean([float(game[h.index(k)]) for k in sales]))
                      for game in games]

        return list_games


# Lista de listas con todos lo registros del archivo
# donde los juegos sean del año 2006 y su rango sea menor a 2000
def fifth_list_comp(name_file: str):
    with open(name_file) as csvfile:

        games = csv.reader(csvfile, delimiter=',')
        h = next(games)
        list_games = [
            game for game in games if game[h.index("Year")] == "2016"
            and float(game[h.index("Rank")]) < 2000
        ]

        return list_games


def run():
    f = './vgsales.csv'

    print("1. Lista con los nombres de los juegos.\n", first_list_comp(f)[:10])

    print("\n2. Lista de tuplas con el nombre y el año de los juegos.\n",
          second_list_comp(f)[:10])

    print(
        "\n3. Lista de tuplas con el nombre, el año y la plataforma de los juegos.\n",
        third_list_comp(f)[:10])

    print((
        "\n4. Lista de tuplas que esten compuestas por las columnas Name y Avg_Sales\n"
        "la cual se obtiene del promedio de las columnas: "
        " NA_Sales, EU_Sales, JP_Sales, Other_Sales y Global_Sales.\n"),
          fourth_list_comp(f)[:10])

    print((
        "\n5. Lista de listas con todos lo registros del archivo donde los juegos\n"
        "sean del año 2006 y su rango sea menor a 2000.\n"),
          fifth_list_comp(f)[:10])


if __name__ == "__main__":
    run()