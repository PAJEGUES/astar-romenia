# astar-romenia

Busca A* de Arad a Bucareste (Russell & Norvig, cap. 3), feita em 6 fases na disciplina IIA-008 Inteligência Artificial I.

Aluno: José Victor Marin Consolaro | RA: 2691622613014 | Disciplina: Inteligência Artificial I

## Como rodar

```
python a_estrela.py
```

## Resultado

```
Arad -> Sibiu -> Rimnicu Vilcea -> Pitesti -> Bucharest
(418 km em 4 passos, igual à Figura 3.24 do livro)
```

## Fases

| Arquivo | Conteúdo |
|---|---|
| mapa.py | dados do mapa da Romênia e heurística h(n) |
| fase1_explorar.py | navegar nos dados |
| fase2_caminhos.py | custo de caminho e valores g, h, f |
| fase3_fronteira.py | nó de busca e fronteira, à mão |
| fase4_expandir.py | função expandir e conjunto de explorados |
| fase5_busca.py | busca A* com laço while |
| a_estrela.py | programa A* completo |

## Diagramas UML

Os diagramas de Engenharia de Software (atividade, sequência, classes, objetos, estados e pacotes) de cada fase estão em [docs/diagramas-uml.md](docs/diagramas-uml.md).
