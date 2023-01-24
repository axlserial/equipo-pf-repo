
#----------------------------------------------

#------------------ Sets  ----------------

# Conjunto de los nombres de las plataformas
def first_set(data: tuple[tuple[str, ...], ...], h: tuple[str, ...]) -> set[str]:
    names = set(map(lambda x: x[h.index("Platform")], data))
    return names


# Conjunto de todos los registros donde sus elementos
# sean la tupla 'Name' y 'Global_Sales' de los juegos
def second_set(data: tuple[tuple[str, ...], ...], h: tuple[str, ...]) -> set[tuple[str, str]]:
    get_data = set(map(lambda x: (x[h.index("Name")], x[h.index("Global_Sales")]), data))
    return get_data


# Conjunto de todos los registros donde sus elementos
# sean la tupla 'Name' y 'NA_Sales' de los juegos
# que hayan vendido más de 5.0 millones en NA
def third_set(data: tuple[tuple[str, ...], ...], h: tuple[str, ...]) -> set[tuple[str, str]]:
    keys = ('Name', 'NA_Sales')
    get_data = set(filter(lambda x: x[keys.index('NA_Sales')] > 5.0, map(lambda x: (x[h.index("Name")], float(x[h.index("NA_Sales")])), data)))
    return get_data


# Conjunto de tuplas con las columnas: 'Name' y 'Global_Sales'
# de juegos donde su 'Publisher' sea Sega, su 'Platform' sea 3DS
# y que contengan la palabra Sonic.
def fourth_set(data: tuple[tuple[str, ...], ...], h: tuple[str, ...]) -> set[tuple[str, str]]:
    # keys = ['Name', 'Global_Sales']
    get_data = filter(lambda x: x[h.index('Publisher')] == "Sega" and x[h.index('Platform')] == "3DS" and x[h.index('Name')].find('Sonic') != -1,
                      data)
    get_filData = set(map(lambda x: (x[h.index('Name')], x[h.index('Global_Sales')]), get_data))
    
    return get_filData
      
      
# Conjunto de los nombres de los 'Publisher' que poseen juegos
# del genero 'Platform' cuyo lanzamiento esté entre los años 2013 y 2016.
def fifth_set(data: tuple[tuple[str, ...], ...], h: tuple[str, ...]) -> set[str]:
    get_data = filter(lambda x: x[h.index('Genre')] == 'Platform' and x[h.index('Year')] >= '2013' and x[h.index('Year')] <= '2016', data)
    get_filData = set(map(lambda x: x[h.index('Publisher')], get_data))    
    return get_filData


#----------------------------------------------

#------------------ Set Operations ----------------


# Conjunto de tuplas con las columnas: Name y Global_Sales
# de juegos que su plublisher sea Sega y su plataforma 3DS.
def conjunto_p(data: tuple[tuple[str, ...], ...], h: tuple[str, ...]) -> set[tuple[str, str]]:
    get_data = filter(lambda x: x[h.index('Publisher')] == "Sega" and x[h.index('Platform')] == "3DS",data)
    get_filData = set(map(lambda x: (x[h.index('Name')], x[h.index('Global_Sales')]), get_data))
    
    return get_filData


# Conjunto de los nombres de las plataformas que tengan juegos del genero Action
def conjunto_q(data: tuple[tuple[str, ...], ...], h: tuple[str,...]) -> set[str]:
    get_data = filter(lambda x: x[h.index('Genre')] == 'Action', data)
    get_filData = set(map(lambda x: x[h.index('Platform')], get_data))
    return get_filData


# Conjunto de todos los registros que sus elementos
# sean la tupla "Name" y "NA_Sales" de los juegos
# que hayan vendido más de 4.0 millones en NA
def conjunto_u(data: tuple[tuple[str, ...], ...], h: tuple[str, ...]) -> set[tuple[str, str]]:
    keys = ('Name', 'NA_Sales')
    get_data = set(filter(lambda x: x[keys.index('NA_Sales')] > 4.0, map(lambda x: (x[h.index("Name")], float(x[h.index("NA_Sales")])), data)))
    return get_data