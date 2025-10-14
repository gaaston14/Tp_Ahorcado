import random
random.seed(0)

letras_intentadas = set()
letras_acertadas = set()
BANCO_PALABRAS = [
    "python",
    "camilo",
    "crossfit",
    "pandas"
]
vidas = 6

def perdio(vidas_restantes):
    return vidas_restantes <= 0

def gano(palabra):
    return all(letra in letras_acertadas for letra in palabra)



def arriesgoPalabra(palabra, palabra_secreta="python"):
        if( palabra == palabra_secreta.lower()):
            return True
        else:
            return False

def arriesgoLetra(letra, palabra_secreta="python"):
    global letras_intentadas, letras_acertadas

    letra = letra.lower()

    # si ya se intentó antes, avisamos y no modificamos nada
    if letra in letras_intentadas:
        return "repetida"

    # registrar la letra como usada
    letras_intentadas.add(letra)

    # si la letra está en la palabra
    if letra in palabra_secreta:
        letras_acertadas.add(letra)
        return True
    else:
        return False

def descuentaVida(letra):
    global vidas
    if letra == False and vidas > 0:
        vidas -= 1
    return vidas
    
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
    global vidas
    palabra_secreta = random.choice(BANCO_PALABRAS)
    vidas = 6

    letras_intentadas.clear()
    letras_acertadas.clear()

    print("¡Bienvenido al juego del Ahorcado!")

    while True:
        print(f"\nPalabra: {mostrarProgreso(palabra_secreta)}")
        print(f"Vidas restantes: {vidas}")
        print(f"Letras intentadas: {' '.join(sorted(letras_intentadas))}")

        entrada = input("Ingresa una letra o arriesga la palabra: ").lower()

        if entrada == 'salir':  # mantener para los tests
            break

        # --- Arriesga palabra completa ---
        if len(entrada) > 1:
            if arriesgoPalabra(entrada, palabra_secreta):
                letras_acertadas.update(set(palabra_secreta))
                print(f"¡Correcto! La palabra era '{palabra_secreta}'.")
                print(mostrarResultado(palabra_secreta))
                break
            else:
                print(f"'{entrada}' no es la palabra. ¡Pierdes una vida!")
                vidas = descuentaVida(False)

                if vidas <= 0:
                    print("¡Perdiste! Te quedaste sin vidas.")
                    print(f"La palabra era: {palabra_secreta}")
                    break

        # --- Arriesga una letra ---
        elif len(entrada) == 1:
            resultado_letra = arriesgoLetra(entrada, palabra_secreta)

            if resultado_letra == True:
                print(f"¡Bien! La letra '{entrada}' está en la palabra.")

            elif resultado_letra == "repetida":
                print(f"Ya habías intentado la letra '{entrada}'. No pierdes una vida. Intenta con otra.")

            else:
                print(f"La letra '{entrada}' no está. ¡Pierdes una vida!")
                vidas = descuentaVida(False)

                if vidas <= 0:
                    print("¡Perdiste! Te quedaste sin vidas.")
                    print(f"La palabra era: {palabra_secreta}")
                    break



# Punto de entrada para ejecutar el juego desde la consola
if __name__ == "__main__":
    jugar()
 