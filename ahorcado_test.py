import pytest
from ahorcado import arriesgoPalabra,arriesgoLetra,descuentaVida


## Test de Funcionalidad Arriesgar Palabra

def test_arriesgo_palabra_y_acierto():
    palabra = arriesgoPalabra("python")
    assert palabra == True
    
def test_arriesgo_palabra_y__no_acierto():
    palabra = arriesgoPalabra("javascript")
    assert palabra == False


## Test de Funcionalidad Arriesgar Letra

def test_arriesgo_letra_y_acierto():
    letra = arriesgoLetra("y")
    assert letra == True

def test_arriesgo_letra_y_no_acierto():
    letra = arriesgoLetra("z")
    assert letra == False

def test_arriesgo_letra_repetida():
    global letras_acertadas, letras_intentadas
    letras_acertadas.clear()
    letras_intentadas.clear()

    # Primer intento con "p"
    resultado1 = arriesgoLetra("p")
    assert resultado1 == True

    # Segundo intento con la misma "p"
    resultado2 = arriesgoLetra("p")
    assert resultado2 == "repetida"   # no debería descontar ni modificar nada


## Test de Funcionalidad de Vidas

def test_no_acierto_descuenta_vida():
    vida = descuentaVida(arriesgoLetra("z"))
    assert vida == -1


