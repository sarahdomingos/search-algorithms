
# As condições de movimento foram baseadas no artigo: 
# http://www.inf.ufsc.br/grafos/temas/travessia/canibais.htm


# Verifica o pai do nó, evitando loops nas movimentações.
def check_parent (node, parents, new_node):
    key = str(node)
    n = str(new_node)
    if (parents[key] == n): 
        return False
    else:
        return True

def next_move (node, parents):
    new_node = {}
    boat_side = node['Side']

    # Verifica os movimentos possíveis no lado esquerdo da margem.
    if boat_side == 'left':
        cL = node['C']
        mL = node['M']
        cR = 3 - cL
        mR = 3 - mL

        # Condição para enviar 1 ou 2 canibais.
        if cL > 0:
            if cL < 2:
                t = 1
            else:
                t = 2
        if cL > 0 and (mR >= cR + t or mR == 0):
            new_node = {'C' : cR + t,'M' : mR,'Side' : 'right'}
            if check_parent(node, parents, new_node):
                return new_node
            else:
                t = 1
                new_node = {'C' : cR + t,'M' : mR,'Side' : 'right'}
                if check_parent(node, parents, new_node):
                    return new_node

        # Condição para enviar 1 ou 2 missionários.
        if mL > 0:
            if mL < 2:
                t = 1
            else:
                t = 2
        if mL > 0 and (cL <= mL - t or mL - t == 0) and (cR == 0 or cR <= mR + t):
            new_node = {'C' : cR,'M' : mR + t,'Side' : 'right'}
            if check_parent(node, parents, new_node):
                return new_node

        # Condição para enviar 1 missionário e 1 canibal.
        if (cL > 0 and mL > 0) and (cR == 0 or cR <= mR):
            new_node = {'C' : cR + 1,'M' : mR + 1,'Side' : 'right'}
            if check_parent(node, parents, new_node):
                return new_node

    # Verifica os movimentos possíveis no lado direito da margem.
    else:
        cR = node['C']
        mR = node['M']
        cL = 3 - cR
        mL = 3 - mR

        # Condição para enviar 1 ou 2 canibais.
        if cR > 0:
            if cR < 2:
                t = 1
            else:
                t = 2
        if cR > 0 and (mL >= cL + t or mL == 0):
            new_node = {'C' : cL + t,'M' : mL,'Side' : 'left'}
            if check_parent(node, parents, new_node):
                return new_node
            else:
                t = 1
                new_node = {'C' : cL + t,'M' : mL,'Side' : 'left'}
                if check_parent(node, parents, new_node):
                    return new_node

        # Condição para enviar 1 ou 2 missionários.
        if mR > 0:
            if mR < 2:
                t = 1
            else:
                t = 2
        if mR > 0 and (cR <= mR - t or mR - t == 0) and (cL == 0 or cL <= mL + t):
            new_node = {'C' : cL,'M' : mL + t,'Side' : 'left'}
            if check_parent(node, parents, new_node):
                return new_node

        # Condição para enviar 1 missionário e 1 canibal.
        if (cR > 0 and mR > 0) and (cL == 0 or cL <= mL):
            new_node = {'C' : cL + 1,'M' : mL + 1,'Side' : 'left'}
            if check_parent(node, parents, new_node):
                return new_node

def print_result (node):
    if node['Side'] == 'left':
        cL = node['C']
        mL = node['M']
        cR = 3 - cL
        mR = 3 - mL
        print(f'C: {cL}, M: {mL} |\U0001F6F6        | C: {cR}, M: {mR}')

    else:
        cR = node['C']
        mR = node['M']
        cL = 3 - cR
        mL = 3 - mR
        print(f'C: {cL}, M: {mL} |        \U0001F6F6| C: {cR}, M: {mR}')

# Função de busca.
def missionaries_cannibals (start, goal):

    # Inicialização do nó de origem.
    node = start
    key = str(node)
    parents = {key: key}
    distance = {key: 0}

    while True:
        print_result(node)

        # Checa se já encontrou o objetivo.
        if node == goal:
            print(f'Movimentos realizados: {distance[key]}')
            break
        
        # Armazena o nó atual como pai para gerar o nó filho.
        parent = str(node)
        node = next_move (node, parents)
        key = str(node)

        # Condição para escolher a melhor solução dada a menor distância, caso o nó já tenha sido registrado.
        if distance.get(key):
            dist_new_node = distance[parent] + 1
            dist_old = distance[key]
            if dist_new_node < dist_old:
                distance[key] = dist_new_node
                parents[key] = parent
        else:
            parents = {key: parent}
            dist = distance[parent] + 1
            distance = {key: dist}

# Início do algoritmo.
start = {
    'C': 3,
    'M': 3,
    'Side' : 'right'
}

goal = {
    'C': 3,
    'M': 3,
    'Side' : 'left'
}

missionaries_cannibals (start, goal)