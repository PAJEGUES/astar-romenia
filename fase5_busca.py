# fase5_busca.py - Arquivo responsável por criar a busca A* com o laço while que repete a expansão até chegar no objetivo (neste caso, nossos dados são as cidades cadastradas em "mapa.py").

# Inicialmente é necessário importar os dados cadastrados no mapa.
from mapa import mapa_romenia, heuristica_bucareste

# Criando a função de busca A*. Neste caso, a função recebe a cidade de início e a cidade objetivo e devolve o MELHOR caminho e o custo dele. Ou seja, é o mesmo processo das rodadas da fase 4, porém agora o "while" repete a expansão sozinho enquanto existir algum nó na fronteira. Caso a fronteira fique vazia e o objetivo não seja encontrado, a função devolve None e infinito.

def busca_a_estrela(inicio, objetivo):
    fronteira = [(heuristica_bucareste[inicio], 0, inicio, [inicio])]
    explorados = set()

    while fronteira:
        # Ordenando a fronteira pelo f e retirando o nó com o MENOR f.
        fronteira.sort(key=lambda no: no[0])
        f_atual, g_atual, cidade_atual, caminho = fronteira.pop(0)

        # O teste de objetivo é feito no momento em que o nó é RETIRADO da fronteira e não quando ele é gerado. Ou seja, assim temos certeza de que nenhum outro caminho mais barato ficou para trás.
        if cidade_atual == objetivo:
            return caminho, g_atual

        # Caso a cidade já tenha sido explorada por um caminho melhor, o "continue" descarta este nó.
        if cidade_atual in explorados:
            continue
        explorados.add(cidade_atual)

        # Gerando os filhos da cidade atual e colocando eles na fronteira (somente os que ainda não foram explorados).
        for vizinho, custo_estrada in mapa_romenia[cidade_atual]:
            if vizinho not in explorados:
                novo_g = g_atual + custo_estrada
                novo_f = novo_g + heuristica_bucareste[vizinho]
                fronteira.append((novo_f, novo_g, vizinho, caminho + [vizinho]))

    return None, float('inf') # Caso o while termine sem encontrar o objetivo, o caminho que irá constar para o usuário é None e o custo é infinito.

# Testando a função de busca partindo de "Arad". Lembrando que a heurística cadastrada em "mapa.py" é a distância em linha reta até Bucharest, por isso o objetivo é sempre "Bucharest".

caminho, custo = busca_a_estrela('Arad', 'Bucharest')
print('Melhor caminho de Arad até Bucharest:', ' -> '.join(caminho))
print('Custo TOTAL do caminho:', custo, 'km')
print('Quantidade de estradas percorridas:', len(caminho) - 1)

# Além de "Arad", também iremos testar a busca partindo de "Timisoara". Neste caso, na fase 2 testamos somente dois caminhos (por Arad e Fagaras com 568 km e por Lugoj com 615 km). Porém, a busca encontra um caminho AINDA MELHOR que nenhum dos dois: voltando por Arad e descendo por Rimnicu Vilcea e Pitesti, com 536 km. Ou seja, é por isso que precisamos da busca A* ao invés de testar os caminhos de forma manual.

caminho, custo = busca_a_estrela('Timisoara', 'Bucharest')
print('\nMelhor caminho de Timisoara até Bucharest:', ' -> '.join(caminho))
print('Custo TOTAL do caminho:', custo, 'km')
print('Quantidade de estradas percorridas:', len(caminho) - 1)

# Partindo de "Rimnicu Vilcea" (que já está no meio do caminho até Bucharest) a busca deve escolher o caminho por Pitesti, pois na fase 2 vimos que ele custa 198 km contra 390 km do caminho por Fagaras.

caminho, custo = busca_a_estrela('Rimnicu Vilcea', 'Bucharest')
print('\nMelhor caminho de Rimnicu Vilcea até Bucharest:', ' -> '.join(caminho))
print('Custo TOTAL do caminho:', custo, 'km')
print('Quantidade de estradas percorridas:', len(caminho) - 1)

# Para descobrirmos o melhor caminho de TODAS as cidades até Bucharest, podemos usar uma estrutura de repetição passando o mapa todo como parâmetro. Ou seja, a função de busca é chamada uma vez para cada cidade cadastrada.

print('\nMelhor caminho de cada cidade até Bucharest:')
for cidade in mapa_romenia:
    caminho, custo = busca_a_estrela(cidade, 'Bucharest')
    print(f'{cidade:<15} {custo:>4} km   {" -> ".join(caminho)}')
