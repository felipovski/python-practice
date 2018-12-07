def n_primos():
    n = int(input("Digite um número:"))
    i = 1
    primos = 0

    while i <= n:
        if ePrimo(i):
            primos += 1
        i += 1
    return primos

def ePrimo(n):

    i = 1
    divisores = 0

    while i <= n:
        if n % i == 0:
            divisores += 1
        i += 1
    if divisores == 2:
        return True
    return False

n_primos()
