"""
Este ficheiro torna o diretório 'tests' num pacote Python.
Pode ser utilizado para configuração de testes ou importações globais.
"""

# Exemplo de configuração inicial comum a todos os testes
import os
import sys
import pytest

# Adiciona o diretório raiz do projeto ao sys.path para facilitar os imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
