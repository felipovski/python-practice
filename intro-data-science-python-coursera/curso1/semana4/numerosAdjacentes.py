def digitoAdjacente():
    numero = input("Digite um número")
    digito = ""
    adjacente = 0

    for ch in numero:
        if(digito == ch):
            adjacente += 1
            break
        digito = ch
    if adjacente > 0:
        print("sim")
    else:
        print("não")
digitoAdjacente()
