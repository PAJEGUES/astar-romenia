# fase1_explorar.py - Arquivo responsável por explorar os dados (neste caso, nossos dados são as cidades cadastradas em "mapa.py").

# Inicialmente é necessário importar os dados cadastrados no mapa.
from mapa import mapa_romenia, heuristica_bucareste

# Por meio do uso da função "len" é possível descobrir o tamanho do dicionário que criamos. Neste caso, este valor também é considerado como a quantidade de cidades do mapa da Romênia. Além disto, é possível descobrir quantas heurísticas existem dentro do mapa.
print('Quantidade de CIDADES Cadastradas no mapa da Romênia:', len(mapa_romenia))
print('Quantidade de HEURÍSTICAS Cadastradas no mapa da Romênia:', len(heuristica_bucareste))

# Quando criamos o dicionário e informamos o nome de cada cidade, na verdade passamos o nome das cidades vizinhas e a distância destas cidades até Arad. Ou seja, além de puxarmos os vizinhos da cidade "Arad", também iremos puxar os vizinhos de "Timisoara" para testar o retorno.

vizinhos_arad = mapa_romenia['Arad']
print('\nTodos os Vizinhos de Arad:', vizinhos_arad)

vizinhos_timisoara = mapa_romenia['Timisoara']
print('Todos os Vizinhos de Timisoara:', vizinhos_timisoara)

# A partir do momento que puxamos uma chave do dicionário, puxamos TODAS AS LISTS que compõem ele. Porém, é possível também puxarmos individualmente as TUPLAS que compõem estas lists. Ou seja, cada vizinho da cidade especificada e a heurística até Bucharest.

dados_arad = vizinhos_arad[0]
print('\nPrimeira Cidade Vizinha de Arad:', dados_arad[0])
print('Heurística de', dados_arad[0], 'até Bucarest:', dados_arad[1])

# Além disso, também é possível usar estruturas de repetição para percorrermos as chaves do dicionário e encontrarmos todas as tuplas registradas em cada chave. Ou seja, conseguimos usar este conceito para descobrirmos todos os vizinhos de uma cidade por meio de uma repetição.

print('\nDistância de Arad até os seus vizinhos:')
for vizinho, custo in mapa_romenia['Arad']:
    print('Distância de Arad ->', vizinho, '=', custo, 'km')

print('\nDistância de Timisoara até os seus vizinhos:')
for vizinho, custo in mapa_romenia['Timisoara']:
    print('Distância de Timisoara ->', vizinho, '=', custo, 'km')

# Para descobrirmos quantos vizinhos cada cidade possui, podemos usar uma estrutura de repetição passando o mapa todo como parâmetro.

print('\nQuantidade de vizinhos de cada cidade:')
for cidade in mapa_romenia:
    quantidade_vizinhos = len(mapa_romenia[cidade])
    print(f'{cidade:<15} {quantidade_vizinhos} Vizinho(s) ou Estrada(s)')

# Quando é necessário descobrir a distância em linha reta de uma cidade até Bucharest (que é o objetivo deste algoritmo) podemos usarmos também uma estrutura de repetição buscando a heurística de cada cidade e seus vizinhos. Neste caso, a heurística é chamada de h(n) onde "n" é a cidade de referência.

print('\nA distância em linha reta de Arad até Bucareste em KM é:', heuristica_bucareste['Arad'])
print('A distância em linha reta de CADA VIZINHO de Arad até Bucareste em KM é:')
for vizinho, custo in mapa_romenia['Arad']:
    h = heuristica_bucareste[vizinho]
    print(f'{vizinho:<10} h = {h:>3} km em linha reta até Bucareste')
