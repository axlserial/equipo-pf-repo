from typing import Callable

def generarLista(h: tuple,data:tuple)-> list:
    listaJuegos = []
    for row in data:
            iterador = zip(h,row)
            listaJuegos.append(tuple(iterador))
    
    return listaJuegos

def promedio(precios : str) -> float:
    prom : float = 0.0
    for i in precios :
        prom = prom + float(i[1])

    return round((prom / 5),2)


def  lista_tupla(lista : list, actividad : int) -> Callable:
    
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

    else:
        return generos
