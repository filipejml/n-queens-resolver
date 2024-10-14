import random
import math
from algoritmos.hill_climbing import gerar_estado_inicial, obter_custo, obter_vizinhos

def simulated_annealing(N, temp_inicial=1000, taxa_resfriamento=0.99):
    estado_atual = gerar_estado_inicial(N)
    custo_atual = obter_custo(estado_atual)
    temperatura = temp_inicial

    while temperatura > 1:
        vizinho = random.choice(obter_vizinhos(estado_atual))
        custo_vizinho = obter_custo(vizinho)
        diferenca_custo = custo_vizinho - custo_atual
        
        if diferenca_custo < 0 or random.uniform(0, 1) < math.exp(-diferenca_custo / temperatura):
            estado_atual = vizinho
            custo_atual = custo_vizinho
        
        temperatura *= taxa_resfriamento
    
    return estado_atual
