# a_estrela.py - Arquivo responsável pelo programa COMPLETO da busca A* (neste caso, nossos dados são as cidades cadastradas em "mapa.py").

# Lembrando que a busca A* escolhe sempre o nó com o menor f(n), onde f(n) = g(n) + h(n). Ou seja, g(n) é a distância em KM que JÁ FOI percorrida desde a cidade de origem até "n" (custo real), h(n) é a distância em linha reta de "n" até Bucharest (heurística) e f(n) é a estimativa do custo TOTAL do caminho que passa por "n".

# Inicialmente é necessário importar os dados cadastrados no mapa.
from mapa import mapa_romenia, heuristica_bucareste

# Criando uma função para mostrarmos a fronteira de forma resumida. Neste caso, cada nó aparece como Cidade(f) separados por vírgula. Ou seja, é a mesma ideia da função "mostrar_fronteira" da fase 4, porém agora ela devolve o texto ao invés de imprimir.

def resumo_fronteira(fronteira):
    return ', '.join(f'{cidade}({f})' for f, g, cidade, caminho in fronteira)

# Criando a função de busca A*. Neste caso, além da cidade de início e da cidade objetivo, a função também recebe o GRAFO (o mapa) e a HEURÍSTICA como parâmetro. Ou seja, a função pode ser usada com qualquer mapa e não somente com o mapa da Romênia. Além disso, o parâmetro "mostrar" informa se a função deve imprimir o rastro de cada iteração ou não.

# Cada nó da fronteira continua sendo a tupla (f, g, cidade, caminho). O f fica na POSIÇÃO 0 porque é por ele que a fronteira é ordenada.

def busca_a_estrela(inicio, objetivo, grafo, heuristica, mostrar=True):
    fronteira = [(heuristica[inicio], 0, inicio, [inicio])]
    explorados = set()
    iteracao = 0

    if mostrar:
        print(f'--- Busca A* de {inicio} para {objetivo} ---')

    while fronteira:
        # Contando as iterações, ordenando a fronteira pelo f e retirando o nó com o MENOR f.
        iteracao = iteracao + 1
        fronteira.sort(key=lambda no: no[0])
        f_atual, g_atual, cidade_atual, caminho = fronteira.pop(0)

        if mostrar:
            print(f'{iteracao}. Expandindo: {cidade_atual} | '
                  f'g(n)={g_atual}, h(n)={heuristica[cidade_atual]} '
                  f'-> f(n)={f_atual}')

        # O teste de objetivo é feito no momento em que o nó é RETIRADO da fronteira, assim como na fase 5.
        if cidade_atual == objetivo:
            return caminho, g_atual

        # Caso a cidade já tenha sido explorada por um caminho melhor, o "continue" descarta este nó.
        if cidade_atual in explorados:
            continue
        explorados.add(cidade_atual)

        # Gerando os filhos da cidade atual. Neste caso, o "grafo.get" devolve uma lista vazia caso a cidade não exista no grafo, ou seja, a busca não quebra com uma cidade desconhecida.
        for vizinho, custo_estrada in grafo.get(cidade_atual, []):
            if vizinho not in explorados:
                novo_g = g_atual + custo_estrada
                novo_f = novo_g + heuristica[vizinho]
                fronteira.append((novo_f, novo_g, vizinho, caminho + [vizinho]))

        if mostrar:
            fronteira.sort(key=lambda no: no[0])
            print('Fronteira:', resumo_fronteira(fronteira))

    return None, float('inf') # Caso o while termine sem encontrar o objetivo, o caminho que irá constar para o usuário é None e o custo é infinito.

# Criando uma função para mostrarmos o resultado da busca. Neste caso, caso a busca encontre um caminho é mostrado o caminho, o custo TOTAL e a quantidade de passos. Porém, caso a busca não encontre nenhum caminho é mostrada uma mensagem para o usuário.

def mostrar_resultado(caminho, custo):
    print('\n--- Resultado ---')
    if caminho:
        print('Caminho encontrado:', ' -> '.join(caminho))
        print(f'Custo real total: {custo} km em {len(caminho) - 1} passos')
    else:
        print('Não foi possível encontrar um caminho.')

# Criando uma função para conferirmos se o resultado da busca é o resultado esperado (teste de regressão). Ou seja, caso alguma alteração no código mude o resultado, esta função avisa o usuário.

def conferir(caminho, custo, custo_esperado, passos_esperados):
    if caminho and custo == custo_esperado and len(caminho) - 1 == passos_esperados:
        print(f'Conferido: {custo_esperado} km em {passos_esperados} passos.')
    else:
        print(f'ATENÇÃO: era esperado {custo_esperado} km em {passos_esperados} passos. Revise o código.')

# Criando o programa principal. Neste caso, a busca é feita com o rastro completo partindo de "Arad", "Timisoara" e "Rimnicu Vilcea" e no fim é mostrado somente o resultado de outras cidades.

def main():
    # Partindo de "Arad" o livro diz que o melhor caminho possui 418 km em 4 passos.
    caminho, custo = busca_a_estrela('Arad', 'Bucharest', mapa_romenia, heuristica_bucareste)
    mostrar_resultado(caminho, custo)
    conferir(caminho, custo, 418, 4)

    # Partindo de "Timisoara" a fase 5 mostrou que o melhor caminho possui 536 km em 5 passos (voltando por Arad e descendo por Rimnicu Vilcea e Pitesti).
    print()
    caminho, custo = busca_a_estrela('Timisoara', 'Bucharest', mapa_romenia, heuristica_bucareste)
    mostrar_resultado(caminho, custo)
    conferir(caminho, custo, 536, 5)

    # Partindo de "Rimnicu Vilcea" (que já está no meio do caminho até Bucharest) a fase 5 mostrou que o melhor caminho possui 198 km em 2 passos (por Pitesti).
    print()
    caminho, custo = busca_a_estrela('Rimnicu Vilcea', 'Bucharest', mapa_romenia, heuristica_bucareste)
    mostrar_resultado(caminho, custo)
    conferir(caminho, custo, 198, 2)

    # Para as outras cidades usamos uma estrutura de repetição com o parâmetro "mostrar=False". Ou seja, a busca NÃO imprime o rastro e é mostrado somente o resultado final de cada cidade.
    print('\n--- Outras origens (sem rastro) ---')
    for origem in ['Oradea', 'Craiova', 'Lugoj', 'Iasi', 'Eforie']:
        caminho, custo = busca_a_estrela(origem, 'Bucharest', mapa_romenia, heuristica_bucareste, mostrar=False)
        if caminho:
            print(f'{origem:<10} {custo:>4} km  ', ' -> '.join(caminho))
        else:
            print(f'{origem:<10} sem caminho até Bucharest') # Caso a busca devolva None, o "join" não é executado para que o programa não quebre.

    # Testando a busca com uma cidade que NÃO existe no mapa. Neste caso, como a cidade também não existe na heurística, o Python gera um erro (KeyError) e o "try/except" trata essa exceção mostrando uma mensagem para o usuário.
    print('\n--- Cidade que não existe no mapa ---')
    try:
        busca_a_estrela('Sao Paulo', 'Bucharest', mapa_romenia, heuristica_bucareste, mostrar=False)
    except KeyError as erro:
        print('A cidade', erro, 'não está cadastrada no mapa da Romênia.')

# O main() só é executado quando o arquivo é rodado diretamente (python a_estrela.py). Ou seja, caso este arquivo seja importado por outro arquivo, a busca não é executada sozinha.
if __name__ == '__main__':
    main()
