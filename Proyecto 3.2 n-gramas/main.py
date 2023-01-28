#Sirve para quitar los numeros iniciales y el igual, para solo dejar las palabras
def change(element): 
    separador = 2
    for n,e in enumerate(element): 
        if e  == "=":
            separador = n+ 1
            break
    element[0] = element[0][separador:]
    return element

#la funcion que genera un iterable que tiene separadas las palabras dependiendo del tamaño del grama n
def separar(linea,secuencia):
    if secuencia > len(linea):
        print("Es mas grande tamaño del grama n que el tamaño de la linea")
        return ["no hay tamaño suficiente"]
    else:
        lineaNueva = []
        for i in range(0,len(linea)-secuencia+1,1):
            lineaNueva.append(linea[i:i+secuencia])
        return lineaNueva

def ordenar(line,secuencia):
    words = change(line.strip().split(','))
    linea_separada = separar(words,secuencia)
    #--------->Continuar aqui, se tiene una lista, la lista ya tiene separados los n gramas a partir de ella se puede hacer el conteo de frecuencia
    return linea_separada

#Lee el archivo txt , toma cada palabra separada por comas las guarda en una lista y esa lista en una lista principal, en pocas palabras una lista que tiene cada linea en otra lista
def leerArchivo(nombre,secuencia):
    with open('Proyecto 3.2 n-gramas\Ejemplo.txt', 'r') as file:
        lines = file.readlines()
        listas_separadas = (ordenar(line,secuencia) for line in lines)
        #en aqui se envian todos los ngramas en iterables, se puede cambiar para que solo entregue las frecuencias, cambiando el return de arriba
        print(next(listas_separadas))

#---------------------En caso de quererse meter a un main dejar como variable global la secuencia para que pueda ser ocupada en las funcines del map


nombre_archivo = input("Ingresa el nombre del archivo: ")
secuencia = int(input("Ingresa el  el tamaño del grama n a utilizar: "))
#umbral
#nombre_archivo_sal = input("Ingresa el nombre del archivo saliente: ")
leerArchivo(nombre_archivo,secuencia)

