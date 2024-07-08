import time
from contextlib import contextmanager

iteracoes = 10**6

@contextmanager
def timer():
    inicio = time.time()
    yield
    fim = time.time()
    print(f"Tempo de execução: {fim - inicio:.2f} segundos")

with timer():
    for _ in range(iteracoes):
        pass 
