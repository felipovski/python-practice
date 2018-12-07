def soma_matrizes(matriz1, matriz2):
    tam_matriz1 = len(matriz1)
    tam_submatriz_1 = len(matriz1[0])
    tam_matriz2 = len(matriz2)
    tam_submatriz_2 = len(matriz2[0])
    nova_matriz = []

    if (tam_matriz1 == tam_matriz2) and (tam_submatriz_1 == tam_submatriz_2):
        for i in range(tam_matriz1):
            nova_lista = []
            for j in range(tam_submatriz_1):
                nova_lista.append(matriz1[i][j] + matriz2[i][j])
            nova_matriz.append(nova_lista)
        return nova_matriz
    else:
        return False
