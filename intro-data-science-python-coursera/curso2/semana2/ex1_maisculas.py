import re

def maiusculas(frase):
    maiusculas = ""
    frase_sem_espaco = re.sub(r'[.!?\s0-9\W]+', "", frase.rstrip()) #frase.replace(r'[.!?]+', "")
    for ch in frase_sem_espaco:
        if ch.upper() == ch:
            maiusculas += ch
    return maiusculas

def testa_maiusculas():
    if maiusculas('Programamos em python 2?') == "P":
        print("Primeiro teste ok")
    else:
        print(maiusculas('Programamos em python 2?'))
    if maiusculas('Programamos em Python 3.') == "PP":
        print("Segundo teste ok")
    else:
        print(maiusculas('Programamos em Python 3.'))
    if maiusculas('PrOgRaMaMoS em python!') == "PORMMS":
        print("Terceiro teste ok")
    else:
        print(maiusculas('PrOgRaMaMoS em python!'))
    if maiusculas('PrOgRaMaMoS, em, python!') == "PORMMS":
        print("Quarto teste ok")
    else:
        print(maiusculas('PrOgRaMaMoS em python!'))
