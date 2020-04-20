def computador_escolhe_jogada(n,m):
    computadortira=1
    while computadortira!=m:
        if (n-computadortira)%(m+1)==0:
            return computadortira
        else:
            computadortira+=1
    return computadortira


def jogador_escolhe_jogada(n,m):
    jogadavalida=False
    while not jogadavalida:
        jogadorremove=int(input('qual a quantidade de peças a tirar?'))
        if jogadorremove > m or jogadorremove <1:
            print('\n\jogada invalida! tente novamente')
        else:
            jogadavalida= True
    return jogadorremove




def campeonato():
    numeroRodada = 1
    while numeroRodada <= 3:
        print()
        print('**** Rodada', numeroRodada, '****')
        print()
        partida()
        numeroRodada += 1
    print()
    print('Placar: Você 0 X 3 Computador')


def partida():
    n=int(input('Quantas peças'))
    m=int(input('Limite de peças por jogada?'))
    vezdopc= False

    if n % (m+1) == 0:
        print('Voce começa')
        
    else:
        print('Computador inicia')
        vezdopc=True
    while n>0:
        if vezdopc==True:
            computadortira=computador_escolhe_jogada(n,m)
            n=n-computadortira
            print('computador tirou', computadortira, 'peças')
            vezdopc=False
        else:
            jogadortira=jogador_escolhe_jogada(n,m)
            n=n-jogadortira
            print('Voce tirou', jogadortira,'peças')
            vezdopc=True
        if n==1:
            print('resta apenas 1 peça no tabuleiro')
        else:
            print('restam', n, 'peças no tabuleiro')

    print('Fim do jogo ! O computador ganhou!!')




print('\n\Bem vindo ao jogo do NIM! Escolha:')
print('1-para jogar uma partida isolada')
print('2-para jogar um campeonato')
escolha=int(input(''))
if escolha == 2:
    print('Você escolheu um campeonato')
    campeonato()
else:
    print('Você escolheu uma partida isolada')
    partida()



