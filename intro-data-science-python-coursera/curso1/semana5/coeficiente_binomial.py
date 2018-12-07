def fatorial(x):

    fatorial = 1

    while n > 1:
        fatorial *= n
        n -= 1
    return fatorial

def testa_fatorial():
    if fatorial(0) == 1:
        print("Funciona para 0")
    else:
        print("Não funciona para 0")
    if fatorial(1) == 1:
        print("Funciona para 1")
    else:
        print("Não funciona para 1")
    if fatorial(2) == 2:
        print("Funciona para 2")
    else:
        print("Não funciona para 2")
    if fatorial(5) == 120:
        print("Funciona para 5")
    else:
        print("Não funciona para 5")

def coeficiente_binomial(n, k):

    return fatorial(n) / (fatorial(k) * fatorial(n - k))

def testa_binomial():
    if coeficiente_binomial(1,0) == 1:
        print("Tudo certo para 1 e 0")
    else:
        print("Deu ruim para 1 e 0")
    if coeficiente_binomial(3,0) == 1:
        print("Tudo certo para 3 e 0")
    else:
        print("Deu ruim para 3 e 1")
    if coeficiente_binomial(12,5) == 792:
        print("Tudo certo para 12 e 5")
    else:
        print("Deu ruim para 12 e 5")
    if coeficiente_binomial(18,7) == 31824:
        print("Tudo certo para 18 e 7")
    else:
        print("Deu ruim para 18 e 7")
