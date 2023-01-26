from pprint import pprint
from functools import reduce
from math import sin, asin, cos, radians, sqrt

data: tuple[tuple[str,
                  str]] = (('37.54901619777347', '-76.33029518659048'),
                           ('37.840832', '-76.27383399999999'), ('38.331501',
                                                                 '-76.459503'),
                           ('38.843334', '-76.298668'), ('37.549',
                                                         '-76.331169'),
                           ('38.330166', '-76.458504'), ('38.976334',
                                                         '-76.47350299999999'))


def haversine(p1: tuple[float, float], p2: tuple[float, float]):
    lat_1, lon_1 = p1
    lat_2, lon_2 = p2
    d_lat = radians(lat_2 - lat_1)
    d_lon = radians(lon_2 - lon_1)
    lat_1 = radians(lat_1)
    lat_2 = radians(lat_2)
    a = sqrt(sin(d_lat / 2)**2 + cos(lat_1) * cos(lat_2) * sin(d_lon / 2)**2)
    c = 2 * asin(a)

    return 3440 * c


# Obtención de las distancias
def inciso_a():
    gen_data = ((float(t[0]), float(t[1])) for t in data)

    first_coord = next(gen_data)
    second_coord = next(gen_data)
    initial_data = [(first_coord, second_coord,
                     haversine(first_coord, second_coord))]

    result: list[tuple[tuple[float, float], tuple[
        float, float], float]] = reduce(
            lambda anterior, punto: [
                *anterior,
                (anterior[len(anterior) - 1][1], punto,
                 haversine(anterior[len(anterior) - 1][1], punto))
            ], gen_data, initial_data)

    return result


# Obtención de la distancia mínima
def inciso_b(t_data: list[tuple[tuple[float, float], tuple[float, float],
                                float]]):

    distancias = map(lambda x: (x[2], x), t_data)

    return min(distancias, key=lambda x: x[0])


# Obtención de la distancia máxima
def inciso_c(t_data: list[tuple[tuple[float, float], tuple[float, float],
                                float]]):

    distancias = map(lambda x: (x[2], x), t_data)

    return max(distancias, key=lambda x: x[0])


def main():

    # Ejercicio 2
    in_a = inciso_a()
    print("Distancias: ")
    pprint(in_a)

    print(f'\nLa distancia mínima es: {inciso_b(in_a)[1]}')
    print(f'\nLa distancia máxima es: {inciso_c(in_a)[1]}')

    # Ejercicio 3
    convertir = map(lambda x: (x[0], x[1], x[2] * (6076.12 / 5280)), in_a)

    print("\nDistancias en millas: ")
    for d in convertir:
        print(d)


if __name__ == "__main__":
    main()