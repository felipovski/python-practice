def menor_nome(name_list):
    smaller_name = name_list[0].strip()

    for i in range(len(name_list)):

        if len(name_list[i].strip()) < len(smaller_name):
            smaller_name = name_list[i].strip()

    return smaller_name.capitalize()

def testa_menor_nome():
    list1 = [" ", "abc", "akjsfdlakjsdkl", "   laksdfkls   "]
    if menor_nome(list1) == " ":
        print("Resposta correta - teste 1")
    list2 = [" asdfas", "ab c", " akjsfdl    akjsdkl", "laksdfkls"]
    if menor_nome(list2) == "Ab c":
        print("Resposta correta - teste 2")
    if menor_nome(['maria', 'josé', 'PAULO', 'Catarina']) == "José":
        print("Resposta correta - teste 3")
    if menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  ']) == "José":
        print("Resposta correta - teste 4")
    if menor_nome(['Bárbara', 'JOSÉ  ', 'Bill']) == "José":
        print("Resposta correta - teste 5")
