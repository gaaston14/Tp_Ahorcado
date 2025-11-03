# ahorcado_test.py (Actualizado)
import pytest
# Importamos el módulo con la nueva lógica, ahora lo llamamos 'logica_juego'
import ahorcado as logica_juego 

## Test de Funcionalidad Arriesgar Palabra

def test_arriesgo_palabra_y_acierto():
    # Ahora pasamos la palabra secreta como argumento
    palabra = logica_juego.arriesgoPalabra("python", "python")
    assert palabra == True
    
def test_arriesgo_palabra_y_no_acierto():
    palabra = logica_juego.arriesgoPalabra("javascript", "python")
    assert palabra == False

## Test de Funcionalidad Arriesgar Letra

def test_arriesgo_letra_y_acierto():
    # Debemos simular el estado del juego: sets vacíos
    intentadas = set()
    acertadas = set()
    letra = logica_juego.arriesgoLetra("y", "python", intentadas, acertadas)
    
    assert letra == "acertada"
    assert "y" in acertadas
    assert "y" in intentadas

def test_arriesgo_letra_y_no_acierto():
    intentadas = set()
    acertadas = set()
    letra = logica_juego.arriesgoLetra("z", "python", intentadas, acertadas)
    
    assert letra == "fallada"
    assert "z" not in acertadas
    assert "z" in intentadas

def test_arriesgo_letra_repetida():
    # Simulamos que 'p' ya se había intentado
    intentadas = {"p"}
    acertadas = {"p"}
    
    resultado = logica_juego.arriesgoLetra("p", "python", intentadas, acertadas)
    assert resultado == "repetida"

## Test de Funcionalidad de Vidas

def test_no_acierto_descuenta_vida():   
    vidas_actuales = 6
    # La nueva función recibe si el intento fue FALSO (no acertó)
    vida_nueva = logica_juego.descuentaVida(False, vidas_actuales)
    assert vida_nueva == 5

def test_acierto_no_descuenta_vida():
    vidas_actuales = 6
     # La nueva función recibe si el intento fue VERDADERO (acertó)
    vida_nueva = logica_juego.descuentaVida(True, vidas_actuales)
    assert vida_nueva == 6

## Test de Funcionalidad Mostrar Progreso de la Palabra

def test_arriesgo_letra_correcta_y_la_muestra():
    # Simulamos que 'p' es la única letra acertada
    acertadas = {"p"}
    progreso = logica_juego.mostrarProgreso("python", acertadas)
    assert progreso == "p _ _ _ _ _"

def test_arriesgo_letra_incorrecta_y_no_la_muestra():
    acertadas = set() # Ninguna acertada
    progreso = logica_juego.mostrarProgreso("python", acertadas)
    assert progreso == "_ _ _ _ _ _"

## Test Ganar o Perder el Juego

def test_gano_y_muestra_que_gane():
    # Simulamos haber acertado todas las letras
    acertadas = set("python")
    vidas = 3 # No importa cuántas vidas, ya ganó
    
    assert logica_juego.gano("python", acertadas) == True
    assert logica_juego.mostrarResultado("python", vidas, acertadas) == "¡Ganaste!"

def test_pierdo_y_muestra_que_perdi():
    acertadas = {"p", "y"} # No completó
    vidas_restantes = 0 # Pero se quedó sin vidas
    
    assert logica_juego.perdio(vidas_restantes) == True
    assert logica_juego.mostrarResultado("python", vidas_restantes, acertadas) == "¡Perdiste!"

# ----------------------------------------------------------------
# NOTA: Los tests que simulaban 'jugar()' (con 'patch')
# ya no aplican, porque 'jugar()' fue eliminado de 'ahorcado.py'.
# Esa lógica ahora vive en 'app.py' y se testea de otra forma
# (con un cliente de prueba de Flask), lo cual es más avanzado.
# Por ahora, nos aseguramos de que la LÓGICA base funciona.
# ----------------------------------------------------------------