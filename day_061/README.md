# Desafio 61

Comparando a velocidade de vetores/matrizes nativos x numpy

## Explicação

### Ferramentas Utilizadas

- `timeit`: Biblioteca para medir o tempo de execução de pequenos trechos de código.
- `numpy`: Biblioteca para computação numérica eficiente.

### Funções Principais

- `timeit.timeit()`: Mede o tempo de execução de uma expressão.
- `np.arange()`: Cria um array NumPy com valores em um intervalo.

## Resultado

```py
import timeit
import numpy as np

def soma_lista(lista):
    return [x + 1 for x in lista]

def soma_numpy(array):
    return array + 1

tamanho = 10000000
lista = list(range(tamanho))
array = np.arange(tamanho)

tempo_lista = timeit.timeit('soma_lista(lista)', globals=globals(), number=10)
tempo_numpy = timeit.timeit('soma_numpy(array)', globals=globals(), number=10)

print(f"Tempo com lista nativa: {tempo_lista:.4f} segundos")
print(f"Tempo com NumPy: {tempo_numpy:.4f} segundos")