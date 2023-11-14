'''
Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de una escuela, finalizando cuando se introduzca “x”. A continuación, solicitar que introduzca los nombres de los alumnos de secundaria, finalizando al introducir “x”.

Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
Mostrar si todos los nombres de primaria están incluidos en secundaria.
'''

def sinRepetir(primaria, secundaria):
    resultado = primaria | secundaria
    return resultado

def repetidos(primaria, secundaria):
    resultado = primaria & secundaria
    if resultado == set():
        mensaje = "Ninguno"
    else:
        mensaje = resultado
    return mensaje

def primNoRepetSecun(primaria, secundaria):
    resultado = primaria - secundaria
    if resultado == set():
        mensaje = "Ninguno"
    else:
        mensaje = resultado
    return mensaje

def primIncluidos(primaria, secundaria):
    resultado = primaria <= secundaria
    if resultado == True:
        resultado = "Todos están incluidos"
    else:
        resultado = "No están incluidos"
    return resultado


if __name__ == "__main__":
    #Entrada
    primaria = []
    primaria = set(primaria)
    secundaria = []
    secundaria = set(secundaria)
    interrutorPrimaria = True
    interrutorSecundaria = True
    while interrutorPrimaria == True:
        addprimaria = input("Introduce un alumno de primaria(Introduce 'x' para salir): ")
        if addprimaria == "" or addprimaria == " ":
            primaria.pop()
        elif addprimaria != "x":
            primaria.add(addprimaria)
        else:
            interrutorPrimaria = False
    while interrutorSecundaria == True:
        addsecundaria = input("Introduce un alumno de secundaria(Introduce 'x' para salir): ")
        if addsecundaria == "" or addsecundaria == " ":
            secundaria.pop()
        if addsecundaria != "x":
            secundaria.add(addsecundaria)
        else:
            interrutorSecundaria = False
    #Proceso
    nombresSinRepe = sinRepetir(primaria, secundaria)
    nombresRepe = repetidos(primaria, secundaria)
    unicosPrimaria = primNoRepetSecun(primaria, secundaria)
    if unicosPrimaria == set():
        unicosPrimaria = "Ninguno"
    primariaIncluida = primIncluidos(primaria, secundaria)
    #Salida
    print(nombresSinRepe)
    print(nombresRepe)
    print(unicosPrimaria)
    print(primariaIncluida)
