def soma_lista(lista):

    if len(lista) < 0:
        return False

    if len(lista) == 1:
        return lista[0]

    soma = lista[0]
    lista_nova = lista[1:]

    return soma + soma_lista(lista_nova)
