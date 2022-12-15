from typing import Callable
from statistics import mean
from utils import all_registers

def generarLista(h: tuple,data:tuple)-> list:
    listaJuegos = []
    for row in data:
            iterador = zip(h,row)
            listaJuegos.append(tuple(iterador))
    
    return listaJuegos

# Lista con los nombres de los juegos
def  letra_nombres(lista : tuple[str, ...]) -> Callable:
    def lista_tupla(letra_inicial : str):
        listaNombres = [name[1] for name in lista if name[1][1][0].lower() == letra_inicial.lower() ]
        print(listaNombres[:5])
    
    return lista_tupla



# Lista de tuplas con el nombre y el año de los juegos
def second_list_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=',')
        h = next(games)

        list_games = [(game[h.index("Name")], game[h.index("Year")]) for game in games]

        return list_games


# Lista de tuplas con el nombre, el año y la plataforma de los juegos
def third_list_comp(name_file: str):
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=',')
        h = next(games)

        list_games = [(game[h.index("Name")], game[h.index("Year")], game[h.index("Platform")]) for game in games]

        return list_games


# Lista de tuplas que esten compuestas por
# las columnas Name y Avg_Sales la cual se obtiene
# del promedio de las columnas NA_Sales, EU_Sales, JP_Sales, Other_Sales y Global_Sales
def fourth_list_comp(name_file: str):
    sales = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']

    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=',')
        h = list(next(games))

        list_games  =  [(game[h.index("Name")], mean([float(game[h.index(k)]) for k in sales])) for game in games]

        return list_games


# Lista de listas con todos lo registros del archivo
# donde los juegos sean del año 2006 y su rango sea menor a 2000
def fifth_list_comp(name_file: str):
    with open(name_file) as csvfile:

        games = csv.reader(csvfile, delimiter=',')
        h = next(games)
        list_games = [ game for game in games if game[h.index("Year")] == "2016" and float(game[h.index("Rank")]) < 2000 ]

        return list_games


def run():
    h, data = all_registers('./vgsales.csv')
    lista = generarLista(h,data)

    first_list = letra_nombres(lista)
    first_list("w")
    first_list("b")

    
    #print("\n2. Lista de tuplas con el nombre y el año de los juegos.\n", second_list_comp(f)[:10])

    #print(
    #    "\n3. Lista de tuplas con el nombre, el año y la plataforma de los juegos.\n",
    #    third_list_comp(f)[:10])

    #print((
    #    "\n4. Lista de tuplas que esten compuestas por las columnas Name y Avg_Sales\n"
    #    "la cual se obtiene del promedio de las columnas: "
    #    " NA_Sales, EU_Sales, JP_Sales, Other_Sales y Global_Sales.\n"),
    #    fourth_list_comp(f)[:10])

    #print((
    #    "\n5. Lista de listas con todos lo registros del archivo donde los juegos\n"
    #    "sean del año 2006 y su rango sea menor a 2000.\n"),
    #    fifth_list_comp(f)[:10])


if __name__ == "__main__":
    run()