import algoritmo_comparacao
import algoritmo_ordenacao
import pytest

class TestaOrdenador():

    @pytest.fixture
    def o(self):
        return algoritmo_ordenacao.Ordenacao()

    @pytest.fixture
    def l_aleatoria(self):
        c = algoritmo_comparacao.ContaTempos()
        return c.lista_aleatoria(100)

    def esta_ordenada(self, l):
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                return False
        return True

    def test_bolha_curta(self, o, l_aleatoria):
        o.bolha_curta(l_aleatoria)
        assert self.esta_ordenada(l_aleatoria)
