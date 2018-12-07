n = int(input("Digite um número: "))
lista = []
lista_invertida = []

while n != 0:
    lista.append(n)
    n = int(input("Digite um número: "))
i = len(lista)

while i > 0:
    lista_invertida.append(lista[i-1])
    i -= 1
for i in lista_invertida:
    print(i)
