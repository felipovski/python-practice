def main():

    numero = int(input("Digite um número: "))

    soma = 0
    numTemp = 0
    numNovo = 0

    i = 10

    while numero != 0:
        numTemp = numero % 10
        soma += numTemp
        numero = numero // 10
        print(numero)
    print(soma)

main()
