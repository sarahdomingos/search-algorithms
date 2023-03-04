import heapq

class estacao:
    def __init__(self, nome, distancias, vizinhos):
        self.nome: int = nome
        self.distancias: list = distancias
        self.vizinhos: list = vizinhos
        self.custo_fn = 0
        self.linha = ''
        self.pai = 0

e1 = estacao(1, [0, 22,	40,	54,	80,	86,	78,	56,	36,	20,	36,	60,	60,	64], [(2, 'azul')])
e2 = estacao(2, [22, 0,	18,	32,	58,	64,	56,	38,	22,	8, 34, 46, 42, 48], [(1, 'azul'), (3, 'azul'), (9, 'amarelo'), (10, 'amarelo')])
e3 = estacao(3, [40, 18, 0,	14,	40,	44,	38,	30,	20,	22,	42,	42,	26,	36], [(2, 'azul'), (4, 'azul'), (9, 'vermelho'), (13, 'vermelho')])
e4 = estacao(4, [54, 32, 14, 0,	26,	32,	24,	26,	26,	36,	52,	42,	22,	34], [(3, 'azul'), (5, 'azul'), (8, 'verde'), (13, 'verde')])
e5 = estacao(5, [80, 58, 40, 26, 0,	6,	4,	42,	50,	62,	76,	54,	32,	40], [(4, 'azul'), (8, 'amarelo'), (7, 'amarelo'), (6, 'azul')])
e6 = estacao(6, [86,64,	44,	32,	6,	0,	8,	46,	56,	66,	82,	60,	34,	40], [(5, 'azul')])
e7 = estacao(7, [78,56,	38,	24,	4,	8,	0,	44,	50,	58,	76,	56,	26,	34], [(5, 'amarelo')])
e8 = estacao(8, [56,38,	30,	26,	42,	46,	44,	0,	18,	44,	36,	14,	50,	60], [(9, 'amarelo'), (5, 'amarelo'), (12, 'verde'), (4, 'verde')])
e9 = estacao(9, [36,22,	20,	26,	50,	56,	50,	18,	0,	26,	24,	24,	46,	56], [(2, 'amarelo'), (8, 'amarelo'), (11, 'vermelho'), (3, 'vermelho')])
e10 = estacao(10, [20,8,22,	36,	62,	66,	58,	44,	26,	0,	40,	54,	40,	46], [(2, 'amarelo')])
e11 = estacao(11, [36,34,42,52,	76,	82,	76,	36,	24,	40,	0,	30,	70,	78], [(9, 'vermelho')])
e12 = estacao(12, [60,46,42,42,	54,	60,	56,	14,	24,	54,	30,	0,	62,	74], [(8, 'verde')])
e13 = estacao(13, [60,	42,	26,	22,	32,	34,	26,	50,	46,	40,	70,	62,	0,	10], [(3, 'vermelho'), (4, 'verde'), (14, 'verde')])
e14 = estacao(14, [64,	48,	36,	34,	40,	40,	34,	60,	56,	46,	78,	74,	10,	0], [(13, 'verde')])
mapa = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14]

def buscaAEstrela(origem: estacao, destino: estacao):

    explorado = []
    borda = [(origem.custo_fn, origem.nome)]

    while(True):
        
        if len(borda) == 0:
            print('Solução não encontrada.')
            break
        
        # Lista ordenada do menor ao maior.
        heapq.heapify(borda)
        estacao_atual = borda.pop(0)
        
        # Busca a estação da borda no mapa.
        for i in mapa:
            if estacao_atual[1] == i.nome and estacao_atual[0] == i.custo_fn:
                estacao_atual = i
                break

        if estacao_atual.nome == destino.nome:
            pai = estacao_atual.pai
            tempoTotal = estacao_atual.distancias[pai - 1]
            caminho = [(estacao_atual.nome, estacao_atual.distancias[pai - 1])]

            while pai != origem.nome:
                for no in explorado:
                    if pai == no.nome:
                        pai = no.pai
                        caminho.append((no.nome, no.distancias[pai - 1]))
                        tempoTotal += no.distancias[pai - 1]
                        break

            caminho.append((origem.nome, 0))
            caminho.reverse()

            print(f'\nTempo total: {tempoTotal} min')
            for i in caminho:
                print(f'Estação: E{i[0]} - Tempo: {i[1]} min')
            break
        
        # Enquanto a solução não é encontrada, a estação entra para explorado.
        explorado.append(estacao_atual)

        for vizinho in estacao_atual.vizinhos:
            for i in mapa:
                if vizinho[0] == i.nome:

                    # Custo A* dos filhos da estação atual.
                    custo_fn = estacao_atual.custo_fn + i.distancias[estacao_atual.nome - 1] + i.distancias[destino.nome - 1]
                    
                    # Checagem da baldeação.
                    if vizinho[1] != estacao_atual.linha and estacao_atual.linha != '':
                            custo_fn += 4
                    
                    # Criação de novos caminhos com os filhos da estação atual.
                    if i not in explorado and (custo_fn, i.nome) not in borda and i.nome != estacao_atual.pai:
                        novo = estacao(i.nome, i.distancias, i.vizinhos)
                        novo.custo_fn = custo_fn
                        novo.pai = estacao_atual.nome
                        novo.linha = vizinho[1]
                        borda.append((novo.custo_fn, novo.nome))
                        mapa.append(novo)

                    break
                    
# Início da função dada origem e destino.                
buscaAEstrela(e4, e11)


