def remove_repetidos(lista):
    i = 0
    j = 0
    
    while i < len(lista):
        j = i+1
        while j < (len(lista)):
            if lista[i] == lista[j]:
                del lista[j]
                print("Lista", lista)
                continue
            j += 1
        i += 1
    
    return sorted(lista)
 
