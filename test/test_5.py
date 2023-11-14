from src.Ejercicio5 import *

def test_numerosPares():
    assert numerosPares({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}) == {0, 2, 4, 6, 8, 10}

def test_multiplo3():
    assert multiplo3({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}) == {3, 6, 9}

def test_interseccion():
    assert intersecion({0, 2, 4, 6, 8, 10},{3, 6, 9}) == {6}