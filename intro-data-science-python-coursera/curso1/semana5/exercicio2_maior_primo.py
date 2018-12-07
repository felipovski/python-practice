def eh_primo(n):

    i = 1
    divisores = 0

    while i <= n:
        if n % i == 0:
            divisores += 1
        i += 1

    if divisores == 2:
        return True
    else:
        return False

def maior_primo(n):

    if n < 2:
        return "O número deve ser maior ou igual a 2"

    while n >= 2:
        if eh_primo(n):
            return n;
        else:
            n -= 1
    
