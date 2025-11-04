import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- Funciones de ayuda (Sin cambios) ---

def arriesgar_entrada(context, texto):
    """Encuentra el input, escribe, presiona el botón Y ESPERA LA RECARGA."""
    try:
        input_field = context.driver.find_element(By.NAME, "entrada")
        submit_button = context.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        
        input_field.clear()
        input_field.send_keys(texto)
        submit_button.click()

        # Espera a que la página se recargue
        WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Juego del Ahorcado')]"))
        )

    except Exception as e:
        print(f"Error al arriesgar entrada: {e}")
        context.driver.save_screenshot("error_arriesgar.png")

# --- Implementación de Steps (Con correcciones) ---

@given('the user is on the home page')
def step_impl(context):
    context.driver.get(context.base_url + "/reiniciar")
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Juego del Ahorcado')]"))
    )

@when('the user guesses the word "{palabra}"')
def step_impl(context, palabra):
    arriesgar_entrada(context, palabra)

@when('the user guesses the letter "{letra}"')
def step_impl(context, letra):
    arriesgar_entrada(context, letra)

# --- ¡ARREGLO PARA STALE ELEMENT! ---
@then('the user sees the victory message "{mensaje}"')
def step_impl(context, mensaje):
    # Esperamos 10 segundos a que el DIV 'popup-content' CONTENGA el texto
    WebDriverWait(context.driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.ID, 'popup-content'), mensaje
        )
    )

# --- ¡ARREGLO PARA STALE ELEMENT! ---
@then('the user sees the defeat message "{mensaje}"')
def step_impl(context, mensaje):
    # Usamos la misma técnica robusta
    WebDriverWait(context.driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.ID, 'popup-content'), mensaje
        )
    )

# --- ¡ARREGLO PARA STALE ELEMENT! ---
@then('the user sees the revealed secret word "{palabra}"')
def step_impl(context, palabra):
    # Y de nuevo aquí. Esto soluciona la "race condition"
    WebDriverWait(context.driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.ID, 'popup-content'), palabra
        )
    )

@then('the user sees the progress "{progreso}"')
def step_impl(context, progreso):
    # Este está en la página principal, por lo que el selector original está bien
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, f"//div[@class='progreso'][text()='{progreso}']"))
    )

@then('the user sees the message "{mensaje}"')
def step_impl(context, mensaje):
    # Este también está en la página principal
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, f"//div[contains(@class, 'mensaje') and contains(text(), '{mensaje}')]"))
    )