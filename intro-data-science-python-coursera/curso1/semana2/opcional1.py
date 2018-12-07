def main():

    nomeCliente = input("Digite o nome do cliente: ")
    diaVenc = int(input("Digite o dia de vencimento: "))
    mesVenc = input("Digite o mês de vencimento: ")
    valorFatura = input("Digite o valor da fatura: ")

    print("Olá,", nomeCliente)
    print("A sua fatura com vencimento em", diaVenc, "de", mesVenc, "no valor de R$", valorFatura, "está fechada.")
main()
