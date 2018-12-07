def main():

    n = int(input("Digite um número: "))

    impares = i = 1

    while impares <= n:
        if i % 2 == 1:
            print(i)
            impares += 1
        i += 1
main()
