# fase4_expandir.py - Arquivo responsável por transformar a expansão de um nó em função e repetir a busca de forma manual (neste caso, nossos dados são as cidades cadastradas em "mapa.py").

# Inicialmente é necessário importar os dados cadastrados no mapa.
from mapa import mapa_romenia, heuristica_bucareste

# Criando uma função para mostrarmos a fronteira de forma resumida. Neste caso, ao invés de imprimir a tupla inteira de cada nó, iremos mostrar somente o nome da cidade e o valor de f. Ou seja, cada nó aparece como Cidade(f=...).

def mostrar_fronteira(fronteira):
    partes = []
    for f, g, cidade, caminho in fronteira:
        partes.append(f'{cidade}(f={f})')
    print('Fronteira:', ', '.join(partes))

# Criando uma função para expandirmos um nó. Neste caso, a função percorre os vizinhos da cidade do nó e devolve uma LIST com os nós filhos. Porém, caso o vizinho já esteja no conjunto de EXPLORADOS, o "continue" pula esse vizinho para que a busca não volte para uma cidade que já foi visitada.

def expandir(no, explorados):
    f_atual, g_atual, cidade_atual, caminho = no
    filhos = []
    for vizinho, custo_estrada in mapa_romenia[cidade_atual]:
        if vizinho in explorados:
            continue
        novo_g = g_atual + custo_estrada
        novo_f = novo_g + heuristica_bucareste[vizinho]
        filhos.append((novo_f, novo_g, vizinho, caminho + [vizinho]))
    return filhos

# Testando a função expandir com o nó de "Sibiu" vindo de "Arad". Ou seja, quando "Arad" já está nos explorados ela NÃO aparece como filho de Sibiu, e quando o conjunto está vazio ela aparece.

no_sibiu = (393, 140, 'Sibiu', ['Arad', 'Sibiu'])
print('Filhos de Sibiu SEM explorados:')
mostrar_fronteira(expandir(no_sibiu, set()))
print('Filhos de Sibiu com Arad nos explorados:')
mostrar_fronteira(expandir(no_sibiu, {'Arad'}))

# Preparando a fronteira e o conjunto de explorados partindo de "Arad". Neste caso, o conjunto de explorados é um SET (que não aceita valores repetidos) e no começo ele é vazio.

inicio = 'Arad'
fronteira = [(heuristica_bucareste[inicio], 0, inicio, [inicio])]
explorados = set()

# Repetindo três rodadas de forma manual (ainda sem o while). Ou seja, em cada rodada a fronteira é ordenada pelo f, o primeiro nó é retirado, a cidade é adicionada nos explorados e os filhos dela entram na fronteira.

print('\nBusca partindo de Arad:')
for rodada in [1, 2, 3]:
    fronteira.sort(key=lambda no: no[0])
    no = fronteira.pop(0)
    cidade = no[2]
    explorados.add(cidade)
    print(f'\nRodada {rodada}: expandindo {cidade} (f={no[0]}, g={no[1]})')
    fronteira = fronteira + expandir(no, explorados)
    mostrar_fronteira(fronteira)
    print('Explorados:', sorted(explorados))

# Além de "Arad", também iremos repetir as rodadas partindo de "Timisoara" para testar o retorno. Neste caso, é feito o mesmo processo, porém com uma nova fronteira e um novo conjunto de explorados.

inicio = 'Timisoara'
fronteira = [(heuristica_bucareste[inicio], 0, inicio, [inicio])]
explorados = set()

print('\nBusca partindo de Timisoara:')
for rodada in [1, 2, 3]:
    fronteira.sort(key=lambda no: no[0])
    no = fronteira.pop(0)
    cidade = no[2]
    explorados.add(cidade)
    print(f'\nRodada {rodada}: expandindo {cidade} (f={no[0]}, g={no[1]})')
    fronteira = fronteira + expandir(no, explorados)
    mostrar_fronteira(fronteira)
    print('Explorados:', sorted(explorados))

# Partindo de "Rimnicu Vilcea" (que já está no meio do caminho até Bucharest) as três rodadas já são suficientes para chegar em Bucharest. Ou seja, na rodada 3 a cidade expandida é a própria Bucharest, porém a busca ainda não sabe parar sozinha (isso será feito na fase 5 com o while).

inicio = 'Rimnicu Vilcea'
fronteira = [(heuristica_bucareste[inicio], 0, inicio, [inicio])]
explorados = set()

print('\nBusca partindo de Rimnicu Vilcea:')
for rodada in [1, 2, 3]:
    fronteira.sort(key=lambda no: no[0])
    no = fronteira.pop(0)
    cidade = no[2]
    explorados.add(cidade)
    print(f'\nRodada {rodada}: expandindo {cidade} (f={no[0]}, g={no[1]})')
    fronteira = fronteira + expandir(no, explorados)
    mostrar_fronteira(fronteira)
    print('Explorados:', sorted(explorados))
