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

print(f"Tempo para listas nativas: {tempo_lista:.6f} segundos")
print(f"Tempo para arrays numpy: {tempo_numpy:.6f} segundos")