from typing import Callable
from statistics import mean
from utils import all_registers


def generarLista(h: tuple,data:tuple)-> list:
    listaJuegos = []
    for row in data:
            iterador = zip(h,row)
            listaJuegos.append(tuple(iterador))
    
    return listaJuegos

def promedio(precios : str) -> float:
    prom = 0
    for i in precios :
        prom = prom + float(i[1])

    return round((prom / 5),2)


# Lista con los nombres de los juegos #1
def  lista_tupla(lista : tuple[str, ...], actividad : int) -> Callable:
    
    #--------------------1-----------------------#
    def letra_nombres(letra_inicial : str):
        listaNombres = [name[1] for name in lista if name[1][1][0].lower() == letra_inicial.lower() ]
        print(listaNombres[:5])
    
    #--------------------2-----------------------#
    def año_juegos(año : str):
        print([(name[1],name[3]) for name in lista if name[3][1] == año][:2])

    #--------------------3-----------------------#
    def plataforma(plataform : str,ordenar : str):
        listaPlatf = [(name[1],name[2],name[3]) for name in lista if name[2][1].lower() == plataform.lower()]
        
        if ordenar == "nombre":
            listaPlatf.sort(key= lambda x : x[0])
            print(listaPlatf[:10])

        elif ordenar  == "plataforma":
            listaPlatf.sort(key= lambda x : x[1])
            print(listaPlatf[:10])

        elif ordenar == "año":
            listaPlatf.sort(key= lambda x : x[2])
            print(listaPlatf[:10])

    #--------------------4-----------------------#
    def ventas(orden : str):
        listaProm = [ (name[1], ("Avg_Sales",promedio(name[6:10]))) for name in lista]
        
        listt = sorted(listaProm[:7],key = lambda x : x[1][1])
        if orden == "ascendentes":
            print(listt[:10])
        elif orden == "descendentes":
            listt.reverse()
            print(listt[:10])

    #--------------------5-----------------------#
    def generos(año : str):
        listaPlatf = [(name[0],name[1],name[4]) for name in lista if name[3][1] == año]
        listt = sorted(listaPlatf[:10],key = lambda x : int(x[0][1]))
        print(listt)

    if actividad == 1:
        return letra_nombres
    
    elif actividad == 2:
        return año_juegos

    elif actividad == 3:
        return plataforma

    elif actividad == 4:
        return ventas

    elif actividad == 5:
        return generos

def run():
    h, data = all_registers('./vgsales.csv')
    lista = generarLista(h,data)

    print("\n #------1.- listas de tuplas con nombres con una letra inicial seleccionada------#\n")
    main_list = lista_tupla(lista,1)
    main_list("w")
    print()
    main_list("b")
    print("\n #------2.- lista de tuplas con nombre y con un año seleccionado------#\n")
    main_list = lista_tupla(lista,2)
    main_list("2006")
    print()
    main_list("2000")
    print("\n #------3.- lista de tuplas con nombre, año y plataforma seleccionada------#\n")
    main_list = lista_tupla(lista,3)
    main_list("wii","nombre")
    print()
    main_list("pc","nombre")
    print("\n #------4.- lista de tuplas con nombre y promedio de las ventas, ordenadas asc o desc------#\n")
    main_list = lista_tupla(lista,4)
    main_list("ascendentes")
    print()
    main_list("descendentes")
    print("\n #------5.- lista con rango, nombre y género a partir del año dado y ordenado por rango ------#\n")
    main_list = lista_tupla(lista,5)
    main_list("2009")
    print()
    main_list("2012")


if __name__ == "__main__":
    run()