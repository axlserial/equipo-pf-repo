import csv

f = './vgsales.csv'


def all_registers(name_file: str)-> tuple[tuple[str,...],...]:
    '''Devuelve una tupla de tuplas con todos los registros y todas las columnas del archivo vgsales.csv'''
    
    with open(name_file) as csvfile:
        games = csv.reader(csvfile, delimiter=',')
        h = next(games)

        tuple_games = tuple(tuple(game) for game in games)

        return tuple_games


def main():
    datos = all_registers(f)
    

if __name__ == '__main__':
    main()