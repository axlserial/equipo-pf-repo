from typing import Callable
import csv

def actividades(csvName) -> Callable:
    #-------------Primera accion del generador (Crear la lista de diccionarios de los juegos)--------------#

    lista = []
    with open(csvName) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            lista.append(row)

    print("-----------Lista Generada--------")
    yield lista


    #----------Actividad, de la lista extraida(del csv) solo dejar el diccionario con nombre, rango, plataforma, año, género---------#

    #Funcion que recibe un diccionario y regresa solo algunos elementos del mismo
    def quitarElementos(diccionario):
        return {'Rank':diccionario['Rank'], 'Name':diccionario['Name'],'Platform':diccionario['Platform'],'Genre':diccionario['Genre'],'Year':diccionario['Year']}

    print("-----------Actividad 1, quitar informacion--------")
    yield map(quitarElementos,lista)

    #----------Actividad, de la lista extraida(del csv) solo dejar los juegos de plataforma Wii

    print("-----------Actividad 2, dejar solo plataforma Wii--------")

    yield filter(lambda x : x['Platform'] == 'Wii',lista)

    #----------Actividad, de la lista extraida(del csv) filtrar por el año 2006 y solo mostrar el rango, el nombre y su género

    print("-----------Actividad 3, Filtrar por año 2006 y mostrar nombre,rango,genero--------")

    yield map(lambda x : {'Rank':x['Rank'],'Name':x['Name'],'Genre':x['Genre']},filter(lambda x : x['Year'] == '2006',lista))

    #----------Actividad, de la lista extraida(del csv) usar Generator comprehensions para tomar todos los juegos publicados por nintendo y sacar el promedio de Sales

    print("-----------Actividad 4, tomar juegos publicados por nintendo y sacar promedio de sus Sales")
    
    def sumaT(x):
        return float(x['NA_Sales']) + float(x['EU_Sales']) + float(x['JP_Sales']) + float(x['Other_Sales']) + float(x['Global_Sales'])

    yield ({'Name':i['Name'], 'Publisher':i['Publisher'] , 'Platform':['Platform'] , 'Sales' : round(sumaT(i)/5,2) } for i in lista if i['Publisher'] == 'Nintendo')

    #----------Actividad, de la lista extraida(del csv) con un generador ordenar los juegos por año de salida pero que se presenten del mas actual al mas viejo (filtrar los que no tengan año N/A ), que se muestre año, nombre y rango.

    print("-----------Actividad 5, Ordenar por año del mas nuevo al mas viejo mostrando  año, nombre y rango")

    yield ( {'Year':i['Year'] , 'Name':i['Name'] , 'Rank':i['Rank']} for i in reversed(sorted( filter( lambda x : x['Year'] != 'N/A' and x['Year'] != 'Adventure',lista), key = lambda x : x['Year'])) )