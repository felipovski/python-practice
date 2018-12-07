def main():

    numero1 = int(input("Digite o primeiro número inteiro: "))
    numero2 = int(input("Digite o segundo número inteiro: "))
    numero3 = int(input("Digite o terceiro número inteiro: "))
    numero4 = int(input("Digite o quarto número inteiro: "))

    x1 = numero1
    y1 = numero2
    x2 = numero3
    y2 = numero4

    if abs(x1 - x2) < 10 and abs(y1 - y2) < 10:
        print("perto")
    else:
        print("longe")
main()

def triangular():
    n = int(input("digite n"))

    i = 0
    produto = 0

    while (i*(i+1)*(i+2)) < n:
        i += 1
    if i*(i+1)*(i+2) == n:
        print(i,"*", i+1, "*", i+2)
    else:
        print("não é")
triangular()
