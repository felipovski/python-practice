def menor_nome(name_list):
    smaller_name = name_list[0]

    for i in range(len(name_list)):

        if len(name_list[i].strip()) < len(smaller_name):
            smaller_name = name_list[i]

    return smaller_name.capitalize()

def testa_menor_nome():
    list1 = [" ", "abc", "akjsfdlakjsdkl", "   laksdfkls   "]
    if menor_nome(list1) == " ":
        print("Resposta correta - teste 1")
    list2 = [" asdfas", "ab c", " akjsfdl    akjsdkl", "laksdfkls"]
    if menor_nome(list2) == "Ab c":
        print("Resposta correta - teste 2")
