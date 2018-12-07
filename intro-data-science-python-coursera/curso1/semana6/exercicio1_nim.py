def campeonato():
    print("\nBem-vindo ao jogo do NIM! Escolha:\n")
    escolha = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))

    if escolha == 2:
        print("\nVoce escolheu um campeonato!\n")
        print("**** Rodada 1 ****\n")
        partida()
        print("**** Rodada 2 ****\n")
        partida()
        print("**** Rodada 3 ****\n")
        partida()
        print("**** Final do campeonato! ****\n")
        print("Placar: Você 0 X 3 Computador")


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if m >= n:
        m = int(input("Número de peças retiradas inválido! Escolha outro menor do que", n, ": "))

    if n % (m+1) == 0:              #or n - m-1 < m
        print("\nVocê começa!\n")
        n = usuario_escolhe_jogada(n, m)
    else:
        print("\nComputador começa!\n")

    while True:
        n = computador_escolhe_jogada(n, m)
        if n == 0:
            break
        n = usuario_escolhe_jogada(n, m)



def usuario_escolhe_jogada(n, m):
    m_usuario = int(input("Quantas peças você vai tirar? "))
    if m_usuario <= m and m >= 1 and m_usuario <= n:
        n = n - m_usuario
        if m_usuario == 1:
            print("Você tirou uma peça.")
        else:
            print("Você tirou", m_usuario, "peças")
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.\n")
        else:
            print("Agora restam", n, "peças no tabuleiro.\n")
        return n
    else:
        print("\nOops! Jogada inválida! Tente de novo.\n")
        return usuario_escolhe_jogada(n, m)

def computador_escolhe_jogada(n, m):
    if m == 1:
        n -= 1
        print("O computador tirou uma peça.")
        return n
    if (n - m) % m+1 == 0:
        n -= m
        n % (m+1)
    else:
        while n % m+1 != 0:
            m -= 1
        n -= m
    return n

    if n - m < 0:
        n = n - n
        print("O computador tirou", n, "peças.")
    else:
        n = n - m
        print("O computador tirou", (m), "peças.")
    if n == 0:
        print("Fim do jogo! O computador ganhou!\n")
        return 0

    print("Agora restam", n, "peças no tabuleiro.\n")
    return n

campeonato()
