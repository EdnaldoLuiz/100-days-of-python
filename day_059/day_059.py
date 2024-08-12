import networkx as nx

grafo_direcionado = nx.DiGraph()
grafo_direcionado.add_node(1)
grafo_direcionado.add_edge(1, 2)
grafo_direcionado.add_nodes_from([3, 4, 5])
grafo_direcionado.add_edges_from([(2, 3), (3, 4), (4, 5)])

nx.draw(grafo_direcionado, with_labels=True)