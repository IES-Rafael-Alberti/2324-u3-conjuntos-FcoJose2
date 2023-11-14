'''
Ejercicio 3.3.3¶
El conjunto potencia de un conjunto S es el conjunto de todos los subconjuntos de S.

Por ejemplo, el conjunto potencia de {1,2,3} es:

{∅,{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}}
Escriba la función conjunto_potencia(s) que reciba como parámetro un conjunto cualquiera s y retorne su «lista potencia» (la lista de todos sus subconjuntos):

conjunto_potencia({6, 1, 4})
[set(), set([6]), set([1]), set([4]), set([6, 1]), set([6, 4]), set([1, 4]), set([6, 1, 4])]
'''

def obtener_domicilios_facturas(compras):
    domicilios_facturas = set()
    clientes_domicilios = {}

    for compra in compras:
        cliente, dia_del_mes, monto, domicilio = compra

        if cliente not in clientes_domicilios:
            clientes_domicilios[cliente] = set()

        clientes_domicilios[cliente].add(domicilio)

    for domicilios in clientes_domicilios.values():
        domicilios_facturas.update(domicilios)

    return list(domicilios_facturas)

if __name__ == "__main__":

    #entrada
    compras = [
    ("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),
    ("Jorge Russo", 7, 699, "Mirasol 218"),
    ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"),
    ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"),
    ("Jorge Russo", 15, 958, "Mirasol 218")
    ]

    #proceso
    domicilios_para_facturas = obtener_domicilios_facturas(compras)

    #salida
    print(domicilios_para_facturas)
