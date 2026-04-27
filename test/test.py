import sys
import os

# Isso permite que o teste encontre a pasta 'src'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from calculadora import soma, subtracao, multiplicacao, divisao

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0

def test_subtracao():
    assert subtracao(10, 5) == 5

def test_multiplicacao():
    assert multiplicacao(3, 4) == 12

def test_divisao():
    assert divisao(10, 2) == 5
    assert divisao(5, 0) == "Erro ao dividir por zero"