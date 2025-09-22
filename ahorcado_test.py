import pytest
from ahorcado import arriesgoPalabra,arriesgoLetra,descuentaVida,letras_acertadas, letras_intentadas, mostrarProgreso,gano,mostrarResultado


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
    letras_acertadas.clear()
    letras_intentadas.clear()

    # Primer intento con "p"
    resultado1 = arriesgoLetra("p")
    assert resultado1 == True

    # Segundo intento con la misma "p"
    resultado2 = arriesgoLetra("p")
    assert resultado2 == "repetida"  

## Test de Funcionalidad de Vidas

def test_no_acierto_descuenta_vida():
    vida = descuentaVida(arriesgoLetra("z"))
    assert vida == -1

def test_acierto_no_descuenta_vida():
    acierto = arriesgoLetra("p")  
    vida = descuentaVida(acierto)
    assert vida == 0

## Test de Funcionalidad Mostrar Progreso de la Palabra

def test_arriesgo_letra_correcta_y_la_muestra():
    # Reiniciamos el estado
    letras_acertadas.clear()
    letras_intentadas.clear()

    # Intentamos la letra "p"
    arriesgoLetra("p")

    # Pedimos el progreso
    progreso = mostrarProgreso("python")

    assert progreso == "p _ _ _ _ _"

def test_arriesgo_letra_incorrecta_y_no_la_muestra():
    # Reiniciamos el estado
    letras_acertadas.clear()
    letras_intentadas.clear()

    # Intentamos una letra que no está en "python"
    arriesgoLetra("z")

    # Pedimos el progreso
    progreso = mostrarProgreso("python")

    assert progreso == "_ _ _ _ _ _"

## Test Ganar o Perder el Juego

def test_gano_y_muestra_que_gane():
    # Reiniciamos el estado
    letras_acertadas.clear()
    letras_intentadas.clear()

    # Simulamos haber acertado todas las letras de la palabra "python"
    for ch in set("python"):
        letras_acertadas.add(ch)

    # El progreso debe mostrar la palabra completa
    assert mostrarProgreso("python") == "p y t h o n"

    assert gano("python") == True
    assert mostrarResultado("python") == "¡Ganaste!"

def test_pierdo_y_muestra_que_perdi():
    # Reiniciamos el estado
    letras_acertadas.clear()
    letras_intentadas.clear()

    # Simulamos que el jugador perdió todas las vidas
    vidas_restantes = 0

    # Aún no implementamos perdio() ni mostrarResultado para derrota
    assert perdio(vidas_restantes) == True
    assert mostrarResultado("python", vidas_restantes) == "¡Perdiste!"