from typing import Callable
import csv

def promedio(precios: str) -> float:
    prom: float = 0.0
    for i in precios:
        prom = prom + float(i[1])

    return round((prom / 5), 2)


def quitarElementos(diccionario):
    return {'Rank':diccionario['Rank'], 'Name':diccionario['Name'],'Platform':diccionario['Platform'],'Genre':diccionario['Genre'],'Year':diccionario['Year']}


def actividades(csvName) -> Callable:
    #-------------Primera accion del generador (Crear la lista de diccionarios de los juegos)--------------#

    lista = []
    with open(csvName) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            lista.append(row)

    print("-----------Lista Generada--------")
    yield lista


    #----------Primera actividad, de la lista extraida solo dejar el diccionario con nombre, rango, plataforma, añoa, género---------#

    listaFiltrada = map(quitarElementos,lista)

    print("-----------Lista Filtrada--------")
    yield list(listaFiltrada)

