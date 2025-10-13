letras_intentadas = set()
letras_acertadas = set()

def perdio(vidas_restantes):
    return vidas_restantes <= 0

def gano(palabra):
    return all(letra in letras_acertadas for letra in palabra)



def arriesgoPalabra(palabra):
        if( palabra == "python"):
            return True
        else:
            return False

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
    else:
        return False
    
def mostrarProgreso(palabra):
    progreso = []
    for letra in palabra:
        if letra in letras_acertadas:
            progreso.append(letra)
        else:
            progreso.append("_")
    return " ".join(progreso)

def mostrarResultado(palabra, vidas_restantes=None):
    if gano(palabra):
        return "¡Ganaste!"
    if vidas_restantes is not None and perdio(vidas_restantes):
        return "¡Perdiste!"

def jugar():
    """Función principal que orquesta el juego del Ahorcado."""
    palabra_secreta = "python"
    vidas = 6

    # Limpiamos los sets por si se juega varias veces
    letras_intentadas.clear()
    letras_acertadas.clear()

    print("¡Bienvenido al juego del Ahorcado!")

    while True:
        print(f"\nPalabra: {mostrarProgreso(palabra_secreta)}")
        print(f"Vidas restantes: {vidas}")
        print(f"Letras intentadas: {' '.join(sorted(letras_intentadas))}")


        entrada = input("Ingresa una letra o arriesga la palabra: ").lower()

        if len(entrada) > 1: # Arriesga palabra
            acerto = arriesgoPalabra(entrada)
            if acerto:
                letras_acertadas.update(set(palabra_secreta))
                print(f"¡Correcto! La palabra era '{palabra_secreta}'.")
                print(mostrarResultado(palabra_secreta))
                break
            else:
                print(f"'{entrada}' no es la palabra. ¡Pierdes una vida!")
                vidas += descuentaVida(False) # Usamos la función que ya tenías

        # Aquí irá la lógica para arriesgar letras

        if entrada == 'salir': # Mantenemos la salida para los tests
            break

# Punto de entrada para ejecutar el juego desde la consola
if __name__ == "__main__":
    jugar()
 