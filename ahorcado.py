letras_intentadas = set()
letras_acertadas = set()

def arriesgoPalabra(palabra):
        if( palabra == "python"):
            return True
        else:
            return False
"""        
def arriesgoLetra(letra):
        if( letra.lower() in "python"):
            return True
        else:
            return False
"""
def arriesgoLetra(letra):
    global letras_intentadas, letras_acertadas

    letra = letra.lower()

    # si ya se intentó antes
    if letra in letras_intentadas:
        return "repetida"

    # registrar la letra como usada
    letras_intentadas.add(letra)

    # si la letra está en la palabra
    if letra in "python":
        letras_acertadas.add(letra)
        return True
    else:
        return False


def descuentaVida(letra):
        if ( letra == False):
            return -1