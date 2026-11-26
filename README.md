# astar-romenia

Repositório responsável pela busca A* partindo de Arad até Bucharest (Russell & Norvig, capítulo 3), feita em 6 fases na disciplina IIA-008 Inteligência Artificial I. Ou seja, cada fase é um arquivo .py que adiciona um novo conceito em cima da fase anterior, até chegarmos no programa completo da busca A*.

Aluno: José Victor Marin Consolaro | RA: 2691622613014 | Disciplina: Inteligência Artificial I

## Como rodar

Para rodar o programa completo da busca A* é necessário executar o arquivo "a_estrela.py" no terminal:

```
python a_estrela.py
```

Além disso, também é possível rodar cada fase separadamente para acompanhar o passo a passo. Neste caso, basta trocar o nome do arquivo pelo nome da fase desejada:

```
python fase1_explorar.py
python fase2_caminhos.py
python fase3_fronteira.py
python fase4_expandir.py
python fase5_busca.py
```

## Resultado

Partindo de Arad, o melhor caminho encontrado pela busca A* até Bucharest é:

```
Arad -> Sibiu -> Rimnicu Vilcea -> Pitesti -> Bucharest
(418 km em 4 passos, igual à Figura 3.24 do livro)
```

Além de Arad, também foram feitos exemplos partindo de Timisoara e de Rimnicu Vilcea (que fica no meio do caminho até Bucharest). Ou seja, é possível comparar o resultado da busca com os caminhos que foram testados de forma manual na fase 2:

| Cidade de origem | Melhor caminho até Bucharest | Custo TOTAL | Passos |
|---|---|---|---|
| Arad | Arad -> Sibiu -> Rimnicu Vilcea -> Pitesti -> Bucharest | 418 km | 4 |
| Timisoara | Timisoara -> Arad -> Sibiu -> Rimnicu Vilcea -> Pitesti -> Bucharest | 536 km | 5 |
| Rimnicu Vilcea | Rimnicu Vilcea -> Pitesti -> Bucharest | 198 km | 2 |

No caso de Timisoara, na fase 2 testamos somente o caminho por Arad e Fagaras (568 km) e o caminho por Lugoj (615 km). Porém, a busca A* encontra um caminho AINDA MELHOR que os dois, com 536 km.

## Fases

| Arquivo | Conteúdo |
|---|---|
| mapa.py | Dados do mapa da Romênia (dicionário de cidades e estradas) e a heurística h(n) até Bucharest. |
| fase1_explorar.py | Navegação nos dados: quantidade de cidades, vizinhos de Arad e de Timisoara e a heurística de cada vizinho. |
| fase2_caminhos.py | Funções de custo de uma estrada e de um caminho inteiro, além dos valores de g, h e f partindo de Arad, Timisoara e Rimnicu Vilcea. |
| fase3_fronteira.py | Nó de busca e fronteira montados de forma manual partindo de Arad, Timisoara e Rimnicu Vilcea. |
| fase4_expandir.py | Função expandir, conjunto de explorados e três rodadas de busca de forma manual (ainda sem o while). |
| fase5_busca.py | Busca A* com o laço while e o melhor caminho de TODAS as cidades até Bucharest. |
| a_estrela.py | Programa A* completo, com o rastro de cada iteração, teste de regressão e tratamento de cidade que não existe no mapa. |

## Diagramas UML

Os diagramas de Engenharia de Software (atividade, sequência, classes, objetos, estados e pacotes) de cada fase estão em [docs/diagramas-uml.md](docs/diagramas-uml.md).
