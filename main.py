import time
from algoritmos.hill_climbing import hill_climbing
from algoritmos.simulated_annealing import simulated_annealing
from algoritmos.local_beam_search import local_beam_search

def testar_algoritmos(N):
    print(f"\n--- Teste para {N} rainhas ---")
    
    # Hill-Climbing
    inicio_hc = time.time()
    solucao_hc = hill_climbing(N)
    tempo_hc = time.time() - inicio_hc
    print(f"Hill-Climbing: {tempo_hc:.4f} segundos, Solução: {solucao_hc}")

    # Simulated Annealing
    inicio_sa = time.time()
    solucao_sa = simulated_annealing(N)
    tempo_sa = time.time() - inicio_sa
    print(f"Simulated Annealing: {tempo_sa:.4f} segundos, Solução: {solucao_sa}")

    # Feixe Local
    inicio_lbs = time.time()
    solucao_lbs = local_beam_search(N)
    tempo_lbs = time.time() - inicio_lbs
    if solucao_lbs:
        print(f"Feixe Local: {tempo_lbs:.4f} segundos, Solução: {solucao_lbs}")
    else:
        print(f"Feixe Local: Nenhuma solução encontrada em {tempo_lbs:.4f} segundos")

if __name__ == "__main__":
    while True:
        try:
            # Solicita ao usuário a quantidade de rainhas para o teste
            N = int(input("Digite o número de rainhas para o teste (ou -1 para sair): "))
            if N == -1:
                print("Saindo do programa.")
                break  # Sai do loop se o usuário digitar -1
            testar_algoritmos(N)
        except ValueError:
            print("Por favor, insira um número válido.")
