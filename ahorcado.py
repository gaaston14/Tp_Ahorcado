# ahorcado.py
import random



letras_intentadas_global = set() 
letras_acertadas_global = set() 

BANCO_PALABRAS = [
    "python",
    "camilo",
    "crossfit",
    "pandas",
    "flask",
    "docker",
    "vercel"
]
VIDAS_INICIALES = 6

def perdio(vidas_restantes):
    """Verifica si al jugador no le quedan vidas."""
    return vidas_restantes <= 0

def gano(palabra, letras_acertadas):
    """Verifica si el jugador adivinó todas las letras de la palabra."""
    return all(letra in letras_acertadas for letra in palabra)

def arriesgoPalabra(palabra, palabra_secreta):
    """Comprueba si la palabra arriesgada es correcta."""
    palabra_secreta_lower = (palabra_secreta or "python").lower()
    return palabra.lower() == palabra_secreta_lower

def arriesgoLetra(letra, palabra_secreta, letras_intentadas, letras_acertadas):
    """
    Procesa el intento de una letra.
    Devuelve un código de estado: "acertada", "fallada", "repetida".
    """
    letra = letra.lower()
    palabra_secreta_lower = (palabra_secreta or "python").lower() # Para tests

    if letra in letras_intentadas:
        return "repetida"

    letras_intentadas.add(letra)

    if letra in palabra_secreta_lower:
        letras_acertadas.add(letra)
        return "acertada"
    else:
        return "fallada"

def descuentaVida(letra_fue_correcta, vidas_actuales):
    """Resta una vida si el intento fue incorrecto."""
    if not letra_fue_correcta:
        return vidas_actuales + 1
    return vidas_actuales
    
def mostrarProgreso(palabra, letras_acertadas):
    """Devuelve un string con el progreso (ej: 'p _ t h _ n')"""
    progreso = []
    for letra in palabra:
        if letra in letras_acertadas:
            progreso.append(letra)
        else:
            progreso.append("_")
    return " ".join(progreso)

def mostrarResultado(palabra, vidas_restantes, letras_acertadas):
    """Devuelve el mensaje final del juego."""
    if gano(palabra, letras_acertadas):
        return "¡Ganaste!"
    if perdio(vidas_restantes):
        return "¡Perdiste!"
    return None 
