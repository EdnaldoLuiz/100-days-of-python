import heapq

fila_de_prioridade = []

heapq.heappush(fila_de_prioridade, (3, 'Três'))
heapq.heappush(fila_de_prioridade, (1, 'Um'))
heapq.heappush(fila_de_prioridade, (2, 'Dois'))
heapq.heappush(fila_de_prioridade, (4, 'Quatro'))

print(fila_de_prioridade)

elemento = heapq.heappop(fila_de_prioridade)

print(f"Elemento removido: {elemento}")

print(fila_de_prioridade)

menor_elemento = fila_de_prioridade[0]

print(f"Menor elemento: {menor_elemento}")