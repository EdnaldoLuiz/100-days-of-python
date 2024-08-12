# Desafio 59

Criando e manipulando gráficos de rede com NetworkX

## Explicação

### Ferramentas Utilizadas

- `networkx`: Biblioteca para criação, manipulação e estudo da estrutura, dinâmica e funções de redes complexas.

### Funções Principais

- `nx.DiGraph()`: Cria um grafo direcionado.
- `grafo.add_node()`: Adiciona um nó ao grafo.
- `grafo.add_edge()`: Adiciona uma aresta ao grafo.
- `grafo.add_nodes_from()`: Adiciona múltiplos nós ao grafo.
- `grafo.add_edges_from()`: Adiciona múltiplas arestas ao grafo.
- `nx.draw()`: Desenha o grafo.

## Resultado

```py
import networkx as nx
import matplotlib.pyplot as plt

# Cria um grafo direcionado
grafo_direcionado = nx.DiGraph()

# Adiciona nós e arestas ao grafo
grafo_direcionado.add_node(1)
grafo_direcionado.add_edge(1, 2)
grafo_direcionado.add_nodes_from([3, 4, 5])
grafo_direcionado.add_edges_from([(2, 3), (3, 4), (4, 5)])

# Desenha o grafo
nx.draw(grafo_direcionado, with_labels=True)
plt.show()