# Diagramas UML — Busca A* (Arad → Bucharest)

Artefatos de Engenharia de Software do projeto: os diagramas UML que descrevem os
arquivos, os dados e o fluxo de cada fase. Os diagramas estão em Mermaid e são
desenhados pelo próprio GitHub.

| Rótulo | Diagrama | Mostra |
|---|---|---|
| act | Atividade | o fluxo de execução: o que acontece em que ordem |
| sd | Sequência | quem chama quem, de cima para baixo no tempo |
| class | Classes | a forma dos dados |
| object | Objetos | os dados num instante, com valores reais |
| stm | Estados | os estados por que algo passa |
| pkg | Pacotes | como os arquivos se organizam |

## Sumário

- [Visão geral do projeto](#visão-geral-do-projeto) — diagramas 1 e 2
- [Fase 0 — Ambiente, Git e GitHub](#fase-0--ambiente-git-e-github) — diagramas 3 e 4
- [Fase 1 — Navegar nos dados](#fase-1--navegar-nos-dados) — diagramas 5, 6 e 7
- [Fase 2 — Custo de caminho e f = g + h](#fase-2--custo-de-caminho-e-f--g--h) — diagrama 8
- [Fase 3 — O nó e a fronteira](#fase-3--o-nó-e-a-fronteira) — diagramas 9, 10 e 11
- [Fase 4 — Expandir vira função](#fase-4--expandir-vira-função) — diagramas 12 e 13
- [Fase 5 — O laço da busca A*](#fase-5--o-laço-da-busca-a) — diagrama 14
- [Fase 6 — O programa completo](#fase-6--o-programa-completo) — diagramas 15 e 16

---

## Visão geral do projeto

### Diagrama 1 — Roteiro do projeto (act)

Cada fase termina com um commit e um push.

```mermaid
flowchart LR
    inicio(( )) --> F0
    F0["Fase 0<br/>ambiente + GitHub"] -->|commit + push| F1
    F1["Fase 1<br/>navegar nos dados"] -->|commit + push| F2
    F2["Fase 2<br/>caminhos e g, h, f"] -->|commit + push| F3
    F3["Fase 3<br/>nó e fronteira"] -->|commit + push| F4
    F4["Fase 4<br/>expandir um nó"] -->|commit + push| F5
    F5["Fase 5<br/>laço while (A*)"] -->|commit + push| F6
    F6["Fase 6<br/>programa completo"] -->|commit + push| TAG
    TAG["tag v1.0"] --> fim((( )))
```

### Diagrama 2 — Arquivos do projeto e suas dependências (pkg)

A seta tracejada «import» quer dizer "usa os dados de". Cada fase é um arquivo novo que faz
`from mapa import mapa_romenia, heuristica_bucareste`.

```mermaid
flowchart LR
    subgraph repo["repositório GitHub: astar-romenia"]
        direction LR
        subgraph dados["«módulo de dados»"]
            mapa["mapa.py<br/>mapa_romenia : dict<br/>heuristica_bucareste : dict"]
        end
        subgraph fases["fases"]
            f1["fase1_explorar.py — Fase 1"]
            f2["fase2_caminhos.py — Fase 2"]
            f3["fase3_fronteira.py — Fase 3"]
            f4["fase4_expandir.py — Fase 4"]
            f5["fase5_busca.py — Fase 5"]
            f6["a_estrela.py — Fase 6"]
        end
        readme["«texto»<br/>README.md"]
        gitignore["«texto»<br/>.gitignore"]
    end
    f1 -.->|«import»| mapa
    f2 -.->|«import»| mapa
    f3 -.->|«import»| mapa
    f4 -.->|«import»| mapa
    f5 -.->|«import»| mapa
    f6 -.->|«import»| mapa
```

---

## Fase 0 — Ambiente, Git e GitHub

### Diagrama 3 — O que se faz no navegador e no computador (act, com raias)

```mermaid
flowchart TB
    inicio(( )) --> C1
    subgraph PC["Computador (terminal e VS Code)"]
        C1["Instalar Python, Git e VS Code<br/>python --version / git --version"]
        C2["git config --global user.name ...<br/>git config --global user.email ..."]
        C3["git clone &lt;URL&gt;<br/>cd astar-romenia<br/>code ."]
        C4["Editar o README.md"]
        C5["git add / git commit / git push"]
    end
    subgraph WEB["Navegador (github.com)"]
        N1["Criar conta no GitHub"]
        N2["Criar repositório astar-romenia<br/>(README + .gitignore Python)"]
        N3["Copiar a URL HTTPS<br/>(botão verde Code)"]
        N4["Atualizar a página do repositório"]
        D{"mudança<br/>apareceu?"}
        N5["ler o erro"]
    end
    C1 --> N1 --> N2 --> N3
    N3 --> C2 --> C3 --> C4 --> C5 --> N4 --> D
    D -->|sim| fim((( )))
    D -->|não| N5 --> C5
```

### Diagrama 4 — Por quais estados um arquivo passa no Git (stm)

```mermaid
stateDiagram-v2
    [*] --> Modificado : você cria ou edita um arquivo
    Modificado --> Preparado : git add
    Preparado --> Commitado : git commit
    Commitado --> Publicado : git push
    Publicado --> Modificado : você edita o arquivo de novo (próxima fase)
    Modificado : Modificado (só no seu disco)
    Preparado : Preparado (staging area)
    Commitado : Commitado (repositório local)
    Publicado : Publicado (no GitHub)
    note right of Modificado
        git status mostra em que estado cada arquivo está.
        git log --oneline lista os commits já feitos.
    end note
```

---

## Fase 1 — Navegar nos dados

### Diagrama 5 — Estrutura de dados do mapa (class)

```mermaid
classDiagram
    class mapa_romenia {
        <<dict>>
        chave : str cidade
        valor : list de estradas
    }
    class heuristica_bucareste {
        <<dict>>
        chave : str cidade
        valor : int km em linha reta
    }
    class lista_de_estradas {
        <<list>>
        itens 0, 1, 2 ... : tuple
    }
    class estrada {
        <<tuple>>
        posicao 0 vizinho : str
        posicao 1 custo : int km
    }
    mapa_romenia .. heuristica_bucareste : mesmas chaves
    mapa_romenia "1" *-- "1" lista_de_estradas : 1 lista por cidade
    lista_de_estradas "1" *-- "1..*" estrada : contém
    note for heuristica_bucareste "20 chaves em cada dicionário."
    note for estrada "Grafo não dirigido: a estrada aparece nas duas cidades."
```

### Diagrama 6 — `mapa_romenia['Arad']` na memória (object)

Os números entre colchetes são os índices.

```mermaid
flowchart LR
    chave["chave<br/>'Arad'"] --> lista
    subgraph lista["valor: uma list com 3 tuples"]
        direction LR
        t0["[0]<br/>('Zerind', 75)"]
        t1["[1]<br/>('Sibiu', 140)"]
        t2["[2]<br/>('Timisoara', 118)"]
    end
    t0 --> det
    subgraph det["a tupla [0] por dentro"]
        direction LR
        v["[0] vizinho (str)<br/>'Zerind'"]
        c["[1] custo (int)<br/>75"]
    end
    n1["mapa_romenia['Arad'][0] -> ('Zerind', 75)<br/>mapa_romenia['Arad'][0][1] -> 75"]
    det -.- n1
```

### Diagrama 7 — Fluxo do script `fase1_explorar.py` (act)

```mermaid
flowchart TB
    inicio(( )) --> P1
    P1["Passo 1: importar os dados de mapa.py<br/>from mapa import ..."]
    P2["Passo 2: contar as cidades<br/>len(mapa_romenia)"]
    P3["Passo 3: ler o valor da chave 'Arad'<br/>mapa_romenia['Arad']"]
    P4["Passo 4: pegar uma tupla e suas partes<br/>primeira[0], primeira[1]"]
    P5["Passo 5: percorrer as estradas de Arad<br/>for vizinho, custo in ..."]
    P6["Passo 6: percorrer o mapa inteiro<br/>for cidade in mapa_romenia"]
    P7["Passo 7: consultar a heurística<br/>heuristica_bucareste[vizinho]"]
    P1 --> P2 --> P3 --> P4 --> P5 --> P6 --> P7 --> fim((( )))
```

---

## Fase 2 — Custo de caminho e f = g + h

### Diagrama 8 — Chamadas para calcular o custo de um caminho (sd)

```mermaid
sequenceDiagram
    participant S as fase2_caminhos.py (script)
    participant CC as custo_do_caminho()
    participant CE as custo_da_estrada()
    participant M as mapa_romenia (dict)
    S->>CC: custo_do_caminho(por_fagaras)
    Note over CC: total = 0
    loop i em range(len(caminho) - 1)
        CC->>CE: custo_da_estrada(caminho[i], caminho[i+1])
        CE->>M: mapa_romenia[origem]
        M-->>CE: lista de (vizinho, custo)
        Note over CE: procura o destino com for + if
        CE-->>CC: return custo
        Note over CC: total = total + custo
    end
    CC-->>S: return total (450)
```

---

## Fase 3 — O nó e a fronteira

### Diagrama 9 — O nó de busca e a fronteira (class)

A fronteira é uma lista de nós. Exemplo de nó: `(393, 140, 'Sibiu', ['Arad', 'Sibiu'])`.

```mermaid
classDiagram
    class no {
        <<tuple>>
        posicao 0 f : int  f = g + h
        posicao 1 g : int  km andados
        posicao 2 cidade : str  onde estou
        posicao 3 caminho : list  cidades até aqui
    }
    class fronteira {
        <<list>>
        itens : list de nós
        append(no) coloca no fim
        sort(key) ordena
        pop(0) tira o primeiro
    }
    fronteira "1" o-- "0..*" no
```

### Diagrama 10 — Primeira expansão, feita à mão (sd)

```mermaid
sequenceDiagram
    participant S as fase3_fronteira.py
    participant F as fronteira (list)
    participant M as mapa_romenia
    participant H as heuristica_bucareste
    S->>H: heuristica_bucareste['Arad']
    H-->>S: 366
    S->>F: [no_inicial] (cria)
    S->>F: pop(0)
    F-->>S: (366, 0, 'Arad', ['Arad'])
    S->>M: mapa_romenia['Arad']
    M-->>S: 3 estradas
    loop para cada (vizinho, custo_estrada)
        S->>H: heuristica_bucareste[vizinho]
        H-->>S: h do vizinho
        S->>F: append((novo_f, novo_g, vizinho, novo_caminho))
    end
    S->>F: sort(key=lambda no: no[0])
    S->>F: pop(0)
    F-->>S: nó de Sibiu (f = 393)
```

### Diagrama 11 — Três fotografias da fronteira (object)

O nó em destaque é o de menor f.

```mermaid
flowchart TB
    subgraph A["1) depois dos append"]
        direction LR
        a0["[0] Zerind<br/>f = 449"] ~~~ a1["[1] Sibiu<br/>f = 393"] ~~~ a2["[2] Timisoara<br/>f = 447"]
    end
    subgraph B["2) depois do sort por f"]
        direction LR
        b0["[0] Sibiu<br/>f = 393"] ~~~ b1["[1] Timisoara<br/>f = 447"] ~~~ b2["[2] Zerind<br/>f = 449"]
    end
    subgraph C["3) depois do pop(0)"]
        direction LR
        c0["[0] Timisoara<br/>f = 447"] ~~~ c1["[1] Zerind<br/>f = 449"]
    end
    A --> B --> C
    nota["pop(0) tirou Sibiu:<br/>é o próximo a ser expandido."]
    C -.- nota
    classDef menor fill:#ffe0b2,stroke:#e65100,stroke-width:2px
    class a1,b0 menor
```

---

## Fase 4 — Expandir vira função

### Diagrama 12 — A função `expandir(no, explorados)` (act)

```mermaid
flowchart TB
    inicio(( )) --> A["Desempacotar o nó<br/>f_atual, g_atual, cidade_atual, caminho = no"]
    A --> B["filhos = []"]
    B --> D1{"ainda há vizinho<br/>na lista?"}
    D1 -->|não| R["return filhos"] --> fim((( )))
    D1 -->|sim: pega o próximo| D2{"vizinho está em<br/>explorados?"}
    D2 -->|sim: continue| D1
    D2 -->|não| C["novo_g = g_atual + custo_estrada<br/>novo_f = novo_g + heuristica_bucareste[vizinho]"]
    C --> E["filhos.append((novo_f, novo_g, vizinho, caminho + [vizinho]))"]
    E --> D1
```

### Diagrama 13 — Uma rodada da busca, repetida 3 vezes (sd)

```mermaid
sequenceDiagram
    participant S as fase4_expandir.py
    participant F as fronteira
    participant X as explorados (set)
    participant E as expandir()
    participant MF as mostrar_fronteira()
    loop rodada em [1, 2, 3]
        S->>F: sort(key=lambda no: no[0])
        S->>F: pop(0)
        F-->>S: nó de menor f
        S->>X: add(cidade)
        S->>E: expandir(no, explorados)
        E->>X: vizinho in explorados ?
        E-->>S: lista de filhos
        Note over S,F: fronteira = fronteira + filhos
        S->>MF: mostrar_fronteira(fronteira)
    end
```

---

## Fase 5 — O laço da busca A*

### Diagrama 14 — O algoritmo A* `busca_a_estrela(inicio, objetivo)` (act)

O teste de objetivo é feito ao **retirar** o nó da fronteira, não ao gerá-lo. É isso que
garante o caminho ótimo.

```mermaid
flowchart TB
    inicio(( )) --> A["Criar a fronteira com o nó inicial<br/>[(h(inicio), 0, inicio, [inicio])]"]
    A --> B["explorados = set()"]
    B --> D1{"fronteira<br/>vazia?"}
    D1 -->|sim| R1["return None, float('inf')"] --> fim1((( )))
    D1 -->|não| C["Ordenar a fronteira pelo f<br/>fronteira.sort(key=lambda no: no[0])"]
    C --> E["Retirar o nó de menor f<br/>f, g, cidade, caminho = fronteira.pop(0)"]
    E --> D2{"cidade ==<br/>objetivo?"}
    D2 -->|sim| R2["return caminho, g"] --> fim2((( )))
    D2 -->|não| D3{"cidade em<br/>explorados?"}
    D3 -->|sim: continue| D1
    D3 -->|não| G["explorados.add(cidade)"]
    G --> H["Para cada vizinho NÃO explorado:<br/>novo_g = g + custo_estrada<br/>novo_f = novo_g + h(vizinho)<br/>fronteira.append((novo_f, novo_g, vizinho, ...))"]
    H -->|volta ao while| D1
```

---

## Fase 6 — O programa completo

### Diagrama 15 — O programa completo `a_estrela.py` (sd)

```mermaid
sequenceDiagram
    participant P as Python
    participant M as main()
    participant B as busca_a_estrela()
    participant F as fronteira
    participant R as resumo_fronteira()
    P->>M: __name__ == '__main__' -> main()
    M->>B: busca_a_estrela('Arad', 'Bucharest', ...)
    loop while fronteira
        B->>F: sort(...) e pop(0)
        F-->>B: nó de menor f
        Note over B: imprime 'N. Expandindo: ...'
        opt cidade == objetivo
            B-->>M: return caminho, g_atual
        end
        B->>F: append(filhos)
        B->>R: resumo_fronteira(fronteira)
        R-->>B: texto 'Cidade(f), ...'
    end
    Note over M: imprime resultado e confere 418
    loop origem em outras cidades
        M->>B: busca_a_estrela(origem, ..., mostrar=False)
        B-->>M: (caminho, custo)
    end
```

### Diagrama 16 — Árvore de busca gerada pelo A* (object)

O número antes do nome é a ordem em que o nó saiu da fronteira. Bucharest (450) foi gerado
mas nunca retirado, porque 418 < 450. Em verde, o caminho ótimo.

```mermaid
flowchart TB
    arad["1 · Arad<br/>f = 366"]
    sibiu["2 · Sibiu<br/>f = 393"]
    tim["Timisoara<br/>f = 447"]
    zer["Zerind<br/>f = 449"]
    ora["Oradea<br/>f = 671"]
    fag["4 · Fagaras<br/>f = 415"]
    rv["3 · Rimnicu Vilcea<br/>f = 413"]
    b450["Bucharest<br/>f = 450"]
    cra1["Craiova<br/>f = 526"]
    pit["5 · Pitesti<br/>f = 417"]
    b418["6 · Bucharest<br/>f = 418"]
    cra2["Craiova<br/>f = 615"]
    arad --> sibiu
    arad --> tim
    arad --> zer
    sibiu --> ora
    sibiu --> fag
    sibiu --> rv
    fag --> b450
    rv --> cra1
    rv --> pit
    pit --> b418
    pit --> cra2
    classDef otimo fill:#c8e6c9,stroke:#2e7d32,stroke-width:2px
    classDef descartado fill:#eeeeee,stroke:#9e9e9e,stroke-dasharray: 4 3
    class arad,sibiu,rv,pit,b418 otimo
    class b450 descartado
```

Rastro completo, iteração por iteração (saída real de `python a_estrela.py`):

| # | Expande | g | h | f | Fronteira depois (ordenada por f) |
|---|---|---|---|---|---|
| 1 | Arad | 0 | 366 | 366 | Sibiu(393), Timisoara(447), Zerind(449) |
| 2 | Sibiu | 140 | 253 | 393 | Rimnicu Vilcea(413), Fagaras(415), Timisoara(447), Zerind(449), Oradea(671) |
| 3 | Rimnicu Vilcea | 220 | 193 | 413 | Fagaras(415), Pitesti(417), Timisoara(447), Zerind(449), Craiova(526), Oradea(671) |
| 4 | Fagaras | 239 | 176 | 415 | Pitesti(417), Timisoara(447), Zerind(449), Bucharest(450), Craiova(526), Oradea(671) |
| 5 | Pitesti | 317 | 100 | 417 | Bucharest(418), Timisoara(447), Zerind(449), Bucharest(450), Craiova(526), Craiova(615), Oradea(671) |
| 6 | Bucharest | 418 | 0 | 418 | (objetivo: fim da busca) |

---

Referência: RUSSELL, S.; NORVIG, P. *Inteligência Artificial*. 3. ed. Rio de Janeiro: Elsevier, 2013. Capítulo 3.
