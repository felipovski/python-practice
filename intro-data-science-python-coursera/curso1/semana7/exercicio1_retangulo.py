def desenha_retangulo():
    largura = int(input("Indique a largura do retângulo: "))
    altura = int(input("Indique a altura do retângulo: "))

    i = j = 0

    while i < altura:
        while j < largura:
            print("#", end="")
            j += 1
        print("")
        j = 0
        i += 1

desenha_retangulo()
