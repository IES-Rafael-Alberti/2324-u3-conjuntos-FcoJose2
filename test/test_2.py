from src.Ejercicio2 import *

def test_sinRepetir():
    assert sinRepetir({"Jose", "Juan", "Lolo"},{"Pepe", "Juan","Dani"}) == {'Dani', 'Jose', 'Juan', 'Lolo', 'Pepe'}

def test_repetidos():
    assert repetidos({"Jose", "Juan", "Lolo"},{"Pepe", "Juan","Dani"}) == {'Juan'}
    assert repetidos({"Jose", "Juan", "Lolo"},{"Pepe", "Julian","Dani"}) == "Ninguno"

def test_primNoRepetSecun():
    assert primNoRepetSecun({"Jose", "Juan", "Lolo"},{"Pepe", "Juan","Dani"}) == {'Jose', 'Lolo'}
    assert primNoRepetSecun({"Juan"},{"Pepe", "Juan","Dani"}) == "Ninguno"

def test_primIncluidos():
    assert primIncluidos({"Jose", "Juan", "Lolo"},{"Pepe", "Juan","Dani"}) == "No están incluidos"
    assert primIncluidos({"Jose", "Juan"},{"Jose", "Juan","Dani","Keria"}) == "Todos están incluidos"