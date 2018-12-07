def main():

    numero = int(input("Digite um número: "))

    numeroSomado = numeroRetirado = 0

    while numero != 0:
        numeroRetirado = numero % 10
        numero = numero // 10
        numeroSomado += numeroRetirado

    print(numeroSomado)
main()
