def fatorial():

    n = int(input("Digite um número: "))

    fatorial = i = 1

    while i <= n:
        fatorial *= i
        i += 1
    print(fatorial)

fatorial()
