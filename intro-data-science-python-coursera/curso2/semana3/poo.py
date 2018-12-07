class Carro:

    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def imprime_dados(self):
        print("%s %s %d" %(self.modelo, self.cor, self.ano))
