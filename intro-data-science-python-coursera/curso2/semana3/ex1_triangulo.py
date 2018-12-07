class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if self.a == self.b and self.b == self.c:
            return "equilátero"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "isóceles"
        else:
            return "escaleno"

    def retangulo(self):
        maior, menor1, menor2 = self.maior_lado()
        return (self.tipo_lado() == "escaleno") and (maior^2 == menor1^2 + menor2^2)

    def maior_lado(self):
        if self.a > self.b and self.a > self.c:
            return self.a, self.b, self.c
        elif self.b > self.a and self.b > self.c:
            return self.b, self.a, self.c
        else:
            return self.c, self.a, self.b

    def semelhantes(self, triangulo):
        return self.a /triangulo.a == self.b / triangulo.b and self.a /triangulo.a == self.c / triangulo.c
