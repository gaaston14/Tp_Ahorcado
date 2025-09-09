import pytest
from ahorcado import arriesgoPalabra

def test_arriesgo_palabra_y_acierto():
    palabra = arriesgoPalabra("python")
    assert palabra == True