def fizzbuzz(x):

    resultado = ""

    if x % 3 == 0:
        resultado = "Fizz"
    if x % 5 == 0:
        resultado += "Buzz"
    if resultado == "":
        return x
    else:
        return resultado
