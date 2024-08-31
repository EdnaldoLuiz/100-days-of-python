# Desafio 78

Implementando um algoritmo de busca em largura (BFS) em um grafo

## Explicação

### Ferramentas Utilizadas

- `queue.Queue`: Estrutura de dados para manipulação de filas.
- Algoritmo de Busca em Largura (BFS): Método para percorrer grafos.

### Funções Principais

- `adicionar_vertice(vertice)`: Adiciona um vértice ao grafo.
- `adicionar_aresta(origem, destino)`: Adiciona uma aresta entre dois vértices.
- `bfs(inicio)`: Implementa o algoritmo de busca em largura.

## Resultado

```py
import queue

class Grafo:
    def __init__(self):
        self.vertices = {}
    
    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []
    
    def adicionar_aresta(self, origem, destino):
        if origem in self.vertices and destino in self.vertices:
            self.vertices[origem].append(destino)
            self.vertices[destino].append(origem)
    
    def bfs(self, inicio):
        visitados = set()
        fila = queue.Queue()
        fila.put(inicio)
        visitados.add(inicio)
        
        while not fila.empty():
            vertice = fila.get()
            print(vertice, end=" ")
            
            for vizinho in self.vertices[vertice]:
                if vizinho not in visitados:
                    fila.put(vizinho)
                    visitados.add(vizinho)

# Exemplo de uso
grafo = Grafo()
for vertice in range(1, 6):
    grafo.adicionar_vertice(vertice)

arestas = [(1, 2), (1, 3), (2, 4), (3, 5)]
for origem, destino in arestas:
    grafo.adicionar_aresta(origem, destino)

print("Busca em Largura (BFS) a partir do vértice 1:")
grafo.bfs(1)