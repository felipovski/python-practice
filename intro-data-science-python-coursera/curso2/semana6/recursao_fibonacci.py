def fibonacci(n):

    if n < 2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

import pytest

@pytest.mark.parametrize("entrada, esperado", [
(0,0),
(1,1),
(2,1),
(3,2),
(4,3),
(5,5),
(6,8),
(7,13) ])

def testa_fibonacci(entrada, esperado):
    assert fibonacci(entrada) == esperado


def busca(lista, elemento):
    inicio = 0
    fim = len(lista)-1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == elemento:
            return meio
        elif lista[meio] > elemento:
            fim = meio - 1
        else:
            inicio = meio + 1
        print(meio)
    return False
