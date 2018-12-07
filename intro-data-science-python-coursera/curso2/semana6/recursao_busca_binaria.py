def busca(lista, elemento, inicio=0, fim=None):
    if fim == None:
        fim = len(lista)-2
    meio = (inicio + fim) // 2

    if fim < inicio:
        return False
    elif lista[meio] > elemento:
        return busca(lista, elemento, inicio, meio-1)
    elif lista[meio] < elemento:
        lista_temp = lista[meio:]
        return busca(lista, elemento, meio+1, fim)
    else:
        return meio
