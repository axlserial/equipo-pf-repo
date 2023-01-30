from functools import reduce
from os.path import exists


#Sirve para quitar los numeros iniciales y el igual, para solo dejar las palabras
def change(element):
    separador = 2
    for n, e in enumerate(element):
        if e == "=":
            separador = n + 1
            break
    element[0] = element[0][separador:]
    return element


#la funcion que genera un iterable que tiene separadas las palabras dependiendo del tamaño del grama n
def separar(linea, secuencia):
    if secuencia > len(linea):
        return False
    else:
        lineaNueva = []
        for i in range(0, len(linea) - secuencia + 1, 1):
            lineaNueva.append(linea[i:i + secuencia])
        return lineaNueva


def ordenar(line, secuencia):
    words = change(line.strip().split(','))
    linea_separada: list[list[str]] | bool = separar(words, secuencia)
    return linea_separada


#Cuenta la frecuencia de cada n-grama
def cuenta_lista(dict_conteo: dict[str, int], lista: list[list[str]] | bool):

    # Sí la lista es vacía, regresa el diccionario sin cambios
    if not lista:
        return dict_conteo

    # Cuenta la frecuencia de cada n-grama
    for n_grama in lista:
        grama_str = ",".join(n_grama)

        if grama_str in dict_conteo:
            dict_conteo[grama_str] += 1
        else:
            dict_conteo[grama_str] = 1

    return dict_conteo


# Procesa el archivo y escribe los resultados en el archivo de salida
def procesa_archivo(nombre_archivo: str, secuencia: int, umbral: int,
                    nombre_salida: str):

    # Lee el archivo, procesa cada linea, crea las listas de n-gramas y
    # cuenta la frecuencia de cada uno
    with open(nombre_archivo, 'r') as file:
        listas_separadas = (ordenar(line, secuencia) for line in file)

        conteo = reduce(cuenta_lista, listas_separadas, {})

    # Filtra los n-gramas que no cumplen con el umbral y los ordena
    # de mayor a menor frecuencia
    resultados = sorted(filter(lambda grama: grama[1] >= umbral,
                               conteo.items()),
                        key=lambda x: x[1],
                        reverse=True)

    # Escribe los resultados en el archivo de salida
    with open(nombre_salida, 'w', encoding="utf-8") as file:
        file.write(
            f'Se encontraron {len(resultados)} gramas de tamaño {secuencia}:\n'
        )
        for grama, frecuencia in resultados:
            file.write(f'[{frecuencia}] {grama}\n')


def main():
    nombre_archivo = input("Ingresa el nombre del archivo: ")
    if not exists(nombre_archivo):
        print("El archivo no existe, ingresa un archivo valido")
        exit(1)

    secuencia = int(input("Ingresa el tamaño del grama n a utilizar: "))
    umbral = int(input("Ingresa el umbral de frecuencia: "))

    nombre_salida = input("Ingresa el nombre del archivo de salida: ")
    if not nombre_salida.endswith(".txt"):
        nombre_salida += ".txt"

    procesa_archivo(nombre_archivo, secuencia, umbral, nombre_salida)


if __name__ == '__main__':
    main()