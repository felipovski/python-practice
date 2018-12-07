def main():

    # leia o tamanho da sequencia
    n = int(input("Digite o tamanho da sequencia (>0): "))

    mdc_atual = int(input("Digite o 1o. numero: "))
    i = 1 # contador de numeros lidos
    while i < n:
        num = int(input("Digite o %do. numero: " %(i+1)))
        i = i + 1
        mdc_atual = mdc(mdc_atual,num)

    print("O mdc eh", mdc_atual)

#-----------------------------------------------------
def mdc(a,b):
    """(int,int) -> int
    Recebe dois inteiros positivos a e b e retorna
    o seu maximo divisor comum.
    """

    mdc = a;
    while a%mdc != 0 or b%mdc != 0:
        mdc -= 1

    return mdc

#-----------------------------------------------------
main() # chamada da funcao principal
