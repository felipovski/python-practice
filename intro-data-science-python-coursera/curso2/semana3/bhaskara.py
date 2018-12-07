import math

class Bhaskara:

    def calcula_delta(self, a, b, c):
        delta = b**2 - 4*a*c
        return delta

    def calcula_raizes(self, a, b, c):
        delta = self.calcula_delta(a,b,c)
        if delta == 0:
            raiz1 = -b / (2 * a)
            return 1, raiz1
        elif delta < 0:
            return 0
        else:
            raiz1 = (-b - math.sqrt(delta)) / 2 * a
            raiz2 = (-b + math.sqrt(delta)) / 2 * a
            return 2, raiz1, raiz2

'''    def bhaskara(self):

        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        c = float(input("Digite o terceiro número: "))

        self.calcula_raizes(a, b, c)
'''
