# fase2_caminhos.py - Arquivo responsável por fornecer as funções de navegação dos dados (neste caso, nossos dados são as cidades cadastradas em "mapa.py").

# Inicialmente é necessário importar os dados cadastrados no mapa.
from mapa import mapa_romenia, heuristica_bucareste

# Criando uma função para registrarmos o custo de uma estrada partindo de uma cidade de origem até a cidade de destino. Neste caso, usamos uma estrutura de repetição para verificarmos se a cidade que foi lida pelo FOR é a mesma que informamos para ser a de destino. Porém, caso seja informado uma cidade de destino que NÃO é vizinha da cidade de origem, a função não encontra nenhuma estrada e devolve None.

def custo_da_estrada(origem, destino):
    for vizinho, custo in mapa_romenia[origem]:
        if vizinho == destino:
            return custo
    return None # Caso o FOR não encontre uma cidade vizinha da cidade informada de Origem, o nome que irá constar para o usuário é None.

# Testando a função custo da estrada. Além de "Arad", também iremos testar a cidade de "Timisoara" e a cidade de "Rimnicu Vilcea" (que fica no caminho até Bucharest). Ou seja, alguns testes possuem estrada direta e outros não possuem para vermos o retorno None.

print('A distância da estrada de Arad -> Sibiu é:', custo_da_estrada('Arad', 'Sibiu'), 'km')
print('A distância da estrada de Arad -> Bucharest é:', custo_da_estrada('Arad', 'Bucharest'), 'km')

print('\nA distância da estrada de Timisoara -> Lugoj é:', custo_da_estrada('Timisoara', 'Lugoj'), 'km')
print('A distância da estrada de Timisoara -> Arad é:', custo_da_estrada('Timisoara', 'Arad'), 'km')
print('A distância da estrada de Timisoara -> Bucharest é:', custo_da_estrada('Timisoara', 'Bucharest'), 'km')

print('\nA distância da estrada de Rimnicu Vilcea -> Pitesti é:', custo_da_estrada('Rimnicu Vilcea', 'Pitesti'), 'km')
print('A distância da estrada de Rimnicu Vilcea -> Bucharest é:', custo_da_estrada('Rimnicu Vilcea', 'Bucharest'), 'km')

# Criando uma função para registrarmos o custo TOTAL de um caminho partindo de uma cidade de origem até Bucareste. Neste caso, iremos percorrer a lista de cidades do caminho somando o custo de cada estrada (da cidade atual até a próxima cidade) com o auxílio de uma variável auxiliadora chamada de "i".

def custo_do_caminho(caminho):
    total = 0
    for i in range(len(caminho) - 1):
        total = total + custo_da_estrada(caminho[i], caminho[i + 1])
    return total

# Testando a função custo do caminho. Partindo de "Arad" existem dois caminhos conhecidos até Bucharest, um passando por "Fagaras" e outro passando por "Pitesti".

por_fagaras = ['Arad', 'Sibiu', 'Fagaras', 'Bucharest']
por_pitesti = ['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest']
print('\nCaminho de Arad por Fagaras:', ' -> '.join(por_fagaras))
print('Custo TOTAL do caminho =', custo_do_caminho(por_fagaras), 'km')
print('Caminho de Arad por Pitesti:', ' -> '.join(por_pitesti))
print('Custo TOTAL do caminho =', custo_do_caminho(por_pitesti), 'km')

# Partindo de "Timisoara" também existem dois caminhos até Bucharest. Ou seja, um voltando por "Arad" e outro descendo por "Lugoj" até "Craiova".

timisoara_por_arad = ['Timisoara', 'Arad', 'Sibiu', 'Fagaras', 'Bucharest']
timisoara_por_lugoj = ['Timisoara', 'Lugoj', 'Mehadia', 'Drobeta', 'Craiova', 'Pitesti', 'Bucharest']
print('\nCaminho de Timisoara por Arad:', ' -> '.join(timisoara_por_arad))
print('Custo TOTAL do caminho =', custo_do_caminho(timisoara_por_arad), 'km')
print('Caminho de Timisoara por Lugoj:', ' -> '.join(timisoara_por_lugoj))
print('Custo TOTAL do caminho =', custo_do_caminho(timisoara_por_lugoj), 'km')

# Partindo de "Rimnicu Vilcea" (que já está no meio do caminho até Bucharest) é possível ir direto por "Pitesti" ou voltar por "Sibiu" e passar por "Fagaras".

rimnicu_por_pitesti = ['Rimnicu Vilcea', 'Pitesti', 'Bucharest']
rimnicu_por_fagaras = ['Rimnicu Vilcea', 'Sibiu', 'Fagaras', 'Bucharest']
print('\nCaminho de Rimnicu Vilcea por Pitesti:', ' -> '.join(rimnicu_por_pitesti))
print('Custo TOTAL do caminho =', custo_do_caminho(rimnicu_por_pitesti), 'km')
print('Caminho de Rimnicu Vilcea por Fagaras:', ' -> '.join(rimnicu_por_fagaras))
print('Custo TOTAL do caminho =', custo_do_caminho(rimnicu_por_fagaras), 'km')

# Criando uma função para mostrarmos os valores de g(n), h(n) e f(n) de cada cidade do caminho. Neste caso, g(n) é a distância que JÁ FOI percorrida desde a cidade de origem, h(n) é a heurística (distância em linha reta que AINDA FALTA até Bucharest) e f(n) é a soma dos dois, ou seja, f(n) = g(n) + h(n).

def mostrar_g_h_f(caminho):
    print(f'{"Cidade":<15} {"g(n)":>5} {"h(n)":>5} {"f(n)":>5}')
    for i in range(len(caminho)):
        cidade = caminho[i]
        g = custo_do_caminho(caminho[:i + 1])
        h = heuristica_bucareste[cidade]
        f = g + h
        print(f'{cidade:<15} {g:>5} {h:>5} {f:>5}')

# Testando a função g, h e f com os caminhos de Arad, Timisoara e Rimnicu Vilcea. Ou seja, é possível perceber que o valor de f(n) na cidade de Bucharest é sempre igual ao custo TOTAL do caminho, pois h(Bucharest) = 0.

print('\nValores ao longo do caminho de Arad por Fagaras:')
mostrar_g_h_f(por_fagaras)
print('\nValores ao longo do caminho de Arad por Pitesti:')
mostrar_g_h_f(por_pitesti)

print('\nValores ao longo do caminho de Timisoara por Arad:')
mostrar_g_h_f(timisoara_por_arad)
print('\nValores ao longo do caminho de Timisoara por Lugoj:')
mostrar_g_h_f(timisoara_por_lugoj)

print('\nValores ao longo do caminho de Rimnicu Vilcea por Pitesti:')
mostrar_g_h_f(rimnicu_por_pitesti)
print('\nValores ao longo do caminho de Rimnicu Vilcea por Fagaras:')
mostrar_g_h_f(rimnicu_por_fagaras)
