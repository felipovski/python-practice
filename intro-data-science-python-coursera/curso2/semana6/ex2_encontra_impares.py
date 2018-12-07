def encontra_impares(lista):

    if len(lista) < 1:
        return

    lista_impares = []
    if lista[0] % 3 == 0:
        lista_impares.append(lista[0])
        encontra_impares(lista[1:])
    encontra_impares(lista[1:])

    return lista_impares.extend()
