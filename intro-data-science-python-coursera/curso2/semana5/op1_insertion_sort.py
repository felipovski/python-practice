def insertion_sort(lista):

    for i in range(0, len(lista)-1, 1):
        for j in range(i+1, 0, -1):
            if lista[j-1] > lista[j]:
                lista[j], lista[j-1] = lista[j-1], lista[j]
                print("Troucou: ", lista[j], "por ", lista[j-1])
    return lista
