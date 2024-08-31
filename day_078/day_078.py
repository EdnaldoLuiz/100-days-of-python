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
    
    def bfs(self, vertice_inicial):
        visitados = set()
        fila = queue.Queue()
        fila.put(vertice_inicial)
        visitados.add(vertice_inicial)
        
        while not fila.empty():
            vertice_atual = fila.get()
            print(vertice_atual)
            
            for vizinho in self.vertices[vertice_atual]:
                if vizinho not in visitados:
                    fila.put(vizinho)
                    visitados.add(vizinho)

grafo = Grafo()
grafo.adicionar_vertice('A')
grafo.adicionar_vertice('B')
grafo.adicionar_vertice('C')

grafo.adicionar_aresta('A', 'B')
grafo.adicionar_aresta('A', 'C')
grafo.adicionar_aresta('B', 'C')

grafo.bfs('A')