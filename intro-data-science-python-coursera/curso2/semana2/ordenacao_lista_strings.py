def ordenacao_lista_strings(lista_strings):
    menor = ""
    nova_ordenacao = []
    for i in range(len(lista_strings)):
        menor = lista_strings[i]
        j = i
        while j < len(lista_strings):
            if menor > lista_strings[j]:
                menor, lista_strings[j] = lista_strings[j], menor
            j += 1
        nova_ordenacao.append(menor)
    return nova_ordenacao

def testa_ordenacao_lista_strings():
    list1 = [" ", "abc", "akjsfdlakjsdkl", "   laksdfkls   "]
    if ordenacao_lista_strings(list1) == [" ", "   laksdfkls   ", "abc", "akjsfdlakjsdkl"]:
        print("Deu certo!")
    else:
        print("A lista ordenada é ", ordenacao_lista_strings(list1))
    if ordenacao_lista_strings(["Je","Fe","Ta","Linux"]) == ["Fe", "Je", "Linux", "Ta"]:
        print("Deu certo!")
    else:
        print("A lista ordenada é ")
