import random
from algoritmos.hill_climbing import gerar_estado_inicial, obter_custo, obter_vizinhos

def local_beam_search(N, k=10):
    estados_atuais = [gerar_estado_inicial(N) for _ in range(k)]
    
    while True:
        custos_atuais = [obter_custo(estado) for estado in estados_atuais]
        melhores_estados = sorted(zip(estados_atuais, custos_atuais), key=lambda x: x[1])
        if melhores_estados[0][1] == 0:  # Solução encontrada
            return melhores_estados[0][0]

        # Manter os k melhores
        estados_atuais = [estado for estado, custo in melhores_estados[:k]]
        proximos_estados = []
        for estado in estados_atuais:
            proximos_estados.extend(obter_vizinhos(estado))
        
        # Convertendo para tupla para poder usar o set, e depois de volta para lista
        estados_atuais = list(map(list, set(map(tuple, proximos_estados))))[:k]
