import random
import unittest.mock
import threading
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from app import app

def before_all(context):
    """Se ejecuta una vez antes de todas las pruebas."""
    
    context.server_thread = threading.Thread(target=app.run, kwargs={
        'port': 5000,
        'debug': True, 
        'use_reloader': False 
    })
    context.server_thread.daemon = True
    context.server_thread.start()

    retries = 5
    while retries > 0:
        try:
            requests.get("http://127.0.0.1:5000/")
            print("Servidor Flask iniciado en un hilo.")
            break
        except requests.ConnectionError:
            time.sleep(1)
            retries -= 1
    if retries == 0:
        raise RuntimeError("No se pudo iniciar el servidor Flask")
    
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    print("Iniciando WebDriver en before_all...")
    
    try:
        s = Service(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(service=s, options=options)
        context.base_url = "http://127.0.0.1:5000"
        print("WebDriver iniciado y 'context.driver' configurado.")
    except Exception as e:
        print(f"ERROR: No se pudo iniciar WebDriver: {e}")
        raise

def before_scenario(context, scenario):
    """Se ejecuta antes de cada Escenario."""
    
    if "set_word_python" in scenario.tags:
        context.mock_random = unittest.mock.patch(
            'app.random.choice', 
            return_value='python'
        )
        context.mock_random.start()

def after_scenario(context, scenario):
    """Se ejecuta después de cada Escenario."""
    
    if hasattr(context, 'mock_random'):
        context.mock_random.stop()

def after_all(context):
    """Se ejecuta una vez al final de todas las pruebas."""
    if hasattr(context, 'driver'):
        print("\nCerrando WebDriver en after_all...")
        context.driver.quit()

    try:
        print("Enviando señal de apagado al servidor Flask...")
        requests.get("http://127.0.0.1:5000/shutdown")
        context.server_thread.join(timeout=5)
        print("Servidor Flask detenido.")
    except Exception as e:
        print(f"Error al apagar el servidor: {e}")
