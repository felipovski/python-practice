n = int(input("Digite um número > 1: "))

fator = 2
multiplicidade = 0

while n > 1:
    while n % fator == 0:
        n = n / fator
        multiplicidade += 1
    if multiplicidade:
        print("Fator: ", fator, "multiplicidade:", multiplicidade)
    fator += 1
    multiplicidade = 0
