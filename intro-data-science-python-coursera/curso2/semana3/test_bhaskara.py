import bhaskara, pytest

class TestBhaskara:

    @pytest.fixture
    def b(self):
        return bhaskara.Bhaskara()
    @pytest.mark.parametrize("entrada, valor_esperado", [
    ((1,0,0),(1,0)),
    ((1,-5,6),(2,2.0,3.0)),
    ((10,10,10),(0)),
    ((10,20,10),(1,-10))])

    def testa_uma_raiz(self, b, entrada, valor_esperado):
        assert b.calcula_raizes(entrada) == (valor_esperado)
    def testa_duas_raizes(self, b):
        assert b.calcula_raizes(entrada) == (valor_esperado)
    def testa_zero_raizes(self, b):
        assert b.calcula_raizes(entrada) == valor_esperado
    def testa_raiz_negativa(self, b):
        assert b.calcula_raizes(entrada) == (valor_esperado)
