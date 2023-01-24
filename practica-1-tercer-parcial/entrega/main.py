from utils import all_registers
from pprint import pprint
import list_comp as lc

def main():

    # List Comprehensions
    print(
        "-------------------- List Comprehensions --------------------------\n"
    )
    print_list()
    print(
        "\n-------------------------------------------------------------------"
    )



# ------------------ list Comps ----------------


def print_list() -> None:
    dir_csv = "./practica-1-tercer-parcial/entrega/vgsales.csv"
    for i in lc.actividades(dir_csv):
        print(i[:3])

if __name__ == '__main__':
    main()