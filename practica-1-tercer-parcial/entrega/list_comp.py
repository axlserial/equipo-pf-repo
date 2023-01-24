from typing import Callable
import csv

def promedio(precios: str) -> float:
    prom: float = 0.0
    for i in precios:
        prom = prom + float(i[1])

    return round((prom / 5), 2)


def actividades(csvName) -> Callable:
    #-------------Primera accion del generador (Crear la lista de juegos)--------------#
    print(csvName)
    lista = []
    with open(csvName, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            lista.append(row)


    yield lista