import math

def calcula_delta(a, b, c):
    delta = b**2 - 4*a*c
    print("Aqui está o delta %d"%delta)
    return delta

def calcula_raizes(a, b, c):
    delta = calcula_delta(a,b,c)
    if delta == 0:
        raiz1 = -b / (2 * a)
        print("a raiz desta equação é", raiz1)
    elif delta < 0:
        print("esta equação não possui raízes reais")
    else:
        raiz1 = (-b - math.sqrt(delta)) / 2 * a
        raiz2 = (-b + math.sqrt(delta)) / 2 * a
        if raiz1 < raiz2:
            print("as raízes da equação são", raiz1, "e", raiz2)
        else:
            print("as raízes da equação são", raiz2, "e", raiz1)

def bhaskara():

    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    c = float(input("Digite o terceiro número: "))

    calcula_raizes(a, b, c)

