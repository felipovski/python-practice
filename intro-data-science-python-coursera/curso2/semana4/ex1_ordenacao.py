def ordenada(lista):

    fim = len(lista)

    for i in range(fim-1):
        posicao_do_menor = i

        for j in range(i+1, fim):
            if lista[j] < lista[posicao_do_menor]:
                return False
                posicao_do_menor = j
    return True
