'''
Dado el conjunto de letras:

vocales = {'a', 'e', 'i', 'o', 'u'}
Crea un conjunto consonantes que contenga las letras del alfabeto que no son vocales.
Crea un conjunto letras_comunes que contenga las letras que están tanto en el conjunto vocales como en el conjunto consonantes.
'''
def consonantes(vocales, alfabeto):
    resultado = alfabeto - vocales
    return resultado

def conjunto(vocales, consonantesVar):
    resultado = vocales & consonantesVar
    return resultado






if __name__ == "__main__":
    #Entrada
    vocales = {'a', 'e', 'i', 'o', 'u'}
    alfabeto = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z'}
    #Proceso
    consonantesVar = consonantes(vocales, alfabeto)
    interseccion = conjunto(vocales,consonantesVar)
    #Salida
    print(consonantesVar)
    print(interseccion)