# Desafio 25

Trabalhando com context managers e o comando `with`

## Explicação

### Ferramentas Utilizadas

- `contextlib.contextmanager`: Decorador para definir um gerenciador de contexto.
- `with`: Comando para usar o gerenciador de contexto.

### Funções Principais

- `@contextmanager`: Define uma função como um gerenciador de contexto.
- `yield`: Pausa a função e retorna ao bloco `with`.
- `time.time()`: Retorna o tempo atual em segundos desde a época.

## Resultado

```py
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