import random

def lista_grande(n):
    lista = []
    for i in range(n):
        lista.append(int(random.random()*100))
    return lista
