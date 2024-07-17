# Desafio 33

Manipulando filas de prioridade com `heapq`

## Explicação

### Ferramentas Utilizadas

- `heapq`: Biblioteca padrão do Python para manipulação de heaps (filas de prioridade).

### Funções Principais

- `heapq.heappush(heap, item)`: Adiciona um item à fila de prioridade.
- `heapq.heappop(heap)`: Remove e retorna o menor item da fila de prioridade.

## Resultado

```py
import heapq

fila_de_prioridade = []

heapq.heappush(fila_de_prioridade, (3, 'Três'))
heapq.heappush(fila_de_prioridade, (1, 'Um'))
heapq.heappush(fila_de_prioridade, (2, 'Dois'))
heapq.heappush(fila_de_prioridade, (4, 'Quatro'))

print(fila_de_prioridade)

elemento = heapq.heappop(fila_de_prioridade)

print(f"Elemento removido: {elemento}")
```