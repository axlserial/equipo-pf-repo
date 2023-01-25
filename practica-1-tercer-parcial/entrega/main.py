from utils import all_registers
from pprint import pprint
import list_comp as lc

def main():

    # List 
    print(
        "-------------------- List  --------------------------\n"
    )
    print_list()
    print(
        "\n-------------------------------------------------------------------"
    )



# ------------------ list Comps ----------------


def print_list() -> None:
    dir_csv = "./practica-1-tercer-parcial/entrega/vgsales.csv"
    
    #Ciclo que sirve como iteradores encadenados y nos muestra las 5 actividades, genera una lista del CSV y musestra las 5 actividades puestas en el modulo List_comp.py
    for i in lc.actividades(dir_csv):

        #Comprueba que sea un iterador (Object)
        if (isinstance(i,object) ):
            for j,k in enumerate(i): 
                #Usando enumerate vamos a verificar que solo 3 se impriman, esto para no imprimir muchos juegos y puedan diferenciarse las actividades
                if j == 3:
                    print(k)
                    break
                print(k)

        # si no es un iterador es un iterable o lista
        else:
            print(i[:4])

if __name__ == '__main__':
    main()