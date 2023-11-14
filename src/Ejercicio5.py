'''
Dado el conjunto de números enteros:

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
Crea un conjunto pares que contenga los números pares del conjunto numeros.
Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos de tres del conjunto numeros.
Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y guárdala en un conjunto llamado pares_y_multiplos_de_tres.
'''

def numerosPares(numeros):
    pares = {}
    pares = set(pares)
    for x in range(0, len(numeros)+1, 2):
        pares.add(x)
    return pares

def multiplo3(numeros):
    multiplosDe3 = {}
    multiplosDe3  = set(multiplosDe3)
    for x in range(1,len(numeros)+1):
        if x % 3 == 0:
            multiplosDe3.add(x)
    return multiplosDe3

def intersecion(pares, multiplosDe3):
    pares_y_multiplos_de_tres = pares & multiplosDe3
    return pares_y_multiplos_de_tres







if __name__ == "__main__":
    #Entrada
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    #Proceso
    pares = numerosPares(numeros)
    multiplosDe3 = multiplo3(numeros)
    pares_y_multiplos_de_tres = intersecion(pares, multiplosDe3)
    #Salida
    print(pares)
    print(multiplosDe3)
    print(pares_y_multiplos_de_tres)