from src.Ejercicio6  import consonantes, conjunto

def test_consonantes():
    assert consonantes({'a', 'e', 'i', 'o', 'u'}, {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z'}) == {'j', 'g', 'z', 'y', 'r', 'q', 't', 'l', 'w', 'b', 'p', 'd', 'ñ', 'x', 'v', 'h', 'f', 'm', 's', 'n', 'c', 'k'}

def test_conjunto():
    assert conjunto({'a', 'e', 'i', 'o', 'u'}, {'j', 'g', 'z', 'y', 'r', 'q', 't', 'l', 'w', 'b', 'p', 'd', 'ñ', 'x', 'v', 'h', 'f', 'm', 's', 'n', 'c', 'k'}) == set()