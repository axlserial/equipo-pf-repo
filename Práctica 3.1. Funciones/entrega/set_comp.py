from typing import Callable
import utils as u

#------------------ Closures ------------------

# Closure para filtrar una tupla de tuplas por columnas y valores.
def filter_columns(columns: list[str], values: list, h: tuple[str, ...]) -> Callable:

    def inner(data: tuple) -> tuple:
        return tuple([d for d in data if all([d[h.index(c)] == v for c, v in zip(columns, values)])])

    return inner


# Closure para filtrar una tupla de tuplas por una columna y un rango de valores.
def filter_column_range(column: str, value1, value2, h: tuple[str, ...]) -> Callable:
    def inner(data: tuple) -> tuple:
        return tuple([d for d in data if value1 <= d[h.index(column)] <= value2])
    
    return inner


# Closure para filtrar una tupla de tuplas por una columna y valores mayores a un valor dado.
def filter_column_nums(column: str, value,h: tuple[str, ...]) -> Callable:
    
    def inner(data: tuple) -> tuple:  
        return tuple([d for d in data if float(d[h.index(column)]) > float(value)])

    return inner


# Closure para encontrar una subcadena en una columna de una tupla.
def find_substring(column: str, substring: str, h: tuple[str, ...]) -> Callable:
    
    def inner(data: tuple) -> tuple:
        return tuple([d for d in data if d[h.index(column)].find(substring) != -1])
    
    return inner

#----------------------------------------------


#------------------ Set Comps ----------------


# Conjunto de los nombres de las plataformas
def first_set_comp(data: tuple[tuple[str, ...], ...], h: tuple[str, ...]) -> set[str]:
    get_platform = u.select_column("Platform", h)
    platforms = {get_platform(game) for game in data}
    return platforms


# Conjunto de todos los registros donde sus elementos
# sean la tupla 'Name' y 'Global_Sales' de los juegos
def second_set_comp(data: tuple[tuple[str, ...], ...], h: tuple[str, ...]) -> set[tuple[str, str]]:
    get_name = u.select_column("Name", h)
    get_global_sales = u.select_column("Global_Sales", h)
    games = {(get_name(game), get_global_sales(game)) for game in data}
    return games


# Conjunto de todos los registros donde sus elementos
# sean la tupla 'Name' y 'NA_Sales' de los juegos
# que hayan vendido más de 5.0 millones en NA
def third_set_comp(data: tuple[tuple[str, ...], ...], h: tuple[str, ...]) -> set[tuple[str, str]]:
    get_name = u.select_column("Name", h)
    get_na_sales = u.select_column("NA_Sales", h)
    get_filter = filter_column_nums("NA_Sales", "5.0", h)
    games = {(get_name(game), get_na_sales(game)) for game in get_filter(data)}
    return games


# Conjunto de tuplas con las columnas: 'Name' y 'Global_Sales'
# de juegos donde su 'Publisher' sea Sega, su 'Platform' sea 3DS
# y que contengan la palabra Sonic.
def fourth_set_comp(data: tuple[tuple[str, ...], ...], h: tuple[str, ...]) -> set[tuple[str, str]]:
    get_name = u.select_column("Name", h)
    get_global_sales = u.select_column("Global_Sales", h)
    get_filters = filter_columns(["Publisher", "Platform"], ["Sega", "3DS"], h)
    get_substring_Sonic = find_substring("Name", "Sonic", h)
    
    games = {(get_name(game), get_global_sales(game)) for game in get_substring_Sonic(get_filters(data))}
    

    return games
    

# Conjunto de los nombres de los 'Publisher' que poseen juegos
# del genero 'Platform' cuyo lanzamiento esté entre los años 2013 y 2016.
def fifth_set_comp(data: tuple[tuple[str, ...], ...], h: tuple[str, ...]) -> set[str]:
    get_publisher = u.select_column("Publisher", h)
    get_filter_Platform = u.filter_column("Genre", "Platform", h)
    get_filter_2013_2016 = filter_column_range("Year", "2013", "2016", h)
    

    games = {get_publisher(game) for game in get_filter_2013_2016(get_filter_Platform(data))}

    return games
       
#----------------------------------------------

#------------------ Set Operations ----------------

# Conjunto de tuplas con las columnas: Name y Global_Sales
# de juegos que su plublisher sea Sega y su plataforma 3DS.

def conjunto_p(data: tuple[tuple[str, ...], ...], h: tuple[str, ...]) -> set[tuple[str, str]]:
    get_name = u.select_column("Name", h)
    get_global_sales = u.select_column("Global_Sales", h)
    get_filters = filter_columns(["Publisher", "Platform"], ["Sega", "3DS"], h)
    games = {(get_name(game), get_global_sales(game)) for game in get_filters(data)}
    return games


# Conjunto de los nombres de las plataformas que tengan juegos del genero Action
def conjunto_q(data: tuple[tuple[str, ...], ...], h: tuple[str, ...]) -> set[str]:
    get_platform = u.select_column("Platform", h)
    get_filter = u.filter_column("Genre", "Action", h)
    platforms = {get_platform(game) for game in get_filter(data)}
    return platforms


# Conjunto de todos los registros que sus elementos
# sean la tupla "Name" y "NA_Sales" de los juegos
# que hayan vendido más de 4.0 millones en NA
def conjunto_u(data: tuple[tuple[str, ...], ...], h: tuple[str, ...]) -> set[tuple[str, str]]:
    get_name = u.select_column("Name", h)
    get_na_sales = u.select_column("NA_Sales", h)
    get_filter = filter_column_nums("NA_Sales", "4.0", h)
    games = {(get_name(game), get_na_sales(game)) for game in get_filter(data)}
    return games

#--------------------------------------------------