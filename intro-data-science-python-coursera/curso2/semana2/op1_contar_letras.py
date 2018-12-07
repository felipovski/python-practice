import re

def conta_letras(frase, contar="vogais"):
    num_vogais = 0
    frase = re.sub(r'[\W\s.!?]', "", frase.rstrip()).lower()
    for ch in frase:
        if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
            num_vogais += 1
    num_consoantes = len(frase) - num_vogais

    if contar == "consoantes":
        return num_consoantes
    return num_vogais

def testa_conta_letras():

    if conta_letras('programamos em python') == 6:
        print("Teste 1 ok")
    if conta_letras('programamos em python', 'vogais') == 6:
        print("Teste 2 ok")
    if conta_letras('programamos em python', 'consoantes') == 13:
        print("Teste 3 ok")
