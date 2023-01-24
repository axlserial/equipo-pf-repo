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
    dir_csv = './vgsales.csv'
    for i in lc.actividades(dir_csv):
        print(i)

if __name__ == '__main__':
    main()