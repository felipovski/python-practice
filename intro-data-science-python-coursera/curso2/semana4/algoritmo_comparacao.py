import time
import random
import algoritmo_ordenacao

class ContaTempos():

    def lista_aleatoria(self, n):
        lista = [random.randrange(1000) for x in range(n)]
        return lista

    def lista_ordenada(self, n):
        lista = [x for x in range(n)]
        return lista

    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]

        o = algoritmo_ordenacao.Ordenacao()

        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print("O algoritmo da bolha demorou", depois - antes, "segundos")

        antes = time.time()
        o.bolha_curta(lista1)
        depois = time.time()
        print("O algoritmo da bolha demorou", depois - antes, "segundos")

        antes = time.time()
        o.selecao_direta(lista1)
        depois = time.time()
        print("O algoritmo de seleção direta demorou", depois - antes, "segundos")
