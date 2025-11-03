# app.py
import random
from flask import Flask, render_template, request, redirect, url_for, session
# Importamos las funciones *modificadas* de nuestro archivo ahorcado
import ahorcado as logica_juego

app = Flask(__name__)
# Una 'secret_key' es necesaria para que las sesiones (memoria) funcionen
app.secret_key = 'tu_llave_secreta_muy_secreta_aqui'

@app.before_request
def make_session_non_permanent():
    session.permanent = False

@app.route('/')
def index():
    """Muestra la página principal del juego."""
    
    if 'palabra_secreta' not in session:
        iniciar_juego()

    # Obtenemos todos los datos de la sesión
    palabra = session['palabra_secreta']
    vidas = session['vidas']
    letras_acertadas = set(session['letras_acertadas'])
    letras_intentadas = set(session['letras_intentadas'])
    mensaje = session.get('mensaje', '')

    # Calculamos el estado actual
    progreso_actual = logica_juego.mostrarProgreso(palabra, letras_acertadas)
    juego_ganado = logica_juego.gano(palabra, letras_acertadas)
    juego_perdido = logica_juego.perdio(vidas)
    juego_terminado = juego_ganado or juego_perdido

    # --- ¡MODIFICADO! ---
    # Calculamos el número de errores
    num_errores = logica_juego.VIDAS_INICIALES - vidas
    
    # Nos aseguramos de no salirnos del rango de imágenes (0 a 6)
    if num_errores < 0: num_errores = 0
    if num_errores > 6: num_errores = 6
    # --- Fin de la modificación ---

    return render_template('index.html', 
                           progreso=progreso_actual,
                           vidas=vidas,
                           intentadas=' '.join(sorted(letras_intentadas)),
                           mensaje=mensaje,
                           juego_terminado=juego_terminado,
                           palabra_secreta=palabra if juego_terminado else None,
                           num_errores=num_errores)

def iniciar_juego():
    """Configura la sesión para un juego nuevo."""
    session.clear() # Limpiamos cualquier juego anterior
    session['palabra_secreta'] = random.choice(logica_juego.BANCO_PALABRAS)
    session['vidas'] = logica_juego.VIDAS_INICIALES
    # Usamos listas en la sesión (son compatibles con JSON), no sets
    session['letras_acertadas'] = []
    session['letras_intentadas'] = []
    session['mensaje'] = '¡Bienvenido! Adivina la palabra.'

@app.route('/jugar', methods=['POST'])
def jugar():
    """Procesa el intento del usuario (letra o palabra)."""
    
    # Obtenemos datos de la sesión (como listas)
    palabra_secreta = session['palabra_secreta']
    vidas = session['vidas']
    letras_acertadas_list = session['letras_acertadas']
    letras_intentadas_list = session['letras_intentadas']

    # Convertimos a sets para usar la lógica
    letras_acertadas = set(letras_acertadas_list)
    letras_intentadas = set(letras_intentadas_list)
    
    entrada = request.form['entrada'].lower().strip() # 'entrada' viene del HTML

    # --- Lógica de validación ---
    if not entrada: # Si no ingresa nada
        session['mensaje'] = 'No ingresaste nada. Intenta de nuevo.'
        return redirect(url_for('index'))
        
    if not entrada.isalpha():
        session['mensaje'] = 'Error: Solo puedes ingresar letras.'
        return redirect(url_for('index'))

    # --- Arriesga palabra completa ---
    if len(entrada) > 1:
        if logica_juego.arriesgoPalabra(entrada, palabra_secreta):
            # ¡AQUÍ ESTÁ EL ARREGLO!
            # 1. Actualizamos el set local de letras acertadas
            letras_acertadas.update(set(palabra_secreta))
            # 2. Ponemos un mensaje de victoria limpio
            session['mensaje'] = "¡Ganaste! Adivinaste la palabra."
            # Ya no necesitamos 'session['letras_acertadas'] = list(palabra_secreta)'
            # porque la línea de abajo lo hará por nosotros.
        else:
            session['mensaje'] = f"'{entrada}' no es la palabra. ¡Pierdes una vida!"
            session['vidas'] = vidas - 1
            # Añadimos la palabra fallida a "intentadas" para mostrarla
            letras_intentadas.add(entrada) 

    # --- Arriesga una letra ---
    elif len(entrada) == 1:
        resultado = logica_juego.arriesgoLetra(entrada, palabra_secreta, letras_intentadas, letras_acertadas)
        
        if resultado == "acertada":
            session['mensaje'] = f"¡Bien! La letra '{entrada}' está."
            # Verificamos si ganó justo con esta letra
            if logica_juego.gano(palabra_secreta, letras_acertadas):
                session['mensaje'] = "¡Ganaste! Completaste la palabra."
        elif resultado == "repetida":
            session['mensaje'] = f"Ya habías intentado la letra '{entrada}'."
        else: # "fallada"
            vidas = vidas - 1
            session['vidas'] = vidas
            if logica_juego.perdio(vidas):
                session['mensaje'] = f"¡Perdiste! La letra '{entrada}' no estaba."
            else:
                session['mensaje'] = f"La letra '{entrada}' no está. ¡Pierdes una vida!"

    # Guardamos los sets actualizados de vuelta como listas en la sesión
    # Esta línea ahora guardará correctamente la palabra completa si se ganó
    session['letras_acertadas'] = list(letras_acertadas)
    session['letras_intentadas'] = list(letras_intentadas)

    return redirect(url_for('index')) # Recargamos la página principal
@app.route('/reiniciar')
def reiniciar():
    """Limpia la sesión y redirige al inicio para un juego nuevo."""
    iniciar_juego()
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Esto permite ejecutarlo localmente con 'python app.py'
    app.run(debug=True)