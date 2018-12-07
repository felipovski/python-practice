import buscador
import pytest
from algoritmo_comparacao import ContaTempos

class TestaBuscador():

    @pytest.fixture
    def o(self):
        return buscador.Buscador()

    @pytest.fixture
    def l_ordenada(self):
        l = ContaTempos()
        return l.lista_ordenada(1000)

    @pytest.fixture
    def elemento(self):
        return 201

    def esta_ordenada(self, l):
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                return False
        return True

    def test_busca_binaria(self, o, l_ordenada, elemento):
         o.busca_binaria(l_ordenada, elemento)
         #assert posicao == 200
