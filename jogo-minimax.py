class NovaPartida:
    def __init__(self):
        self.tabuleiro = [' '] * 9
        self.jogador_atual = 'X'
        self.encerrado = False
        self.ganhador = None

def print_tabuleiro(tabuleiro):
    cont = 0
    for posicao in tabuleiro:
        if cont == 3:
            print('\n')
            cont = 0
        cont += 1
        print(posicao, ' | ', end="")

def print_ganhador(ganhador):
    if ganhador == 'X':
        print('Parabéns jogador X, você venceu!')
    elif ganhador == 'O':
        print('Parabéns jogador O, você venceu!')
    else:
        print('Os dois jogaram tão bem que acabou em empate!')

def check_encerrado(partida : NovaPartida):

    # Loop para checar linhas e colunas.
    for i in range(0, 3):

        ultima_jogada = partida.tabuleiro[i]
        if ultima_jogada != ' ' and ultima_jogada == partida.tabuleiro[i+3] and ultima_jogada == partida.tabuleiro[i+6]:
            partida.encerrado = True
            partida.ganhador = ultima_jogada
            return 
        else: 
            ultima_jogada = partida.tabuleiro[i*3]
            if ultima_jogada != ' ' and ultima_jogada == partida.tabuleiro[3*i+1] and ultima_jogada == partida.tabuleiro[3*i+2]:
                partida.encerrado = True
                partida.ganhador = ultima_jogada
                return
    
    # Checa a diagonal principal.
    ultima_jogada = partida.tabuleiro[0]
    if ultima_jogada != ' ' and ultima_jogada == partida.tabuleiro[4] and ultima_jogada == partida.tabuleiro[8]:
        partida.encerrado = True
        partida.ganhador = ultima_jogada
        return
    
    # Checa a diagonal inversa.
    ultima_jogada = partida.tabuleiro[2]
    if ultima_jogada != ' ' and ultima_jogada == partida.tabuleiro[4] and ultima_jogada == partida.tabuleiro[6]:
        partida.encerrado = True
        partida.ganhador = ultima_jogada
        return
    
    # Checa empate.
    if ' ' not in partida.tabuleiro:
        partida.encerrado = True
        partida.ganhador = None
        return
    
def fazer_movimento(partida : NovaPartida, posicao):
    if partida.tabuleiro[posicao] == ' ':
        partida.tabuleiro[posicao] = partida.jogador_atual
        if partida.jogador_atual == 'X':
            partida.jogador_atual = 'O'
        else:
            partida.jogador_atual = 'X'
        check_encerrado(partida)

# Lista os movimentos disponíveis no tabuleiro.
def movimentos_possiveis(partida : NovaPartida):
    movimentos = []
    for i in range(9):
        if partida.tabuleiro[i] == ' ':
            movimentos.append(i)
    return movimentos

# Avalia para quando o jogador X é o computador.
def func_avaliacao_PC_X(partida : NovaPartida):
    if partida.ganhador == 'X':
        return 1
    elif partida.ganhador == 'O':
        return -1
    elif partida.ganhador == None:
        return 0

# Avalia para quando o jogador O é o computador.
def func_avaliacao_PC_O(partida : NovaPartida):
    if partida.ganhador == 'X':
        return -1
    elif partida.ganhador == 'O':
        return 1
    elif partida.ganhador == None:
        return 0
    
def minimax(partida: NovaPartida, arvore_minimax, op):

    if partida.encerrado:
        if op == 2:
            return func_avaliacao_PC_O(partida)
        else:
            return func_avaliacao_PC_X(partida)
    
    if arvore_minimax:

        # Função MAX.
        melhor_valor = -1000
        for posicao in movimentos_possiveis(partida):
            fazer_movimento(partida, posicao)
            valor = minimax(partida, False, op)
            partida.tabuleiro[posicao] = ' '
            if ' ' in partida.tabuleiro:
                partida.encerrado = False
                partida.ganhador = None
                if partida.jogador_atual == 'X':
                    partida.jogador_atual = 'O' 
                else:
                    partida.jogador_atual = 'X'
            if valor > melhor_valor:
                    melhor_valor = valor
        return melhor_valor
    else:

        # Função MIN.
        melhor_valor = 1000
        for posicao in movimentos_possiveis(partida):
            fazer_movimento(partida, posicao)
            valor = minimax(partida, True, op)
            partida.tabuleiro[posicao] = ' '
            if ' ' in partida.tabuleiro:
                partida.encerrado = False
                partida.ganhador = None
                if partida.jogador_atual == 'X':
                    partida.jogador_atual = 'O' 
                else:
                    partida.jogador_atual = 'X'
            if valor < melhor_valor:
                    melhor_valor = valor
        return melhor_valor

# Função de decisão baseada no minimax.
def melhor_escolha(partida: NovaPartida, op):
    melhor_valor = -1000
    melhor_movimento = 0
    for posicao in movimentos_possiveis(partida):
        fazer_movimento(partida, posicao)
        if op == 3:
            valor = minimax(partida, False, op)
        elif op == 2:
            valor = minimax(partida, True, op)
        partida.tabuleiro[posicao] = ' '
        if valor > melhor_valor:
            melhor_valor = valor
            melhor_movimento = posicao
    return melhor_movimento

# Menu de opções.
while(True):
    partida = NovaPartida()

    print ('\n', '-'*5, 'JOGO DA VELHA', '-'*5)
    print('\nComo jogar: Considere que cada casa equivale a um valor de 0 a 8, como no exemplo abaixo.\nDigite o valor da casa para ocupá-la.\nOBS: O jogador X sempre começará a partida.\n')
    print('0 | 1 | 2\n3 | 4 | 5\n6 | 7 | 8\n')
    print('\n[1] - Jogador X Jogador\n[2] - Jogador X Computador (Jogador começa a partida como X)\n[3] - Computador X jogador (Computador começa a partida como X)\n[4] - Sair do jogo')
    op = int(input('Digite uma opção: '))

    if op == 1: # Jogador X Jogador.
        while(not partida.encerrado):
            print_tabuleiro(partida.tabuleiro)
            print(f'\nÉ a vez do jogador: {partida.jogador_atual}')
            mov = int(input('Nº DA CASA: '))
            print('\n')
            if mov not in movimentos_possiveis(partida):
                print('Movimento inválido, tente novamente.')
            else:
                fazer_movimento(partida, mov)
        print_ganhador(partida.ganhador)

    elif op == 2: # Jogador X Computador (Jogador começa a partida como X).
        while(not partida.encerrado):
            print_tabuleiro(partida.tabuleiro)
            print(f'\nÉ a vez do jogador: {partida.jogador_atual}')
            if partida.jogador_atual == 'X':
                mov = int(input('Nº DA CASA: '))
                print('\n')
                if mov not in movimentos_possiveis(partida):
                    print('Movimento inválido, tente novamente.')
                else:
                    fazer_movimento(partida, mov)    
            else: 
                tabuleiro = tuple(partida.tabuleiro)
                mov = melhor_escolha(partida, op)
                partida.tabuleiro = list(tabuleiro)
                partida.encerrado = False
                partida.jogador_atual = 'O'
                partida.ganhador = None
                fazer_movimento(partida, mov)  
                #print_tabuleiro(partida.tabuleiro)
                print(f'Nº DA CASA: {mov}')
                print('\n')
        print_ganhador(partida.ganhador)

    elif op == 3: # Computador X jogador (Computador começa a partida como X).
        while(not partida.encerrado):
            print_tabuleiro(partida.tabuleiro)
            print(f'\nÉ a vez do jogador: {partida.jogador_atual}')
            if partida.jogador_atual == 'X':
                tabuleiro = tuple(partida.tabuleiro)
                mov = melhor_escolha(partida, op)
                partida.tabuleiro = list(tabuleiro)
                partida.encerrado = False
                partida.jogador_atual = 'X'
                partida.ganhador = None
                fazer_movimento(partida, mov)  
                #print_tabuleiro(partida.tabuleiro)
                print(f'Nº DA CASA: {mov}')
                print('\n')    
            else: 
                mov = int(input('Nº DA CASA: '))
                print('\n')
                if mov not in movimentos_possiveis(partida):
                    print('Movimento inválido, tente novamente.')
                else:
                    fazer_movimento(partida, mov)
        print_ganhador(partida.ganhador)

    elif op == 4: # Sair.
        print('Espero que tenha se divertido;D')
        break

    else:
        print('Opção inválida, tente novamente.')
