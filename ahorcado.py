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

    letras_intentadas.clear()
    letras_acertadas.clear()

    print("¡Bienvenido al juego del Ahorcado!")

    while True:
        print(f"\nPalabra: {mostrarProgreso(palabra_secreta)}")
        print(f"Vidas restantes: {vidas}")
        print(f"Letras intentadas: {' '.join(sorted(letras_intentadas))}")

        entrada = input("Ingresa una letra o arriesga la palabra: ").lower()

        if entrada == 'salir': # Mantenemos la salida para los tests
            break

        if len(entrada) > 1: # Arriesga palabra
            if arriesgoPalabra(entrada):
                letras_acertadas.update(set(palabra_secreta))
                print(f"¡Correcto! La palabra era '{palabra_secreta}'.")
                print(mostrarResultado(palabra_secreta))
                break
            else:
                print(f"'{entrada}' no es la palabra. ¡Pierdes una vida!")
                vidas += descuentaVida(False)
        
        elif len(entrada) == 1: # Arriesga una letra
            resultado_letra = arriesgoLetra(entrada)
            if resultado_letra == True:
                print(f"¡Bien! La letra '{entrada}' está en la palabra.")
            elif resultado_letra == "repetida":
                print(f"Ya habías intentado la letra '{entrada}'. Intenta con otra.")
            else: # La letra es incorrecta (NUEVO)
                print(f"La letra '{entrada}' no está. ¡Pierdes una vida!")
                vidas += descuentaVida(False)
                
# Punto de entrada para ejecutar el juego desde la consola
if __name__ == "__main__":
    jugar()
 