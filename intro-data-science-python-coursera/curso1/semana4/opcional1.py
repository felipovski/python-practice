def eh_primo():

    numero = int(input("Digite um número: "))

    i = 1
    divisores = 0

    while i <= numero:
        if numero % i == 0:
            divisores += 1
        i += 1

    if divisores == 2:
        print("primo")
    else:
        print("não primo")

eh_primo()
