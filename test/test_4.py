from src.Ejercicio4 import *

def test_crearConjunto1():
    assert crearConjunto1(["manzana", "pera", "naranja", "plátano", "uva"]) == {'manzana', 'naranja', 'pera', 'plátano', 'uva'}

def test_crearConjunto2():
    assert crearConjunto2(["manzana", "pera", "durazno", "sandía", "uva"]) == {'durazno', 'manzana', 'pera', 'sandía', 'uva'}

def test_inter():
    assert inter({'manzana', 'naranja', 'pera', 'plátano', 'uva'}, {'durazno', 'manzana', 'pera', 'sandía', 'uva'}) == {'manzana', 'pera', 'uva'}

def test_solo_en_frutas1():
    assert solo_en_frutas1({'manzana', 'naranja', 'pera', 'plátano', 'uva'}, {'durazno', 'manzana', 'pera', 'sandía', 'uva'}) == {'naranja', 'plátano'}

def test_solo_en_frutas2():
    assert solo_en_frutas2({'manzana', 'naranja', 'pera', 'plátano', 'uva'}, {'durazno', 'manzana', 'pera', 'sandía', 'uva'}) == {'durazno', 'sandía'}