import random
import time
from algoritmos.hill_climbing import gerar_estado_inicial, obter_custo, obter_vizinhos

def local_beam_search(N, k=10, max_tempo=60):
    estados_atuais = [gerar_estado_inicial(N) for _ in range(k)]
    tempo_inicio = time.time()

    while True:
        # Verifica o tempo limite
        if time.time() - tempo_inicio > max_tempo:
            print(f"Feixe Local: Tempo limite de {max_tempo} segundos excedido.")
            return None  # Retorna None se não encontrar uma solução em tempo hábil

        custos_atuais = [obter_custo(estado) for estado in estados_atuais]
        melhores_estados = sorted(zip(estados_atuais, custos_atuais), key=lambda x: x[1])

        if melhores_estados[0][1] == 0:  # Solução encontrada
            return melhores_estados[0][0]

        # Manter os k melhores
        estados_atuais = [estado for estado, custo in melhores_estados[:k]]
        proximos_estados = []
        for estado in estados_atuais:
            proximos_estados.extend(obter_vizinhos(estado))

        # Remover duplicatas convertendo para tuplas e de volta para listas
        estados_atuais = list(map(list, set(map(tuple, proximos_estados))))[:k]
