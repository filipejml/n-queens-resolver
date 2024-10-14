import random

def gerar_estado_inicial(N):
    return [random.randint(0, N-1) for _ in range(N)]

def obter_custo(estado):
    ataques = 0
    N = len(estado)
    for i in range(N):
        for j in range(i + 1, N):
            if estado[i] == estado[j] or abs(estado[i] - estado[j]) == abs(i - j):
                ataques += 1
    return ataques

def obter_vizinhos(estado):
    vizinhos = []
    N = len(estado)
    for i in range(N):
        for j in range(N):
            if j != estado[i]:
                novo_estado = estado[:]
                novo_estado[i] = j
                vizinhos.append(novo_estado)
    return vizinhos

def hill_climbing(N):
    estado = gerar_estado_inicial(N)
    while True:
        custo = obter_custo(estado)
        vizinhos = obter_vizinhos(estado)
        proximo_estado = min(vizinhos, key=obter_custo)
        proximo_custo = obter_custo(proximo_estado)
        if proximo_custo >= custo:
            break
        estado = proximo_estado
    return estado
