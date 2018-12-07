def ordena(lista):

    fim = len(lista)

    for i in range(fim-1):
        posicao_do_menor = i

        for j in range(i+1, fim):
            if lista[j] < lista[posicao_do_menor]:
                posicao_do_menor = j
        lista[i], lista[posicao_do_menor] = lista[posicao_do_menor], lista[i]
    return lista
