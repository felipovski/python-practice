import time
from algoritmo_comparacao import ContaTempos

class Buscador():

    def busca_sequencial(self, lista, elemento):

        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return False

    def busca_binaria(self, lista, x):
        inicio = 0
        fim = len(lista)-1

        while inicio <= fim:
            meio = (inicio+fim)//2
            if lista[meio] == x:
                return meio
            elif lista[meio] > x:
                fim = meio-1
            else:
                inicio = meio+1
        return -1

    def compara(self, n, elemento):
        l = ContaTempos().lista_ordenada(n)
        l2 = l[:]

        antes = time.time()
        self.busca_sequencial(l, 90)
        depois = time.time()
        print("O tempo da busca sequencial foi de", depois - antes, "segundos")

        antes = time.time()
        self.busca_binaria(l2, 90)
        depois = time.time()
        print("O tempo da busca binária foi de", depois - antes, "segundos")
