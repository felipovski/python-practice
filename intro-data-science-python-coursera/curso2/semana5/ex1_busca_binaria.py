def busca(lista, elemento):
    inicio = 0
    fim = len(lista)-1

    while inicio <= fim:
        meio = inicio + (inicio + fim) // 2
        if lista[meio] == elemento:
            return meio
        elif lista[meio] > elemento:
            fim = meio - 1
        else:
            inicio = meio + 1
        print(meio)
    return False
