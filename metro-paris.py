"""
Considere que o passageiro na estação E11 deseja chegar a E7

horas = distancia / 30
baldeacao = 4 / 60 = 0.06
"""
import heapq

def buscaAEstrela(mapa, estadoInicial, estadoFinal):
    fn = estadoInicial[1] + 0 # f(n) = g(n) + h(n)
    no = {fn: estadoInicial[0]}
    estacao = estadoInicial
    linha = estacao[2]
    noList = list(no.items())
    borda = []
    borda.append(noList)
    explorado = []
    #print(no)
    while(True):
        if len(borda) == 0:
            print("Solução não encontrada.")
            break
        heapq.heapify(borda)
        no = borda.pop(0)
        fn = no[0][0]
        print(no)
        if estacao == estadoFinal and no[0] <= fn:
            return no
        explorado.append(no)
        #print(estacao)
        #no[1] = 'E3'
        for i in range(0, len(mapa)):
            if no[0][1] == mapa[i][0]:
                estacao = mapa[i]
                break
        vizinhos = dict(estacao[3])
        #print(vizinhos)
        for filho in vizinhos.items():
            #print(filho)
            for j in range(0, len(mapa)):
                if filho[0] == mapa[j][0]:
                    estacaoVizinha = mapa[j]
                    #print(estacaoVizinha)
                    break
                    
            noList = list(filho)
            if noList not in borda or noList not in explorado:
                borda.append(noList)
            #else if 

            for linhaVizinha in estacaoVizinha[2]:
                if linhaVizinha == linha:
                    fn = 0
                    break
                fn = 0.06

            
            

        
        break

def custoTempo(custoObjetivo):
    return round(custoObjetivo/30, 2)

def inserirEstacao(mapa, nome, custoTempo, linha, vizinhos):
    estacao = [nome, custoTempo, linha, vizinhos]
    mapa.append(estacao)

mapa = []

inserirEstacao(mapa, 'E1', custoTempo(39), ['azul'], {'E2': custoTempo(11)})
inserirEstacao(mapa, 'E2', custoTempo(28), ['azul', 'amarelo'], {'E1': custoTempo(11), 'E10': custoTempo(4), 'E9': custoTempo(11), 'E3': custoTempo(9)})
inserirEstacao(mapa, 'E3', custoTempo(19), ['azul', 'vermelho'], {'E2': custoTempo(9), 'E9': custoTempo(10), 'E4': custoTempo(7), 'E13': custoTempo(13)})
inserirEstacao(mapa, 'E4', custoTempo(12), ['azul', 'verde'], {'E3': custoTempo(7), 'E8': custoTempo(13), 'E13': custoTempo(11), 'E5': custoTempo(13)})
inserirEstacao(mapa, 'E5', custoTempo(2), ['azul', 'amarelo'], {'E4': custoTempo(13), 'E7': custoTempo(2), 'E6': custoTempo(3), 'E8': custoTempo(21)})
inserirEstacao(mapa, 'E6', custoTempo(4), ['azul'], {'E5': custoTempo(3)})
inserirEstacao(mapa, 'E7', custoTempo(0), ['amarelo'], {'E5': custoTempo(2)})
inserirEstacao(mapa, 'E8', custoTempo(22), ['amarelo', 'verde'], {'E9': custoTempo(9), 'E12': custoTempo(7), 'E5': custoTempo(21), 'E4': custoTempo(13)})
inserirEstacao(mapa, 'E9', custoTempo(25), ['amarelo', 'vermelho'], {'E11': custoTempo(12), 'E2': custoTempo(11), 'E3': custoTempo(10), 'E8': custoTempo(9)})
inserirEstacao(mapa, 'E10', custoTempo(29), ['amarelo'], {'E2': custoTempo(4)})
inserirEstacao(mapa, 'E11', custoTempo(38), ['vermelho'], {'E9': custoTempo(12)})
inserirEstacao(mapa, 'E12', custoTempo(28), ['verde'], {'E8': custoTempo(7)})
inserirEstacao(mapa, 'E13', custoTempo(13), ['vermelho', 'verde'], {'E14': custoTempo(5), 'E3': custoTempo(13), 'E4': custoTempo(11)})
inserirEstacao(mapa, 'E14', custoTempo(17), ['verde'], {'E13': custoTempo(5)})

#for i in mapa:
 #   print(i)

estadoInicial = mapa[10]
estadoFinal = mapa[6]

buscaAEstrela(mapa, estadoInicial, estadoFinal)



