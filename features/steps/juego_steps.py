import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- Funciones de ayuda ---

def arriesgar_entrada(context, texto):
    """Encuentra el input, escribe, presiona el botón Y ESPERA LA RECARGA."""
    try:
        input_field = context.driver.find_element(By.NAME, "entrada")
        submit_button = context.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        
        input_field.clear()
        input_field.send_keys(texto)
        submit_button.click()

        # --- ARREGLO IMPORTANTE (ESPERA DE RECARGA) ---
        WebDriverWait(context.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Juego del Ahorcado')]"))
        )
        # --- FIN DEL ARREGLO ---

    except Exception as e:
        print(f"Error al arriesgar entrada: {e}")
        context.driver.save_screenshot("error_arriesgar.png")

# --- Implementación de Steps ---

@given('the user is on the home page')
def step_impl(context):
    context.driver.get(context.base_url + "/reiniciar")
    WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Juego del Ahorcado')]"))
    )

@when('the user guesses the word "{palabra}"')
def step_impl(context, palabra):
    arriesgar_entrada(context, palabra)

@when('the user guesses the letter "{letra}"')
def step_impl(context, letra):
    arriesgar_entrada(context, letra)

@then('the user sees the victory message "{mensaje}"')
def step_impl(context, mensaje):
    WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, f"//div[@id='popup-content']//h2[text()='{mensaje}']"))
    )

@then('the user sees the defeat message "{mensaje}"')
def step_impl(context, mensaje):
    WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, f"//div[@id='popup-content']//h2[contains(text(), '{mensaje}')]"))
    )

@then('the user sees the revealed secret word "{palabra}"')
def step_impl(context, palabra):
    # --- ARREGLO IMPORTANTE (IGNORAR ESPACIOS) ---
    xpath_selector = f"//div[@id='popup-content']//*[normalize-space()='{palabra}']"
    WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, xpath_selector))
    )
    # --- FIN DEL ARREGLO ---

@then('the user sees the progress "{progreso}"')
def step_impl(context, progreso):
    WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, f"//div[@class='progreso'][text()='{progreso}']"))
    )

@then('the user sees the message "{mensaje}"')
def step_impl(context, mensaje):
    # --- ARREGLO IMPORTANTE (CONTAINS) ---
    WebDriverWait(context.driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, f"//div[contains(@class, 'mensaje') and contains(text(), '{mensaje}')]"))
    )
    # --- FIN DEL ARREGLO ---