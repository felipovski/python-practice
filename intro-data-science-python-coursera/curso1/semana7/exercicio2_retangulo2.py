def desenha_retangulo():
    largura = int(input("Indique a largura do retângulo: "))
    altura = int(input("Indique a altura do retângulo: "))

    i = j = 0

    while i < altura:
        while j < largura:
            if((i == 0 or i == altura-1) or (j == 0 or j == largura-1)):
                print("#", end="")
            else:
                print(" ", end="")
            j += 1
        print("")
        j = 0
        i += 1

desenha_retangulo()
