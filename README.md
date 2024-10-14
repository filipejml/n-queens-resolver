# Resolução do Problema das N-Rainhas

Este projeto implementa a solução do problema das N-rainhas utilizando três algoritmos de inteligência artificial: **Hill-Climbing**, **Simulated Annealing** e **Feixe Local**. O objetivo é encontrar uma configuração em que N rainhas possam ser posicionadas em um tabuleiro de N x N, sem que nenhuma rainha ataque outra.

## Descrição do Problema

O problema das N-rainhas consiste em colocar N rainhas em um tabuleiro de xadrez de tal forma que nenhuma rainha ataque outra. As rainhas atacam umas às outras se estiverem na mesma linha, coluna ou diagonal.

## Algoritmos Implementados

1. **Hill-Climbing**: Um algoritmo de busca local que começa com um estado inicial e tenta fazer melhorias iterativas, movendo-se para estados vizinhos que têm um custo menor.

2. **Simulated Annealing**: Um algoritmo que imita o processo de resfriamento de metais, permitindo movimentos para estados de custo maior em algumas iterações, para evitar ficar preso em ótimos locais.

3. **Feixe Local**: Uma extensão do algoritmo de Hill-Climbing que mantém múltiplos estados (k melhores) e explora os vizinhos desses estados, buscando uma solução em um espaço de busca mais amplo.

## Como Usar

### Pré-requisitos

- Python 3.x
- Bibliotecas necessárias: `random`, `time`

### Estrutura do Projeto


### Execução

Para rodar o algoritmo, execute o script `main.py`:

```bash
python main.py
Digite o número de rainhas para o teste (ou -1 para sair): 8
--- Teste para 8 rainhas ---
Hill-Climbing: 0.0234 segundos, Solução: [2, 4, 6, 1, 3, 5, 7, 0]
Simulated Annealing: 0.0456 segundos, Solução: [3, 1, 4, 6, 0, 2, 5, 7]
Feixe Local: 0.0321 segundos, Solução: [0, 4, 7, 1, 3, 6, 2, 5]

### Dicas para o `README.md`

- **Personalização**: Adapte a descrição e exemplos conforme necessário, dependendo do comportamento específico de seus algoritmos e da estrutura do seu projeto.
- **Licença**: Se você estiver usando uma licença específica, adicione um arquivo de licença ao seu projeto e faça referência a ele no `README.md`.
- **Instalação**: Se houver pacotes adicionais necessários para a execução, inclua instruções para instalação.

Sinta-se à vontade para modificar e expandir o `README` conforme a necessidade do seu projeto!
