'''
Dadas las siguientes listas:

frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]
Crea conjuntos a partir de estas listas y nómbralos set_frutas1 y set_frutas2.
Encuentra las frutas que están en ambas listas y guárdalas en un nuevo conjunto llamado frutas_comunes.
Encuentra las frutas que están en frutas1 pero no en frutas2 y guárdalas en un conjunto llamado frutas_solo_en_frutas1.
Encuentra las frutas que están en frutas2 pero no en frutas1 y guárdalas en un conjunto llamado frutas_solo_en_frutas2.
'''

def crearConjunto1(frutas1):
    set_frutas1 = set(frutas1)
    return set_frutas1

def crearConjunto2(frutas2):
    set_frutas2 = set(frutas2)
    return set_frutas2

def inter(set_frutas1, set_frutas2):
    resultado = set_frutas1 & set_frutas2
    return resultado

def solo_en_frutas1(set_frutas1, set_frutas2):
    resultado = set_frutas1 - set_frutas2
    return resultado

def solo_en_frutas2(set_frutas1, set_frutas2):
    resultado = set_frutas2 - set_frutas1
    return resultado







if __name__ == "__main__":
    #Entrada
    frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]
    #Proceso
    set_frutas1 = crearConjunto1(frutas1)
    set_frutas2 = crearConjunto2(frutas2)
    frutas_comunes = inter(set_frutas1, set_frutas2)
    frutas_solo_en_frutas1 = solo_en_frutas1(set_frutas1, set_frutas2)
    frutas_solo_en_frutas2 = solo_en_frutas2(set_frutas1, set_frutas2)
    #Salida
    print(frutas_comunes)
    print(frutas_solo_en_frutas1)
    print(frutas_solo_en_frutas2)

    
