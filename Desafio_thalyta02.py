from random import randint


while True:
    # cria a senha aleatória, contador de tentativas e pontuação
    senha = randint(1000, 9999)
    tentativas = 5
    pontos_jogador = 0
    vencedor = False

    print(senha)

    while vencedor == False:
        # pede tentativa do usuário
        tentativa = int(input('tente acertar a senha(4 digitos): '))

        # retirar uma tentativa
        tentativas -= 1
        if tentativas == 0:
            break

        print(tentativas)

        # verifica a diferença
        diferença = senha - tentativa

        # verifica se está longe, perto, por um fio ou se venceu
        if diferença == 0:
            print('VOCÊ VENCEU!!!')
            vencedor = True
        elif diferença > 3000 or diferença < -3000:
            print('MUITO LONGE!')
        elif diferença == 1 or diferença == -1:
            print('POR UM FIO!')
        elif diferença < 500 or diferença > -500:
            print('ESTÁ PERTO!')

    # sitema de pontuação
    if tentativas == 0:
        pontos_jogador += 1000
    elif tentativas == 1:
        pontos_jogador += 2000
    elif tentativas == 2:
        pontos_jogador += 3000
    elif tentativas == 3:
        pontos_jogador += 4000
    elif tentativas == 4:
        pontos_jogador += 5000
    print(f'sua pontuação é {pontos_jogador}')

    # verificar se o jogador quer continuar
    continuar = input('mais um jogo? (y/n): ')
    if continuar == 'n':
        break

