# fase3_fronteira.py - Arquivo responsável por montar o nó de busca e a fronteira de forma manual (neste caso, nossos dados são as cidades cadastradas em "mapa.py").

# Inicialmente é necessário importar os dados cadastrados no mapa.
from mapa import mapa_romenia, heuristica_bucareste

# Criando o nó inicial da busca. Neste caso, um nó é uma TUPLA com 4 posições: (f, g, cidade, caminho). Ou seja, f(n) = g(n) + h(n), g(n) é a distância JÁ PERCORRIDA (que no começo é 0), a cidade é onde estamos e o caminho é a lista de cidades que passamos até chegar nela.

inicio = 'Arad'
g = 0
h = heuristica_bucareste[inicio]
no_inicial = (g + h, g, inicio, [inicio])

# A fronteira é uma LIST que guarda todos os nós que ainda podem ser expandidos. Ou seja, no começo da busca a fronteira possui somente o nó inicial.

fronteira = [no_inicial]
print('Fronteira no começo da busca partindo de Arad:', fronteira)

# Para expandirmos um nó é necessário retirá-lo da fronteira por meio da função "pop". Neste caso, o "pop(0)" retira o PRIMEIRO nó da lista e é possível desempacotar as 4 posições da tupla em 4 variáveis.

no = fronteira.pop(0)
f_atual, g_atual, cidade_atual, caminho = no
print('\nNó retirado da fronteira:', no)
print('f =', f_atual, '| g =', g_atual, '| cidade =', cidade_atual, '| caminho =', caminho)
print('Fronteira depois de retirar o nó:', fronteira)

# Gerando os filhos (vizinhos) do nó que foi retirado. Neste caso, usamos uma estrutura de repetição para percorrer os vizinhos da cidade atual e calcular o novo g, o novo h e o novo f de cada vizinho. Além disso, o caminho de cada filho é o caminho do pai somado com o nome do vizinho.

for vizinho, custo_estrada in mapa_romenia[cidade_atual]:
    novo_g = g_atual + custo_estrada
    novo_h = heuristica_bucareste[vizinho]
    novo_f = novo_g + novo_h
    novo_caminho = caminho + [vizinho]
    fronteira.append((novo_f, novo_g, vizinho, novo_caminho))

print('\nFronteira depois de expandir Arad (na ordem em que foram inseridos):')
for item in fronteira:
    print(item)

# Ordenando a fronteira pelo valor de f(n). Neste caso, o "sort" usa a função "lambda" para informar que a ordenação deve ser feita pela POSIÇÃO 0 da tupla (que é o f). Ou seja, o nó com o MENOR f fica na primeira posição da fronteira.

fronteira.sort(key=lambda no: no[0])
print('\nFronteira ordenada pelo f (posição 0 da tupla):')
for item in fronteira:
    print(item)

# O próximo nó a ser expandido é sempre o primeiro da fronteira depois de ordenada. Ou seja, o nó com o menor f.

proximo = fronteira.pop(0)
print('\nPróximo nó a expandir:', proximo[2], 'com f =', proximo[0])

# Continuando a busca de Arad por mais um passo. Neste caso, iremos expandir "Sibiu" (que foi o nó retirado acima) e ver qual cidade a caminho de Bucharest fica com o menor f. Ou seja, os filhos de Sibiu entram na fronteira junto com os nós que já estavam nela.

f_atual, g_atual, cidade_atual, caminho = proximo
for vizinho, custo_estrada in mapa_romenia[cidade_atual]:
    novo_g = g_atual + custo_estrada
    novo_h = heuristica_bucareste[vizinho]
    novo_f = novo_g + novo_h
    novo_caminho = caminho + [vizinho]
    fronteira.append((novo_f, novo_g, vizinho, novo_caminho))

fronteira.sort(key=lambda no: no[0])
print('\nFronteira ordenada depois de expandir Sibiu:')
for item in fronteira:
    print(item)

proximo = fronteira.pop(0)
print('\nPróximo nó a expandir:', proximo[2], 'com f =', proximo[0], '| caminho =', ' -> '.join(proximo[3]))

# Além de "Arad", também iremos montar a fronteira partindo de "Timisoara" para testar o retorno. Ou seja, é feito o mesmo processo: criar o nó inicial, retirar da fronteira, gerar os filhos e ordenar pelo f.

inicio = 'Timisoara'
g = 0
h = heuristica_bucareste[inicio]
fronteira_timisoara = [(g + h, g, inicio, [inicio])]
print('\nFronteira no começo da busca partindo de Timisoara:', fronteira_timisoara)

f_atual, g_atual, cidade_atual, caminho = fronteira_timisoara.pop(0)
for vizinho, custo_estrada in mapa_romenia[cidade_atual]:
    novo_g = g_atual + custo_estrada
    novo_h = heuristica_bucareste[vizinho]
    novo_f = novo_g + novo_h
    novo_caminho = caminho + [vizinho]
    fronteira_timisoara.append((novo_f, novo_g, vizinho, novo_caminho))

fronteira_timisoara.sort(key=lambda no: no[0])
print('\nFronteira ordenada depois de expandir Timisoara:')
for item in fronteira_timisoara:
    print(item)

proximo = fronteira_timisoara.pop(0)
print('\nPróximo nó a expandir:', proximo[2], 'com f =', proximo[0], '| caminho =', ' -> '.join(proximo[3]))

# Partindo de "Rimnicu Vilcea" (que já está no meio do caminho até Bucharest) os vizinhos ficam com f MUITO menores, pois a cidade já está mais perto do objetivo. Neste caso, é possível perceber que "Pitesti" fica na frente da fronteira.

inicio = 'Rimnicu Vilcea'
g = 0
h = heuristica_bucareste[inicio]
fronteira_rimnicu = [(g + h, g, inicio, [inicio])]
print('\nFronteira no começo da busca partindo de Rimnicu Vilcea:', fronteira_rimnicu)

f_atual, g_atual, cidade_atual, caminho = fronteira_rimnicu.pop(0)
for vizinho, custo_estrada in mapa_romenia[cidade_atual]:
    novo_g = g_atual + custo_estrada
    novo_h = heuristica_bucareste[vizinho]
    novo_f = novo_g + novo_h
    novo_caminho = caminho + [vizinho]
    fronteira_rimnicu.append((novo_f, novo_g, vizinho, novo_caminho))

fronteira_rimnicu.sort(key=lambda no: no[0])
print('\nFronteira ordenada depois de expandir Rimnicu Vilcea:')
for item in fronteira_rimnicu:
    print(item)

proximo = fronteira_rimnicu.pop(0)
print('\nPróximo nó a expandir:', proximo[2], 'com f =', proximo[0], '| caminho =', ' -> '.join(proximo[3]))
