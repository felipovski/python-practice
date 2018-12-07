def incomodam(n):

    if n < 1:
        return ""
    if n < 2:
        return "\nincomoda"

    return incomodam(n-1) + "incomodam"

def elefantes(n):

    if n == 1:
        return "Um elefante", incomodam(),"muita gente"
    return n, "elefantes", incomodam(), "muito mais"
