def escreve_poesia():
    
    nome = "poesia.txt"    # poderia ser um input("Digite o nome do arquivo: ")

    with open(nome, 'w', encoding='utf-8') as arq:
        # CORPO DO WITH
        arq.write("    O poeta é um fingidor.      \n")
        arq.write("    Finge tão completamente     \n")
        arq.write("    Que chega a fingir que é dor\n")
        arq.write("    A dor que deveras sente.    \n")
        arq.write("                Fernando Pessoa.\n")

def abre_arquivo(path):
    nome = path    # poderia ser um input("Digite o nome do arquivo: ")

    with open(nome, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            print(linha)

    # continue o programa usando conteudo
    print(conteudo)
