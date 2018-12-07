def primeiro_lex(lista):
    menor = ""
    nova_ordenacao = []
    for i in range(len(lista)):
        menor = lista[i]
        j = i
        while j < len(lista):
            if menor > lista[j]:
                menor, lista[j] = lista[j], menor
            j += 1
        nova_ordenacao.append(menor)
    return nova_ordenacao[0]

def testa_ordenacao_lista_strings():
    list1 = [" ", "abc", "akjsfdlakjsdkl", "   laksdfkls   "]
    if primeiro_lex(list1) == [" ", "   laksdfkls   ", "abc", "akjsfdlakjsdkl"]:
        print("Deu certo!")
    else:
        print("A lista ordenada é ", primeiro_lex(list1))
    if primeiro_lex(["Je","Fe","Ta","Linux"]) == ["Fe", "Je", "Linux", "Ta"]:
        print("Deu certo!")
    else:
        print("A lista ordenada é ")
    if primeiro_lex(["Je","fe","Ta","Linux"]) == ["Je", "Linux", "Ta", "fe"]:
        print("Deu certo!")
        print(primeiro_lex(["Je","fe","Ta","Linux"]))
    else:
        print("A lista ordenada é ")
